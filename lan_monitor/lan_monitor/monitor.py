import ipaddress
import socket
from time import time

from scapy.all import ARP, Ether, srp
from scapy.layers import l2

from lan_monitor.constant import CONST_MESSAGE, CONST_MESSAGE_PORT

import logging

_LOGGER = logging.getLogger("root")

class Monitor:

    def __init__(self, target_subnet: ipaddress.IPv4Network, probe_interval: int = 60, verbose=False):
        self.target_subnet = target_subnet
        self.probe_interval = probe_interval
        self._last_probe_time = 0

        self.verbose = verbose

    def ping_apple_device(self, target_ip: ipaddress.IPv4Address) -> None:
        """Send UDP message to probe Apple device."""
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(1)
            s.sendto(CONST_MESSAGE, (str(target_ip), CONST_MESSAGE_PORT))
            # _LOGGER.debug(f"Probe sent to {target_ip}")

    def probe(self, subnet: ipaddress.IPv4Network) -> None:
        """probe all address in the subnet"""
        # TODO add threading
        _LOGGER.debug(f"Probing network {str(subnet)}")
        for host in subnet.hosts():
            self.ping_apple_device(host)

    def __construct_arp_packet(self, subnet: ipaddress.IPv4Network) -> l2.Ether:
        arp = ARP(pdst=str(subnet))
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        return ether / arp

    def _send(self, packet):
        return srp(packet, timeout=10, retry=1, verbose=self.verbose)[0]

    def _get_clients(self):
        """get all devices in the subnet using arp

        returns:
            clients: an array of dict of all clients found by ARP
        """
        arp_packet = self.__construct_arp_packet(self.target_subnet)
        result = self._send(arp_packet)

        clients = []
        for sent, received in result:
            clients.append({
                "src_ip": received.psrc,
                "mac": received.hwsrc,
            })
        return clients

    def get_clients(self, sample=1):
        """collect multiple samples of ARP result and return
        args:
            sample: number of sample to collect

        returns:
            clients: an array of dict of all clients found by arp in multiple samples
        """
        clients = []
        seen_clients = set()

        # probe periodically
        if time() - self._last_probe_time > self.probe_interval:
            self._last_probe_time = time()
            self.probe(self.target_subnet)

        # find by arp
        for i in range(sample):
            cli = self._get_clients()
            for c in cli:
                if c["mac"] not in seen_clients:
                    clients.append(c)
                    seen_clients.add(c["mac"])

        return clients

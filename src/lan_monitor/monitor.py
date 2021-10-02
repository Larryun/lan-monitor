from scapy.all import ARP, Ether, srp
from scapy.layers import l2


class Monitor:

    def __init__(self, target_subnet: str):
        self.target_subnet = target_subnet

    def __construct_arp_packet(self, subnet: str) -> l2.Ether:
        arp = ARP(pdst=subnet)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        return ether / arp

    def _send(self):
        packet = self.__construct_arp_packet(self.target_subnet)
        return srp(packet, timeout=3)[0]

    def get_clients(self):
        result = self._send()
        clients = []
        for sent, received in result:
            clients.append({
                "src_ip": received.psrc,
                "mac": received.hwsrc,
            })
        return clients

from scapy.all import ARP, Ether, srp
from scapy.layers import l2


class Monitor:

    def __init__(self, target_subnet: str):
        self.target_subnet = target_subnet

    def __construct_arp_packet(self, subnet: str) -> l2.Ether:
        arp = ARP(pdst=subnet)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        return ether / arp

    def _send(self, packet, verbose=False):
        return srp(packet, timeout=10, verbose=verbose)[0]

    def _get_clients(self, verbose=False):
        arp_packet = self.__construct_arp_packet(self.target_subnet)
        result = self._send(arp_packet, verbose)

        clients = []
        for sent, received in result:
            clients.append({
                "src_ip": received.psrc,
                "mac": received.hwsrc,
            })
        return clients

    def get_clients(self, verbose=False, sample=1):
        clients = []
        seen_clients = set()

        for i in range(sample):
            cli = self._get_clients(verbose)
            for c in cli:
                if c["mac"] not in seen_clients:
                    clients.append(c)
                    seen_clients.add(c["mac"])

        return clients






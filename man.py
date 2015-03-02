# Project MAN
# Modular Automation Network
#
# Cisco Geekfest Hackathon
# Austin, TX 2015
#

import requests
from mininet.topo import Topo
from mininet.net import Controller
from mininet.net import Mininet
from mininet.cli import CLI

class NetBlock:

    def __init__(self, name, addressBase, network):
        podHosts = []
        podSwitch = None
        for i in range(1,4):
            self.addHost(name, addressBase + i)
            self.createPodSwitch()

    def addHost(self, name, i):
        hostName = 'host' + name + str(i)
        ipAddress = '10.0.0.' + str(i)
        podHosts.append(net.addHost(hostName, ip=ipAddress))

    def createPodSwitch(self):
        podSwitch = net.addSwitch( 's3' )
        for host in self.posHosts:
            net.addLink( host, podSwitch )


def buildMainNetwork():
    print '*** Adding hosts\n'
    h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )

    print '*** Adding switch\n'
    s3 = net.addSwitch( 's3' )

    print '*** Creating links\n'
    net.addLink( h1, s3 )
    net.addLink( h2, s3 )


if __name__ == "__main__":
    # network = Mininet()
    net = Mininet(controller=Controller)

    print '*** Adding controller\n'
    net.addController( 'c0' )
    block1 = NetBlock('block1', 10, net)
    buildMainNetwork()

    print '*** Starting network\n'
    net.start()

    print '*** Running CLI\n'
    CLI( net )

    print '*** Stopping network'
    net.stop()
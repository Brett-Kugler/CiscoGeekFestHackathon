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
from mininet.node import OVSController

class NetBlock:

    def __init__(self, name, addressBase, network):
        self.podHosts = []
        self.podSwitch = None
        for i in range(1,4):
            self.addHost(name, addressBase + i)
            self.createPodSwitch()

    def addHost(self, name, i):
        hostName = 'host' + name + str(i)
        ipAddress = '10.0.0.' + str(i)
        self.podHosts.append(net.addHost(hostName, ip=ipAddress))

    def createPodSwitch(self):
        self.podSwitch = net.addSwitch( 's3' )
        for host in self.podHosts:
            net.addLink( host, self.podSwitch )


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
    net = Mininet(controller=OVSController)

    print '*** Adding controller\n'
    net.addController( 'c0' )
    buildMainNetwork()

    print '*** Starting network\n'
    net.start()
    
    block1 = NetBlock('block1', 10, net)

    print '*** Running CLI\n'
    CLI( net )

    print '*** Stopping network'
    net.stop()

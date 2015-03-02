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
from mininet.node import RemoteController

class NetBlock:

    def __init__(self, name, network, block):
        self.podHosts = []
        self.podSwitch = None
	self.net = network
        self.block = block
	self.name = name

    def nextBlock(self):
        for i in range(1,4):
            self.addHost(self.name, i)
        self.createPodSwitch()

    def addHost(self, name, i):
        hostName = 'h' + name + str(i)
	print "Adding host", hostName
        ipAddress = '10.0.0.' + str((self.block*10)+i)
        self.podHosts.append(self.net.addHost(hostName, ip=ipAddress))

    def createPodSwitch(self):
	print "Adding switch", self.block+2
        self.podSwitch = self.net.addSwitch( 's'+str(self.block+2) )
        for host in self.podHosts:
	    print "Adding host link for", host
            host.linkTo(self.podSwitch)


def buildMainNetwork(net):
    print '*** Adding hosts\n'
    h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )

    print '*** Adding switch\n'
    s3 = net.addSwitch( 's1' )

    print '*** Creating links\n'
    net.addLink( h1, s3 )
    net.addLink( h2, s3 )


if __name__ == "__main__":
    rc = RemoteController(name="ODL", ip="127.0.0.1")
    net = Mininet(controller=rc)

    #print '*** Adding controller\n'
    #net.addController( 'c0' )
    #net.start()
    buildMainNetwork(net)

    print '*** Starting network\n'
    #net.start()
    
    block1 = NetBlock('b', net, 1)
    block1.nextBlock()

    net.start()

    print '*** Running CLI\n'
    CLI( net )

    print '*** Stopping network'
    net.stop()

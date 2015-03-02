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

class NetBlock:

    def __init__():
        podHosts = []

    def addHost():
        pass

    def createPodSwitch():
        pass


if __name__ == "__main__":
    #network = Mininet()
    net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )

    info( '*** Adding switch\n' )
    s3 = net.addSwitch( 's3' )

    info( '*** Creating links\n' )
    net.addLink( h1, s3 )
    net.addLink( h2, s3 )

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()
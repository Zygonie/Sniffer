#!/usr/bin/env python
from scapy.all import *

def pkt_handler(pkt):
  if pkt.haslayer(Dot11):
    hwAddr = pkt.addr2
    signal = ord(pkt.notdecoded[-4:-3])-256
    if pkt.type==0 and pkt.subtype==4:
      print "MAC {0} with Signal {1}dBm".format(hwAddr, signal)

sniff(iface="mon1", prn=pkt_handler)
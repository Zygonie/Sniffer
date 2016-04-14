#!/usr/bin/env python

"""
802.11 Scapy Packet Builder
"""

# if we set logging to ERROR level, it supresses the warning message
# from Scapy about ipv6 routing
#   WARNING: No route found for IPv6 destination :: (no default route?)
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import Dot11Beacon, Dot11Elt, RadioTap, Dot11, sendp, Dot11ProbeReq, conf


class PacketBuilder():

    def  __init__(self,\
                  intf='wlan0mon',\
                  ssid='test',\
                  source='00:00:de:ad:be:ef',\
                  bssid='00:11:22:33:44:55'):

      self.rates = "\x03\x12\x96\x18\x24\x30\x48\x60"

      self.ssid = ssid
      self.source = source
      self.bssid = bssid
      self.intf = intf
      self.intf = intf

      # set Scapy conf.iface
      conf.iface = self.intf


    def Beacon(self, count=10, ssid=None, dst='ff:ff:ff:ff:ff:ff'):
      if ssid is not None:
          self.ssid=ssid
      beacon = Dot11Beacon(cap=0x2104)
      essid  = Dot11Elt(ID='SSID',info=self.ssid)
      rates  = Dot11Elt(ID='Rates',info=self.rates)
      dsset  = Dot11Elt(ID='DSset',info='\x01')
      tim    = Dot11Elt(ID='TIM',info='\x00\x01\x00\x00')
      pkt = RadioTap()\
        /Dot11(type=0,subtype=8,addr1=dst,addr2=self.source,addr3=self.bssid)\
        /beacon/essid/rates/dsset/tim

      print '[*] 802.11 Beacon: SSID=[%s], count=%d' % (ssid,count)
      try:
        sendp(pkt,iface=self.intfmon,count=count,inter=0.1,verbose=0)
      except:
        raise


    def ProbeReq(self,\
                 count=10,\
                 ssid=None,\
                 dst='ff:ff:ff:ff:ff:ff',\
                 bssid='ff:ff:ff:ff:ff:ff',\
                 source=None):
      # * The service set identifier or SSID is the logical(i.e.human readable) name used by a wireless network.
      #
      # * The basic service set or BSS consists of a single access point( or virtual access point) and any
      #   stations associated to the AP(VAP).Each WLAN that an AP provides service
      #   for will use a 48-bit address as the BSSID for the BSS, which is very similar to a MAC address
      #   (and may use the MAC address of the AP).
      #
      # * The extended service set or ESS consists of one or more BSS connected to the same network.

      if ssid is not None:
        # SSID field set to "OPEN" indicating it is a directed probe request
        self.ssid = ssid
      if source is not None:
        self.source=source
      if bssid is not None:
          self.bssid = bssid
      param = Dot11ProbeReq()
      essid = Dot11Elt(ID='SSID',info=self.ssid)
      rates  = Dot11Elt(ID='Rates',info=self.rates)
      dsset = Dot11Elt(ID='DSset',info='\x01')
      pkt = RadioTap()\
        /Dot11(type=0,subtype=4,addr1=dst,addr2=self.source,addr3=self.bssid)\
        /param/essid/rates/dsset
      # Address Field - 1 = Receiver Address( = Destination Address) ff:ff:ff:ff:ff:ff
      # Address Fiedl - 2 = Transmitter Address( = Source Address) 84:38:38:58:63:D5
      # Address Field - 3 = BSSID ff:ff:ff:ff:ff:ff

      print '[*] 802.11 Probe Request: SSID=[%s], count=%d' % (ssid,count)
      try:
        sendp(pkt,count=count,inter=0.1,verbose=0)
      except:
        raise

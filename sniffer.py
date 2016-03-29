#!/usr/bin/env python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import time
from logging.handlers import TimedRotatingFileHandler
from scapy.all import *
from pymongo import MongoClient
import os

def pkt_handler(pkt):
    if pkt.haslayer(Dot11):
        hwAddr = pkt.addr2
        signal = ord(pkt.notdecoded[-4:-3])-256
        if pkt.type==0 and pkt.subtype==4:
            now = time.time()
            str = '{{"ts":{}, "moduleId":"{}", "uuid":"{}","dBm_signal":{}}}'.format(now, moduleId, hwAddr, signal)
            logger.info(str)


formatter = logging.Formatter("%(asctime)s -- %(message)s")
logger = logging.getLogger("nanalytics")
logger.setLevel(logging.INFO)
handler = logging.handlers.TimedRotatingFileHandler(
    "probe_request.log",
    when="s",
    interval=15,
    encoding="utf-8",
    utc=True)
handler.setFormatter(formatter)
logger.addHandler(handler)
moduleId = "RPi-1"

sniff(iface="mon0", prn=pkt_handler) 

#!/usr/bin/env python

from glob import glob
import os
import re
import json
from pymongo import MongoClient

#Check if there are files to dump to database
files = glob('probe_request.log.*')
if len(files)>0:
    #Mongo
    client = MongoClient(os.environ['SNIFFER_DB_URL'])
    db = client.nanalytics
    collection = db.log_entry
    for file in files:
        try:
            with open(file,'r') as logfile:
                print '**** file {} ****'.format(file)
                for line in logfile:
                    m=re.match('.*(?P<entry>\{.*\}.*)',line)
                    if m is not None:
                        entry = m.group('entry')
                        print 'insert {}'.format(entry)
                        collection.insert_one(json.loads(entry))
            os.remove(file)
        except Exception as err:
            print err
            pass

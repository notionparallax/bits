import pymongo
from pymongo import MongoClient
import datetime
import dateutil.parser
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import requests
from scipy.misc import imread
from StringIO import StringIO
import math
import pytz
import time

print "go"

personNumber = 304
url = "http://ec2-52-65-111-92.ap-southeast-2.compute.amazonaws.com:3000"

responses = []

def tryIt(i,last,startStopwatch, ws, we):
    request = "{}/toiletdata?minor[]={}&windowend={}&windowstart={}".format(url, personNumber, we, ws)
    try:
        response = requests.request("GET", request)
        print "{0:02d}| status:{1} --- That took {2} seconds ({3} total)".format(
            i,
            response.status_code,
            (datetime.datetime.now()-last).total_seconds(),
            (datetime.datetime.now() - startStopwatch).total_seconds())
        return {"response":response, "start":ws, "end":ws, "status":response.status_code, "body":json.loads(response.text)}
    except Exception,e:
        print e, "pausing"
        time.sleep(10)
        print "unpausing"
        return False


ws = datetime.datetime(2016, 10, 14, 0, 0)
we = datetime.datetime(2016, 10, 31, 0, 0)
chunks = 7000 #roughly 700 hours in a month
delta = (we-ws)/chunks
for i in range(1,110):
    last = datetime.datetime.now()
    startStopwatch = datetime.datetime.now()

    if i>100:
        r = tryIt(i,last,startStopwatch, ws, we)
        responses.append(r)

    we = ws + delta
    ws = we

print responses
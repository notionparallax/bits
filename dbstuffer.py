import datetime
import json
import requests
import sys
import time
import StringIO
import gzip
import dateutil.parser


url = "http://localhost:3000"

data = [
    { "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.219Z", "rssi" : -72, "agentId" : "00000000b648975e", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.240Z", "rssi" : -69, "agentId" : "0000000063a52908", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.252Z", "rssi" : -74, "agentId" : "00000000c7ce4c76", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.255Z", "rssi" : -66, "agentId" : "000000005de72066", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.259Z", "rssi" : -99, "agentId" : "0000000018550a76", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.261Z", "rssi" : -78, "agentId" : "000000007d418b7a", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.265Z", "rssi" : -84, "agentId" : "0000000013bed9f7", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.265Z", "rssi" : -70, "agentId" : "000000002f9f3fae", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.268Z", "rssi" : -74, "agentId" : "000000005e6ed248", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.269Z", "rssi" : -96, "agentId" : "00000000035d7102", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.271Z", "rssi" : -77, "agentId" : "0000000023e614ba", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.272Z", "rssi" : -60, "agentId" : "00000000fc7843f8", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.279Z", "rssi" : -62, "agentId" : "000000002c4ab387", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.280Z", "rssi" : -73, "agentId" : "0000000044bfba76", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.280Z", "rssi" : -79, "agentId" : "00000000b571f8e3", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:32.160Z", "rssi" : -61, "agentId" : "000000005de72066", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:32.168Z", "rssi" : -63, "agentId" : "000000002f9f3fae", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:32.182Z", "rssi" : -78, "agentId" : "000000002c4ab387", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:33.079Z", "rssi" : -73, "agentId" : "00000000b648975e", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:33.114Z", "rssi" : -82, "agentId" : "000000004ff7d75b", "minor" : 304},

	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:10.279Z", "rssi" : -62, "agentId" : "000000003d6e520a", "minor" : 304},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:20.280Z", "rssi" : -73, "agentId" : "000000003d6e520a", "minor" : 305},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:30.280Z", "rssi" : -79, "agentId" : "000000003d6e520a", "minor" : 306},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:42.160Z", "rssi" : -61, "agentId" : "000000003d6e520a", "minor" : 307},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:52.168Z", "rssi" : -63, "agentId" : "000000003d6e520a", "minor" : 308},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:02.182Z", "rssi" : -78, "agentId" : "000000003d6e520a", "minor" : 309},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:33.079Z", "rssi" : -73, "agentId" : "000000003d6e520a", "minor" : 310},
	{ "major" : 1, "uuid" : "17520757a1412b175c03687a7102a104", "tx" : -58, "time" : "2016-10-17T00:21:33.114Z", "rssi" : -82, "agentId" : "000000003d6e520a", "minor" : 311 }
]
print "number of things to insert:", len(data)

payload = json.dumps(data)
zipheaders = {
    'authorization': "Basic dW5kZXJzdGFuZGluZ1NwYWNlOmtub3dsZWRnZUlzUG93ZXI=",
    "content-type":"application/octet-stream",
    'cache-control': "no-cache"
    }

print "context"
print "z:",zipheaders
print "- - - - - - - - - -\n\n"


def test(testID, description, res, expect=200):
    print "\n"+str(testID)+" - - - - - - - - - -"
    print "decription:", description
    if expect != res.status_code:
        print "\n".join(["************","*          *","* !!FUCK!! *","*          *","************"])
    print description
    print "Status: " + str(res.status_code)
    print res.text[:200] #crop print to 200 chars
    print
    return res


out = StringIO.StringIO()
with gzip.GzipFile(fileobj=out, mode="w") as f:
  f.write(payload)
out.getvalue()
test(0, "/detections. expect success of 3 entries - zipped",
     requests.request("POST",
     	              url+"/detections",
     	              data=out.getvalue(),
     	              headers=zipheaders))
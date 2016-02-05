from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pandas as pd
import time
import re
import math

def ignoreDickCell(cellValue):
    if type(cellValue) == float:
        if math.isnan(cellValue):
            return ""
    else:
        return cellValue

def thisRowIsFresh(row):
    try:
        if row["googled"] != True:
            return True
        else:
            return False
    except:
        return True

def makeSearchQuery(placeName):
    a = placeName.replace(" ", "+").replace(",","%2C")
    return a

def getUsefulBit(query):
    a = driver.find_element_by_css_selector(query).text.split("\n")
    return a

def isDuff(thing):
    duffLines = [  u'Permanently closed'
              ,u'See photos'
              ,u'Are you the business owner?'
              ,u'Be the first to review'
              ,u'Directions'
              ,u'Feedback'
              ,u'Map for'
              ,u'People also search for'
              ,u'Reviews'
              ,u'Write a review'
              ,u'View 15+'
             ]
    a = thing in duffLines or re.match(thing, u"\d* Google review[s]*")
    return a

driver      = webdriver.Firefox()
csvFileName = 'VisionClientVendorExports_20150630_update.csv'
companies   = pd.read_csv(csvFileName)

searchPrefix= "https://www.google.com.au/search?q="

#['VisionClientID', 'EpicorCustomerID', 'ClientNumber', 'Name', 'Type', 'Status', 
# 'WebSite', 'Memo', 'CurrentStatus', 'ClientInd', 'VendorInd', 'LinkedVendor',
# 'VisionClientAddressID', 'AddressDescription', 'Address2', 'Address3', 'Address4',
# 'City', 'State', 'Zip', 'Country', 'Phone', 'FAX']

#from: http://stackoverflow.com/questions/20692122/edit-pandas-dataframe-row-by-row
#
# >>> for i, trial in dfTrials.iterrows():
# ...     dfTrials.loc[i, "response"] = "answer {}".format(trial["no"])
# ...     
# >>> dfTrials
#    condition  no  response
# 0          2   1  answer 1
# 1          1   2  answer 2
# 2          1   3  answer 3
def runThroughTheCompanies():
    for i, row in companies.iterrows():
        #row = row[1] #this is because itterrows returns a tuple of (index, row, stuff   )
        if row.Name and row.City and thisRowIsFresh(row):
            placeName = row.Name + ", " + ignoreDickCell(row.City)
            print "\n>>>" + placeName + " ("+str(i)+")"

            searchQuery = makeSearchQuery(placeName)
            driver.get(searchPrefix+searchQuery)
            
            searchData = getUsefulBit("#rhs_block")

            googleExtras = ""
            for thing in searchData:
                if isDuff(thing):
                    pass
                else:
                    if 'Address:' in thing:
                        companies.loc[i, "GoogleAddress"] = thing
                    elif 'Phone:' in thing:
                        companies.loc[i, "GooglePhone"  ] = thing
                    else:
                        googleExtras += " | " + thing.encode('ascii', 'ignore')
            companies.loc[i, "googleExtras"] = googleExtras
            companies.loc[i, "googled"]      = True

            companies.to_csv(csvFileName, encoding='utf-8')
            print companies.loc[i]
            time.sleep(2)

while True:
    try:
        runThroughTheCompanies()
    except:
        print "locked out again"
        time.sleep(30)
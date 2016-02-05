from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pandas as pd
import time
import re
import math

driver      = webdriver.Firefox()
csvFileName = 'BWPhotos.csv'
thePeople   = pd.read_csv(csvFileName)

# Login, current_condition, work_email, bwphotoURL
def runThroughThePeople():
    for i, row in thePeople.iterrows():
        #row = row[1] #this is because itterrows returns a tuple of (index, row, stuff   )
        status = ""
        if row.bwphotoURL[0:4] == "http":
            driver.get(row.bwphotoURL)
            try:
                if driver.find_element_by_tag_name('img'):
                    status = "all good bro"
            except:
                status = "can't find an image :("
        else:
            status = "your URL is malformed"
        print row.Login + ", " + status
        # time.sleep(1)


runThroughThePeople()
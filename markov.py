from collections import Counter
from StringIO import StringIO
import json
import numpy as np
import pandas as pd
import requests

#the state transition matrix lives in a google spreadsheet. This goes to get it, then parses it into a pandas dataframe.
r = requests.get('https://docs.google.com/spreadsheets/d/1njYra2wdGLKFw49qRWP57DtcyEgs7tQ6NnXPgOivLp4/pub?gid=436853951&single=true&output=csv')
data = r.content
stateTable = pd.read_csv(StringIO(data))

#trim off the unecesary columns
stateTable.drop(stateTable.columns[[0,1]], 1, inplace=True)
# print stateTable.head()

states = list(stateTable.columns.values)

armyOfMeArray = []
armySize = 10 #make n potential days
lobby = 9 #index of lobby
numOfTimePeriods = 60*8


for j in range(armySize): # for each person-day
    currentState = lobby
    stateList = [states[currentState]]
    for i in range(numOfTimePeriods):  # for each time period
        rawRowState = sum(stateTable.values[currentState])
        weights = list(stateTable.values[currentState]/rawRowState)
        nextState =  np.random.choice(states, 1, p=weights)
        currentState = states.index(nextState[0])
        stateList.append( nextState[0] )

    armyOfMeArray.append(stateList)
    print Counter(stateList)

meJSON = json.dumps(armyOfMeArray)
#setup to write to a document
armyOfMe = open("armyOfMe.json", 'w')
armyOfMe.write(meJSON)

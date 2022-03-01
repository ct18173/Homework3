#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:10:37 2018

@author: pratham
"""

import os 
os.chdir("/Users/pratham/Downloads")
import pandas as pd

globalTop = pd.read_csv("Global Top 200.csv")


TrackID = []

s1 = globalTop['URL'][1]
s2 = "world"

URL = list(globalTop['URL'])

for i in range(200):
    TrackID.append((URL[i])[31:])
    
globalTop["TrackID"] = TrackID

#First 100 Features
#Not Getting all at once due to internal server error
print(",".join(TrackID[:100]))

#Get the rest 100 features
print(",".join(TrackID[100:]))

#Load the data of first 100 audio features
TrackID1 = pd.read_csv("document.csv")

TrackID2 = pd.read_csv("document (1).csv")

combineID = [TrackID1,TrackID2]

Features = pd.concat(combineID)

#Remove Unncessary datasets
del TrackID1,TrackID2,combineID

Features["TrackID"] = Features["id"]

del Features["id"]


spotify = pd.merge(globalTop,Features,on = "TrackID")

spotify.to_csv('spotify.csv')

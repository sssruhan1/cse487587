#!/usr/bin/env python

"""

Use Twitter API to grab user information from list of organizations; 
export text file

Uses Twython module to access Twitter API

"""

import sys
import string
import simplejson
from twython import Twython

#WE WILL USE THE VARIABLES DAY, MONTH, AND YEAR FOR OUR OUTPUT FILE NAME
import datetime
now = datetime.datetime.now()
day=int(now.day)
month=int(now.month)
year=int(now.year)


#FOR OAUTH AUTHENTICATION -- NEEDED TO ACCESS THE TWITTER API
t = Twython(app_key='Jt0iBEeT4Dk1nsYW2g4CGJ1ZY', #REPLACE 'APP_KEY' WITH YOUR APP KEY, ETC., IN THE NEXT 4 LINES
    app_secret='Xx1F66OssdUnKIpY4Plih3RpGce6T7Xsuvca69nYXyeh15Wp1B',
    oauth_token='2652772872-W9GTB3c973ayomnFPW1qEFgieNpskT5yJAD0c29',
    oauth_token_secret='nHdpiqLHzQVGSfVqgM7JgFN89FSpdkJpLdTNX1YYskx0G')
   
data = t.search(q='#UB', count=30)
tweets = data['statuses']

#NAME OUR OUTPUT FILE - %i WILL BE REPLACED BY CURRENT MONTH, DAY, AND YEAR
outfn = "tweets_data_%i.%i.%i.txt" % (now.month, now.day, now.year)

#NAMES FOR HEADER ROW IN OUTPUT FILE
fields = "id text".split()

#INITIALIZE OUTPUT FILE AND WRITE HEADER ROW   
outfp = open(outfn, "w")
outfp.write(string.join(fields, "\t") + "\n")  # header

for entry in tweets:
   
    r = {}
    for f in fields:
        r[f] = ""
    #ASSIGN VALUE OF 'ID' FIELD IN JSON TO 'ID' FIELD IN OUR DICTIONARY
    r['id'] = entry['id']
    r['text'] = entry['text']
    print r
    #CREATE EMPTY LIST
    lst = []
    #ADD DATA FOR EACH VARIABLE
    for f in fields:
        lst.append(unicode(r[f]).replace("\/", "/"))
    #WRITE ROW WITH DATA IN LIST
    outfp.write(string.join(lst, "\t").encode("utf-8") + "\n")

outfp.close()  

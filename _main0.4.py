#Autonomous Tor Traffic Generator Copyright (C) 2016 Prosthetic.Conscience
#Contact: prosthetic.conscience@riseup.net
#
#This file is part of the Autonomous Tor Traffic Generator.
#Autonomous Tor Traffic Generator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
#Autonomous Tor Traffic Generator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with the Autonomous Tor Traffic Generator. If not, see <https://www.gnu.org/licenses/>

#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import socks    #code to import packages required; socks and requests are thirdparty
import socket
import time
import requests
import random

from dictURL import dict_url    #reading dictionaries from dict files
from dictREF import dict_ref


def connectTor():   #code to route traffic over tor
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)
    socket.socket = socks.socksocket


def URLrequest():   #code to compiles and send request
    connectTor()    #calls code to connect to tor
    global dict_url_hit
    global dict_ref_hit
    dict_len_rawUrl = len(dict_url) #size of dictURL file
    dict_len_rawRef = len(dict_ref) #size of dictREF file
    
    for count in range(1, dict_len_rawUrl):     #for loop to iterate through dictURL file
        dict_url_hit = "URLRaw" + str(count)    #combines the current count with 'URLRaw' to prepair to pull value from dictionary file
        RANDom = random.randint(1,dict_len_rawRef)  #random value to pull from dictREF file
        dict_ref_hit = "RefURL" + str(RANDom)   #similar to dict_url_hit
        ref_comp = dict_ref.get(dict_ref_hit)   #takes the generated string and uses it to fetch the value from the corresponding key in the subsiquent dictfile
        url_comp = dict_url.get(dict_url_hit)   #same as above but for url dictionaryfile
        raw_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': ref_comp,
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0',
            }
        
        try:
            req_url = requests.get(url_comp, headers = raw_headers,verify=True, timeout=10) #combines the headers from above with the url generated from earlier
        except Exception:   
            pass
            print('!Error connecting to URL!')    #passes error if it fails to connect to a url for any reason. Usually Timeout Errors or blocking Tor Nodes
        print(req_url.url)      #print the URL im currently hitting
        count = count + 1       #iterates count of for loop to call next url
        time.sleep(timeDel)     #code to cause a delay between each url call

        
def mainControl():  #code to just print some text, run the test 3 times, currently just for long testing
    print('Starting A.T.T.G.')
    print('Generating Requests')
    runTimer()
    time.sleep(2)
    URLrequest()
    ''' #remove this line and the comment and run the URL requests an aditional 2 times before completing the script
    print('second cycle') 
    time.sleep(2)
    URLrequest()
    print('third cycle')
    time.sleep(2)
    URLrequest()
    ''' #remove this line to remove the comment 
    print('A.T.T.G. Finished.')

    

def runTimer(): #time delay
    global timeDel
    timeDel = 1 #time delay in seconds between each calls. with 1 second avg run time is 20 minutes
#
if __name__ == "__main__":
    mainControl()   #execute mainControl
else:
    print('Error try again?')

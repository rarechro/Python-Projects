'''
Version 1.0

By Payton J.
url https://www.indeed.com/q-Software-Engineering-Internship-l-Tempe,-AZ-jobs.html?vjk=52fa3fde68e721e5
'''
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import time
import sys
searcher = "running"
if searcher != "running":
        close()
#imports needed to run the below code without error...hopefully.
while searcher == running:


    def urllookup():  
        print("Thankyou for using Rare's Software Engineer job finder:)")
        global url
        url = input("Paste your indeed url here")
        print("working.")
        time.sleep(.5)
        print("working..")
        time.sleep(.5)
        print("working...")


    def jobgrabber(url):
        uClient = uReq(url)
        page_Soup = soup(uClient.read(), "html.parser")
        uClient.close()

        return print(page_Soup.body.find_all(class_="title"))





#cool functions that do cool things/requests url, parses html into variable and returns result.


urllookup() 
jobgrabber(url)
q1 = input("Would you like to search another url?   Y/N")



if q1 == 'yes' or 'Y' or 'y':
    urllookup()
elif q1 == 'no' or 'n' or 'N':
    print("Thankyou for using Rare's Job Finder ;)")
    if searcher == "running":
        close()

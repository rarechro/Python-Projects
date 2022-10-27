'''
objective grab important info from rusty pot real time/coinflip total value, number of flips, average win red or black
Ver. 1.0
By : Payton J.
'''


import bs4
import urllib.request
#from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

page_Url = "https://rustypot.com/coinflip" 
uClient = urllib.request.Request(
    page_Url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)





f = urllib.request.urlopen(uClient)
dirtytext = f.read().decode('utf-8')

def usefulInfo(dirtytext):
    dirtytext = soup.findAll("Title", "Winner", "Profit", "Loss")
    return dirtytext
print(dirtytext)


print(f.read().decode('utf-8'))








page_Soup = soup(f.read().decode('utf-8'))

print(page_Soup)
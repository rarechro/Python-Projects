import bs4
import urllib.request
#from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

page_Url = "https://www.bestbuy.com/site/pny-geforce-gt-730-2gb-ddr3-single-fan-graphics-card/6471621.p?skuId=6471621" 
uClient = urllib.request.Request(
    page_Url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
    }
)


f = urllib.request.urlopen(uClient)
dirtytext = f.read().decode('utf-8')

def usefulInfo(dirtytext):
    dirtytext = soup.findAll(class="c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button")
    return dirtytext
print(dirtytext)








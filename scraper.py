import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from collections import deque

import requests.compat
class Scrapper:
    def __init__(self,url):
        self.url=url
        self.neulr=list()
    def getUrls():
        re=requests.get(url)
        soup=BeautifulSoup(re.text,"html.parser")
        links=soup.find_all("a")
        with open("urls3.text","w") as f:
            for li in links:
                f.write(f"{li.get('href')} \n")
    def bfsLink():
        pass






if __name__=="__main__":
    baseUrl="https://www.mayoclinic.org"
    url="https://www.mayoclinic.org/diseases-conditions"

    

    re=requests.get(url)
    print(re)
    soup=BeautifulSoup(re.text,"lxml")
    links=soup.find_all("a")
    for li in links:
        urlp=urlparse(li.get('href'))
        if urlp.params=="letter=A":
            print(f"{li.get('href')} \n")
    
    div=soup.find("div",{"class":"aem-GridColumn aem-GridColumn--default--6 aem-GridColumn--offset--default--0 aem-GridColumn--default--none aem-GridColumn--mayo_x-large--5 aem-GridColumn--offset--mayo_x-large--1 aem-GridColumn--mayo_x-large--none aem-GridColumn--mayo_medium--12 aem-GridColumn--offset--mayo_medium--0 aem-GridColumn--mayo_medium--none aem-GridColumn--mayo_x-small--12 aem-GridColumn--offset--mayo_x-small--0 aem-GridColumn--mayo_x-small--none aem-GridColumn--mayo_large--5 aem-GridColumn--offset--mayo_large--1 aem-GridColumn--mayo_large--none aem-GridColumn--mayo_small--12 aem-GridColumn--offset--mayo_small--0 aem-GridColumn--mayo_small--none aem-GridColumn"})
    if div:
        with open("./root.text","w") as f:
            link=div.find_all("a")
            for l in link:
                
                heref=l.get("href")
                tet=l.text
                if heref.startswith("/"):
                    heref=requests.compat.urljoin(baseUrl,heref)
                f.write(f"{heref}\n") 
    else:
        print("div not found")      
"""    Scrapper(url)
    Scrapper.getUrls()"""
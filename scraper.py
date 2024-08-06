import requests
from bs4 import BeautifulSoup
class Scrapper:
    def __init__(self,url):
        self.url=url
        self.neulr=list()
    def getUrls():
        re=requests.get(url)
        soup=BeautifulSoup(re.text,"html.parser")
        links=soup.find_all("a")
        with open("urls2.text","w") as f:
            for li in links:
                f.write(li.get('href'))
            




if __name__=="__main__":
    url="https://www.mayoclinic.org/diseases-conditions"
    Scrapper(url)
    Scrapper.getUrls()
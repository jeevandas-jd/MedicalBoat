import bfsLink as bl
import requests
from bs4 import BeautifulSoup

with open("root.text","r") as f:

    lines=f.readlines()

links=[line.strip() for line in lines]

def ExtactDisease(url,class_name):
    print("call 1")
    responce=requests.get(url)

    soup=BeautifulSoup(responce.text,"lxml")

    names=soup.find_all("a",{"class":class_name})
    with open("disease.txt","a") as f:
        print("call 2")
        for n in names:
            name=n.get("href")
            f.write(f"{n.text} \t link :{name} \n")

base_class="cmp-anchor--plain cmp-button cmp-button__link cmp-result-name__link"

ExtactDisease(links[4],base_class)

for i in range(1,len(links)):

    ExtactDisease(links[i],base_class)




import bfsLink as bl
import requests
from bs4 import BeautifulSoup
import os

import re

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
    with open("diseaselink.txt","a") as f:
        print("call 2")
        for n in names:
            name=n.get("href")
            f.write(f"{name} \n")

base_class="cmp-anchor--plain cmp-button cmp-button__link cmp-result-name__link"

"""ExtactDisease(links[4],base_class)"""
"""
for i in range(1,len(links)):

    ExtactDisease(links[i],base_class)"""
def ExtractSymptom(url,save_directory):
    response=requests.get(url)
    print(response)

    soup=BeautifulSoup(response.text,"html.parser")
    

    symptom=soup.find("div",class_="content")
    
    pattern = r'diseases-conditions/([^/]+)' 
    match=re.search(pattern,url)
    name=match.group(1)
    inc=0
    print(name)
    if symptom:
        symptom=symptom.get_text().strip()

        pattern2 = r'Symptoms\s*(.*?)\s*(?=Causes|When to see a doctor)'
        match = re.search(pattern2, symptom, re.DOTALL)
        if match:
            symptom = match.group(1).strip()
            os.makedirs(save_directory, exist_ok=True)
            file_path = os.path.join(save_directory, f"{name}.txt") 
            file_path2 = os.path.join(save_directory, "123LIST.txt") 

            with open(file_path,"w") as f:
                f.write(symptom.strip())
            with open(file_path2,"a") as f:
                f.write(f"{name}\n")

    else :
        file_path2 = os.path.join(save_directory, "123LIST-COMPLIMENT.txt") 
        with open(file_path2,"a") as f:
                f.write(f"{name}\n")
                print(inc+1)
    

with open("diseaselink.txt","r") as r:
    lines=r.readlines()


links=[line.strip() for line in lines]

"""
for i in range(0,1200):
    ExtractSymptom(links[i],"/home/jeevandas/myproject/MedicalBoat/save_directory")

"""






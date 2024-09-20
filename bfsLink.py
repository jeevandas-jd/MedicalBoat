from collections import deque
import requests

from bs4 import BeautifulSoup
import requests.compat

def fetch_link(url,div=""):
    try:
        response=requests.get(url)
        soup=BeautifulSoup(response.text,"html.parser")
        links=set()
        if div !="":
            dive=soup.find("div",{"class":div})
            a_tag=dive.find_all("a")
            print("i am here div!!")
        else:
            a_tag=soup.find_all("a")
            print("no div")
        

        for li in a_tag:
            link = li['href']
            if link.startswith("http"):
                links.add(link)
            elif link.startswith("/"):
                links.add(requests.compat.urljoin(url,link))
        return links
    except Exception as e:
        print(f"faild to fetch url {url} :\n ERROR{e}")
        return set()
    

def bfs_link_traversal(root_url,max_depth,div=""):
    

    visited=set()
    queue=deque([(root_url,0)]) #Queue holds a tuple of current url and depth

    while queue:
        current_url,depth=queue.popleft()
        if current_url  in visited or  depth>max_depth:
            continue
        print(f"visiting {current_url} :depth {depth}")
        if div !="" and depth ==0:
            print("hello div")
            links=fetch_link(root_url,div=div)
        else:

            links =fetch_link(current_url)
            print("heyy no div")


        for link in links:
            if link not in visited:
                queue.append((link,depth+1))
"""base_url="https://www.mayoclinic.org/diseases-conditions"
div_class="aem-GridColumn aem-GridColumn--default--6 aem-GridColumn--offset--default--0 aem-GridColumn--default--none aem-GridColumn--mayo_x-large--5 aem-GridColumn--offset--mayo_x-large--1 aem-GridColumn--mayo_x-large--none aem-GridColumn--mayo_medium--12 aem-GridColumn--offset--mayo_medium--0 aem-GridColumn--mayo_medium--none aem-GridColumn--mayo_x-small--12 aem-GridColumn--offset--mayo_x-small--0 aem-GridColumn--mayo_x-small--none aem-GridColumn--mayo_large--5 aem-GridColumn--offset--mayo_large--1 aem-GridColumn--mayo_large--none aem-GridColumn--mayo_small--12 aem-GridColumn--offset--mayo_small--0 aem-GridColumn--mayo_small--none aem-GridColumn"
bfs_link_traversal(base_url,max_depth=1,div=div_class)"""
"""with open("root.text","r") as f:
    lines=f.readlines()

print(lines)
links=[line.strip() for line in lines]

for li in lines:
    print(li)"""



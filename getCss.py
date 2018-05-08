from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll("span",{"class":"green"})
findtest = bsObj.findAll(text="the prince")

print(len(findtest))
# for name in nameList:
#     print (name.get_text())
#     print(name)
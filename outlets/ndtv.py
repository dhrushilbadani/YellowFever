from bs4 import BeautifulSoup
import urllib2

def getTotal(url):
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, "html.parser")
    elements = soup.findAll("div", {"class":"search_title_box"})
    val = -1
    for ele in elements:
        title = ele.find('h2').text
        if "News" in title:
            start = title.find('- ') + 2
            end = title.find('News')
            val = title[start:end]
    return int(val)

def indraniTotal():
    indraniUrl = "http://www.ndtv.com/topic/indrani-mukerjea"
    indraniTotal = getTotal(indraniUrl)
    return indraniTotal

def hardikTotal():
    hardikUrl = "http://www.ndtv.com/topic/hardik-patel"
    hardikTotal = getTotal(hardikUrl)
    return hardikTotal

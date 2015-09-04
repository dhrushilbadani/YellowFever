from bs4 import BeautifulSoup
import urllib2

def getTotal(incomplete_url):
    i = 0
    total = 0
    currCount = -1
    while currCount != 0:
        url = incomplete_url + str(i)
        content = urllib2.urlopen(url).read()
        soup = BeautifulSoup(content, "html.parser")
        element = soup.findAll("div", {"class":"col-sm-12 col-md-12 mrgn-tp1"})
        currCount= len(element)
        total += currCount
        i +=1
    return total

def indraniTotal():
    indraniUrl = "http://zeenews.india.com/tags/indrani-mukerjea.html?page="
    indraniTotal = getTotal(indraniUrl)
    return indraniTotal

def hardikTotal():
    hardikUrl = "http://zeenews.india.com/tags/hardik-patel.html?page="
    hardikTotal = getTotal(hardikUrl)
    return hardikTotal

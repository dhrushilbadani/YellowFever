from bs4 import BeautifulSoup
import urllib2

def getTotal(url):
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, "html.parser")
    element = soup.find("div", {"class":"search-result"}).find('h6').text
    start = element.find("of ") + 3
    end = element.find(" Article")
    return int(element[start:end])

def indraniTotal():
    indraniUrl = "http://indianexpress.com/?s=indrani+mukerjea"
    indraniTotal = getTotal(indraniUrl)
    return indraniTotal

def hardikTotal():
    hardikURL = "http://indianexpress.com/tag/hardik-patel/"
    hardikTotal = getTotal(hardikURL)
    return hardikTotal

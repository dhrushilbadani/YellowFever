from bs4 import BeautifulSoup
import urllib2

def getTotal(url):
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, "html.parser")
    element = soup.find("p", {"class":"srch_rslt_count"})
    s = element.text
    start = s.find("from ") + 5
    end = s.rfind(' ')
    val = s[start:end]
    return int(val)

def indraniTotal():
    indraniUrl = "http://www.firstpost.com/?s=indrani+mukerjea"
    indraniTotal = getTotal(indraniUrl)
    return indraniTotal

def hardikTotal():
    hardikUrl = "http://www.firstpost.com/?s=hardik+patel"
    hardikTotal = getTotal(hardikUrl)
    return hardikTotal


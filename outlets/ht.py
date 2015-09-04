from bs4 import BeautifulSoup
import urllib2

def getTotal(url):
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, "html.parser")
    element = soup.select("#ctl00_ContentPlaceHolder1_Search1_hdnTotalRows")
    s = str(element[0]).split('=')[4]
    start = 1
    end = len(s) - 3
    val = int(s[start:end])
    return val

def indraniTotal():
    indraniUrl = "http://www.hindustantimes.com/Search/Search.aspx?q=%22Indrani+Mukerjea%22&op=story&pt=all&auth=all"
    indraniTotal = getTotal(indraniUrl)
    return indraniTotal

def hardikTotal():
    hardikUrl = "http://www.hindustantimes.com/Search/Search.aspx?q=%22Hardik+Patel%22&op=story&pt=all&auth=all"
    hardikTotal = getTotal(hardikUrl)
    return hardikTotal

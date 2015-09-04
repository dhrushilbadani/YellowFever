from bs4 import BeautifulSoup
import urllib2


def getTotal(url):
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, "html.parser")
    element = soup.find("div", {"class":"heading-left"}).find('p').text.encode('utf-8')
    start = element.find("of ") + 3
    end = element.find("for")
    val = element[start:end]
    final = ''
    for c in val:
        if c.isdigit():
            final += c
        else:
            break
    return int(final)

def indraniTotal():
    indraniUrl = "http://www.abplive.in/search/?keywords=indrani%20mukerjea"
    indraniTotal = getTotal(indraniUrl)
    return indraniTotal

def hardikTotal():
    hardikUrl = "http://www.abplive.in/search/?keywords=hardik%20patel"
    hardikTotal = getTotal(hardikUrl)
    return hardikTotal

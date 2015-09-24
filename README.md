# YellowFever
**Visualization of the yellow journalism prevalent in Indian news media. Written in Python.**

>But are we overdoing it? Is such salacious journalism, one that respects no boundaries, desirable or justified?

The quote above is from [an article from the Hindustan Times (HT)] (http://www.hindustantimes.com/india-news/sheena-bora-murder-why-yellow-journalism-is-evergreen/article1-1385440.aspx) itself, which is ironical if you look at the results. Apparently, the Indian media seems to have been hit with a bout of fever - that of yellow journalism. The [Indrani Mukerjea](https://en.wikipedia.org/wiki/Indrani_Mukerjea) - Sheena Bora murder case is quite clearly getting a disproportionate amount of coverage, which in all probability is due to its "scandalous" and sensational nature. The coverage for this story, akin to every other murder case except that it involves members of high society, is so great that it even trumps the coverage the [Hardik Patel](https://en.wikipedia.org/wiki/Hardik_Patel) story is given. That's saying a lot, especially since the Patel-reservation protests led by Hardik Patel have led to violence and ["bandhs"](https://en.wikipedia.org/wiki/Bandh) in the state of Gujarat, affecting the people on a much larger scale than a murder case that has nothing to do with the people of the country.

I have attempted to quantify the effects of this ongoing bout of "Yellow Fever" in the Indian media by scraping data from 6 news websites using Python and its [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4) library. The news websites I scraped are as follows:
* Firstpost
* Zee News
* NDTV
* Hindustan Times (HT)
* ABP Live
* Indian Express (IE)

I then used the [numpy](http://www.numpy.org/) and [matplotlib] (http://matplotlib.org/) Python libraries to create a graphical visualization of this scraped data with two plots (as of 4th Sept 2015 - 1346 hrs IST):
* <strong>No. of articles on Indrani Mukerjea vs Hardik Patel - </strong>
![Sept4-1346hrsIST](/results/Sept4-1346hrsIST.png)

* <strong>The value of "yellowness" for each outlet - </strong>
![Yellowness-Sept4-1346hrsIST](/results/Yellowness-Sept4-1346hrsIST.png)
    "Yellowness" in this case is a simple measure of the disproportion in coverage given by (no. of articles on Indrani Mukerjea) / (no. of articles on Hardik Patel). A higher "yellowness" indicates higher disproportionality in coverage. If the yellowness < 1, it means there have been more articles on Hardik Patel and the Gujarat protests than on Indrani Mukerjea, as is the case with the Indian Express (IE) in the figure above. 

##Usage##
1. Download the .zip file from the pane on the right >> , and extract its contents.
2. Run YellowFever:
```
    python YellowFever.py
```
**Note:** The code is written for Python 2.7. Please make necessary changes, if any, for other versions. You will also need [Beautiful Soup](https://pypi.python.org/pypi/beautifulsoup4), [numpy](http://www.numpy.org/) and [matplotlib] (http://matplotlib.org/) to run this.

##Certain Notes w.r.t. the data scraped:##
* I had to skip the Times of India (TOI) because of a very weirdly structured search functionality. Run a search on ‘indrani mukerjea’ and you'll find the following the search navigation bar on the bottom won't let you go beyond 10. But if you manipulate the URL, you can go beyond it. In fact, choosing a high enough number like 100 returns absolutely irrelevant news. Let me know if you've found a way to scrape TOI.
* Hindustan Times: If you search for ‘indrani mukerjea’ or ‘hardik patel,’ the last few search results are absolutely irrelevant. You need to use quotes [“”] to get more accurate results, i.e. search for ‘”indrani mukerjea’’’ instead. 
* Taking into consideration accuracy and completeness, articles from search results have on occasion been used interchangeably with tagged articles.

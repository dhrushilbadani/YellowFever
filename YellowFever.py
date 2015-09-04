from outlets import zee
from outlets import firstpost
from outlets import ndtv
from outlets import ht
from outlets import indianexpress
from outlets import abp
import numpy as np
import matplotlib.pyplot as plt
import sys

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

yellownessDict={}
outlets = ['Zee', 'Firstpost', 'NDTV', 'HT', 'IE', 'ABP']
print 'Scraping data from the web..'
indrani = np.array([zee.indraniTotal(), firstpost.indraniTotal(), ndtv.indraniTotal(), ht.indraniTotal()
    ,indianexpress.indraniTotal(), abp.indraniTotal()])
hardik = np.array([zee.hardikTotal(), firstpost.hardikTotal(), ndtv.hardikTotal(), ht.hardikTotal()
    ,indianexpress.hardikTotal(), abp.hardikTotal()])

print 'Calculating and sorting by "Yellowness" measure..'
yellowness = np.around((indrani + 0.0)/(hardik + 0.0), 2)

index = 0
for yellowVal in yellowness:
    yellownessDict[yellowVal] = outlets[index]
    index += 1

yellowness[::-1].sort()
sortedOutlets=[]
for yellowVal in yellowness:
    sortedOutlets.append(yellownessDict[yellowVal])

print 'Preparing plots..'
n_groups = len(indrani)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, indrani, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config,
                 label='Indrani Mukerjea')
rects2 = plt.bar(index+bar_width, hardik, bar_width,
                 alpha=opacity,
                 color='r',
                 error_kw=error_config,
                 label='Hardik Patel')
plt.xlabel('Media Outlet')
plt.ylabel('No. of Articles')
plt.title("Indrani vs. Hardik, in the Indian news media")
plt.xticks(index + bar_width, ('Zee', 'Firstpost', 'NDTV', 'HT', 'IE', 'ABP'))
plt.legend()
autolabel(rects1)
autolabel(rects2)

plt.figure()
yellowBar = plt.bar(index, yellowness, bar_width*1.25,
                    alpha=opacity,
                    color = 'y',
                    error_kw=error_config,
                    label = '"Yellowness"')

plt.xlabel('Media Outlet')
plt.ylabel('"Yellowness"')
plt.title('"Yellowness" Measure in the Indian News Media')
plt.xticks(index + bar_width*0.625, sortedOutlets)
plt.legend()
table = plt.table(cellText=[[yellowval] for yellowval in yellowness],
                  colWidths = [0.1],
                  rowLabels=sortedOutlets,
                  colLabels=['"Yellowness"'],
                  loc='center right')
table.set_fontsize(8)
table.scale(1.5, 1.5)

print 'Done!'
plt.tight_layout()
plt.show()

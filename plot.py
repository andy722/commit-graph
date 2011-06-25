#
# Constructs a graph of commit count by date based on VCS log.
#

import numpy as np
import matplotlib.pyplot as plt

from xml.dom import minidom


# parse SVN log

# run the following to get such log:
# $ svn log --xml -l 1000 --with-revprop svn:date $URL_OF_REPOSITORY
xml = minidom.parse('last1000commits')
log = xml.firstChild

commits = {}

for commit in [e for e in log.childNodes if e.nodeType == xml.ELEMENT_NODE]:
    date = commit.childNodes[1].firstChild.data[0:10]
    if not date in commits:
        commits[date] = 0
    else:
        commits[date] += 1


# construct a graph

x = np.arange(len(commits))

bar = plt.bar(x, commits.values())

plt.xlabel('Date')
plt.ylabel('# of commits')
plt.title('Commits by date')
plt.xticks(x, commits.keys())

plt.show()
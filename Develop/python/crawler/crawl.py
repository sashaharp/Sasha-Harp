from urllib.request import Request, urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from textblob import TextBlob
import numpy as np
import re

links = []
for i in range(10):
        req = Request('https://www.google.com/search?q=stephen+hawking&start=' + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        soup = BeautifulSoup(page)
        links += soup.findAll("a")
for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    links.append (re.split(":(?=http)",link["href"].replace("/url?q=",""))[-1].split("&sa")[0])
links = [str(x) for x in links if str(x)[:4]=="http" and "youtube" not in str(x) and "video" not in str(x) and "clip" not in str(x) and "google.com" not in str(x)]

print(links)

nounPhs = []

for l in links:
        try:
                html = urlopen(l).read()
                soup = BeautifulSoup(html)
                # kill all script and style elements
                for script in soup(["script", "style"]):
                        script.extract()    # rip it out

                # get text
                text = soup.get_text()

                # break into lines and remove leading and trailing space on each
                lines = (line.strip() for line in text.splitlines())
                # break multi-headlines into a line each
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                # drop blank lines
                text = '\n'.join(chunk for chunk in chunks if chunk)

                nounPhs += TextBlob(text).noun_phrases
        except HTTPError:
                print(l + " does not work")

nounNums = {}
for n in nounPhs:
        if n in nounNums:
                nounNums[n]+=1
        else:
                nounNums[n]=1
import operator
print(sorted(nounNums.items(), key=operator.itemgetter(1)))
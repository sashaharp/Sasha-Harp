from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from textblob import TextBlob

for start in range(0,10):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    reg_url = "https://www.google.com/search?q=stephen+hawking&start=" + str(start*10)
    req = Request(url=reg_url, headers=headers) 
    page = urlopen(req).read()
    soup = BeautifulSoup(page)

    for cite in soup.findAll('cite'):
        print(cite.text)

url = "http://www.hawking.org.uk/"
html = urlopen(url).read()
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

print(text)
print(TextBlob(text).noun_phrases)
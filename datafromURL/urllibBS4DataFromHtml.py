# coding: utf-8
import urllib.request
import sys
from bs4 import BeautifulSoup

totalArgs=len(sys.argv)
if totalArgs==3:
	url=sys.argv[2]
else:	
	url="http://moebiuscurve.livejournal.com/33766.html"

html=urllib.request.urlopen(url).read().decode('utf8')
raw=BeautifulSoup(html).get_text()
#tokens=word_tokenize(raw)
#tokens

fh = open(sys.argv[1], "w")
fh.write(raw)
fh.close()

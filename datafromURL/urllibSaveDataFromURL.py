# coding: utf-8
import urllib.request
import sys

totalArgs=len(sys.argv)
if totalArgs==3:
	url=sys.argv[2]
else:	
	url="http://moebiuscurve.livejournal.com/33766.html"
response=urllib.request.urlretrieve(url,sys.argv[1])

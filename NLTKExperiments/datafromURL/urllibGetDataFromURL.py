# coding: utf-8
import urllib.request
url="http://moebiuscurve.livejournal.com/33766.html"
response=urllib.request.urlopen(url)
data = response.read()
text=data.decode('utf-8')

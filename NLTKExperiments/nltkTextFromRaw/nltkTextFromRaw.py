# coding: utf-8
import nltk
f=open("NPTELCourses.txt",'rU')
rawData=f.read()
tokens=nltk.word_tokenize(rawData)
nltkTextObject=nltk.Text(tokens)

# coding: utf-8
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext
with open('/home/naveenk/nltk_data/corpora/webtext/overheard.txt', encoding='ISO-8859-2') as f:
    text=f.read()
    
sent_tokenizer=PunktSentenceTokenizer(text)
sents=sent_tokenizer.tokenize(text)
sents[0]

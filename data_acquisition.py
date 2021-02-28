import requests
from urllib import urlopen
# to get URL---
android_url="https://en.wikipedia.org/wiki/Android_version_history"
# to convert into http /json data
android_data=urlopen(android_url)
print(type(android_data))
# read http data
android_html=android_data.read()
# to parser the data
from bs4 import BeautifulSoup as soup
# soup only understand html data
android_soup=soup(android_html,'html.parser')
# print data which has heading
m=android_soup.h1
print(m)
# to fatch all data oftables and class is wikitable
tables= android_soup.findAll('table',{'class':'wikitable'})
# give total table length
print(len(tables))
# fetch only first table
android_table = tables[0]
# print all data
print (android_table)

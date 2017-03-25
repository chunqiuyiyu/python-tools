# coding:utf-8
import requests
from bs4 import BeautifulSoup
import webbrowser

r = requests.get('http://www.yxdown.com/')
r.encoding = 'gbk'

soup = BeautifulSoup(r.text, 'lxml')
tree = soup.find_all('div',class_="ifo_con1")
liData = []

for x in tree:
  tmpTree = x.ul
  for i in tmpTree:
    if i == '\n':
      continue
    liData.append(i)

newsData = []
linkData = []

for x in liData:
  item = x.get_text()
  newsData.append(item[:-4])
  a = x.span.i.a
  linkData.append(a['href'])

def setData(l):
  if not newsData:
    return
  for m,n in enumerate(newsData):
    l.insert('end', n)
    if m%2 == 0:
      l.itemconfigure(m, background='#f0f0ff')
  l.bind('<<ListboxSelect>>', getIndex)

def query():
  link = linkData[index]
  webbrowser.open(link)


def about():
  webbrowser.open('http://www.chunqiuyiyu.com/2017/03/newsreader-simple-information-reader.html')

def getIndex(e):
  global index
  tmp = e.widget.curselection()
  index = tmp[0]

#coding=utf-8
import urllib  
import re
import os
import Queue

q = Queue.Queue()

#we need to filter the incorrect resource path
game_name = ''
def deal_path(n):
	if  n.count(game_name) > 0:
		return n

def mak_dirs(filename):
	f = open(filename)
	s = f.read()
	f.close()
	#add new reg pattern:some site use https protocol
	#the url would noet be long,I limit it in 80 characters
	reg=re.compile(r'https?://.{0,80}\.(?:png|js|ogg|json|mp3|jpg|css|bin|plist|wav|xml|fnt|ini)')
	x = re.findall(reg,s)
	x = filter(deal_path, x)

	count = 0
	length = len(x)

	while (count<length):
		url = x[count]
		print url
		path = "res/"+"/".join(url.split('/')[3:-1])
		if os.path.exists(path):
			pass
		else:
			#can't create the same path in os
			os.makedirs(path)
		count += 1
	return x;
def down_game(x,root):
	#download resource
	count = 1
	for res in x:
		#down img, js
		local = "res/"+"/".join(res.split('/')[3:])
		urllib.urlretrieve(res, local)
		s="资源总数："+str(len(x))+"，已下载："+str(count)
		root.event_generate("<<TIPS>>", when="tail")
		q.put(s)
		count +=1

def html_data(data):
	'''
	deal some complex situation
	some game html will be contained in site html
	we must deal it
	'''
	if(len(data)==1):
		#if only one html,we don't deal it
		return data[0]
	else:
		#if there are many htmls,we need the shortest html
		tmp = min(map(lambda x:len(x) ,data))
		tmp = filter(lambda x:len(x)==tmp,data)[0]

		return tmp

def down_html(filename):
	'''
	down and write html file
	'''
	f = open(filename)
	s = f.read()
	f.close()
	#down html
	reg=re.compile(r'<!.*>')
	x = re.findall(reg,s)
	x = html_data(x)

	if(x.find(r'\r')!=-1):
		x = x.split(r'\r\n')
	else:
		x = x.split(r'\n')
	ft = open("res/"+game_name+".html", 'w')
	#prettify html code
	for entry in x :
	    try:
	        ft.write(entry.replace(r'\"',r'"').replace(r'\t','')+'\n')
	    except:
	        log.error('write file error!')
	#close the file if we have written something in it
	ft.close()
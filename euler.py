#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
f = open("ProjectEuler.txt","w")
for i in range (1,10):
	try:
		soup = BeautifulSoup(urllib2.urlopen('https://projecteuler.net/problem='+str(i)))
	except:
		break;
	else:		
		try:
			problemHeader = soup.h2.string
			problemNumber = soup.h3.string
			problemStatement = soup.find(class_='problem_content').find_all('p')
			print "**************************************"
			print problemNumber
			print problemHeader
			print "\n".join([x.string for x in problemStatement])
			print "\n\n"
		except:
			continue	


'''
for row in soup.find_all(class_='MsoNormal'):
	if row.span:
		print row.span.contents[0]
		f.write(str(row.span.contents[0]))
'''
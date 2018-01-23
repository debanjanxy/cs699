import sys;
import getpass;
import re;
import requests;
import bs4;
import urllib;

login_url="http://moodle.iitb.ac.in/login/index.php" 
user=input('username:')
passwd=getpass.getpass()
session=requests.session()
result=session.post(login_url, data={'username':user,'password':passwd})
content=bs4.BeautifulSoup(result.text,'html.parser')
tag1=content.find('a', text=re.compile('699'))
course_url=tag1['href']
print("The course page is :")
print(course_url)
result1=session.post(course_url)
content1=bs4.BeautifulSoup(result1.text,'html.parser')
tag2=content1.find('a',href=re.compile('forum'))
forum_url=tag2['href']
print("The forum link ")
print(forum_url)
result2=session.post(forum_url)
content2=bs4.BeautifulSoup(result2.text,'html.parser')
print("the thread links are printed below"+ '\n')
count=0
tags=content2.findAll("td",{'class':'topic starter'})
for i in tags:
	thread_link=i.find('a').get('href')
	print(thread_link)
	result3=session.post(thread_link)
	#It is BeautifulSoup not "Beautifulsoup" :)
	content3=bs4.BeautifulSoup(result3.text,'html.parser')
	matchings = re.findall(r'.*Assignment.*',str(content3))
	tag3=content3.find("Assignment",count+1)  # now i need to open each link and search for assignemnt word and print the count of it 
	print(len(matchings)) 
      
	

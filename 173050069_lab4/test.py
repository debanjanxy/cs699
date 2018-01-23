from bs4 import BeautifulSoup
import getpass
import requests
import re

def start_moodle_session():
    start_url ="http://moodle.iitb.ac.in/mod/forum/discuss.php?d=62595"
    login_url="http://moodle.iitb.ac.in/login/index.php"
    user="173050069"
    passwd="Titi.1234"
    session=requests.session()
    result=session.post(login_url, data={'username':user,'password':passwd})
    if result.status_code != 200:
        print ("Error status", result.status_code, "when logging", login_url)
    return start_url,session


def get_page(url, session):
    result = session.get(url)
    if result.status_code != 200:
        print ("Error status", result.status_code, "when fetching", url)
    content = BeautifulSoup(result.text,'html.parser')
    return content

start_url,session = start_moodle_session()
soup = get_page(start_url,session)
nice_html = soup.prettify()
d = str(nice_html).split(' ')
print(d)
count = 0
for i in d:
    if "+1\n" in i:
        count = count+1
        #print(i)
print("Number = ",count)
lst = re.findall(r'.*\+1\n.*',nice_html)
print(len(lst))
'''
tags = soup.findAll('div',attrs={'class':'clearfix'})

#print(tags)
count = 0
matchobj = re.compile(r'\n+1\n',re.M)
#print(tags[0].text)
for div in tags:
    #value = div.find('p')
    lst = div.text
    #print(lst.split(' '))
    story = div.text
    #m = re.findall(r'.*\+1\n$',story,re.M)
    match_plus1 = matchobj.match(story)
    print(match_plus1)
    print(story)
    #count = count+len(m)
    if "+1\xa0" in story:
        count = count+1
#count = int(count/2)
print(count)   
#soup = BeautifulSoup(content,'html.parser')
#print(soup.findAll('div', attrs={'class':'posting fullpost'}))
count = 0
for div in soup.findAll('div', attrs={'class':'posting fullpost'}):
    a = div.find_all('p')
    for i in range(len(a)):
        if(a[i].contents[0]=='+1'):
            count = count+1
        print(a[i].contents[0])
print("Number of votes: ",count)
'''
#!/bin/python3
import sys;
import getpass;
import re;
import requests
import re;
import bs4;

def start_moodle_session():
  start_url ="http://moodle.iitb.ac.in/my"
  login_url="http://moodle.iitb.ac.in/login/index.php"
  user = sys.argv[1]
  passwd = sys.argv[2]
  session=requests.session()
  result=session.post(login_url, data={'username':user,'password':passwd})
  if result.status_code != 200:
    print ("Error status", result.status_code, "when logging", login_url)
  return start_url,session

#returns html contents of the webpage
def get_page(url, session):
  result = session.get(url)
  if result.status_code != 200:
    print ("Error status", result.status_code, "when fetching", url)
  content=bs4.BeautifulSoup(result.text,'html.parser')
  return content

#finds the number of +1's in each discussion thread.
def find_pattern(my_urls,session):
  for i in my_urls:
    flag = 0
    soup = get_page(i,session)
    nice_html = soup.prettify()
    lst = re.findall(r'\<p\>\+1\<p\>\n.*',nice_html)
    n = len(lst)
    if(n):
      print(n," +1\'s are present in link: ",i)
    else:
      print("Pattern not found in ",i)

#returns all the urls of discussion threads
def discussion_threads_urls(discuss_url,session):
	content = get_page(discuss_url, session)
	my_tag = re.findall(r'http\:\/\/moodle\.iitb\.ac\.in\/mod\/forum\/discuss\.php\?d=\d{5}',str(content))
	tag = content.find("a", href=re.compile('discuss'))
	my_tag = list(set(my_tag))
	thread_url = tag['href']
	return my_tag

def main(argv):
  start_url,session = start_moodle_session()
  content = get_page(start_url, session)
  tag = content.find("a", text=re.compile('699'))
  print (tag.text)
  course_url = tag['href']
  content = get_page(course_url, session)
  tag = content.find("a", href=re.compile('forum'))
  discuss_url = tag['href']
  print ("News forum link: ",discuss_url)
  my_urls = discussion_threads_urls(discuss_url,session)
  find_pattern(my_urls,session)
  return

if __name__ == "__main__":
	main(sys.argv)

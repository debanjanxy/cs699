#!/usr/bin/python3
import re

def encode_phone_number(mydata):
	match_phone = re.findall(r'\+91[ -][7-9]\d{9}', mydata)
	phone_num = len(match_phone)
	for i in range(len(match_phone)):
		match_phone[i] = re.sub(r'\d{10}',"**********",match_phone[i])
	for i in range(len(match_phone)):
		ph_new = re.sub(r'\+91[-][7-9]\d{9}',match_phone[i],mydata)
	return ph_new,phone_num

def encode_email_id(ph_new):
	match_mail = re.findall(r'[a-zA-Z][a-zA-Z0-9]*@[a-z]*\.[\w]*',ph_new)
	email_num = len(match_mail)
	mail_new = re.sub(r'[a-zA-Z][a-zA-Z0-9]*@[\w]*\.[\w]*',"xxx@yy.zz",ph_new)
	return mail_new,email_num
	
def encode_date(mail_new):
	dob = re.findall(r'\d{2}\.\d{2}\.\d{4}',mail_new)
	dob_num = len(dob)
	#dob = re.sub(r'[0-3][0-9]\.[0-1][1-9]\.\d{4}',"dd.mm.yyyy",mail_new)
	dob = re.sub(r'[0][1-9]\.[0][1-9]\.\d{4}',"dd.mm.yyyy",mail_new)
	dob = re.sub(r'[0][1-9]\.[1][0-2]\.\d{4}',"dd.mm.yyyy",dob)
	dob = re.sub(r'[1][0-9]\.[0][1-9]\.\d{4}',"dd.mm.yyyy",dob)
	dob = re.sub(r'[1][0-9]\.[1][0-2]\.\d{4}',"dd.mm.yyyy",dob)
	dob = re.sub(r'[2][0-9]\.[0][1-9]\.\d{4}',"dd.mm.yyyy",dob)
	dob = re.sub(r'[2][0-9]\.[1][0-2]\.\d{4}',"dd.mm.yyyy",dob)
	dob = re.sub(r'[3][0-1]\.[0][1-9]\.\d{4}',"dd.mm.yyyy",dob)
	dob = re.sub(r'[3][0-1]\.[1][0-2]\.\d{4}',"dd.mm.yyyy",dob)
	return dob,dob_num

def encode_roll(dob):
	x = re.findall(r'[1][7][3][0]\d{5}',dob)
	roll_num = len(x)
	roll = re.sub(r'[1][7][3][0]\d{5}',"1730*****",dob)
	return roll,roll_num

def encode_time(roll):
	time = re.findall(r'T(?i)ime: \d{2}\:\d{2}\:\d{2}',roll)
	time_num = len(time)
	#time = re.sub(r'[0-2][0-9]\:[0-5][0-9]\:[0-5][0-9]',"hh:mm:ss",roll)
	time = re.sub(r'[2][0-3]\:[0-5][0-9]\:[0-5][0-9]',"hh:mm:ss",roll)
	time = re.sub(r'[0-1][0-9]\:[0-5][0-9]\:[0-5][0-9]',"hh:mm:ss",time)
	return time,time_num

#MAIN PROGRAM
data = open('input.txt','r+')
mydata = data.read()
mydata,phone = encode_phone_number(mydata)
mydata,mail = encode_email_id(mydata)
mydata,date = encode_date(mydata)
mydata,roll = encode_roll(mydata)
mydata,time = encode_time(mydata)
f = open('output.txt','a')
f.seek(0)
f.truncate()
f.write(mydata)
f.write("--------------------------------")
f.write("\nStatistics: ")
f.write("\nNo. of valid phone numbers: ".rstrip('\n'))
f.write(str(phone))
f.write("\nNo. of valid mail ids: ".rstrip('\n'))
f.write(str(mail))
f.write("\nNo. of valid dates: ".rstrip('\n'))
f.write(str(date))
f.write("\nNo. of valid roll numbers: ".rstrip('\n'))
f.write(str(roll))
f.write("\nNo. of valid time formats: ".rstrip('\n'))
f.write(str(time))

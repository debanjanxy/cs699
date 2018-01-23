1)
Pattern of Indian mobile numbers: +91-9876543210
Pattern of masked mobile numbers: +91-**********
I have only considered mobile numbers which starts from 7,8 or 9.

2)
Pattern of email-id: something@something.something
Pattern of masked email-id: xxx@yy.zz

3)
Pattern of date: 20.03.1995
Pattern of masked date: dd.mm.yyyy

4)
Pattern of roll number: 173050069
Pattern of masked roll number: 1730*****

5)
Pattern of time: 21:23:34
Pattern of masked time: hh:mm:ss

Input: Write inputs in input.txt
Output: Check output.txt

Command: python solution.py

SAMPLE INPUT: 
Person 1: Mob: 9038424147 EmailID: abcd@gmail.com
person2: mob: +91-9038424147 email-id: dasdebanjan624@gmail.com
person3: mob: +91-7234556666 email-id: xyasdsa@abcd.nhj
My DOB: 20.03.1995
12.03.4567 is a date.
23:56:12 is in time format.
DOB1: 02.11.1994
time: 20:13:59
My roll no. : 173050069 time: 12:34:43
173050068 is a roll number.
873050069 is not a roll number.
False Time: 24:07:12
In-valid date: 32.11.1234

SAMPLE OUTPUT:
I am giving a list of test contacts of some persons:
Person 1: Mob: 9038424147 EmailID: xxx@yy.zz
person2: mob: +91-********** email-id: xxx@yy.zz
person3: mob: +91-********** email-id: xxx@yy.zz
My DOB: dd.mm.yyyy
dd.mm.yyyy is a date.
hh:mm:ss is in time format.
DOB1: dd.mm.yyyy
time: hh:mm:ss
My roll no. : 1730***** time: hh:mm:ss
1730***** is a roll number.
873050069 is not a roll number.
False Time: 24:07:12
In-valid date: 32.11.1234
--------------------------------
Statistics: 
No. of phone numbers: 2
No. of mail ids: 3
No. of valid dates: 4
No. of roll numbers: 2
No. of valid time formats: 3

#!/usr/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

users = [10,20,30,40,50,60,70,80,90,100,150,200,250,300,400,500,600,700,800,1000]
throughput = [1,2,3,4,5,6,7,8,8.5,8.7,8.8,8.9,8.99,9,9,9,9,9,9,9]
rt = [1,1,1,1,1,1,1,2,4,4.5,5,8,16,32,64,128,256,512,1024,2048]
uti = [1,2,8,16,32,64,128,256,512,1024,2048,2048,2048,2048,2048,2048,2048,2048,2048,2048]

plt.figure(1)
plt.plot(users,throughput)
plt.ylabel('No. of Users')
plt.xlabel('Throughput')
plt.savefig('plot1.pdf')

#histogram
plt.figure(2)
plt.hist(throughput,50)
plt.ylabel('No. of Users')
plt.xlabel('Throughput')
plt.savefig('plot2.pdf')

#line chart with red dots
plt.figure(3)
plt.plot(users,rt,'ro')
plt.ylabel('Response Time')
plt.xlabel('No. of Users')
plt.savefig('plot3.pdf')

#line chart
plt.figure(4)
plt.plot(users,uti)
plt.ylabel('Utilization')
plt.xlabel('No. of Users')
plt.savefig('plot4.pdf')

#bar chart
plt.figure(5)
objects = ('10','100','200','500','1000')
throughput = [1,4.5,8,9,9]
y_pos = np.arange(len(objects))
plt.bar(y_pos,throughput,align='center',facecolor='green',alpha=0.5)
plt.xticks(y_pos,objects)
plt.ylabel('Throughput')
plt.xlabel('No. of Users')
plt.savefig('plot5.pdf')

df = pd.DataFrame({'No. of Users':users,'Response Time':rt})
file_str = df.to_latex()
file = open("table.tex","w+")
file.write(file_str)
file.close()

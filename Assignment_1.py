import math as m
import numpy as np
import random as rnd
import matplotlib.pyplot as p
#1st Task
sat=[[0,0,0],[10,20,30],[120,130,140],[60,80,40],[150,200,180]]
time=[]
c=299792458  #speed of light in m/s(we will assume the distance unit to be in metre)
for i in range(5):
    tym=(100-sat[i][0])**2+(100-sat[i][1])**2+(100-sat[i][2])**2
    tym=m.sqrt(tym)
    tym=tym/c
    time.append(tym)
print("Given the satellite co-ordinates to be - ")
for i in range(5):print(sat[i])
print("The time taken to reach the GPS at (100,100,100) is respectively - ",time)
print("-------------------------------------------------------------------------------------------------")

# 2nd Task
r=[]
for i in range(5):
    r.append(time[i]*c)
A=[[2*(sat[i+1][0]-sat[i][0]),2*(sat[i+1][1]-sat[i][1]),2*(sat[i+1][2]-sat[i][2])] for i in range(3)]
B=[(r[i]**2-r[i+1]**2)-(sat[i][0]**2-sat[i+1][0]**2)-(sat[i][1]**2-sat[i+1][1]**2)-(sat[i][2]**2-sat[i+1][2]**2) for i in range(3)]
X=np.linalg.inv(A) #X=A^-1
X=np.dot(X,B)      #X=A^-1*B
print("The calculated co-ordinates are - ",X)
print("-------------------------------------------------------------------------------------------------")

#3rd Task 
r=[]
delta=rnd.randint(0,100)
for i in range(5):
    r.append((time[i]+delta/1000000000)*c)
A=[[2*(sat[i+1][0]-sat[i][0]),2*(sat[i+1][1]-sat[i][1]),2*(sat[i+1][2]-sat[i][2])] for i in range(3)]
B=[(r[i]**2-r[i+1]**2)-(sat[i][0]**2-sat[i+1][0]**2)-(sat[i][1]**2-sat[i+1][1]**2)-(sat[i][2]**2-sat[i+1][2]**2) for i in range(3)]
X=np.linalg.inv(A) #X=A^-1
X=np.dot(X,B)      #X=A^-1*B
error=m.sqrt((X[0]-100)**2+(X[1]-100)**2+(X[2]-100)**2)
print("The calculated co-ordinates are(with random error- ",error,") - ",X)
# print("Error is - ", error)
# print("delta is - ",delta)
# print(A,B,end="     ")
print("-------------------------------------------------------------------------------------------------")

#4th task
timing_error=[]
localisation_error=[]
for j in range(20):
    r=[]
    delta=rnd.randint(0,1000)
    timing_error.append(delta)
    for i in range(5):
        r.append((time[i]+delta/1000000000)*c)
    A=[[2*(sat[i+1][0]-sat[i][0]),2*(sat[i+1][1]-sat[i][1]),2*(sat[i+1][2]-sat[i][2])] for i in range(3)]
    B=[(r[i]**2-r[i+1]**2)-(sat[i][0]**2-sat[i+1][0]**2)-(sat[i][1]**2-sat[i+1][1]**2)-(sat[i][2]**2-sat[i+1][2]**2) for i in range(3)]
    X=np.linalg.inv(A) #X=A^-1
    X=np.dot(X,B)      #X=A^-1*B
    # print("The calculated co-ordinates are(with random error) - ",X)
    error=m.sqrt((X[0]-100)**2+(X[1]-100)**2+(X[2]-100)**2)
    localisation_error.append(error)
    # print(A,B,end="     ")
#Plotting the graph
figure,axis = p.subplots()
axis.plot(timing_error,localisation_error, color='black',marker='o')
axis.set_xlabel('Error in Timing(ns) ')
axis.set_ylabel('Error in Localisation')
axis.set_title('Error Correlation b/w Timing Error and Localisation Error')
p.show()



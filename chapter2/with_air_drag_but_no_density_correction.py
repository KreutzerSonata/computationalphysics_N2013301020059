# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt
t=[]
dt=0.01
B_2_m=4*10**(-5)
g=9.8
end_time = 200
a=22.5*math.pi/180
b=45*math.pi/180
c=67.5*math.pi/180
angle = [a,b,c]
t.append(0)
x_1=[]
v_x_1=[]
y_1=[]
v_y_1=[]
x_1.append(0)
y_1.append(0)
v_x_1.append(700*math.cos(angle[0]))
v_y_1.append(700*math.sin(angle[0]))
for i in range(int(end_time/dt)):
	m=x_1[i]+v_x_1[i]*dt
	x_1.append(m)
	n=v_x_1[i]-B_2_m*((v_x_1[i]**2+v_y_1[i]**2)**0.5)*v_x_1[i]*dt
	v_x_1.append(n)
	o=y_1[i]+v_y_1[i]*dt
	y_1.append(o)
	p=v_y_1[i]-g*dt-B_2_m*((v_x_1[i]**2+v_y_1[i]**2)**0.5)*v_y_1[i]*dt
	v_y_1.append(p)
	#print x_1[-1],y_1[-1]
    	if o <= 0 :
    		break
print x_1[-1],y_1[-1]

x_2=[]
v_x_2=[]
y_2=[]
v_y_2=[]
x_2.append(0)
y_2.append(0)
v_x_2.append(700*math.cos(angle[1]))
v_y_2.append(700*math.sin(angle[1]))
for i in range(int(end_time/dt)):
	m=x_2[i]+v_x_2[i]*dt
	x_2.append(m)
	n=v_x_2[i]-B_2_m*((v_x_2[i]**2+v_y_2[i]**2)**0.5)*v_x_2[i]*dt
	v_x_2.append(n)
	o=y_2[i]+v_y_2[i]*dt
	y_2.append(o)
	p=v_y_2[i]-g*dt-B_2_m*((v_x_2[i]**2+v_y_2[i]**2)**0.5)*v_y_2[i]*dt
	v_y_2.append(p)
	#print x_2[-1],y_2[-1]
    	if o <= 0 :
    		break
print x_2[-1],y_2[-1]
		
x_3=[]
v_x_3=[]
y_3=[]
v_y_3=[]
x_3.append(0)
y_3.append(0)
v_x_3.append(700*math.cos(angle[2]))
v_y_3.append(700*math.sin(angle[2]))
for i in range(int(end_time/dt)):
	m=x_3[i]+v_x_3[i]*dt
	x_3.append(m)
	n=v_x_3[i]-B_2_m*((v_x_3[i]**2+v_y_3[i]**2)**0.5)*v_x_3[i]*dt
	v_x_3.append(n)
	o=y_3[i]+v_y_3[i]*dt
	y_3.append(o)
	p=v_y_3[i]-g*dt-B_2_m*((v_x_3[i]**2+v_y_3[i]**2)**0.5)*v_y_3[i]*dt
	v_y_3.append(p)
	#print x_3[-1],y_3[-1]
    	if o <= 0 :
    		break
print x_3[-1],y_3[-1]

plt.figure(figsize=(8,6))
plt.plot(x_1,y_1,label="$22.5^\circ$",color="red",linewidth=2)
plt.plot(x_2,y_2,label="$45^\circ$",color="green",linewidth=2)
plt.plot(x_3,y_3,label="$67.5^\circ$",color="black",linewidth=2)
plt.xlabel("x(m)")
plt.ylabel("y(m)")
plt.ylim(0,15000)
plt.legend()
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import *
from visual import *

x=[0]
y=[1]
z=[0]
v=31
vx=31
vy=0
vz=0
dt=0.01

w=200*pi/3

ax=-(0.0039+0.0058/(1+exp((31-35)/5)))*v*31
ay=-9.8
az=-4.1*10**(-4)*31*w
ball=sphere(pos=(-6,1,0), radius=0.1,color=color.red)

i=0
while y[i]>=0:
    x.append(x[i]+vx*dt)
    y.append(y[i]+vy*dt)
    z.append(z[i]+vz*dt)
    vx=vx+ax*dt
    vy=vy+ay*dt
    vz=vz+az*dt
    v=(vx**2+vy**2+vz**2)**0.5
    ax=-(0.0039+0.0058/(1+exp((v-35)/5)))*v*vx
    az=-4.1*10**(-4)*vx*w
    i=i+1


fig = plt.figure(figsize=(8,5))
ax = Axes3D(fig)


plt.xlabel("x(m)")
plt.ylabel("y(m)")
ax.set_zlabel("z(m)")
plt.title("trajectory of battedball")
ax.set_zlim(-1,1)
#plt.ylim(-1.2,1.2)


ax.plot(x, y, z,label="trajectory",color="green",linewidth=2)
ax.scatter(x[0],y[0],z[0],label="initial position",color="red")
ax.scatter(x[-1],y[-1],z[-1],label="final position",color="black")
plt.legend()
plt.show()


box=box(pos=vector(0,0,-0.5),size=(17,10,0.01),color=color.orange)
arrow(pos=(-6,0,2),axis=(5,0,0), shaftwidth=0.01)
arrow(pos=(-6,0,2),axis=(0,3,0), shaftwidth=0.1)
arrow(pos=(-6,0,2),axis=(0,0,5), shaftwidth=0.1)
ball=sphere(pos=(x[0]-6,y[0],z[0]), radius=0.3,color=color.red)
ball=sphere(pos=(x[-1]-6,y[-1],z[-1]), radius=0.3,color=color.black)
j=0
while j<=i:
    ball=sphere(pos=(x[j]-6,y[j],z[j]), radius=0.1,color=color.blue)
    rate(20)
    j=j+1
#print x[-1],y[-1],z[-1];13.5037105294 -0.0143 -0.265878000108

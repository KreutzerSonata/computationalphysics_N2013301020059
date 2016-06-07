from math import *
from visual import *
import numpy as np
import matplotlib.pyplot as plt

initialangle=60
theta=[initialangle]
time=[0]
omega,i,dt=0,0,0.01

while time[i]<=100:
    theta.append(theta[i]+(omega-(4.9*sin((theta[i]+0.5*omega*dt)*pi/180))*dt)*dt)
    omega=omega-(9.8*sin((theta[i]+0.5*omega*dt)*pi/180))*dt        
    i=i+1
    time.append(i*dt)

print '''
scene=display(width=600,height=600)
arrow(pos=vector(0,1,0),axis=vector(0,0,1.7), shaftwidth=0.02,fixedwidth=1, color=color.green)
arrow(pos=vector(0,1,0),axis=vector(0,-2.2,0), shaftwidth=0.02,fixedwidth=1, color=color.green)
ball=sphere(pos=(0,1-cos(theta[0]*pi/180),sin(theta[0]*pi/180)),radius=0.05, color=color.red)
ball.trail = curve(color=color.blue)



j=1
while 50*j<=i:
    ball.pos=vector(0,1-cos(theta[50*j]*pi/180),sin(theta[50*j]*pi/180))
    ball.trail.append(pos = ball.pos)
    rate(20)
    j=j+1

print '''
plt.figure(figsize=(8,6), dpi=80)
plt.xlabel("time(s)")
plt.ylabel("$\Theta$")
plt.title("Simulation of the pendulum,g=9.8,l=1.0,initialangle="+str(initialangle))
plt.plot(time,theta,color="orange",label="position",linewidth=2)
plt.legend()
plt.show()


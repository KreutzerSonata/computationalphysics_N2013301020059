[本次作业实验报告Markdown格式实验报告](https://www.zybuluo.com/Memorieddd/note/316373)
# **第一章习题1.3实验报告** #
##一、题目
It is often the case that the frictional force on an object will increase as the object moves faster. A fortunate example of this is a parachutist; the role of the parachute is to produce a frictional force due to air drag, which is larger than would normally be the case without the parachute. The physics of air drag will be discussed in more detail in the next chapter. Here we consider a very simple example in which the frictional force depends on the velocity. Assume that the velocity of an object obeys an equation of the form


where a and b are constants. You could think of a as coming from an applied force, such as gravity, while b arises from friction. Note that the frictional force is negative (we assume that b > 0), so that it opposes the motion, and that it increases in magnitude as the velocity increases. Use the Euler method to solve (1.10) for v as a function of time.- A convenient choice of parameters is a = 10 and b = 1. You should ﬁnd that 1; approaches a constant value at long times; this is called the terminal velocity.
$$\frac{dv}{dt}=a-bv$$
##二、欧拉方法分析
$$v(\Delta t)=V(0)+\frac{dv(t)}{dt}\Delta t+\frac{1}{2} \frac{d^2v(t)} {d^2t}(\Delta t)^2+······$$
只保留一阶项有：
$$V(\Delta t)≈V(0)+\frac{dv}{dt}\Delta t$$整理的：
$$\frac{dv(t)}{dt}=\lim_{\Delta t\to 0} \frac{v(t+\Delta t)-v(t)}{\Delta t}≈ \frac{v(t+\Delta t)-v(t)}{\Delta t}$$
因为：$\frac{dv}{dt}=a-bv$，带入上式得：
$$v(t+\Delta t)≈v(t)+(a-bv)\Delta t$$
##三、代码及其注释
```python
import numpy as np
import matplotlib.pyplot as plt  #to import matplotlib's package

v=[]       #velocity
t=[]       #time
a=10       #assign a value to a
b=1        #assign a value to b
det_t=0.05     #time step
v.append(0) #assign a value to first item of v[]
t.append(0) #assign a value to first item of t[]
end_time=15  #total time

for i in range(int(end_time/det_t)):
    tmp=v[i]+(a-b*v[i])*det_t  #Euler method
    v.append(tmp)  #add new value of v to v[]
    t.append(det_t*(i+1)) #add new value of t to t[]
    print t[-1],v[-1] #print the value of v and t on each stap

plt.figure(figsize=(8,6))  #set the size of corresponding figure
plt.plot(t,v,label="v(t)",color="black",linewidth=1) #plot the figure and set label and color and linewidth of the figure
plt.xlabel("t(s)")   #set the label of x axis
plt.ylabel("v(m/s)")  #set the label of y axis
plt.title("a=10,b=1,v=0") #set title
plt.ylim(0,25) #set the range of y axis
plt.legend()  #make it to show everything
plt.show()  #activate
```
并画出图像得：
####初速度为0时：
![当初速度为0时](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter1/figure_1%28V%29%3D0%29.png)
####初速度为20m/s时:
![当初速度为20时](https://raw.githubusercontent.com/Memorieddd/computationalphysics_N2013301020059/master/chapter1/figure_2%28V0%3D20%29.png)

##结论
#####降落伞模型中，如果速度低于10m/s,此时重力大于阻力，速度会增加，到10m/s后，此时重力等于阻力，速度保持恒定，然后匀速下降；
同样如果速度高于10m/s,此时重力小于阻力，速度会降低，到10m/s后，此时重力等于阻力，速度保持恒定，然后匀速下降；
（在此不支持markdown公式格式）




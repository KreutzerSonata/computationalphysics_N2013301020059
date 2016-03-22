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




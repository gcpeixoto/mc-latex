from matplotlib.pyplot \
import figure,plot,title,savefig
from numpy import linspace
from math import exp

def relu(x):
    return max(0.0, x)

def sigmoid(x,a):
    return 1.0 / (1.0 + exp(-a*x))

# plot
x = [v for v in linspace(-5,5,50)]
r = [relu(v) for v in x ]
s05 = [sigmoid(v,0.5) for v in x ]
s1 = [sigmoid(v,1) for v in x ]
s2 = [sigmoid(v,1.5) for v in x ]

figure(figsize=(6,4))
plot(x,r)
title('relu function')
savefig('../figs/relu.png')
figure(figsize=(6,4))
plot(x,s05,'r',x,s1,'g',x,s2,'b')
title('sigmoid function')
savefig('../figs/sigmoid.png')

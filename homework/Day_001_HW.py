import numpy as np
import matplotlib.pyplot as plt

w = 3 
b= 0.5 

def mean_absolute_error(y,yp):
    mae= sum(abs(y-yp)/len(y))
    
    return mae

def mean_square_error(y,yp):
    mse= sum((y-yp)**2)/len(y)
    return mse
x_lin= np.linspace(0,100,101)
print(x_lin)
y = (x_lin + np.random.randn(101)*5)*w+b
print(y)

plt.plot(x_lin, y, "b.", label=" Data ")
plt.title( "Assume we have data points")

y_hat= x_lin*w+b
plt.plot(x_lin, y_hat, "r-", label= "prediction")
plt.legend(loc=2)
plt.show()

mean= mean_absolute_error(y, y_hat)
mean2= mean_square_error(y,y_hat)
print(" The mean absolute error is %.3f" %(mean))
print(" The mean square error is %.3f" %(mean2))
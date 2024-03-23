#plottask.py
#Wite a program that displays: 
#A Histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
#A Plot of the function h(x)=x^3 in the range of 0 to 10 
#On the one set of axes
#Author: Brianne McGrath 

import numpy as np 
import matplotlib.pyplot as plt

mean = 5
std_dev = 2
data = np.random.normal(mean, std_dev, 1000)

#Plotting histogram 
plt.hist(data, bins=30, density=False, alpha=0.5, color='m', label='Normal Distribution')

#Define the function
def h(x):
    return x ** 3 

#Generate x vales in the range of 0 to 10
x_values = np.linspace(0, 10, 100)
#Calculate corresponding y values using h(x)
y_values = h(x_values)

#Plotting function 
plt.plot(x_values, y_values, 'r-', label='$h(x) = x^3$')
         
#Labels, titles and legend
plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Histogram of Normal Distribution and $h(x) = x^3$ Function')
plt.legend()

#Display 
plt.grid(True)
plt.show()
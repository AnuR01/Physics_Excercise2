#Question 1
'''1. Let us consider the logistic map
xn+1=rxn(1−xn),
where r is a real number and the iteration starts from some initial condition x0.
Write a code which iterates this expression.
Check if your code works correctly:'''
# If we use the values r=1.5 and x0=0.1, we should get x11≈0.3323
#initail value:

import numpy as np;
num_initial = 0.1
num_final = 11
r = 1.5

for n in range (num_final):
    num_new = r*num_initial*(1-num_initial)
    num_initial = num_new
print(num_new)

#If we use the values r=2.9 and x0=0.5, we should get x50≈0.6548
#initail value:
import numpy as np;
num_initial = 0.5
num_final = 50
r = 2.9

for n in range (num_final):
    num_new = r*num_initial*(1-num_initial)
    num_initial= num_new
print(num_new)



#Question 2
'''Let us again consider the mass hanging from a spring using Euler's method, but let us 
now also include a simple model for air resistance. In this case, the discretised equations 
of motion can be written as
xn+1 = xn+Δt⋅vn,
vn+1 = vn−Δt⋅[g-(k/m)⋅(xn−L)-(b/m)⋅vn],
x0 = = x0,
v0 = v0.

What's new is the term −bmvn
 on the second row, with b
 some coefficient indicating the strength of the resistance.

Modify the code "Mass_spring_Euler.py" that we wrote during the lecture so that it takes into account the air resistance as described above. You can find the code under the same link as the lecture notes and recordings, inside the folder "Codes".

Try to run the code with the following parameters:
g=10;  k=1;  m=1;  L=0; b=0,25;
x0 =1;   v0=0;
t0 = 0; tmax=20;  Δt=0.01'''

# Path: Mass_spring_Euler.py
import numbers as np;
import matplotlib.pyplot as plt
g = 10
k = 1
m = 1
L = 0
b = 0.25

#Initial values
x_0 = 1
v_0 = 0

#Variable related to time:
t_0 = 0
t_max = 20 
del_t = 0.01
# Initialise the variables:
x = x_0
v = v_0
t = t_0

#Arrays to hold the values
x_array = [x_0]
v_array = [v_0]
t_array = [t_0]

# Iterate time
while t < t_max:
    x_new = x + del_t * v
    v_new = v + del_t * (g - k/m * (x-L) - b/m * v)
    t_new = t + del_t

    #update the values
    x = x_new
    v = v_new
    t = t_new

    # Add new values to arrays
    x_array.append(x)
    v_array.append(v)
    t_array.append(t)

#Plot the data
fig, ax = plt.subplots()
ax.plot(t_array, x_array)
plt.show()
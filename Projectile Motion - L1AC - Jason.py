import numpy as np                  # api for math for inputing the sin cos tan
import matplotlib.pylab as plt      # api for plotting the graph
import math as m                    # api for math for inputing the angle

#initialize variables
#velocity, gravity
v1 = int(input("Enter your velocity: "))
g = 9.8
angle1 = m.radians(int(input("Enter the desired angle: ")))      # for inputing the angle must use m.radians

formulat1 = ((2*v1)*np.sin(angle1))/g               # formula to find the time
formulatv1 = formulat1 * np.linspace(0,1)              # formula to find the time vector. Linspace = for loop between 0 and 1
x1 = (v1 * formulatv1) * np.cos(angle1)                  # x for finding the distance
y1 = (v1 * formulatv1) * np.sin(angle1) - (g/2) * (formulatv1**2)      # y for finding the height

v2 = int(input("Enter your velocity: "))
g = 9.8
angle2 = m.radians(int(input("Enter the desired angle: ")))      # for inputing the angle must use m.radians

formulat2 = ((2*v2)*np.sin(angle2))/g               # formula to find the time
formulatv2 = formulat2 * np.linspace(0,1)              # formula to find the time vector. Linspace = for loop between 0 and 1
x2 = (v2 * formulatv2) * np.cos(angle2)                  # x for finding the distance
y2 = (v2 * formulatv2) * np.sin(angle2) - (g/2) * (formulatv2**2)      # y for finding the height

v3 = int(input("Enter your velocity: "))
g = 9.8
angle3 = m.radians(int(input("Enter the desired angle: ")))      # for inputing the angle must use m.radians

formulat3 = ((2*v3)*np.sin(angle3))/g               # formula to find the time
formulatv3 = formulat3 * np.linspace(0,1)              # formula to find the time vector. Linspace = for loop between 0 and 1
x3 = (v3 * formulatv3) * np.cos(angle3)                  # x for finding the distance
y3 = (v3 * formulatv3) * np.sin(angle3) - (g/2) * (formulatv3**2)      # y for finding the height



plt.title("Projectile Motion Example", fontsize = 24)       # Title in the plot
plt.xlabel("x - coordinates", fontsize = 16)            # x coordinates
plt.ylabel("y - coordinates", fontsize = 16)            # y coordinates

plt.plot(x1,y1,label="ball1")           #show the plot for x1,y1
plt.plot(x2,y2,label="ball2")           #show the plot for x2,y2
plt.plot(x3,y3,label="ball3")           #show the plot for x3,y3
plt.legend()                # legend

plt.show()          # print the plot

# Reference from Eris



'''
import numpy as np
import matplotlib.pylab as plot

#initialize variables
#velocity, gravity
v = 25
g = -9.8
#increment theta 25 to 60 then find  t, x, y
#define x and y as arrays
theta = np.arange(250)

t = ((2 * v) * np.sin(theta)) / g #the total time projectile remains in the #air
t1 = np.array(t) #why are some negative



x = ((v * t1) * np.cos(theta))
y = ((v * t1) * np.sin(theta))

plot.plot(x,y)
plot.show()
'''

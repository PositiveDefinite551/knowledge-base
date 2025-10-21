import matplotlib.pyplot as plt
import math


def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

def circumference_radius(n,a):
    return a/(2*math.sin((math.pi)/n))

def polygon_plot(n, a):
    #r = 6
    r = circumference_radius(n, a)
    #r = a*math.sin(math.pi/2-math.pi/(2*n))/math.sin(math.pi/n) #Radius des Kreises
    t = [i/1000 for i in range(0, 6280)]
    x = [r*math.cos(i) for i in t]
    y = [r*math.sin(i) for i in t]
    plt.plot(x, y, label='Kreis')
    
    m = len(t)//n
    k=0
    a1=a2=[]
    tj = [i/1000 for i in range(0,6280,m)]
    last = 0
    for k in range(len(tj)-1):
        #a1.append(sin(t[k]))
        #a2.append(cos(t[k]))
        plt.plot([r*math.sin(tj[k]),r*math.sin(tj[k+1])], [r*math.cos(tj[k]), r*math.cos(tj[k+1])])
        print(k)
        last = k+1
    plt.plot([r*math.sin(tj[0]),r*math.sin(tj[k+1])], [r*math.cos(tj[0]), r*math.cos(tj[k+1])])



polygon_plot(7, 2)
#plt.plot([i/100 for i in range(-120,120)], [i/100 for i in range(-120,120)])
plt.grid(True)
plt.show()

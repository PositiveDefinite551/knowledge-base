import matplotlib.pyplot as plt
import math

def parabel_geo_vis(m,F, l, parabel_x, parabel_y):
    plt.scatter([parabel_x[m]],[parabel_y[m]],color = "red", alpha=0.1)
    plt.plot([F[0], parabel_x[m]],[F[1], parabel_y[m]], color = "grey",  alpha=0.1)
    plt.plot([parabel_x[m], parabel_x[m]],[l, parabel_y[m]], color = "grey",  alpha=0.1)

def parabel(F, l):
    x = [x/100 for x in range(-1000, 1000,1)]
    y = [y/100 for y in range(-1000, 1000,1)]
    
    parabel_x = []
    parabel_y = []
    for xj in x:
        for yj in y:
            if (abs(yj-l)==((xj-F[0])**2+(yj-F[1])**2)**(1/2)):
                parabel_x.append(xj)
                parabel_y.append(yj)
    plt.grid(True)
    plt.plot(parabel_x, parabel_y)
    plt.plot(parabel_x, [-1 for xj in parabel_x])
    #------------------------------------
    for k in range(0,len(parabel_x),2):
        parabel_geo_vis(k,F,l, parabel_x, parabel_y)
    #------------------------------------
    plt.scatter([F[0]],[F[1]],color = "red")
    


plt.show()
parabel((0,1),-1)
    

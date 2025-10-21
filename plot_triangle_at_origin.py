import matplotlib.pyplot as plt
import numpy as np

def triangle_at_origin(u,v):
    a = np.rad2deg(np.arccos( np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v)) ))
    x = [0, u[0], v[0]]
    y = [0, u[1], v[1]]
    plt.plot(x,y)
    plt.text(0,1, "Angle = "+str(round(a,2)) )
    plt.fill(x,y, alpha = 0.3)
    
    return a

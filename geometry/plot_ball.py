import numpy as np
import matplotlib.pyplot as plt


def plot_ball(r=1):
    """
    Plots a sphere with radius r centered at the origin
    Args:
       r (int): Radius

    """
    u = np.linspace(0, 2*np.pi, 100)
    v = np.linspace(0, 2*np.pi, 100)
    
    
    u,v = np.meshgrid(u,v)
    
    
    
    x = r*np.cos(u)*np.sin(v)
    y = r*np.sin(u)*np.sin(v) 
    np.meshgrid(x,y)
    z = r*np.cos(v)
    
    
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot_surface(x,y,z)
    
plot_ball()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
from sympy import S


def paraboloide_plot(a,b,c,x0,y0, ax):
   """
   Plots a paraboloid given by the equation z = a*(x-x0)**2 + b*(y-y0)**2 + c with a respect to z
   """
    x = np.linspace(-5,5,100)
    y = np.linspace(-5,5,100)
    x,y = np.meshgrid(x,y)
    z = a*(x-x0)**2 + b*(y-y0)**2 + c
    ax.plot_surface(x,y,z, color="red", alpha = 0.8)

    
def zeroes_paraboloide_z0(a,b,c,x0,y0, ax):
   """
   Calculates and plots the intersection curve of a paraboloid given
   by a*(x-x0)**2 + b*(y-y0)**2 + c with a respect to z with the plane z=0/
   """
    #---------find zeroes of the paraboloid-----------------------
    x,y = sy.symbols('x, y')
    expr = a*(x-x0)**2 + b*(y-y0)**2 + c
    equa = sy.Eq(expr, 0)
    sol = sy.nonlinsolve([equa],[x,y], S.Reals)
    
    #----------substitute numbers, get two curves-----------------
    t1,t2 = sol
    k = np.linspace(-5,5,100)
    f1 = [t1[0].evalf(50, subs={y: xj}) for xj in k]
    f2 = [t2[0].evalf(50, subs={y: xj}) for xj in k]
    
    #-----------filter out complex numbers------------------------
    f1 = [t for t in f1 if t.is_real]
    f2 = [t for t in f2 if t.is_real]
    k = np.linspace(-5,5,len(f1)) #adjust the length of the free variable set
    z = [0 for j in f1]
    
    #----------plot-3d---------------------------------------------
    ax.plot(f1,k,z, color="blue")
    ax.plot(f2,k,z, color="blue")
    

def paraboloide_mit_nst_plot(a,b,c,x0,y0, ax): #
    paraboloide_plot(a,b,c,x0,y0, ax)
    zeroes_paraboloide_z0(a,b,c,x0,y0, ax)
    

#--------------plot the figure-----
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
paraboloide_mit_nst_plot(1,1,-10,1,-1, ax) # EXAMPLE
plt.show()

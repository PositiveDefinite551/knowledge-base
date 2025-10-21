import matplotlib.pyplot as plt
import math

def dreieck_plot(x1,y1,x2,y2,x3,y3):
  """
  plots a triangle givem by coordinates
  """
    plt.plot([x1, x2, x3], [y1,y2, y3])
    plt.fill([x1, x2, x3], [y1,y2, y3])

def dreieck_seiten(x1,y1,x2,y2,x3,y3):
  """
  calculates the sides of a triangle
  """
    return ((x1-x2)**2+(y1-y2)**2)**(1/2), ((x3-x2)**2+(y3-y2)**2)**(1/2), ((x1-x3)**2+(y1-y3)**2)**(1/2)

def dreieck_winkel(x1,y1,x2,y2,x3,y3):
  """
  calculates the angles of a triangle
  """
    def cos_theorem(a,b,c):
        return math.acos((c**2-a**2-b**2)/(-2*a*b))
    a,b,c = dreieck_seiten(x1,y1,x2,y2,x3,y3)
    return cos_theorem(a,b,c), cos_theorem(c, a,b), cos_theorem(b, c, a)

def dreieck_st(x1,y1,x2,y2,x3,y3, deg):
  """
  plots a triangle, together with side lengthes and angles (optionally in radians)
  """
    c,a,b = dreieck_seiten(x1,y1,x2,y2,x3,y3)
    B, C, A = dreieck_winkel(x1,y1,x2,y2,x3,y3)
    if deg:
        C *= 360/(math.pi*2)
        A *= 360/(math.pi*2)
        B *= 360/(math.pi*2)
    C = round(C, 2)
    A = round(A, 2)
    B = round(B, 2)
    dreieck_plot(x1,y1,x2,y2,x3,y3)
    plt.text(x3,y3, f"A={A}")
    plt.text(x2,y2, f"B={B}")
    plt.text(x1,y1, f"C={C}")
    
    plt.text((x1+x2)/2,(y1+y2)/2, f"c={c}")
    plt.text((x3+x2)/2, (y3+y2)/2,f"a={a}")
    plt.text((x3+x1)/2, (y3+y1)/2, f"b={b}")

    dreieck_plot(x1,y1,x2,y2,x3,y3)


#-----------
dreieck_st(5,4,-1,3,9,9, True) # Example

plt.grid(True)
plt.show()

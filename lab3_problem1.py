import numpy as np
def triangle(x,y):
    theta= np.arctan(x/y) * 180 / np.pi
    gamma= np.arctan (x/y) * 180 / np.pi
    d= np.sqrt(x**2 + y**2)
    s= 1/ np.cos(theta * np.pi / 180)
    return theta, gamma, d, s 
myresult = triangle(3,4)

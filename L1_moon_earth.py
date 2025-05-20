
import math

def f(r):
    G = 6.674e-8 #cm^3 g^-1 s^-2
    M = 5.974e27 # Earth mass in g
    m = 7.348e25 # Moon mass in g
    R = 3.844e10 # Earth-Moon distance in cm
    w = math.sqrt(G*M/R**3) # Satellite and moon angular frequence
    
    return G*M/r**2 -G*m/(R-r)**2 - w*r**2

def der_f(x):
        h = 1e-6
        return (f(x+h/2)-f(x-h/2))/h
    
def newton(r0, r):
    tol = 1e-6
    while abs(r-r0)>tol:
        r = r0 - f(r0)/der_f(r0)
        r0 = r
    return r

def bisection(x1, x2):
    iter = 0
    tol = 1e-6
    if f(x1)*f(x2)>0:
        return 0
    else:
        while abs(x1-x2)>tol:
            if f(x1)*f(x2)<0:
                x = ((x1+x2)/2)
                if f(x)*f(x2)<0:
                    x1 = x
                elif f(x)*f(x1)<0:
                    x2 = x   
            iter +=1 
        
    print("Bisection iterations:", iter)  
    return x 


print(f"{newton(8e9,7e9)/1e5:.2f} km") # Very sensitive to r0,r and h
print(f"{bisection(1e8,1e2)/1e5:.2f} km") # res = 35km: there's something wrong!

    
import math

def f(x):
    return x - F - e*math.sin(x)   

def der_f(x):
    h = 1e-6
    return (f(x+h/2) - f(x-h/2))/h

# RELAXATION METHOD
def relaxation(Eold,E,e,F):  
    tol = 1e-6
    iter = 0
    while abs(E-Eold)>tol:
        Eold = E
        E = F +e*math.sin(Eold)
        iter+=1
    print("Relaxation iterations:", iter)
    return E

# BISECTION METHOD
def bisection(x1, x2,e,F):
    iter = 0
    tol = 1e-6
    if f(x1)*f(x2)>0:
        return 0
    else:
        while abs(x1-x2)>tol:
            # print((x1,x2))
            if f(x1)*f(x2)<0:
                x = ((x1+x2)/2)
                # print(x)
                if f(x)*f(x2)<0:
                    x1 = x
                elif f(x)*f(x1)<0:
                    x2= x   
            iter +=1 
        
    print("Bisection iterations:", iter)  
    return x       

# NEWTON METHOD
def newton(x0,x,e, F):
    tol = 1e-6      
    iter = 0
    while abs(x-x0)>tol:
        x0 = x
        x = x0 - f(x0)/der_f(x0)
        iter +=1
        # print(x-x0)
    print("Newton iterations:", iter)  
    return x
        

e , F = 0.9,math.pi
x1,x2 =1,4

print(f"Relaxation : E = {relaxation(x1,x2,e,F):.6f}")
print(f"Bisection: E = {bisection(x1,x2,e,F):.6f} (if = 0 : change interval)")
print(f"Newton: {newton(x1,x2,e,f):.6f}")

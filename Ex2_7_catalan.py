"""
Exercise 2.7: Catalan numbers
The Catalan numbers Cn are a sequence of integers 1, 1, 2, 5, 14, 42, 132. . . that play an important role in quantum mechanics and the theory of disordered systems. (They were central to Eugene Wigner’s proof of the so-called semicircle law.) They are given by
C0 = 1, Cn+1 = (4n + 2)/(n+2)  * Cn. 
Write a program that prints in increasing order all Catalan numbers less than or equal to one billion.
"""

def catalan(n):
    if n ==0:
        return 1    
    return int((4*(n-1)+2)/((n-1)+2) * catalan(n-1))

c = [-1]
i=0
while c[-1]<1e9:
    c.append(catalan(i))
    i+=1

c.pop(0) # to remove the first element (needed for the while condition)
print(f"n = {len(c)} iterations")    
print(c)
"""
Exercise 2.11: Binomial coefficients
The binomial coefficient (n,k) is an integer equal to

(n,k) = n!/((n-k)! * k!)

when k ≥ 1 , or (n,0) = 1 when k = 0.
"""
"""
a)Using this form for the binomial coefficient,
write a user-defined function binomial(n,k) that calculates the binomial coefficient for given n and k.
Make sure your function returns the answer in the form of an integer (not a float)
and gives the correct value of 1 for the case where k = 0."""

def factorial(n):
    if n==0: return 1
    return n * factorial(n-1)

def binomial(n,k):
    if k==0: return 1
    if n>=k:
        return int(factorial(n)/(factorial(n-k) * factorial(k)))
    else: raise ValueError("k must be <=n")
 
n= 3
k =2
print(f"Binomial({n},{k}):", binomial(3,2))

"""
b) Using your function write a program to print out the first 20 lines of “Pascal’s triangle.”
The nth line of Pascal’s triangle contains n + 1 numbers,
which are the coefficients (n0), (n1), and so on up to (n)
"""
def pascal_triang(n):
    triang = []
    for l in range(1,n+1):
        layer= []
        for k in range(l+1):
            layer.append(binomial(l,k))
        triang.append(layer)
    for layer in triang:
        print(*layer)
 
print("Pascal Triangle")
pascal_triang(4)

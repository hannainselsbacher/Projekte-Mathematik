from functools import cache
#@cache

#-------------------------------------------------------------------------------------------------------------------
#standard fibonacci implementation 
def stfib(n): 
    if n in {0, 1}: 
        return n 
    else: 
        return stfib(n-2) + stfib(n-1)


list = [stfib(n) for n in range (20)]   #list with the first x fibonacci numbers 
print(list)                             
print(list[-1])                         #n'th fibonacci number 

#-------------------------------------------------------------------------------------------------------------------
#fibonacci numbers with cache 
c = [ -1 ] * 10**6

def fibo(n): 
    if c[n] != -1:
        return c[n]
    if n in {0, 1}: 
        c[n] = n
        return n 
    else: 
        c[n] = fibo(n-2) + fibo(n-1)
        return c[n]

print(fibo(500))

#--------------------------------------------------------------------------------------------------------------------
#fast fibonacci

# f(2n) = f(n)² + f(n+1)²
# f(2n + 1) = 2 * f(n+1) * f(n) - f(n)
'''
def fibo2n(n): 
    if n in {0, 1}: 
        return n 
    elif n % 2: 
        k = (n - 1) // 2
        return stfib(k)**2 + stfib(k + 1)**2
    else: 
        k = n // 2
        return stfib(k) * (2 * stfib(k + 1) - stfib(k))
'''
#print(fibo2n(1000))

#---------------------------------------------------------------------------------------------------------------------



def fibo2n(n): 
    if n in {0, 1}: 
        return n
    if n == 2: 
        return 1 
    elif n % 2: 
        k = (n - 1) // 2
        return fibo2n(k)**2 + fibo2n(k + 1)**2
    else: 
        k = n // 2
        return fibo2n(k) * (2 * fibo2n(k + 1) - fibo2n(k))
  
print(fibo2n(1000))


from functools import cache
@cache

#-------------------------------------------------------------------------------------------------------------------
#standard tribonacci implementation 
def tribo(n): 
    if n in {0, 1}: 
        return n
    elif n == 2: 
        return 1
    else: 
        return tribo(n-1) + tribo(n-2) + tribo(n-3)

list = [tribo(n) for n in range (20)]   #list with the first n tribonacci numbers 
print(list)                             
print(tribo(10))                         #n'th tribonacci number

#-------------------------------------------------------------------------------------------------------------------
#tribonacci numbers with cache 
c = [ -1 ] * 10**6

def ctribo(n): 
    if c[n] != -1:
        return c[n]
    if n in {0, 1}: 
        c[n] = n
        return n 
    elif n == 2: 
        c[n] = 1
        return 1
    else: 
        c[n] = tribo(n-1) + tribo(n-2) + tribo(n-3)
        return c[n]

print(ctribo(100))

#--------------------------------------------------------------------------------------------------------------------
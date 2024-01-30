#-------------------------------------------------------------------------------------------------
#standard padovan implementation 
def padovan(n): 
    if n in {0, 1}: 
        return n 
    elif n == 2: 
        return 1 
    else: 
        return padovan(n-2) + padovan(n-3)

list = [padovan(n) for n in range(20)]
print(list) 
print(padovan(10))

#--------------------------------------------------------------------------------------------------
#padovan numbers with cache 
c = [ -1 ] * 10**7

def padoca(n): 
    if c[n] != -1:
        return c[n]
    if n in {0, 1}: 
        c[n] = n
        return n 
    elif n == 2: 
        c[n] = 1
        return 1
    else: 
        c[n] = padovan(n-2) + padovan(n-3) 
        return c[n]

print(padoca(25))

#--------------------------------------------------------------------------------------------------------------------
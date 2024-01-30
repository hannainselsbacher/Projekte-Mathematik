#-------------------------------------------------------------------------------------------------------------------
#standard narayana implementation 
def narayana(n): 
    if n in {0, 1}: 
        return n
    elif n == 2: 
        return 1
    else: 
        return narayana(n-1) + narayana(n-3)

list = [narayana(n) for n in range (20)]   #list with the first n narayana numbers 
print(list)                             
print(narayana(10))                         #n'th narayana number

#-------------------------------------------------------------------------------------------------------------------
#narayana numbers with cache 
c = [ -1 ] * 10**7

def naraca(n): 
    if c[n] != -1:
        return c[n]
    if n in {0, 1}: 
        c[n] = n
        return n 
    elif n == 2: 
        c[n] = 1
        return 1
    else: 
        c[n] = narayana(n-1) + narayana(n-3) 
        return c[n]

print(naraca(25))

#--------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
#standard tetranacci implementation 
def tetra(n): 
    if n in {0, 1}: 
        return n
    elif n in {2, 3}: 
        return (n-1)
    else: 
        return tetra(n-1) + tetra(n-2) + tetra(n-3) + tetra(n-4)

list = [tetra(n) for n in range (20)]   #list with the first n tetranacci numbers 
print(list)                             
print(tetra(10))                         #n'th tetranacci number

#-------------------------------------------------------------------------------------------------------------------
#tetranacci numbers with cache 
c = [ -1 ] * 10**7

def tetraca(n): 
    if c[n] != -1:
        return c[n]
    if n in {0, 1}: 
        c[n] = n
        return n 
    elif n in {2, 3}: 
        c[n] = (n-1)
        return (n-1)
    else: 
        c[n] = tetra(n-1) + tetra(n-2) + tetra(n-3) + tetra(n-4)
        return c[n]

print(tetraca(25))

#--------------------------------------------------------------------------------------------------------------------
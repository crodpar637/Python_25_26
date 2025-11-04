

l = [1,2,3,4,5]

l2 = [ n**2 for n in l if (n**2)%2==0]

print(l2)

l3 = ( n**2 for n in l if (n**2)%2==0 )

print(l3)

for n in l3:
    print(n)
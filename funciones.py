
def funcion( p1, p2, *others):
    print(others)


def f2( p1, p2, **others):
    print(others)


funcion(1,2,3,4,5,6)
funcion('a','b','c','d')

f2(1,2,t=3,z=4,j=5,m=6)
f2('a','b',l1='c',l2='d')
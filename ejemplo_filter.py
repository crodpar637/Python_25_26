l = [1,5,6,7,3,5,7,8]

f = filter(lambda x : x % 2 == 0, l)

print(f)

for n in f:
    print(n)


f = filter(lambda x : x % 2 == 0, l)

print(list(f))
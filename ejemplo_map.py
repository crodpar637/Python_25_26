
l = [1,2,3]

objeto_mapa = map(lambda x : x + 1, l)

print(objeto_mapa)
l2 = list(objeto_mapa)
print(l2)

objeto_mapa = map(lambda x : x + 1, l)

l.append(4)
l.append(5)

elem = next(objeto_mapa);
print("next:", elem)
for elem in objeto_mapa:
    print(elem)


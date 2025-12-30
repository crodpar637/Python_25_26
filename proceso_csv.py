f = open("datos.csv", "r", encoding="utf-8") 
lineas = f.readlines()
f.close()

lista_campos = lineas[0].strip().split(",")
print("Cabecera:", lista_campos)

for linea in lineas[1:]:
    campos = linea.strip().split(",")
    print(campos)
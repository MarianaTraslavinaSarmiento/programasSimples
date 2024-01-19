#Escriba un programa que reciba como entrada las longitudes de los dos catetos a
# y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
#del triangulo, dado por el teorema de Pitágoras:


import math
raiz = math.sqrt

cat_a = float(input("Ingrese cateto A\n"))
cat_b = float(input("Ingrese cateto B\n"))
paso1 = cat_a**2 + cat_b**2
resultado = round(raiz(paso1) ,3) 

print(f"La hipotenusa del triangulo es: {resultado}")

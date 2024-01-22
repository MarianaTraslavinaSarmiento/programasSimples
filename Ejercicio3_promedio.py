#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:

suma = 0

for i in range(4):
    num = float(input(f"Ingresa el número {i+1}: "))
    suma += num

promedio = suma/4

print(f"El promedio de las notas es {promedio}")
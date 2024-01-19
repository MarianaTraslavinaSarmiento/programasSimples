#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:

from statistics import mean

notas_list = []

for i in range(4):
    num = float(input(f"Ingresa el número {i+1}: "))
    notas_list.append(num)
    
print(f"El promedio de las notas es {mean(notas_list)}")
#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

num = input("Ingrese número\n")
invierte = ""
for i in range (len(num)):
    invierte += num[-(i+1)]

print(invierte)
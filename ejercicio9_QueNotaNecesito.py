#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

nc1 = float(input("Ingrese nota certamen 1: "))
nc2 = float(input("Ingrese nota certamen 2: "))
nlab = float(input("Ingrese nota laboratorio: "))


promedio = (60-nlab*0.3)/0.7

nc3 = (promedio*3)-nc1-nc2
print(f"Necesita nota {round(nc3)} en el certamen 3")
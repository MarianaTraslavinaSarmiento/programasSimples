#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

hora1 = float(input("Hora actual: "))
hora2 = float(input("Canrtidad de horas: "))

suma = hora1 + hora2
resultado = suma%24

print(f"En {hora2} horas, el reloj marcará las {resultado}")
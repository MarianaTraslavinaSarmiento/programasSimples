

#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

import math
num_pi = math.pi


while True:
    radio = (input("Ingrese el radio del círculo\n"))
    try:
        radio = float(radio)
        perimetro = round(2*num_pi*radio ,1)
        print(f"El perímetro del circulo es {perimetro}")

        area = round(num_pi*(radio**2) ,1)
        print(f"El área del circulo es {area}")
        break
    except ValueError:
        print("Por favor ingrese un número válido")




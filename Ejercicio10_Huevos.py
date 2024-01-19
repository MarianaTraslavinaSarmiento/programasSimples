#Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.

import math 

TH = float(input("Temperatura original del huevo\n"))
TE = 100
M = 47
P = 1.038
C = 3.7
K = 0.0054

dividendo = math.pow(M, (2/3)) * (C*(math.pow(P, (1/3))))
divisor = (K * math.pow(math.pi, 2)) * math.pow((4*math.pi) / 3, (2/3))
resultado = dividendo / divisor
resultado2 = math.log(0.76 * ((TH - TE) / (70 - TE)))
segundos = resultado * resultado2
minutos = round(segundos/60)

print(f"El tiempo maximo para preparar el huevo a la copa es {round(segundos)} segundos")
print(f"El tiempo maximo para preparar el huevo a la copa es {round(minutos)} minutos")


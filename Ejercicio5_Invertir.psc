Algoritmo invertir 
	
	definir num como cadena 
	escribir "Escriba un numero de tres digitos: "
	leer num
	definir cadena_invertida como cadena 
	
	para x<-3 hasta 1 con paso -1 hacer 
		cadena_invertida <- cadena_invertida+subcadena(num, x, x)
	FinPara
	
	escribir cadena_invertida
FinAlgoritmo

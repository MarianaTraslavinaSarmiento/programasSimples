Algoritmo que_nota_necesito
	
	definir nota1, nota2, nota_lab como real 
	
	Escribir "Ingrese nota certamen 1: "
	leer nota1
	Escribir "Ingrese nota certamen 2: "
	leer nota2
	Escribir "Ingrese nota laboratorio: "
	leer nota_lab
	
	promedio = (60-nota_lab*0.3)/0.7
	
	nota3 = (promedio*3)-nota1-nota2
	
	escribir"Necesita nota de " redon(nota3) " en el certamen 3"
	
	
FinAlgoritmo

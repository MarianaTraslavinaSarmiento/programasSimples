Algoritmo huevosALaCopa
	
	definir Temperatura como real
	
	Escribir "Temperatura original del huevo: "
	leer Temperatura
	
	TH = Temperatura
	TE <- 100
	M <- 47
	P <- 1.038
	C <- 3.7
	K <- 0.0054
	
	dividendo <- (M^(2/3))*(C*(P^(1/3)))
	divisor = (K*(pi^(2))*((4*pi)/3)^(2/3))
	resultado = dividendo/divisor
	resultado2 = ln(0.76*((TH-TE)/(70-TE)))
	segundosa = resultado * resultado2
	minutos = redon(segundosa/60)
	
	Escribir "El tiempo maximo para preparar el huevo es: " redon(segundosa) " segundos"
	Escribir "El tiempo maximo para preparar el huevo es: " redon(minutos) " minutos"
	
	
	
FinAlgoritmo

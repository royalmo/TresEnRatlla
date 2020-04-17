"""
Funcions.py by Eric Roy for TresEnRatlla.py
Copyright (c) Todos los derechos reservados.
Programa amb totes les funcions necesaries
per fer el programa. Instruccions de com
executar el programa al programa principal.
"""

import random	#Falta millorar jugada aleatoria

def iniciarTaulell():
	"""
	Retorna un taulell-codi (llista) amb 9 lines de
	un caracter de espai. Nomes te return.
	"""
	return [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
def dibuixaTaulell(l, n):
	"""
	Retorna en forma print el dibuix del taulell amb els
	caracters modificats de la llista anterior (Per X i O)
	Tambe fa print amb el numero de torn (Parametre n)
	"""
	if l==[]:
		print ("Error de Parametres")
	else:
		print ("Numero de torn: " + str(n))
		print ("")
		print ("==========================================")
		print ("|             |             |            |")
		print ("|             |             |            |")
		print ("|      " + l[0] + "      |      " + l[1] + "      |      " + l[2] + "     |")
		print ("|             |             |            |")
		print ("|             |             |            |")
		print ("------------------------------------------")
		print ("|             |             |            |")
		print ("|             |             |            |")
		print ("|      " + l[3] + "      |      " + l[4] + "      |      " + l[5] + "     |")
		print ("|             |             |            |")
		print ("|             |             |            |")
		print ("------------------------------------------")
		print ("|             |             |            |")
		print ("|             |             |            |")
		print ("|      " + l[6] + "      |      " + l[7] + "      |      " + l[8] + "     |")
		print ("|             |             |            |")
		print ("|             |             |            |")
		print ("==========================================")
def triaJugadorInicial(a, b):
	"""
	Aquesta funcio retornara en cadena qui
	sera el primer jugador aleatoriament.
	"""
	if random.randint(0, 1) == 0:
		return a
	else:
		return b
def esEspaiLliure(taulell, quadre):
	"""
	En aquesta funcio es dona el taulell actualitzat i
	la posicio que vol ocupar el jugador. La funcio
	retorna True si es lliure i False si esta ocupat.
	"""
	quadre=int(quadre)
	quadre-=1
	return str(not(taulell[quadre]=="X" or taulell[quadre]=="O"))
def taulellPle(l):
	"""
	Si cap jugador pot ficar mes marques al taulell retorna True.
	Si encara es poden ficar mes marques al taulell retorna False.
	"""
	return str( not(l[0]==" " or l[1]==" " or l[2]==" " or l[3]==" " or l[4]==" " or l[5]==" " or l[6]==" " or l[7]==" " or l[8]==" ") )
def aplicarJugada(taulell, simbol, quadre, player):
	"""
	Funcio que intercanvia un numero de la
	llista per el simbol del parametre.
	Tambe fa print de la posicio.
	"""
	print (player + " ocupa la posicio " + str(quadre))
	quadre=int(quadre)
	quadre-=1
	taulell[quadre]=simbol
	return taulell
def esJugadaGuanyadora(t, s):
	"""
	Retorna True si es guanyadora la jugada
	que ha fet el player o ordinador.
	Sino retornara False.
	"""
	return (t[0]==s and t[1]==s and t[2]==s) or (t[0]==s and t[3]==s and t[6]==s) or (t[6]==s and t[7]==s and t[8]==s) or (t[2]==s and t[5]==s and t[8]==s) or (t[3]==s and t[4]==s and t[5]==s) or (t[6]==s and t[4]==s and t[2]==s) or (t[1]==s and t[4]==s and t[7]==s) or (t[0]==s and t[4]==s and t[8]==s)
def canviJugador(actual, a="Jugador", b="Ordinador"):
	"""
	Si hi ha ordinador canvia a jugador.
	Si hi ha jugador canvia a ordinador.
	"""
	if actual==a:
		return b
	else:
		return a
def jugadaAleatoria(l, LP, LC):
	"""
	Retorna una posicio lliure del taulell i fa que
	es puqui jugar aleatoriament.
	"""
	actual=0
	Guanya=potGuanyaAlgu(l, LP, LC)
	Perdre=potSalvarAlgu(l, LP, LC)
	if Guanya!=False:
		return Guanya
	elif Perdre!=False:
		return Perdre
	else:
		while actual==0:
			temporal=random.randint(1, 9)
			if esEspaiLliure(l, temporal) == "True":
				actual=temporal
	return str(actual)
def sumarPartida1(linea):
	"""
	Guarda a la linea 1 del fitxer variables
	les dades de la partida ja feta 1Player.
	"""
	fin=open("Variables.txt", "r")
	part1=fin.readline()
	part2=fin.readline()
	part1=part1.split()
	part2=part2.split()
	fin.close()
	suma=part1[linea]
	suma=int(suma)
	suma=suma+1
	part1[linea]=suma
	fout=open("Variables.txt", "w")
	fout.write(str(part1[0]) + " " + str(part1[1]) + " " + str(part1[2]) + " " + str(part1[3]) + "\n" + str(part2[0]) + " " + str(part2[1]) + " " + str(part2[2]) + " " + str(part2[3]))
	fout.close()
def sumarPartida2(linea):
	"""
	Guarda a la linea 2 del fitxer variables
	les dades de la partida ja feta 2Players.
	"""
	fin=open("Variables.txt", "r")
	part1=fin.readline()
	part2=fin.readline()
	part1=part1.split()
	part2=part2.split()
	fin.close()
	suma=part2[linea]
	suma=int(suma)
	suma+=1
	part2[linea]=suma
	fout=open("Variables.txt", "w")
	fout.write(str(part1[0]) + " " + str(part1[1]) + " " + str(part1[2]) + " " + str(part1[3]) + "\n" + str(part2[0]) + " " + str(part2[1]) + " " + str(part2[2]) + " " + str(part2[3]))
	fout.close()
def jugada(l, s=""):
	"""
	Retorna la posicio escollida per el jugador
	si la posicio no es lliure ho torna a preguntar.
	"""
	lletra=input(s + "Escull la posicio a on vols jugar (1-9): ")
	while (lletra != "1" and lletra != "2" and lletra != "3" and lletra != "4" and lletra != "5" and lletra != "6" and lletra != "7" and lletra != "8" and lletra!="9") or (esEspaiLliure(l, lletra)=="False") :
		print ("Posicio no valida.")
		lletra=input(s + "Escull la posicio a on vols jugar (1-9): ")
	return lletra
def triaLletraJugador(s):
	"""
	Retorna la lletra escollida per el jugador.
	Si la lletra es incorrecta ho torna a preguntar.
	"""
	lletra=input(s + "Vols ser les X o les O?")
	lletra = lletra.upper()
	while lletra != 'X' and lletra != 'O':
		print ("Lletra incorrecta.")
		lletra=input(s + "Vols ser les X o les O?")
		lletra = lletra.upper()
	if lletra=="X":
		return "X"
	else:
		return "O"
def jugarAltreCop(n=1):
	"""
	Segons si el jugador vol jugar un altre cop o no,
	la funcio executara el menu o un altre cop el joc.
	"""
	lletra=input("Vols jugar un altre cop? (s/n)")
	lletra = lletra.upper()
	while lletra != 'S' and lletra != 'N':
		print ("Lletra incorrecta.")
		lletra=input("Vols jugar un altre cop? (s/n)")
		lletra = lletra.upper()
	if lletra=="S":
		if n==1:
			opcio1()
		else:
			opcio2()
	else:
		print ("")
		print ("")
		menu()
def potGuanyaAlgu(l, LP, LC):
	"""
	Si computer pot guanyar retorna posicio.
	En cas contrari retorna False.
	"""
	if l[0]==LP and l[1]==LP and l[2]==" ":
		return 3
	elif l[1]==LP and l[2]==LP and l[0]==" ":
		return 1
	elif l[0]==LP and l[2]==LP and l[1]==" ":
		return 2
	elif l[0]==LP and l[3]==LP and l[6]==" ":
		return 7
	elif l[3]==LP and l[6]==LP and l[0]==" ":
		return 1
	elif l[0]==LP and l[6]==LP and l[3]==" ":
		return 4
	elif l[6]==LP and l[7]==LP and l[8]==" ":
		return 9
	elif l[7]==LP and l[8]==LP and l[6]==" ":
		return 7
	elif l[6]==LP and l[8]==LP and l[7]==" ":
		return 8
	elif l[2]==LP and l[5]==LP and l[8]==" ":
		return 9
	elif l[5]==LP and l[8]==LP and l[2]==" ":
		return 3
	elif l[2]==LP and l[8]==LP and l[5]==" ":
		return 6
	elif l[3]==LP and l[4]==LP and l[5]==" ":
		return 6
	elif l[4]==LP and l[5]==LP and l[3]==" ":
		return 4
	elif l[3]==LP and l[5]==LP and l[4]==" ":
		return 5
	elif l[6]==LP and l[4]==LP and l[2]==" ":
		return 3
	elif l[4]==LP and l[2]==LP and l[6]==" ":
		return 7
	elif l[6]==LP and l[2]==LP and l[4]==" ":
		return 5
	elif l[1]==LP and l[4]==LP and l[7]==" ":
		return 8
	elif l[1]==LP and l[7]==LP and l[4]==" ":
		return 5
	elif l[4]==LP and l[7]==LP and l[1]==" ":
		return 2
	elif l[0]==LP and l[4]==LP and l[8]==" ":
		return 9
	elif l[0]==LP and l[8]==LP and l[4]==" ":
		return 5
	elif l[4]==LP and l[8]==LP and l[0]==" ":
		return 1
	else:
		return False
def potSalvarAlgu(l, LC, LP):
	"""
	Si computer pot guanyar retorna posicio.
	En cas contrari retorna False.
	"""
	if l[0]==LP and l[1]==LP and l[2]==" ":
		return 3
	elif l[1]==LP and l[2]==LP and l[0]==" ":
		return 1
	elif l[0]==LP and l[2]==LP and l[1]==" ":
		return 2
	elif l[0]==LP and l[3]==LP and l[6]==" ":
		return 7
	elif l[3]==LP and l[6]==LP and l[0]==" ":
		return 1
	elif l[0]==LP and l[6]==LP and l[3]==" ":
		return 4
	elif l[6]==LP and l[7]==LP and l[8]==" ":
		return 9
	elif l[7]==LP and l[8]==LP and l[6]==" ":
		return 7
	elif l[6]==LP and l[8]==LP and l[7]==" ":
		return 8
	elif l[2]==LP and l[5]==LP and l[8]==" ":
		return 9
	elif l[5]==LP and l[8]==LP and l[2]==" ":
		return 3
	elif l[2]==LP and l[8]==LP and l[5]==" ":
		return 6
	elif l[3]==LP and l[4]==LP and l[5]==" ":
		return 6
	elif l[4]==LP and l[5]==LP and l[3]==" ":
		return 4
	elif l[3]==LP and l[5]==LP and l[4]==" ":
		return 5
	elif l[6]==LP and l[4]==LP and l[2]==" ":
		return 3
	elif l[4]==LP and l[2]==LP and l[6]==" ":
		return 7
	elif l[6]==LP and l[2]==LP and l[4]==" ":
		return 5
	elif l[1]==LP and l[4]==LP and l[7]==" ":
		return 8
	elif l[1]==LP and l[7]==LP and l[4]==" ":
		return 5
	elif l[4]==LP and l[7]==LP and l[1]==" ":
		return 2
	elif l[0]==LP and l[4]==LP and l[8]==" ":
		return 9
	elif l[0]==LP and l[8]==LP and l[4]==" ":
		return 5
	elif l[4]==LP and l[8]==LP and l[0]==" ":
		return 1
	else:
		return False
def menu():
	"""
	Simula el menu del joc i crida una funcio diferent depen
	del que esculli el jugador.
	"""
	print ("MENU")
	print ("====")
	print ("1. Un jugador")
	print ("2. Multijugador")
	print ("3. Historial de Partides")
	print ("4. Credits del Joc")
	print ("5. Sortir del Joc")
	print ("")
	opcio  = input("Tria una opcio: ")
	while opcio!="1" and opcio!="2" and opcio!="3" and opcio!="4" and opcio!="5":
		print ("Opcio incorrecta.")
		opcio=input("Tria una opcio: ")
	if opcio=="1":
		opcio1()
	elif opcio=="2":
		opcio2()
	elif opcio=="4":
		opcio4()
	elif opcio=="5":
		opcio5()
	else:
		opcio3()
def opcio1():
	"""
	Fa la opcio 1: jugar partida.
	"""
	Taulell=iniciarTaulell()
	print ("")
	print ("")
	LletraJugador=triaLletraJugador("")
	Jugador=triaJugadorInicial("Jugador", "Ordinador")
	print ("")
	print ("El primer en jugar es: " + Jugador)
	print ("")
	FiPartida=0
	Torn=1
	dibuixaTaulell(['1', '2', '3', '4', '5', '6', '7', '8', '9'], Torn)
	while FiPartida==0:	#Aquest While es un torn per un sol jugador.
		Torn+=1
		if Jugador=="Jugador":
			Lletra=LletraJugador
			Escollit=jugada(Taulell)
		else:
			if LletraJugador=="X":
				Lletra="O"
			else:
				Lletra="X"
			Escollit=jugadaAleatoria(Taulell, LletraJugador, Lletra)
		Taulell=aplicarJugada(Taulell, Lletra, Escollit, Jugador)
		dibuixaTaulell(Taulell, Torn)
		if taulellPle(Taulell)== "True":
			FiPartida="Empatat"
		if esJugadaGuanyadora(Taulell, Lletra)== True:
			FiPartida=Lletra
		Jugador=canviJugador(Jugador)
	Guardar=0
	if FiPartida=="Empatat":
		print ("")
		Guardar=3
		print ("Jugador i Ordinador han empatat!")
		print ("")
	elif FiPartida==LletraJugador:
		print ("")
		Gruardar=1
		print ("Enhorabona! Has guanyat la partida!")
		print ("")
	else:
		print ("")
		Guardar=2
		print ("Llastima... Ordinador ha guanyat la partida.")
		print ("")
	sumarPartida1(0)
	sumarPartida1(Guardar)
	print ("La partida s'ha guardat correctament al historial de partides")
	print ("")
	jugarAltreCop()
def opcio2():
	"""
	Partida de 2 jugadors.
	"""
	Taulell=iniciarTaulell()
	print ("")
	print ("")
	LletraJugador1=triaLletraJugador("Player1: ")
	if LletraJugador1 == "X":
		LletraJugador2="O"
	else:
		LletraJugador2="X"
	Jugador=triaJugadorInicial("Player1", "Player2")
	print ("")
	print ("El primer en jugar es: " + Jugador)
	print ("")
	FiPartida=0
	Torn=1
	dibuixaTaulell(['1', '2', '3', '4', '5', '6', '7', '8', '9'], Torn)
	while FiPartida==0:	#Aquest While es un torn per un sol jugador.
		Torn+=1
		if Jugador=="Player1":
			Lletra=LletraJugador1
			Escollit=jugada(Taulell, "Player1: ")
		else:
			Lletra=LletraJugador2
			Escollit=jugada(Taulell, "Player2: ")
		Taulell=aplicarJugada(Taulell, Lletra, Escollit, Jugador)
		dibuixaTaulell(Taulell, Torn)
		if taulellPle(Taulell)== "True":
			FiPartida="Empatat"
		if esJugadaGuanyadora(Taulell, Lletra)== True:
			FiPartida=Lletra
		Jugador=canviJugador(Jugador, "Player1", "Player2")
	if FiPartida=="Empatat":
		print ("")
		Guardar=3
		print ("Heu empatat la partida!")
		print ("")
	elif FiPartida==LletraJugador1:
		print ("")
		Gruardar=1
		print ("Victoria per Player1!")
		print ("")
	else:
		print ("")
		Guardar=2
		print ("Victoria per Player2!")
		print ("")
	sumarPartida2(0) # Parametre: 0=Sumar a partides jugades (defecte)
	sumarPartida2(Guardar) #Parametre: 1=Victoria Player1 2=Victoria Player2 3=Empate
	print ("La partida s'ha guardat correctament al historial de partides")
	print ("")
	jugarAltreCop(2)
def opcio3():
	"""
	Diu el historial de partides.
	"""
	fin= open("Variables.txt", "r")
	part1= fin.readline()
	part2= fin.readline()
	fin.close()
	part1=part1.split()
	part2=part2.split()
	print ("")
	print ("")
	print ("Un Jugador:")
	print ("===========")
	print ("")
	print ("Partides jugades: " + str(part1[0]))
	print ("Partides guanyades: " + str(part1[1]))
	print ("Partides perdudes: " + str(part1[2]))
	print ("Partides empatades: " + str(part1[3]))
	print ("")
	print ("Multijugador")
	print ("============")
	print ("")
	print ("Partides jugades: " + str(part2[0]))
	print ("Player1: Partides guanyades: " + str(part2[1]))
	print ("player2: Partides guanyades: " + str(part2[2]))
	print ("Partides empatades: " + str(part2[3]))
	print ("")
	print ("")
	menu()
def opcio4():
	"""
	Credits del joc.
	"""
	print ("")
	print ("")
	print ("CREDITS")
	print ("=======")
	print ("")
	print ("Idea Original: Jordi Vives")
	print ("Autor i Ampliacions: Eric Roy")
	print ("Programes: Python i Notepad++")
	print ("Agraiments: Codelearn Manresa")
	print ("")
	print ("")
	menu()
def opcio5():
	"""
	Surt del joc.
	"""
	print ("")
	print ("Gracies per haver jugat.")
	print ("")
	print ("")

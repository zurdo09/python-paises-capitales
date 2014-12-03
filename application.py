#-*- coding: utf-8-*-
import smtplib
import sys
encabezado={"Paises":"Capitales"}
pais = {}
capitales = []
#***********************************************************
#*******************Ingreso de pais Opcio 1*****************
#***********************************************************

def Ingreso():
	print "                                         "
	print "	     •Ingreso de país y capital•	    "
	print "                                         "
	eleccion=True
	while eleccion==True:
		opcion=raw_input("Desea Ingresar un pais o capital Si/No: ")
		try:
			if opcion.isalpha()==True:
				if opcion.lower()=="si":
					eleccion_pais=True
					while eleccion_pais==True:
						pais=raw_input("Ingrese el pais: ")
						try:
							if pais.isalpha()==True:
								eleccion_pais=False
							else:
								print "no se aceptan datos numericos"
						except:
							eleccion_pais=True
					eleccion_capital=True
					while eleccion_capital==True:
						capital=raw_input("Ingrese la capital: ")
						try:
							if capital.isalpha()==True:
								eleccion_capital=False
							else:
								print "No se aceptan datos numericos"
						except:
							eleccion_capital=True
					paises[pais]=capital
				elif opcion.lower()=="no":
					break
				else:
					print "dato no reconocido"
			else:
				print "no se aceptan datos numericos"
		except:
			eleccion=True


#****************************************************
#********************Menu****************************
#****************************************************

salir=False
while salir==False:
	print " MENÚ PAÍSES Y CAPITALES "
	print "¿Qué desea realizar?"
	print "1) Ingresar paises y capitales"
	print "2) Lista de paises"
	print "3) Lista de capitales"
	print "4) Pais y capital"
	print "5) Todo Ordenado"
	print "6) Envio De correo"
	menu = int(raw_input("ingrese número de opción:"))
	try:
		if menu ==1:
			print Ingreso()
			opcionmenu=raw_input("Desea volver al menu Si/No: ")
			if opcionmenu.lower()=="si":
				salir=False
			else:
				break

#*************************************************************
#*****************Lista de paises opcion 2********************
#*************************************************************

		elif opcion_menu.lower()=="2":
			print "Lista De Paises"
			for elemento in paises:
				print (elemento)
			correcto=True
			while correcto==True:
				print ""
				volver=raw_input("Desea volver al menu Si/No: ")
				print ""
				try:
					if volver.isalpha()==True:
						if volver.lower()=="si":
							correcto=False
						elif volver.lower()=="no":
							op_menu=False
							break
					else:
						print "dato no valido"
				except:
					print "no se aceptan datos numericos"

#*************************************************************
#*****************Lista de capitales opcion 3*****************
#*************************************************************

		elif opcion_menu.lower()=="3":
				print "Lista De Capitales"
				for x in paises:
					print paises[x]
				validar=True
				while validar==True:
					print""
					volver=raw_input("Desea volver al menu Si/No: ")
					print ""
					try:
						if volver.isalpha()==True:
							if volver.lower()=="si":
								validar=False
							elif volver.lower()=="no":
								op_menu=False
								break
						else:
							print "dato no valido"
					except:
						print "no se aceptan datos numericos"

		elif opcion_menu.lower()=="4":
				print "*** LISTA PAISES/CAPITALES ***"
				print ""
				for clave in encabezado:
					print clave,":",encabezado[clave] 
				for clave in paises:
					print clave,":",paises[clave] 
				validar=True
				while validar==True:
					print ""
					volver=raw_input("Desea volver al menu Si/NO?: ")
					print ""
					try:
						if volver.isalpha()==True:
							if volver.lower()=="si":
								validar=False
							elif volver.lower()=="no":
								op_menu=False
								break
						else:
							print "dato no valido"
					except:
						print "no se aceptan datos numericos"

		elif opcion_menu.lower()=="5":
			print "Lista Paises y Capitales Ordenado"
			print "Paises"
			for item in paises:
				print (item)
			print ""
			print "Capitales Ordenados"

			for x in paises:
				lista_capitales.append(x)
			print lista_capitales.sort()
			print " ".join(lista_capitales)
			validar=True
			while validar==True:
				print ""
				volver=raw_input("Desea volver al menu YES/NO?: ")
				print ""
				try:
					if volver.isalpha()==True:
						if volver.lower()=="yes":
							validar=False
						elif volver.lower()=="no":
							op_menu=False
							break
					else:
						print "dato no valido"
				except:
					print "no se aceptan datos numericos"

		elif menu ==6:
			print correo()
			opcionmenu=raw_input("Desea vover al menu Si/No: ")
			if opcionmenu.lower()=="si":
				salir=False
			else:
				break
	except:

		print "Gracias por utilizar el servicio cognits."
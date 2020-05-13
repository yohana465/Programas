# Alba Gabriela Yool Alvarado ________1990-19-15166
# Paula Yohana Hernandez Morales _____1990-19-17246
#_____________________________________________________________________________
#_____________________________________________________________________________


#json (JavaScript Object Notation) es un formato ligero de intercambio de datos.
import json
import os
def menu():
	"""
	"""
 #Menu principal de lavado de autos 
	print("")
	print("_______________________________")
	print("BIENVENIDO A CARWASH YOHABY'S |")
	print("***************************   |")
	print ("SELECCIONE UNA OPCIPN         |")
	print("******************************|")
	print ("1) INGRESAR                   |")
	print ("2) SALIR                      |")
	print ("______________________________|")
	print("")
 
while True:
    # Mostramos el menu
	menu()
    # solicituamos una opcion al usuario
	opcionMenu = input("INSERTAR LA OPCION QUE DESEE REALIZAR  >> ")
 
	if opcionMenu=="1":
		print ("")
		datos = []
		#total=[]
		os.system('clear')
        #cantidad de registros o veces que se desean ingresar
		valor = int(input("INGRESE CUANTOS REGISTROS DESEA ALMACENAR  >>  "))
        # opciones a elegir
		for i in range (valor):
				 
			registro = {}
			os.system('clear') 
			tipo = input("  Tipos de vehiculos \n (1) Motocicleta[Q.15] \n (2)Automovil[Q.30] \n (3)Camioneta[Q.50] )  \n >>  ")
			if tipo == "1":
				precio = 15
				tipo1 = 'Motocicleta'

			elif tipo == "2":
				precio = 30
				tipo1 = 'Automovil'
			elif tipo == "3":
				precio = 50
				tipo1 = 'Camioneta'	
			else: print("error")
         #os.systemen("cls") se utiliza para limpiar pantalla
			os.system('clear') 
			cliente = input(" Tipo de cliente \n (1)Estandar, \n (2)Miembro  \n >>   ")
			if cliente == "1":
				descuento= 0
				cliente1 = 'Estandar'
			elif cliente == "2":
				descuento = precio*0.1
				cliente1 = 'Miembro'
				
			os.system('clear') 
			fin_de_semana = input("Es fin de semana (True/False)   >>  ")
			if fin_de_semana == "True":
				descuento1 = 0
			elif fin_de_semana == "False":
				descuento1 = precio*0.1 

			descuentos = descuento + descuento1
			total = precio - descuento - descuento1
		
            #totalventas=totalventas[i] + total
            
			os.system('clear') 
			print("_____REGISTROS_____")	
			print("")
			registro['Tipo'] = tipo1
			registro['Precio'] = precio
			registro['Cliente'] = cliente1
			registro['fin de semana'] = fin_de_semana
			registro['Descuentos'] = descuentos
			registro['Total'] = total
			datos.append(registro)

		print(datos)
		print("")
		print("________________________________________")
		print ("LA SUMA TOTAL DE LO GASTADO ES: ", sum(item["Total"] for item in datos))
		print("")
		print("SUMA TOTAL DE REGISTROS: ", len(datos))
		print("________________________________________ \n")
        #print("SUMA TOTAL de ventas")
		salto=input("Precione una tecla para continuar.........")
		os.system('clear')
		respuesta= input("Ingrese el nombre con que desee guardar el Json   > >   ")
		respuesta1=respuesta+".json"
		print(respuesta1)
		direccion= input("Ingrese la ubicacion donde desea almacenar el archivo   > >  ")
		#dir = 'C:/Pruebas'  # Tambien es valido 'C:\\Pruebas' o direccion de Desktop y de carpeta donde se va a almacenar.
		with open(os.path.join(direccion, respuesta1),  'w') as archivo:
			json.dump(datos, archivo)
			print("")
			print("____________________Archivo exportado____________________")
			print("")
		

		def cargar(ruta):#su funcion es llamar al archivo JSON generado previamente
			with open(ruta) as contenido:
				resultado = json.load(contenido)
				print("_______Datos desde un archivo JSON generado previamente_____")	
				print("")
				for resultados in resultado:
					print(resultados)
					print("")
		if __name__== '__main__':
			ruta=direccion+ f'/{respuesta1}'
			cargar(ruta)
		break
		
	elif opcionMenu=="2":
		break
	else:
		print ("")
		input("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")
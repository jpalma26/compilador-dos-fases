import json

#La clave es el lexema (lo que lee del programa) y el valor es el token
#ejemplo lexema: = ; toquen: operador asignacion

#aqui en el token en vez de que se repita lo mismo a parte podria ir una descripcion
#ejemplo 'ari': 'ari / condicional if'
#Faltan varias fijense en la tablita y agregenlas porfaa
reservadas = { 'ari':'if', 							#if
				'chayri':'else',  					#else
				'kawsachiy':'while',				#while
				'jaykaxpax':'for',					#for
				'imbabura':'function',				#function
				'harkay':'break',					#break
				'apachimuy' : 'import',  			#import
				'kutichipuy' : 'return', 			#return
				'pachan': 'tipo_entero',			#int
				'killaywaska' : 'tipo_string', 		#string
				'pasaqlla': 'tipo_flotante',		#float
				'huknin':'tipo_booleano',			#boolean
				'chiqap':'valor_booleano',					#true
				'llulla':'valor_booleano',					#false
				'chitiripuy' : 'tipo_alerta',		#alerta. Nuevo tipo de dato para nuestro contexto
				'chaa' : 'alerta',					#verde
				'karwa':'alerta',					#amarillo	
				'antipuka':'alerta',					#rojo
				'anchuna' : 'sen_evacuar',			#evacuar
				'kakuy':'sen_no_evacuar',			#no evacuar	
				#'apachimuy': 'apachimuy / decision',	#decision
				'rikhuchiy':'imprimir',				#print
				'puncu': 'input',					#input
				'tapuyAriq':'funcion_medir_volcan',	#medirVolcan
				'apu':'operador_or',
				'alqa':'operador_and'
}

operadores = {'=': 'operador_asignacion',
				'+': 'operador_suma',
				'-' : 'operador_resta', 
				'/' : 'operador_division', 
				'*': 'operador_multiplicacion', 
				'++' : 'operador_incremento', 
				'--' : 'operador_decremento'}
				
comparadores = {'<':'comparador', 
				'<=':'comparador', 
				'>':'comparador',
				'>=':'comparador',
				'==':'comparador',
				'!=':'comparador'}

delimitadores = {'(':'parentesis_apertura',
				')':'parentesis_cierre',
				'{':'delimitador_apertura',
				'}':'delimitador_cierre',
				';':'fin_sentencia'}



#obtengo los lexemas posibles de cada bloque (un arreglo)
#por ejmplo para delimitadores_lexema seria : ['(',')','{','}']
operadores_lexema = operadores.keys()
comparadores_lexema = comparadores.keys()
reservadas_lexema = reservadas.keys()
delimitadores_lexema = delimitadores.keys()

"""
for i in reservadas:
	print (i)
for i in operadores:
	print (i)
for i in comparadores:
	print (i)
for i in delimitadores:
	print (i)"""


#Letras del quechua que estan permitidas
permitidos = ['a','c','h','i','j','k','l','m','n','ntilde','p','q', 'r', 's', 't', 'u','w','y',
					'A','C','H','I','J','K','L','M','N','NTILDE','P','Q', 'R', 'S', 'T', 'U','W','Y','_']

numeros = ['0','1','2','3','4','5','6','7','8','9']


#comprueba si el lexema que lee desde el archivo es un identificador (letra seguidad de letras o numeros)
def es_identificador(lexema):
	esIdentificador = True
	inicial = lexema[0] #primera palabra si es una letra
	if not inicial in permitidos:
		esIdentificador = False
	if len(lexema) > 1:
		for i in range(1,len(lexema)):
			if not lexema[i] in permitidos and not lexema[i] in numeros:
				esIdentificador = False
	return esIdentificador

#comprueba si el lexema que lee desde el archivo es un numero flotante (que lleva . si o si)
def es_flotante(lexema):
	comprobacion = False
	for dig in lexema:
		if dig == ".":
			comprobacion = True
	if comprobacion:
		try:
			float(lexema)
		except:
			comprobacion = False
	return comprobacion

#comprueba si el lexema que lee desde el archivo es un entero
def es_entero(lexema):
	return lexema.isdigit()

"""def es_cadena(lexema):
	return type(lexema).__name__ == "str"""


#tabla contendra todos los tokens que detecte en el archivo
estructura = {}
tabla = []

#a tabla se le agregara cada token (un elemento que retorn crearToken)
def crearToken(token,lexema,linea):
	myToken = {}
	myToken["token"] = token
	myToken["lexema"] = lexema
	myToken["linea"] = linea
	return myToken

def eliminarEspaciosyComentarios(codigo):
	for i in range(len(codigo)):
		codigo[i] = codigo[i].strip()
	cod_sin_espacio = []
	for lex in codigo:
		if lex != "":
			cod_sin_espacio.append(lex)
	indice = len(codigo)
	for i in range(len(cod_sin_espacio)):
		if len(cod_sin_espacio[i]) >= 2:
			if cod_sin_espacio[i][0] =='/' and cod_sin_espacio[i][1] =='/':
				print(indice)
				indice = i
				print("new")
				print(indice)
	cod_sin_espacio = cod_sin_espacio[:indice]
	return cod_sin_espacio

#Se abre el archivo en modo lectura
f=open("programa", "r")
i =f.read()

linea = 0
program =  i.split('\n') #separados por salto de linea y metidos a un array['todo','el','programa','asi']

identificado = False
for line in program:
	#los separa por espacio
	codigo = line.split(' ')

	#Elimina espacios en blanco en el codigo
	codigo = eliminarEspaciosyComentarios(codigo)

	#Se eliminan los espacios en blanco
	
	#for i in range(len(codigo)):
		#codigo[i] = codigo[i].strip()
	linea += 1
	for lexema in codigo:
		if lexema in operadores_lexema:
			myToken = crearToken(operadores[lexema],lexema,linea)
			identificado = True

		if lexema in reservadas_lexema:
			myToken = crearToken(reservadas[lexema],lexema,linea)
			identificado = True

		if lexema in comparadores_lexema:
			myToken = crearToken(comparadores[lexema],lexema,linea)
			identificado = True

		if lexema in delimitadores_lexema:
			myToken = crearToken(delimitadores[lexema],lexema,linea)
			identificado = True

		if es_entero(lexema):
			myToken = crearToken("numero_entero",lexema,linea)
			identificado = True

		if es_flotante(lexema):
			myToken = crearToken("numero_flotante",lexema,linea)
			identificado = True


		#Si no se identifico el lexema
		if not identificado:
			#Ve si se trata de un identificador
			if es_identificador(lexema):
				myToken = crearToken("identificador",lexema,linea)
				tabla.append(myToken)

			#Si difinitivamente no lo identifica 
			else:
				print ("error, no se que es:", lexema, "en la linea", linea)


		#Si se identifico el lexema
		else:
			#se agrega a la tabla de tokens
			tabla.append(myToken)
			identificado = False

estructura["Tokens"] = tabla


#Muestra tabla de tokens
#for token in tabla:
#	print (token)

with open('tokens.json', 'w') as json_file:
    json.dump(estructura, json_file)



#detalles:
#por ahora cada token debe estar separado por un espacio en el archivo ejmplo:
#estara bien: a = 20 / 3.8 (porque estan separados)
#estara mal: a = 20/ 3.8 (porque el 20 lo lee como 20/ y no sabe lo que es eso)
#igual se puede arreglar eso

#en el ejemplo no sabe lo que es x porque no esta en el alfabero (asi debe ser)
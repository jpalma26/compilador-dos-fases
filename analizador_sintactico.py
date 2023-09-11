# -*- coding: cp1252 -*-
import os
import json
import Tkinter, tkFileDialog
from Tkinter import *

root = Tkinter.Tk()
root.title("Analizador Sintactico")
root.geometry("800x600")
root.resizable(False, False)

def create_window(archivo_codigo):
            ventana_codigo = Tkinter.Tk()
            ventana_codigo.title("Código")
            ventana_codigo.geometry("600x800")

            scrollbar = Tkinter.Scrollbar(ventana_codigo)
            c = Tkinter.Canvas(ventana_codigo, yscrollcommand=scrollbar.set)
            scrollbar.config(command=c.yview)
            scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
            myframe = Tkinter.Frame(c)
            c.pack(side="left", fill="both", expand=True)
            c.create_window(0, 0, window=myframe, anchor="nw")
            texto=Tkinter.Label(myframe, wraplength=600, text=archivo_codigo, anchor="w", justify=LEFT)
            texto.pack()
            ventana_codigo.update()
            c.config(scrollregion=c.bbox("all"))
            ventana_codigo.mainloop()
            
            #codigo = Label(ventana_codigo, bg="white", text="", justify=LEFT, anchor="w")
            #codigo.grid(column=1, row=1)
            #codigo.place(x=0, y=0, height=1100, width=1000)
            #codigo.config(text=archivo_codigo)
    
            
def clicked():
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Elegir un archivo')
        abs_path = os.path.abspath(file.name)
        nombre_archivo = os.path.split(abs_path)[1]
        print("Archivo abierto:", nombre_archivo)
        if file != None:
            data = file.read()
            file.close()
            print("El archivo abierto pesa %d bytes." % len(data))
            lbl2.config(text=nombre_archivo)
            mainProgram()
            create_window(data)

btn = Button(text="Abrir archivo", command=clicked)
btn.grid(column=1, row=0)
btn.place(relx=0.2, rely=0.5, anchor=CENTER)

lbl = Label(root, text="Archivo abierto: ")
lbl.grid(column=1, row=2)
lbl.place(x=10, y=10)

lbl2 = Label(root, text="No se ha abierto ningún archivo")
lbl2.grid(column=2, row=2)
lbl2.place(x=100, y=10)

salida = Label(root, text="")
salida.grid(column=1, row=3)


salida2 = Label(root, bg="white", text="")
salida2.place(x=300, y=50, height=500, width=450)


#-----------------------------------------------------------------------------------------------------------------

def mainProgram():
        #Lectura de los tokens que se encuentran en el archivo
        with open('tokens.json') as json_file:
            datos = json.load(json_file)
        tokens = datos["Tokens"]

        #DEFINICION GRAMATICA

        # simbolos no terminales
        noTerminales = ["tipo_alerta", "identificador", "operador_asignacion", 
                                        "alerta", "fin_sentencia", "tipo_entero", "numero_entero"]
        #reglas de produccion

        #Reglas para la asignacion de variables
        p1 = ["tipo_alerta" , "identificador" , "fin_sentencia"]
        p2 = ["tipo_alerta" , "identificador" , "operador_asignacion" , "alerta" , "fin_sentencia"]
        p3 = ["identificador" , "operador_asignacion" , "alerta" , "fin_sentencia"]
        p4 = ["tipo_alerta" , "identificador" , "operador_asignacion" , "parentesis_apertura" , "alerta" , "parentesis_cierre" , "fin_sentencia"]
        p5 = ["identificador" , "operador_asignacion" , "parentesis_apertura" , "alerta" , "parentesis_cierre" , "fin_sentencia"]


        p6 = ["tipo_entero" , "identificador" , "fin_sentencia"]
        p7 = ["tipo_entero" , "identificador" ,	"operador_asignacion" , "numero_entero", "fin_sentencia"]
        p_extra = ["tipo_entero" , "identificador" ,	"operador_asignacion" , "funcion_medir_volcan", "fin_sentencia"]
        p8 = ["identificador" , "operador_asignacion" , "numero_entero" , "fin_sentencia"]

        p66 = ["tipo_entero" , "identificador" , "operador_asignacion" , "operacion_matematica", "fin_sentencia"]
        p67 = ["identificador" , "operador_asignacion" , "operacion_matematica" , "fin_sentencia"]



        p9 = ["tipo_flotante" , "identificador" , "fin_sentencia"]
        p10 = ["tipo_flotante" , "identificador" ,	"operador_asignacion" , "numero_flotante", "fin_sentencia"]
        p11 = ["identificador" , "operador_asignacion" , "numero_flotante" , "fin_sentencia"]

        p68 = ["tipo_flotante" , "identificador" ,	"operador_asignacion" , "operacion_matematica", "fin_sentencia"]
        p69 = ["identificador" , "operador_asignacion" , "operacion_matematica" , "fin_sentencia"]



        p12 = ["tipo_booleano" , "identificador" , "fin_sentencia"]
        p13 = ["tipo_booleano" , "identificador" , "operador_asignacion" , "valor_booleano" , "fin_sentencia"]
        p14 = ["identificador" , "operador_asignacion" , "valor_booleano" , "fin_sentencia"]
        p15 = ["tipo_booleano" , "identificador" , "operador_asignacion" , "parentesis_apertura" , "valor_booleano" , "parentesis_cierre" , "fin_sentencia"]
        p16 = ["identificador" , "operador_asignacion" , "parentesis_apertura" , "valor_booleano" , "parentesis_cierre" , "fin_sentencia"]


        #Estructura condicionales

        p17 = ["if", "identificador" , "comparador" , "numero_entero" , "delimitador_apertura" , "delimitador_cierre"]
        p18 = ["if", "identificador" , "comparador" , "numero_flotante" , "delimitador_apertura" , "delimitador_cierre"]
        p19 = ["if", "identificador" , "comparador" , "alerta" , "delimitador_apertura" , "delimitador_cierre"]
        p20 = ["if", "identificador" , "comparador" , "valor_booleano" , "delimitador_apertura" , "delimitador_cierre"]
        p21 = ["if", "numero_entero" , "comparador" , "identificador" , "delimitador_apertura" , "delimitador_cierre"]
        p22 = ["if", "numero_entero" , "comparador" , "numero_entero" , "delimitador_apertura" , "delimitador_cierre"]
        p23 = ["if", "numero_flotante" , "comparador" , "identificador" , "delimitador_apertura" , "delimitador_cierre"]
        p24 = ["if", "numero_flotante" , "comparador" , "numero_flotante" , "delimitador_apertura" , "delimitador_cierre"]
        p25 = ["if", "valor_booleano" , "comparador" , "identificador" , "delimitador_apertura" , "delimitador_cierre"]
        p26 = ["if", "valor_booleano" , "comparador" , "valor_booleano" , "delimitador_apertura" , "delimitador_cierre"]
        p27 = ["if", "alerta" , "comparador" , "identificador" , "delimitador_apertura" , "delimitador_cierre"]
        p28 = ["if", "alerta" , "comparador" , "alerta" , "delimitador_apertura" , "delimitador_cierre"]
        p29 = ["if", "identificador" , "comparador" , "identificador" , "delimitador_apertura" , "delimitador_cierre"]

        p30 = ["if", "identificador", "delimitador_apertura" , "delimitador_cierre"]
        p31 = ["if", "numero_entero", "delimitador_apertura" , "delimitador_cierre"]
        p32 = ["if", "numero_flotante", "delimitador_apertura" , "delimitador_cierre"]
        p33 = ["if", "valor_booleano", "delimitador_apertura" , "delimitador_cierre"]
        p34 = ["if", "alerta", "delimitador_apertura" , "delimitador_cierre"]



        p35 =["else", "delimitador_apertura", "delimitador_cierre"]

        #importar funciones
        p36 = ["import", "funcion_medir_volcan", "fin_sentencia"]

        #Imprimir datos en pantalla
        p37 = ["imprimir", "parentesis_apertura", "sen_evacuar", "parentesis_cierre", "fin_sentencia"]
        p38 = ["imprimir", "parentesis_apertura", "sen_no_evacuar", "parentesis_cierre", "fin_sentencia"]
        p39 = ["imprimir", "parentesis_apertura", "numero_entero", "parentesis_cierre", "fin_sentencia"]
        p40 = ["imprimir", "parentesis_apertura", "numero_flotante", "parentesis_cierre", "fin_sentencia"]
        p41 = ["imprimir", "parentesis_apertura", "valor_booleano", "parentesis_cierre", "fin_sentencia"]
        p42 = ["imprimir", "parentesis_apertura", "alerta", "parentesis_cierre", "fin_sentencia"]
        p43 = ["imprimir", "parentesis_apertura", "identificador", "parentesis_cierre", "fin_sentencia"]

        #Ciclo while

        p44 = ["while", "identificador" , "comparador" , "numero_entero" , "delimitador_apertura" , "delimitador_cierre"]
        p45 = ["while", "identificador" , "comparador" , "numero_flotante" , "delimitador_apertura" , "delimitador_cierre"]
        p46 = ["while", "identificador" , "comparador" , "alerta" , "delimitador_apertura" , "delimitador_cierre"]
        p47 = ["while", "identificador" , "comparador" , "valor_booleano" , "delimitador_apertura" , "delimitador_cierre"]
        p48 = ["while", "numero_entero" , "comparador" , "identificador" , "delimitador_apertura" , "delimitador_cierre"]
        p49 = ["while", "numero_entero" , "comparador" , "numero_entero" , "delimitador_apertura" , "delimitador_cierre"]
        p50 = ["while", "numero_flotante" , "comparador" , "identificador" , "delimitador_apertura" , "delimitador_cierre"]
        p51 = ["while", "numero_flotante" , "comparador" , "numero_flotante" , "delimitador_apertura" , "delimitador_cierre"]
        p52 = ["while", "valor_booleano" , "comparador" , "identificador" , "delimitador_apertura" , "delimitador_cierre"]
        p53 = ["while", "valor_booleano" , "comparador" , "valor_booleano" , "delimitador_apertura" , "delimitador_cierre"]
        p54 = ["while", "alerta" , "comparador" , "identificador" , "delimitador_apertura" , "delimitador_cierre"]
        p55 = ["while", "alerta" , "comparador" , "alerta" , "delimitador_apertura" , "delimitador_cierre"]
        p56 = ["while", "identificador" , "comparador" , "identificador" , "delimitador_apertura" , "delimitador_cierre"]
        p57 = ["while", "identificador", "delimitador_apertura" , "delimitador_cierre"]
        p58 = ["while", "numero_entero", "delimitador_apertura" , "delimitador_cierre"]
        p59 = ["while", "numero_flotante", "delimitador_apertura" , "delimitador_cierre"]
        p60 = ["while", "valor_booleano", "delimitador_apertura" , "delimitador_cierre"]
        p61 = ["while", "alerta", "delimitador_apertura" , "delimitador_cierre"]


        #ciclo for
        p62 = ["for", "parentesis_apertura", "tipo_entero", "identificador","operador_asignacion", "numero_entero", 
        "fin_sentencia", "identificador", "comparador", "numero_entero", "fin_sentencia", "identificador", 
        "operador_incremento" ,"parentesis_cierre","delimitador_apertura" , "delimitador_cierre"]

        p63 = ["for", "parentesis_apertura", "tipo_entero", "identificador","operador_asignacion", "numero_entero",
         "fin_sentencia", "identificador", "comparador", "numero_entero", "fin_sentencia", "identificador", 
         "operador_decremento" ,"parentesis_cierre","delimitador_apertura" , "delimitador_cierre"]

        p64 = ["for", "parentesis_apertura", "tipo_entero", "identificador","operador_asignacion", "numero_entero", 
        "fin_sentencia", "identificador", "comparador", "identificador", "fin_sentencia", "identificador", 
        "operador_incremento" ,"parentesis_cierre","delimitador_apertura" , "delimitador_cierre"]

        p65 = ["for", "parentesis_apertura", "tipo_entero", "identificador","operador_asignacion", "numero_entero",
         "fin_sentencia", "identificador", "comparador", "identificador", "fin_sentencia", "identificador", 
         "operador_decremento" ,"parentesis_cierre","delimitador_apertura" , "delimitador_cierre"]

        #coloco las reglas de produccion dentro de una estructura de tipo diccionario para mejorar el rendimiento
        reglas = {}
        reglas["tipo_alerta"] = [p1, p2, p4]
        reglas["identificador"] = [p3, p5, p8, p11, p14, p16, p67, p69]
        reglas["tipo_entero"] = [p6, p7, p_extra,p66]
        reglas["tipo_flotante"] = [p9, p10, p68]
        reglas["tipo_booleano"] = [p12, p13, p15]
        reglas["imprimir"] = [p37, p38, p39, p40, p41, p42, p43]
        
        reglas["if"] = [p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34]
        reglas["else"] = [p35]
        reglas["import"] = [p36]
        reglas["while"] = [p44, p45, p46, p47, p48, p49, p50, p51, p52, p53, p54, p55, p56, p57, p58, p59, p60, p61]
        reglas["for"] = [p62, p63, p64, p65]
        #Separar instrucciones
        instrucciones = []
        instruccion = []
        dic_instruccion = {}
        linea = tokens[0]["linea"] #obtengo linea de la primera instruccion
        """ultima_linea = tokens[len(tokens)-1]["linea"]
        print(ultima_linea)"""
        for lista in tokens:

                token = lista["token"]
                
                if linea == lista["linea"] :
                        instruccion.append(token)
                #separar las instrucciones que no sean ciclos ni if, else por linea
                else:
                        dic_instruccion["instruccion"] = instruccion
                        dic_instruccion["linea"] = linea

                        instrucciones.append(dic_instruccion)
                        instruccion = []
                        instruccion.append(token)
                        dic_instruccion = {}
                        linea = lista["linea"]
        print(instrucciones)
        print(instruccion)
        print(dic_instruccion)
        #agrego la ultima linea
        dic_instruccion["instruccion"] = instruccion
        dic_instruccion["linea"] = linea
        instrucciones.append(dic_instruccion)

        #print (eval('4'))


        def verificarOperacionMatematica (instruccion, i, j):
                #print (instruccion[i:])
                """print (instruccion)
                                        print (len(instruccion))
                                        print (i)"""
                if i+1 < len(instruccion):
                        #intento armar la expresion matematica
                        #print(instruccion[i+1:])
                        if len(instruccion[i+1:]) > 2:
                                string_matematico = ""
                                for simbolo in instruccion[i+1:]:

                                        if simbolo != "fin_sentencia":

                                                if simbolo == "operador_suma":
                                                        simbolo = "+"
                                                if simbolo == "operador_resta":
                                                        simbolo = "-"
                                                if simbolo == "operador_division":
                                                        simbolo = "/"
                                                if simbolo == "operador_multiplicacion":
                                                        simbolo = "*"
                                                if simbolo == "parentesis_apertura":
                                                        simbolo = "("
                                                if simbolo == "parentesis_cierre":
                                                        simbolo = ")"
                                                if simbolo == "numero_flotante":
                                                        simbolo = "1.0"
                                                if simbolo == "numero_entero" or simbolo == "identificador":
                                                        simbolo = "1"
                                                        

                                                string_matematico += simbolo
                                                #print(simbolo)

                                #print (string_matematico)
                                #si string_matematico es una operacion matematica
                                
                                try:
                                        #print (eval('4'))
                                        mat = eval(string_matematico)
                                        instruccion = instruccion[:i+1]
                                        instruccion.append("operacion_matematica")
                                        instruccion.append("fin_sentencia")

                                        #solo aqui modificar instrucciones
                                        #sprint("llego al try", j)
                                        instrucciones[j]["instruccion"] = instruccion
                                        #print (instruccion)
                                        
                                        #instrucciones.pop()

                                        #print (j)

                                except:
                                        pass

        #Caso de las instrucciones en bloques como los if
        j = 0

        for instruccion in instrucciones:
                #print (instruccion["instruccion"][0])
                ulimo_simbolo = len(instruccion["instruccion"]) - 1
                if (instruccion["instruccion"][0] == "if" or instruccion["instruccion"][0] == "else" or instruccion["instruccion"][0] == "while" or instruccion["instruccion"][0] == "for") and instruccion["instruccion"][ulimo_simbolo] == "delimitador_apertura":
                        #recorrer instrucciones de abajo hacia arriba buscando el delimitador_cierre
                        delimitador_agregado = False
                        for i in range(len(instrucciones)-1, -1, -1):

                                simbolo = instrucciones[i]["instruccion"][0]
                                if simbolo == "delimitador_cierre" and not delimitador_agregado:
                                        #elimino la instruccion
                                        instrucciones.pop(i)
                                        #agrego el delimitador_cierre a la instruccion del if
                                        instruccion["instruccion"].append("delimitador_cierre")
                                        delimitador_agregado = True

                #detectar operaciones matematicas
                #print (instruccion["instruccion"])

                for i in range(len(instruccion["instruccion"])):

                        if instruccion["instruccion"][i] == "operador_asignacion":
                                #print (instruccion["instruccion"])
                                #simbolos siguientes a operador_asignacion
                                verificarOperacionMatematica(instruccion["instruccion"], i, j)
                                break

                                #print (instruccion_nueva)

                j+=1



        #cambia las instrucciones que tienen operadoraciones matematicas
        #for i in range(len(instrucciones_op_matematicos)):

        #instrucciones[posicion_de_cambio[i]]["instruccion"] = instrucciones_op_matematicos[i]
        def verificaPrimerSimbolo(primer_simbolo):
                keys_reglas = list(reglas.keys())
                correcto = False
                i = 0
                while i < len(keys_reglas) and not correcto:
                        if keys_reglas[i] == primer_simbolo:
                                correcto = True
                        i += 1
                return correcto


        def esInstruccionCorrecta(instruccion):
                primer_simbolo = instruccion[0]
                es_correcta = False
                #si el primer simbolo corresponde a alguna key de reglas
                if verificaPrimerSimbolo(primer_simbolo):
                        #comparo la instruccion con las reglas 
                        #print ("reglas para "+primer_simbolo)
                        #print ("instruccion: ",instruccion)

                        for regla in reglas[primer_simbolo]:
                                #como paro el largo de la instruccion
                                if len(instruccion) == len(regla) and not es_correcta:
                                        es_correcta = True
                                        #realizo la comparacion entre regla e instruccion
                                        for i in range(len(regla)):
                                                if (regla[i] != instruccion[i]):
                                                        es_correcta = False
                                #print (regla)

                return es_correcta		

                
        #print ( list(reglas.keys()))	
        def detallesError(instruccion):
                alerta = "error de sintaxis en la linea", instruccion["linea"]
                alerta = alerta[0] + " " + str(alerta[1])
                salida2.config(text=alerta)
                #print("error de sintaxis en la linea", instruccion["linea"])
        programa_correcto = True 
        for instruccion in instrucciones:
                if not esInstruccionCorrecta(instruccion["instruccion"]):
                        #linea = tokens[]
                        detallesError(instruccion)
                        programa_correcto = False

        if programa_correcto:
                salida2.config(text="0 errores sintacticos")
                #print ("0 errores sintacticos")


        #instrucciones[0]["instruccion"] = []
        #print (instrucciones)


root.mainloop()





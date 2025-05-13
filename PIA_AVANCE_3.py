import json
import re
import requests
from statistics import mean, median, mode

CHISTES = {
    "error" : "",
    "category" : 0,
    "type" : 0,
    "setup" : "",
    "delivery": "",
    "id": "",
    "safe": "",
    "lang": ""
}



DatosProcesados = {
    "chistes_dos_partes": "",
    "prom_chistes_dos_lineas": "",
    "prom_exito_ejecucion": ""
    }



ListaDatosProcesados = []
ListaDatosProcesados.append(DatosProcesados)

      
listaChistes = []
listaDatos = []

with open("Avance2Archivo.txt", "r") as file:
    lineas = file.readlines()#funcion que lee cada linea y devuelve lista de str
    
    
    lineas_chistes = lineas[:-1]   #todas las lineas del archivo menos la última (o sea los chistes)
    linea_datos = lineas[-1]       #ultima linea (las consultas que calculamos)

    for line in lineas_chistes:
        line = line.replace('\n', '')
        info_chiste = line.split(',')

        
        CHISTES["error"] = info_chiste[0]
        CHISTES["category"] = info_chiste[1]
        CHISTES["type"] = info_chiste[2]
        CHISTES["setup"] = info_chiste[3]
        CHISTES["delivery"] = info_chiste[4]
        CHISTES["safe"] = info_chiste[5]
        CHISTES["id"] = int(info_chiste[6])
        CHISTES["lang"] = info_chiste[7]
        copia = CHISTES.copy()
        listaChistes.append(copia)

    #ultima linea del archivo que contiene las consultas
    linea_datos = linea_datos.replace('\n', '')
    info_datos = linea_datos.split(',')

    
    DatosProcesados["chistes_dos_partes"] = int(info_datos[0])
    DatosProcesados["prom_chistes_dos_lineas"] =float(info_datos[1])
    DatosProcesados["prom_exito_ejecucion"] = float(info_datos[2])
    copia2 = DatosProcesados.copy()
    listaDatos.append(copia2)
    
#print("------------")
print("lista de chistes leída desde el archivo", listaChistes)
print("lista de consultas leída desde el archivo", listaDatos)



"""EXPRESIONES REGULARES"""

chistes2 = listaChistes.copy()
texto = str(chistes2)

DetectorId = re.compile(r"\d+")
IdValido = DetectorId.findall(texto)
#print(IdValido)
if len(IdValido) == 0:
    print("Hubo un fallo en los ID")
else:
    print("No hubieron errores en los IDS, todos son numeros según las expresiones regulares")

#reorganizacion de los datos categoria e id
#calculo de media y mediana de los id

listaIDS= []

for i in range(len(listaChistes)):
        listaIDS.append(listaChistes[i]["id"])
print(listaIDS)
        
print("Media de los IDs:  ", mean(listaIDS))

print("Mediana de los IDs:  ", median(listaIDS))

#calculo de la moda de las categorías
listaCATEGORIAS = []
for i in range(len(listaChistes)):
        listaCATEGORIAS.append(listaChistes[i]["category"])
print(listaCATEGORIAS)
print("La moda de las categorías", mode(listaCATEGORIAS))

        

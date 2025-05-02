import requests
import re
def obtener_chiste(i):
    chistes = []
    for n in range (cant):
        url = f"https://v2.jokeapi.dev/joke/{i}?safe-mode"
        respuesta = requests.get(url)
        info = respuesta.json()
        chistes.append(info)
    return chistes
        
            

#CHISTES comprobación de conexión exitosa a la API
#import requests
url = "https://v2.jokeapi.dev/joke/Any?safe-mode"
respuesta = requests.get(url)
if respuesta.status_code == 200:
    print("exito")
    info = respuesta.json()
    #print(info)
else:
    print(f"error {respuesta.status_code}")


#pedir datos y validar con int y str
cant = int(input("Ingresa la cantidad de chistes que quieres:  "))
while (cant<=0):
    print("No puede ser numero negativo o 0")
    cant = int(input("Ingresa la cantidad de chistes que quieres:  "))

#expresiones regulares para verificar que la categoria existe
DetectorCategoria = re.compile(r'any|misc|spooky|programming')
i = str(input("Ingresa la categoría (any, misc, spooky, programming):  "))
CategoriaValida = DetectorCategoria.findall(i)
while len(CategoriaValida) == 0:
    print("Esa categoría no existe o la escribiste mal")
    i = str(input("Ingresa la categoría (misc, spooky, programming):  "))
    CategoriaValida = DetectorCategoria.findall(i)

#print(CategoriaValida)
chistes = obtener_chiste(i)
print(chistes)

#CONSULTAS BASICAS
#saber cuantos chistes son single y cuantos son twopart para sacar un promedio despues
contador_single = 0
contador_twopart = 0
for a in range (len(chistes)):
    if chistes[a]["type"] == "single":
        contador_single += 1
    else:
        contador_twopart += 1

print("cantidad de chistes de una parte", contador_single)
print("cantidad de chistes de dos partes", contador_twopart)


cant_chistes = cant
promedio_single = (contador_single/cant)*100
promedio_twopart = (contador_twopart/cant)*100
print(f"El promedio de chistes de una linea es: {promedio_single}%")
print(f"El promedio de chistes de dos lineas es: {promedio_twopart}%")


#promedio de veces que no hubo error al ejecutar
j=0
contador_error = 0
for j in range (len(chistes)):
    if chistes[j]["error"] == False:
        contador_error += 1 
prom_error = (contador_error/cant)*(100)
if prom_error == 100:
    print(f"El promedio de exito en la ejecucion de chistes fue de {prom_error}%. Felicidades")
else:
    print(f"El promedio de error es de: {prom_error}%")


#Extraccion de datos (validar consultas usando expresiones regulares)
#expresiones regulares para verificar que no hubo error
chistes2 = chistes.copy()
texto = str(chistes2)
DetectorError = re.compile(r"'error':\sFalse") 
ErrorValido = DetectorError.findall(texto)
if cant == len(ErrorValido):
    print("Basado en las expresiones regulares, se encontraron", cant, "'error: False' "
          "en la lista de chistes")

#validar con expresiones regulares que el ID sea un numero
DetectorId = re.compile(r"\d+")
IdValido = DetectorId.findall(texto)
#print(IdValido)
if len(IdValido) == 0:
    print("Hubo un fallo en los ID o pediste 0 chistes")
else:
    print("No hubieron errores en los IDS, todos son numeros")


#Limpieza de datos 
# No vamos a quitar ningun dato porque la api no da tanta informacion y si quitamos pensamos
#que  nos va a faltar informacion

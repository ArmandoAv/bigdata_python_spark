"""
    Obtener al heroe mas y menos popular de Marvel

    Se ocupan 2 sets de datos
    Marvel-Graph.txt
    empieza con el ID de superheroe a revisar
    seguido con una lista todos los ID de superheroes
    que han aparecido con el, por ejemplo
    271 4935 5716 4309 3829 5794 3405 4929 1449 2940
    3519 4704 2460 763 1602 5306 5358 6121
    
    Marvel-Names.txt
    Vienen dos columnas el ID y el Nombre del superheroe
    1 "24-HOUR MAN/EMMANUEL"
    2 "3-D MAN/CHARLES CHAN"

    No se ocupara la funcion broadcast para ver otra
    alternativa de cruzar informacion entre RDDs
"""

# Importamos las librerias de Spark
from pyspark import SparkConf
from pyspark import SparkContext

"""
    Se realiza la configuracion de Spark, de manera local
    se configura para que sea de manera local y se le asigna un nombre
    se la pasa la configuracion realizada al contexto de Spark
    en setMaster se le pueden pasar los nucleos a ejecutar
    esto depende de los nucleos de la maquina local 
    con local[n] siendo n el numero de nucleos a usar
"""
conf = SparkConf().setMaster("local").setAppName("HeroeMasMenosPopular")
sc = SparkContext(conf = conf)


"""
    Se crea una funcion que separa las lineas
    en listas por el caracter de espacio y
    devuelve el primer elemento ademas de
    cuantos elementos hay despues del primero
"""
def cuentaOcurrencia(linea):
    elementos = linea.split()
    return (int(elementos[0]), len(elementos) - 1)

"""
    Se crea una funcion que separa las lineas
    en listas por el caracter de comillas dobles (")
    debido a que comillas es un caracter especial
    para poder usarlo se usa \"  
    La funcion devuelve el primer y segundo elemento
    para el segundo elemento se puede usar la funcion
    encode() es para indicar el tipo de codificacion
"""
def parseaNombre(linea):
    fields = linea.split('\"')
    return (int(fields[0]), fields[1])
    #return (int(fields[0]), fields[1].encode("utf8"))

"""
    Se crean los dos RDD con los datos a procesar
    se usan las funciones creadas para darles formato

    La ruta en textFile puede ser de dos maneras
    Con la ruta absoluta "file:///Users/...../bigdata_python_spark/datos/nombre_arch.txt"
    Con la ruta relativa "../datos/ml-100k/nombre_arch.txt"
"""
nombres = sc.textFile("../datos/marvel-names.txt")
nombre_RDD = nombres.map(parseaNombre)

lineas = sc.textFile("../datos/marvel-graph.txt")
popular = lineas.map(cuentaOcurrencia)

"""
    Se busca el nombre de los heroes mas y menos populares
    y se muestra si el set tuviera alguna reundancia se elimina
    con la funcion reduceByKey() y la primer funcion lambda
    se invertira el mapeo del DDR
    clave/valor a valor/clave
    heroeID/num_ocurrencias a num_ocurrencias/heroeID
    con la funcion map() y la segunda funcion lambda
    se encuentra el mayor y menor numero de ocurrencias
    con la funcion max() y min() respectivamente
"""
totales_por_heroe = popular.reduceByKey(lambda x, y : x + y)
invierte_par = totales_por_heroe.map(lambda xy: (xy[1], xy[0]))

mas_popular = invierte_par.max()
menos_popular = invierte_par.min()

"""
    Usando la funcion lookup para buscar el nombre de los superheroes
    al aplicar el mas_popular[1] es el elemento valor heroeID
    clave/valor: num_ocurrencias/heroeID
    esa es la columna que se va a ocupar de pivote
    Para buscar entre DDRs devolviendo de nombre_RDD 
    de clave/valor como superID/nameID
    por eso se pone en el indice el valor de [0]
"""
mas_popular_nombre = nombre_RDD.lookup(mas_popular[1])[0]
menos_popular_nombre = nombre_RDD.lookup(menos_popular[1])[0]

"""
    Se imprime el nombre de los superheroes con sus apariciones
    si se pone el caracter '\' se puede seguir codificando
    en otra linea sin errores
"""
print("El heroe mas popular es " + str(mas_popular_nombre) + " con " + \
    str(mas_popular[0]) + " apariciones con otros superherores." + \
    "\nEl heroe menos popular es " + str(menos_popular_nombre) + " con " + \
    str(menos_popular[0]) + " apariciones con otros superherores.")

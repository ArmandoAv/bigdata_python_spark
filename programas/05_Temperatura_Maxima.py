"""
    Obtener las temperaturas maximas de cada estacion de clima
    del dataset temp1800.txt creado
    
    Recordar que las columnas por archivo son
    estacion_clima_id fecha tipo_observacion temperatura
    11175,18000118,TMAX,27
    1031,18000219,TMAX,36 
    En donde TMAX significa temperatura maxima
"""

# Importamos las librerias de Spark
from pyspark import SparkConf, SparkContext

"""
    Se realiza la configuracion de Spark, de manera local
    se configura para que sea de manera local y se le asigna un nombre
    se la pasa la configuracion realizada al contexto de Spark
    en setMaster se le pueden pasar los nucleos a ejecutar
    esto depende de los nucleos de la maquina local 
    con local[n] siendo n el numero de nucleos a usar
"""
conf = SparkConf().setMaster("local").setAppName("TemperaturasMaximas")
sc = SparkContext(conf = conf)

"""
    Separamos los campos del archivo en listas tomando el caracter ',' como separador
    obtenemos de la lista los campos de la estacion de clima, tipo de medicion y temperatura
"""
def parseoLinea(lineas):
    campos = lineas.split(',')
    estacion_id = campos[0]
    tipo_medicion = campos[2]
    temperatura = campos[3]
    # Si la temperatura se desea en farenheit en lugar de celsius
    #temperatura = float(campos[3]) * 0.1 * (9.0 / 5.0) + 32.0
    return(estacion_id, tipo_medicion, temperatura)

"""
    Se crea el RDD con los datos procesados a partir del archivo original
    filtramos la informacion que necesitamos con el valor de TMAX

    La ruta en textFile puede ser de dos maneras
    Con la ruta absoluta "file:///Users/...../bigdata_python_spark/datos/temp1800.txt"
    Con la ruta relativa "../datos/temp1800.txt"
"""
lineas = sc.textFile("../datos/temp1800.txt")
parseo_lineas = lineas.map(parseoLinea)
temp_max = parseo_lineas.filter(lambda x: "TMAX" in x[1])

"""
    Se crea el nuevo mapa conteniendo las claves y valores
    donde clave/Valor son estacionDeClimaID/temperatura
"""
temp_estacion = temp_max.map(lambda x: (x[0], x[2]))

"""
    Se busca la temperatura maxima por cada estacion
    reduceByKey agrega cada temperatura maxima de cada estacion
    la funcion lambda determinara como hacemos esta accion
    en x, y: se combinan las temperaturas de la misma estacion
    con la funcion max() se encuentra el valor maximo de cada estacion
"""
temp_max_unica = temp_estacion.reduceByKey(lambda x, y: max(x, y))

"""
    Esta funcion regresa todos los elementos de los nodos al nodo controlador
    es decir que recolecta los resultados de la operacion que se acaba de realizar
"""
resultados = temp_max_unica.collect()

# Imprime los resultados obtenidos con ayuda del ciclo for
print("Las temperaturas maximas por cada estacion son las siguientes: ")
for resultado in resultados:
    print(resultado[0] +"\t{}".format(resultado[1]))
    # Si la temperatura hubiera estado en farenheit
	# Se usa el formato {:.2f}F para mostar los resultados a dos decimales y F de farenheit
    # print(resultado[0] +"\t{:.2f}F".format(resultado[1]))

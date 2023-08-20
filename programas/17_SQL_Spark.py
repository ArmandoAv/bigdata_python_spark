"""
    Revisar el comportamiento de algunas funciones de sql en Spark
    del dataset fakefriends.csv

    El archivo tiene la siguiente estructura
    userID Nombre Edad Amigos
"""

# Importamos las librerias de Spark y de collections
from pyspark.sql import SparkSession
from pyspark.sql import Row
import collections

"""
    Se configura la sesion de SQL con la funcion de
    spark.sql.warehouse.dir y el nombre del directorio
"""
sc = SparkSession.builder.config("spark.sql.warehouse.dir", "../datos").appName("SQLSpark").getOrCreate()

"""
    Se crea una funcion que mapea las lineas y se agrega
    nombres a las columnas
    Los nombres son tomados como columnas de una tabla
    en SQL pero el orden que maneja Spark es por orden
    alfabetico dandole prioridad a las mayusculas sobre 
    las minusculas
    En la funcion Row() se asigan el nombre y el tipo de
    columna a cada uno de los campos del archivo
"""
def mapeo(linea):
    campos = linea.split(',')
    return Row(ID=int(campos[0]), nombre=str(campos[1]), edad=int(campos[2]),  num_amigos=int(campos[3]))

"""
    Se crea el DataFrame con los datos a procesar
    se llama a la funcion creada para darle formato

    La ruta en textFile puede ser de dos maneras
    Con la ruta absoluta "file:///Users/...../bigdata_python_spark/datos/fakefriends.csv"
    Con la ruta relativa "../datos/fakefriends.csv"
"""
lineas = sc.sparkContext.textFile("../datos/fakefriends.csv")
gente = lineas.map(mapeo)
print("\nGenerando el DataFrame...")

"""
    Se infiere el esquema y el registro del DataFrame como una tabla
    se asigna el nombre de la tabla y se ocupa la funcion cache()
    para mantener el DataFrame en memoria
"""
esquema_gente = sc.createDataFrame(gente).cache()
esquema_gente.createOrReplaceTempView("people")

# SQL puede correr sobre un DataFrame que han sido registrados como tablas
print("\nSe obtienen todas las columnas como las ordena el DataFrame: \n")
jovenes = sc.sql("SELECT * FROM people WHERE edad >= 18 AND edad <= 25 ORDER BY 2, 4 DESC")

"""
    Los resultados de las consultas SQL soportan las operaciones normales de los RDDs
    el ciclo for devuelve el resultado obtenido de la consulta
"""
for resultado in jovenes.collect():
  print(resultado)

# Se pueden crear consultas SQL con alias y ordenando las columnas como se quiera
print("\nSe obtienen las columnas del DataFrame en un orden especifico y con alias: \n")
joven_orden = sc.sql("""SELECT
      ID as ID_USUARIO,
      nombre as NOMBRE,
      edad as EDAD,
      num_amigos as NUM_AMIGOS
FROM  people 
WHERE edad >= 18 AND edad <= 25 
ORDER BY 3, 4 DESC""")

"""
    Los resultados de las consultas SQL soportan las operaciones normales de los RDDs
    el ciclo for devuelve el resultado obtenido de la consulta
"""
for resultado in joven_orden.collect():
  print(resultado)

"""
    Se pueden usar funciones en lugar de consultas SQL pero solo
    devuelve un top 20 de los resultados
"""
print("\nSe aplica al DataFrame un agrupado y ordenado por edad y un conteo: \n")
esquema_gente.groupBy("edad").count().orderBy("edad").show()
# Tambien se puede aplicar la funcion sort()
#esquema_gente.groupBy("edad").count().sort("edad").show()

print("\nSe aplica al DataFrame un agrupado y ordenado descendente por edad y un conteo: \n")
esquema_gente.groupBy("edad").count().orderBy(esquema_gente.edad.desc()).show()
# Con la funcion sort() se puede hacer de dos formas el ordenamiento descendente
#esquema_gente.groupBy("edad").count().sort("edad", ascending=False).show()
#esquema_gente.groupBy("edad").count().sort(esquema_gente.edad.desc()).show()


# Se detiene la sesion de sparkContext
sc.stop()

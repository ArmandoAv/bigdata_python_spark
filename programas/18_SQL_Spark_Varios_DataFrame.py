"""
    Se revisaran consultas SQL con joins en Spark
    Se usaran los siguientes dataset
    u.data
    u.item
    u.user
    u.genre
"""

# Importamos las librerias de Spark y de collections
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import when
import collections

"""
    Se configura la sesion de SQL con la funcion de
    spark.sql.warehouse.dir y el nombre del directorio
"""
sc = SparkSession.builder.config("spark.sql.warehouse.dir", "../datos/ml-100k").appName("SQLSpark").getOrCreate()

"""
    Se crean varias funciones que mapean las lineas y se
    agrega nombres a las columnas de cada dataset
    Los nombres son tomados como columnas de una tabla
    en SQL pero el orden que maneja Spark es por orden
    alfabetico dandole prioridad a las mayusculas sobre 
    las minusculas
    En la funcion Row() se asigan el nombre y el tipo de
    columna a cada uno de los campos del archivo
"""
def rating(linea):
    campos = linea.split()
    return Row(ID_USUARIO=int(campos[0]), ID_PELICULA=int(campos[1]), RATING=int(campos[2]),  CVE_USUARIO=int(campos[3]))

def pelicula(linea):
    campos = linea.split('|')
    return Row(ID_PELICULA=int(campos[0]), NOM_PELICULA=str(campos[1].encode("utf8")), FCH_CREACION=str(campos[2]), VIDEO=str(campos[3]), \
        URL=str(campos[4]), FLG_GEN_DESCONOCIDO=int(campos[5]), FLG_GEN_ACCION=int(campos[6]), FLG_GEN_AVENTURA=int(campos[7]),\
        FLG_GEN_ANIMACION=int(campos[8]), FLG_GEN_INFANTIL=int(campos[9]),  FLG_GEN_COMEDIA=int(campos[10]), FLG_GEN_CRIMEN=int(campos[11]), \
        FLG_GEN_DOCUMENTALES=int(campos[12]), FLG_GEN_DRAMA=int(campos[13]),  FLG_GEN_FANTASIA=int(campos[14]), FLG_GEN_NEGRO=int(campos[15]), \
        FLG_GEN_TERROR=int(campos[16]), FLG_GEN_MUSICAL=int(campos[17]), FLG_GEN_MISTERIO=int(campos[18]), FLG_GEN_ROMANCE=int(campos[19]), \
        FLG_GEN_SCI_FI=int(campos[20]), FLG_GEN_THRILLER=int(campos[21]), FLG_GEN_GUERRA=int(campos[22]), FLG_GEN_OESTE=int(campos[23]))

def usuario(linea):
    campos = linea.split('|')
    return Row(ID_USUARIO=int(campos[0]), EDAD=int(campos[1]), GENERO_USUARIO=str(campos[2]), OCUPACION=str(campos[3]), CDP=str(campos[4]))

def genero(linea):
    campos = linea.split('|')
    return Row(TIPO_GENERO=str(campos[0]), FLG_GEN=int(campos[1]))

"""
    Se crean los DataFrames con los datos a procesar
    se llaman a las funciones creadas para darles formato

    La ruta en textFile puede ser de dos maneras
    Con la ruta absoluta "file:///Users/...../bigdata_python_spark/datos/ml-100k/nom_arch.txt"
    Con la ruta relativa "../datos/ml-100k/nom_arch.txt"
"""
udata = sc.sparkContext.textFile("../datos/ml-100k/u.data")
ratings = udata.map(rating)

uitem = sc.sparkContext.textFile("../datos/ml-100k/u.item")
peliculas = uitem.map(pelicula)

uuser = sc.sparkContext.textFile("../datos/ml-100k/u.user")
usuarios = uuser.map(usuario)

ugenre = sc.sparkContext.textFile("../datos/ml-100k/u.genre")
generos = ugenre.map(genero)

print("\nGenerando los DataFrames...")

"""
    Se infiere el esquema y el registro de los DataFrames como tablas
    se asignan los nombres de la tablas y se ocupa la funcion cache()
    para mantener los DataFrames en memoria
"""
esquema_ratings = sc.createDataFrame(ratings).cache()
esquema_ratings.createOrReplaceTempView("RATINGS")

esquema_peliculas = sc.createDataFrame(peliculas).cache()
esquema_peliculas.createOrReplaceTempView("PELICULAS")

esquema_usuarios = sc.createDataFrame(usuarios).cache()
esquema_usuarios.createOrReplaceTempView("USUARIOS")

esquema_generos = sc.createDataFrame(generos).cache()
esquema_generos.createOrReplaceTempView("GENEROS")

# SQL puede correr sobre un DataFrame que han sido registrados como tablas
print("\nSe obtienen todas las columnas como las ordena el DataFrame ratings: \n")
resultado_ratings = sc.sql("SELECT * FROM RATINGS WHERE ID_PELICULA = 50 LIMIT 10")

"""
    Los resultados de las consultas SQL soportan las operaciones normales de los RDDs
    el ciclo for devuelve el resultado obtenido de la consulta
"""
for resultados in resultado_ratings.collect():
  print(resultados)

print("\nSe obtienen todas las columnas como las ordena el DataFrame peliculas: \n")
resultado_peliculas = sc.sql("SELECT * FROM PELICULAS LIMIT 10")

"""
    Los resultados de las consultas SQL soportan las operaciones normales de los RDDs
    el ciclo for devuelve el resultado obtenido de la consulta
"""
for resultados in resultado_peliculas.collect():
  print(resultados)

print("\nSe obtienen todas las columnas como las ordena el DataFrame usuarios: \n")
resultado_usuarios = sc.sql("SELECT * FROM USUARIOS LIMIT 10")

"""
    Los resultados de las consultas SQL soportan las operaciones normales de los RDDs
    el ciclo for devuelve el resultado obtenido de la consulta
"""
for resultados in resultado_usuarios.collect():
  print(resultados)

print("\nSe obtienen todas las columnas como las ordena el DataFrame generos: \n")
resultado_generos = sc.sql("SELECT * FROM GENEROS LIMIT 10")

"""
    Los resultados de las consultas SQL soportan las operaciones normales de los RDDs
    el ciclo for devuelve el resultado obtenido de la consulta
"""
for resultados in resultado_generos.collect():
  print(resultados)

# No olvidar dar los espacios requeridos para la consulta SQL
print("\nSe obtienen datos de los usuarios para la pelicula de Terminator 2: \n")
pelicula_usuario = sc.sql("""SELECT 
      R.ID_USUARIO AS ID_USUARIO,
      R.ID_PELICULA AS ID_PELICULA,
	  P.NOM_PELICULA AS NOM_PELICULA,
      P.FCH_CREACION,
	  P.FLG_GEN AS FLG_GEN,
	  G.TIPO_GENERO AS GENERO_PELICULA,
      R.RATING AS RATING,
      U.OCUPACION AS OCUPACION_USUARIO,
      U.GENERO_USUARIO AS GENERO_USUARIO,
      U.EDAD AS EDAD
FROM RATINGS AS R
LEFT JOIN USUARIOS AS U
ON R.ID_USUARIO = U.ID_USUARIO
LEFT JOIN (SELECT 
                 ID_PELICULA,
                 NOM_PELICULA,
                 FCH_CREACION,
                 MIN(CASE WHEN FLG_GEN_DESCONOCIDO= 1 THEN 0
                          WHEN FLG_GEN_ACCION= 1 THEN 1
                          WHEN FLG_GEN_AVENTURA= 1 THEN 2
                          WHEN FLG_GEN_ANIMACION= 1 THEN 3
                          WHEN FLG_GEN_INFANTIL= 1 THEN 4
                          WHEN FLG_GEN_COMEDIA= 1 THEN 5
                          WHEN FLG_GEN_CRIMEN= 1 THEN 6
                          WHEN FLG_GEN_DOCUMENTALES= 1 THEN 7
                          WHEN FLG_GEN_DRAMA= 1 THEN 8
                          WHEN FLG_GEN_FANTASIA= 1 THEN 9
                          WHEN FLG_GEN_NEGRO= 1 THEN 10
                          WHEN FLG_GEN_TERROR= 1 THEN 11
                          WHEN FLG_GEN_MUSICAL= 1 THEN 12
                          WHEN FLG_GEN_MISTERIO= 1 THEN 13
                          WHEN FLG_GEN_ROMANCE= 1 THEN 14
                          WHEN FLG_GEN_SCI_FI= 1 THEN 15
                          WHEN FLG_GEN_THRILLER= 1 THEN 16
                          WHEN FLG_GEN_GUERRA= 1 THEN 17
                          WHEN FLG_GEN_OESTE= 1 THEN 18
                          ELSE 0
                     END) AS FLG_GEN
           FROM  PELICULAS
           GROUP BY ID_PELICULA,
                    NOM_PELICULA,
                    FCH_CREACION) AS P
ON R.ID_PELICULA = P.ID_PELICULA
LEFT JOIN GENEROS AS G
ON P.FLG_GEN = G.FLG_GEN
WHERE R.ID_PELICULA = 96""")

"""
    Los resultados de las consultas SQL soportan las operaciones normales de los RDDs
    el ciclo for devuelve el resultado obtenido de la consulta
"""
for resultado in pelicula_usuario.collect():
  print(resultado)

"""
    Se hace un analisis de los resultados obtenidos de la anterior consulta
    devuelve un top 20 de los resultados
"""
print("\nSe hacen analisis a partir de los datos obtenidos de la pelicula de Terminator 2:")
print("\nSe validan los totales de los ratings de la pelicula Terminator 2:")
pelicula_usuario.groupBy("RATING").count().orderBy("RATING").show()

print("\nSe validan las edades que vieron la pelicula Terminator 2:")
pelicula_usuario.groupBy("EDAD").count().orderBy("EDAD").show()

print("\nSe validan las ocupaciones de los usuarios que vieron la pelicula Terminator 2:")
pelicula_usuario.groupBy("OCUPACION_USUARIO").count().show()

print("\nSe validan cuantos hombres y mujeres vieron la pelicula Terminator 2:")
pelicula_usuario.groupBy("GENERO_USUARIO").count().orderBy(pelicula_usuario.GENERO_USUARIO.desc()).show()

# Se detiene la sesion de sparkContext
sc.stop()

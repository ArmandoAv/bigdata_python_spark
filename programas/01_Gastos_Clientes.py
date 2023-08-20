"""
    Obtener el conteo de ratings de los usuarios
    del dataset customer-orders.csv
    
    Recordar que las columnas del archivo son
    ClienteID Clave Monto
    44,8602,37.19
    35,5368,65.89
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
conf = SparkConf().setMaster("local").setAppName("SpendByCustomerSorted")
sc = SparkContext(conf = conf)

"""
    Se crea el RDD con los datos procesados a partir del archivo original
    separamos los campos del archivo en listas tomando el caracter ',' como separador
    obtenemos de la lista los campos de la edad y el numero de amigos
    creamos el par (clave, valor)
    donde clave/Valor son cliente/monto
    ademas obtenemos el monto total por cada cliente con la funcion lambda

    La ruta en textFile puede ser de dos maneras
    Con la ruta absoluta "file:///Users/...../bigdata_python_spark/datos/customer-orders.csv"
    Con la ruta relativa "../datos/customer-orders.csv"
""" 
def extractCustomerPricePairs(linea):
    campos = linea.split(',')
    return (int(campos[0]), float(campos[2]))

arch = sc.textFile("../datos/customer-orders.csv")
cliente = arch.map(extractCustomerPricePairs)
total_cliente = cliente.reduceByKey(lambda x, y: x + y)

# Invierte el orden del par monto/cliente
invierte_par = total_cliente.map(lambda x: (x[1], x[0]))
# La siguiente funcion es para Python anterior a la version 3
#invierte_par = total_cliente.map(lambda (x,y):(y,x))

# Ordena los clientes
cliente_ordenado = invierte_par.sortByKey()

# Se presentan los datos de los clientes
resultados = cliente_ordenado.collect()
print("Los gastos de los clientes son los siguientes: \n")
print("Monto gastado\tCliente")

for resultado in resultados:
    print(resultado)

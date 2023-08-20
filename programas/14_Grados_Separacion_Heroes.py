"""
    Obtener los grados de separacion entre 2 superheroes
    con el metodo de busqueda Breadth First

    Esto se ocupa mucho al analizar la red de contactos
    en las redes sociales

    Se le deben de pasar dos argumentos al programa
    ID_origen y ID_destino, por ejemplo
    14_Grados_Separacion_Heroes.py 1 2

    Se ocupa el sets de datos
    Marvel-Graph.txt
    empieza con el ID de superheroe a revisar
    seguido con una lista todos los ID de superheroes
    que han aparecido con el, por ejemplo
    271 4935 5716 4309 3829 5794 3405 4929 1449 2940
    3519 4704 2460 763 1602 5306 5358 6121

    Con los siguientes IDs se encuentra al superheroe destino
    Spiderman
    ID_origen: 5306
    Adam 3
    ID_destino: 14

    Con los siguientes IDs no se encuentra al superheroe destino
    24-Hour man
    ID_origen = 1
    Master of vengeance
    ID_destino = 3518

    El metodo funciona como una red de nodos que va 
    aumentando con cada nueva conexion que se va 
    realizando a partir de cada nueva red de contactos
    en el diagrama se observa que los grados de
    separacion del nodo 'n' al nodo 'q' son 5

    m    n    o    p    q    r    s
    1    0    2    3    5    5    ∞
    ®----®    ®----®    ®    ®----®
    |    |  / |    |    |  / |    
    |    | /  |    |    | /  |
    ®    ®----®----®----®----®----®
    2    1    2    3    4    5    ∞
    t    u    v    w    x    y    z
"""

# Importamos las librerias de Spark
import sys
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
conf = SparkConf().setMaster("local").setAppName("GradosSeparacion")
sc = SparkContext(conf = conf)

"""
    Se inicializan las variables con los IDs de los superheroes
    que se desan buscar sus grados de separacion

    Si no se pasan los IDs al ejecutar el programa mandara
    el siguiente error
    id_inicial = int(sys.argv[1])
    IndexError: list index out of range

    Con la funcion argv obtenemos todos los argumentos que se
    pasan al ejecutar un programa incluyendo el nombre del
    programa por lo que el valor de sys.argv[0] en este caso
    seria: 14_Grados_Separacion_Heroes.py
"""
id_inicial = int(sys.argv[1])
id_final = int(sys.argv[2])

"""
    Se ocupa una variable de tipo acumulador
    esta es una variable compartida que sirve como un
    contador en un cluster, pero solo el controlador
    puede acceder a su valor con la funcion value()
    generalmente se inicializa en 0
"""
acumula = sc.accumulator(0)

"""
    Se define el RDD con el que se va a trabajar
    se puede hacer como una funcion y no solo por comandos

    Se crea la funcion que obtiene el archivo original
    que a su vez manda a llamar la funcion generaRDD que
    genera el RDD con ayuda de la funcion map()

    La ruta en textFile puede ser de dos maneras
    Con la ruta absoluta "file:///Users/...../bigdata_python_spark/datos/Marvel-Graph.txt"
    Con la ruta relativa "../datos/Marvel-Graph.txt"
"""
def creaRDDInicial():
    nombre_RDD = sc.textFile("../datos/Marvel-Graph.txt")
    return nombre_RDD.map(generaRDD)

"""
    Funcion que genera el DDR
    Separa las lineas en listas por el caracter de espacio
    y devuelve el ID del heroe asi como una lista todos los 
    IDs a los que esta asociado
	
    Crea las condiciones iniciales de todos los nodos
    agrandoles su color blanco y la distancia 9999 (infinito)
	
    Una vez que se encuentra el nodo inical se pone su
    color gris y su distancia en 0

    Genera una estructura de nodos en forma de una lista anidada
    en donde cada elemento se compone de la siguiente forma
    Posible nodo inicial, (sublista de sus nodos asociados, color, distancia)
    Para los nodos que no contienen al superheroe a buscar
    (106, ([748, 1722, 3752, 4655, 5743, 1872, 3413, 5527], 9999, 'WHITE'))
    Para el nodo que contien al superheroe a buscar
    (5306, ([3569, 5353, 4087, 2653, 2058, 2218, 5354, 5306], 0, 'GRAY'))
"""
def generaRDD(linea):
    campos = linea.split()
    id_heroe = int(campos[0])
    conexiones = []
    for conexion in campos[1:]:
        conexiones.append(int(conexion))
    # Se inicializan todos los nodos del RDD con el color: blanco y la distancia infinito: 9999
    color = 'WHITE'
    distancia = 9999
    # Se cambia el color: gris y la distancia: 0 del nodo inicial
    if (id_heroe == id_inicial):
        color = 'GRAY'
        distancia = 0

    # Devuelve la lista con el arreglo de todos los nodos
    return (id_heroe, (conexiones, distancia, color))

"""
    Se define una funcion que crea nuevos vértices según sea necesario 
    para oscurecer o reducir distancias si encontramos el nodo destino
    que estamos buscando como un nodo de color GRIS se incrementa el 
    acumulador para indicar que hemos terminado

    Los nodos que tienen un color gris se cambian a negro para indicar
    que ya fueron analizados
"""
def actualizaNuevosNodos(nodo):
    # Separa los elementos de la lista y sublista para ser tratados
    id_heroe = nodo[0]
    datos = nodo[1]
    conexiones = datos[0]
    distancia = datos[1]
    color = datos[2]

    resultados = []

    # Se evalua si el nodo necesita ser expandido, por el color del nodo
    # solo se expande si el color del nodo es gris
    if (color == 'GRAY'):
        for conexion in conexiones:

            # Para cada nodo asociado se aumenta el valor de la distancia
            # se pone en gris su color
            id_heroe_nuevo = conexion
            distancia_nueva = distancia + 1
            color_nuevo = 'GRAY'

             # Se valida si alguno de los nuevos nodos es el nodo destino
             # en caso afirmativo se aumenta el valor del acumulador en 1
            if (id_final == conexion):
                acumula.add(1)

            # A los nuevos nodos asociados, se agregan en una lista
            # el primer elemento es el ID del nodo y para la sublista
            # su primer elemento se crea una lista vacia para seguir
            # conservando la misma estructura, su segundo elemento
            # es la nueva distancia y el ultimo es el color es gris
            entrada_nueva = (id_heroe_nuevo, ([], distancia_nueva, color_nuevo))
            resultados.append(entrada_nueva)

        # Al nodo procesado se le cambia el color a negro
        color = 'BLACK'

    # Se agrega a la lista los valores del nodo procesado
    # con el nuevo color negro
    resultados.append( (id_heroe, (conexiones, distancia, color)) )
    return resultados

"""
    Se define una funcion que elimina los registros que tienen sublistas 
    duplicadas esto es para eliminar los nodos que quedaron con sublistas 
    vacias asi como nodos con sublistas que puedan estar duplicadas
    
    Por ejemplo
    (6294, ([], 1, 'GRAY')),
    (6294, ([4898, 1127, 3220], 9999, 'WHITE')),
    (271, ([4935, 5716, 4309], 9999, 'WHITE')),
    (271, ([4929, 1449, 2940], 9999, 'WHITE')),

    Se revisan los colores para que los nodos queden con el color correcto
"""
def unificaNodos(datos_1, datos_2):
    edges1 = datos_1[0]
    edges2 = datos_2[0]
    distancia1 = datos_1[1]
    distancia2 = datos_2[1]
    color1 = datos_1[2]
    color2 = datos_2[2]

    distancia = 9999
    color = 'WHITE'
    edges = []

    # Se revisan las listas de elementos de las sublistas y se
    # obtienen las sublistas que tienen datos por lo que los 
    # nodos con sublistas sin datos se van eliminando siempre
    # que haya otro nodo con sublistas con datos y con la
    # funcion extend() se agregan los resultados obtenidos
    # 
    # Por lo que los siguientes registros
    # []
    # [4898, 1127, 3220]
    #
    # [4935, 5716, 4309]
    # [4929, 1449, 2940]
    # 
    # Quedan de la siguiente manera
    # [4898, 1127, 3220]
    # [4935, 5716, 4309, 4929, 1449, 2940]
    if (len(edges1) > 0):
        edges.extend(edges1)

    if (len(edges2) > 0):
        edges.extend(edges2)

    # Se actualiza la distancia si ya no tiene el valor de 9999
    # esto es para los nodos que se van revisando
    if (distancia1 < distancia):
        distancia = distancia1

    if (distancia2 < distancia):
        distancia = distancia2

    # El color mas oscuro es el que se preserva
    # esto es para los nodos que se van revisando
    # para que los nodos pueden no estar sincronizados
    if (color1 == 'WHITE' and (color2 == 'GRAY' or color2 == 'BLACK')):
        color = color2

    if (color1 == 'GRAY' and color2 == 'BLACK'):
        color = color2

    if (color2 == 'WHITE' and (color1 == 'GRAY' or color1 == 'BLACK')):
        color = color1

    if (color2 == 'GRAY' and color1 == 'BLACK'):
        color = color1

    # Devuelve la sublista, distancia y color sincronizados
    return (edges, distancia, color)

"""
    Este es el cuerpo del programa principal
    se manda a llamar la funcion que crea el DDR
"""
itera_RDD = creaRDDInicial()

"""
    Se crea un ciclo for con un maximo de posible de relacion entre superheroes
    esto es debido a que si dos superheroes no tiene conexion entre ambos el
    programa pueda detenerse despues de 10 iteraciones
"""
print("\nSe inicia el proceso para llegar del ID de superheroe: " + \
    str(id_inicial) + " al ID de superheroe " + str(id_final))
for iteraciones in range(0, 10):
    print("\nEjecutando la iteration # " + str(iteraciones + 1) + \
        " para llegar al ID de superheroe destino")

    # Se manda llamar la funcion que crea nuevos vértices según sea necesario 
    # utlizando la funcion flatMap(): para poder tratar los elementos de la
    # lista y la sublista de nodos de distintas formas
    # Posible nodo inicial, (sublista de sus nodos asociados, color y distancia)
    # Para los valores que no cumplen con las condiciones de la funcion 
    # actualizaNuevosNodos() la funcion flatMap() los deja igual ya que
    # esta funcion tiene la capacidad de obtener varias salidas de una
    # misma entrada
    mapeado = itera_RDD.flatMap(actualizaNuevosNodos)

    # Se revisa como se va actualizando el DDR con la expension de nodos
    # asi como la reducion de nodos duplicados
    print("Procesando " + str(mapeado.count()) + " valores.")

    # Se evalua si el acumulador ya tiene un valor mayor 0
    # este valor se modifica cuando se encuentra el nodo destino
    # en la funcion actualiza_unificaNodos()
    if (acumula.value > 0):
        print("\nSe encontro al superheroe destino! Tiene " + str(iteraciones + 1) \
            + " grado(s) de separacion con el super heroe origen.")
        break

    # Reduce las sublistas, distancia y colores de los nodos duplicados
    # con la funcion reduceByKey() se mandan a la funcion unificaNodos()
    # todos los datos sin los nodos (claves), debido a su funcionalidad
    itera_RDD = mapeado.reduceByKey(unificaNodos)

    # Valida si el nodo destino no fue encontrado
    # despues de 10 iteraciones que tiene el ciclo for
    if (acumula.value == 0 and iteraciones == 9):
        print("\nNo se pudo encontrar al superheroe destino!")

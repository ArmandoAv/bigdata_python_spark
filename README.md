# bigdata_python_spark

Anaconda

El software se obtiene de la siguiente liga

https://anaconda.org

Debido a que esta instalación se hizo en Windows 7, se obtuvo la versión de Anaconda3 4.4.0 para 64 bits, de la siguente liga

https://repo.anaconda.com/archive/

Una vez instalado anaconda, se abre su navegador y se crea un nuevo ambiente indicando que se requiere python 3.5, esto es debido a que Spark funciona con python 3.5.

Si se tiene una versión diferente de python previamente instalado, no es necesario desinstalarlo ya que al momento de crear el ambiente con anaconda la versión de python que se indica será instalada para dicho ambiente.

Java

Se debe de instalar el jdk y jre, por lo menos debe de instalarse la version 8 con la actualizacion 60 jdk-8u60-windows-i586. Dentro del instalador viene el jdk y el jre, se deben de instalar sobre las carpetas C:\jdk y C:\jre respectivamente.

De la siguiente ruta vienen diferentes versiones de java 8

https://www.oracle.com/mx/java/technologies/javase/javase8-archive-downloads.html

Spark

De la siguiente liga se pueden ver diferentes versiones de Spark

https://archive.apache.org/dist/spark/

Como es Windows 7 donde se está realizando la instalación se baja la version spark-2.4.3-bin-hadoop2.7.tgz. Como el archivo viene con extension .tgz, se debe de tener instalado winrar para poder abrirlo.

Al abrir el archivo el contenido del mismo se debe de copiar a la carpeta C:\spark

Una vez que el contenido se pasó a la carpeta de de spark, en la carpeta C:\spark. Se debe de buscar en la carpeta C:\spark\conf el archivo log4j.properties.template y renombrarlo como log4j.properties. Despues se abre el archivo renmbrado con un editor de texto y en la siguiente linea del archivo

log4j.rootCategory=INFO, console

Se debe de cambiar por

log4j.rootCategory=ERROR, console

Esto se hace para que al momento de ejecutar comandos de Spark en una terminal esta no se llene de información que no es necesaria.

WinUtils

Debido a que en windows no se puede utilizar Spark de forma nativa, se debe de bajar el archivo winutils.exe, en la siguente liga vienen diferentes versiones del archivo

https://github.com/steveloughran/winutils/tree/master

Se baja un archivo para version de hadoop 2.7. Este archivo se debe de poner en la carpeta C:\winutils\bin

Activacion de Spark

Una vez hecho estos pasos se crean la siguientes variables de ambiente

JAVA_HOME = C:\jdk
SPARK_HOME = C:\spark
HADOOP_HOME = C:\winutils

Se agregan las variables %JAVA_HOME%\bin, %SPARK_HOME%\bin y %HADOOP_HOME%\bin a la variable Path

Una vez hecho esto se abre una terminal y ejecutan los siguientes comandos

cd /spark
pyspark

El comando pyspark levanta el ambiente de Spark, si todo funciona correctamente debe de salir al final lo siguiente

Welcome to
\_**\_ **
/ **/** **\_ \_\_\_**/ /**
_\ \/ _ \/ \_ `/ **/ '_/
/** / .**/\_,_/_/ /_/\_\ version 2.4.3
/\_/

Using Python version 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019 22:22:05)
SparkSession available as 'spark'.

> > >

Mientras este activado Spark o se esté ejecutando algún programa, se puede ir a la siguiente liga

localhost:4040

Ahi se encuentra la consola grafica de Spark

Los archivos que se necesitan, ya se encuentran en la carpeta de datos. Correran bien si se respeta la jerarquía del proyecto, de lo contrario se deberan de hacer las modificaciones pertinentes en los programas para que apunten a las nuevas rutas donde se depositaran los archivos.

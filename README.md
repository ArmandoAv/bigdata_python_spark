# bigdata_python_spark

The following software was used to carry out this project:

- Python 3.7.3
- Jdk of Java 1.8_u60 or higher
- Jre of Java 1.8_u60 or higher
- Apache Spark 2.4.3
- winutils.exe

## Python

In the following link is the version of Python 3.7.3

https://www.python.org/downloads/release/python-373/

To install Python, run the file python-3.7.3-amd64.exe which was downloaded from the link. When executing the file, in the same process it indicates that if you want to save the Python variable in the environment variables, so it is no longer necessary to add them when finishing the installation.

A cmd terminal is opened and validated, execute the next command

```
python --version
```

Python has a library with which you can install plugins on the command line called pip. Copy the script from the following link into a notepad

https://bootstrap.pypa.io/get-pip.py

Save the copied script as get-pip.py and open a cmd terminal in the path where you saved the file and executed the following command

```
python get-pip.py
```

The following environment variable must be created

```
PIP_HOME = C:\Users\.....\AppData\Local\Programs\Python\Python37
```
The %PIP_HOME%\Scripts variable is added to the Path variable.

## Java

In the following link there are different versions of Java 8

https://www.oracle.com/mx/java/technologies/javase/javase8-archive-downloads.html

To install jdk and jre, run the file jdk-...-i586.exe which was downloaded from the link. When executing the file, the paths C:\jdk and C:\jre must be indicated when installing each one. When the jdk and jre are installed, the following environment variable must be created

```
JAVA_HOME = C:\jdk
```

The %JAVA_HOME%\bin variable is added to the Path variable.

A cmd terminal is opened and it is validated that any of the following commands are valid.

```
java
java --version
```

## Spark

In the following link there is the version of Apache Spark 2.4.3

https://archive.apache.org/dist/spark/

Once you have the spark-2.4.3-bin-hadoop2.7.tgz file, you must create the C:\spark directory and copy all the contents of the file to that path.

Once the content has been copied, look in the C:\spark\conf directory for the log4j.properties.template file and rename it as log4j.properties. Then open the renamed file with a text editor and on the next line of the file

```
log4j.rootCategory=INFO, console
```

It should be changed to

```
log4j.rootCategory=ERROR, console
```

This is done so that when executing Spark commands in a terminal, it does not fill up with information that is not necessary. The following environment variable must be created

```
SPARK_HOME = C:\spark
```

The %SPARK_HOME%\bin variable is added to the Path variable.

## Winutils

In the following link is the winutils software with version hadoop 2.7

https://github.com/steveloughran/winutils/tree/master

You must create the C:\winutils\bin directory and copy the winutils.exe file to that path. Once the file has been copied, the following environment variable must be created

```
HADOOP_HOME = C:\winutils
```

The %HADOOP_HOME%\bin variable is added to the Path variable.

A cmd terminal is opened and validated, execute the nexts commands, if everything works correctly, the Spark environment will start.

```
cd C:\spark
pyspark
```

If everything works correctly, the following should appear at the end

```
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.4.3
      /_/

Using Python version 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019 22:22:05)
SparkSession available as 'spark'.
>>>
```

While Spark is activated or a program is running, you can go to the following link

localserver: 4040

Here is the Spark graphical console.

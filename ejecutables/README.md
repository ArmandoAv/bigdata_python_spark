Para generar dos RDD de amigos y temperatura.

se deben ejecutar los pasos que se enlistan a continuación. Estos pasos son para Windows con los archivos .bat, pero se crearon scripts de tipo .sh para que puedan ser ejecutados en Linux también.

1. Se debe de crear la carpeta de ejecutables y entradas al mismo nivel

      nom_proyecto
      ├───ejecutables
      └───datos

2. Abrir una consola de cmd e irse a la ruta de ejecutables definida en el punto 1

2. Ejecutar el comando dir 
      Con esto se veran todos los archivos ejecutables, solo hay dos tipos de archivos
            Los archivos que empiezan por un numero
                  01_Genera_amigos_Lnx.sh
                  01_Genera_amigos_Win.bat
                  02_Genera_temperatura_Lnx.sh
                  02_Genera_temperatura_Win.bat

            Estos archivos son los que generan algun DDR.

            El archivo llamado
                  Ejecuta_archivo_nveces.bat
            Este archivo ejecuta los archivos que empiezan por un número

3. Ejecutar el comando Ejecuta_archivo_nveces.bat
      Este archivo pedira dos parametros
            El nombre del archivo a ejecutar y las veces que se desea ser ejecutado
            Se deben de ejecutar varios 1000 de veces para generar un buen volumen de datos

      Al ejecutar el archivo mandará esta salida en la consola
            Poner el nombre del archivo a ejecutar con la extension .bat:
            Aqui se escribe algun archivo que empiece con un numero

            Cuantas veces se desa ejecutar el archivo, debe ser mas de 1:
            Aqui se escribe cuantas veces se desea ejecutar ese archivo

4. Al ejecutar el paso tres nos da la siguiente salida
   Poniendo al archivo 02_Genera_temperatura.bat de ejemplo y ejecutandolo 2500 veces
   
      C:\.....\proyecto\ejecutables>Ejecuta_archivo_nveces.bat
      Poner el nombre del archivo a ejecutar con la extension .bat:
      02_Genera_temperatura.bat
      Cuantas veces se desea ejecutar el archivo, debe ser mas de 1:
      2500

      C:\.....\proyecto\ejecutables>

5. El archivo genera en automatico el RDD en la ruta de entradas, en esta caso seria

      C:\.....\proyecto\datos\temp1800.txt

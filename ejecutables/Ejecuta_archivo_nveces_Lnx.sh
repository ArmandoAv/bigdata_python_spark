# Ejecuta un archivo que genera datos n veces
# Se deben de pasar dos parámetros al shell
# El primer parametro es el nombre del shell que se desea ejecutar
# 01_Genera_amigos_Lnx.sh o 02_Genera_temperatura_Lnx.sh
# El segundo parametro son las veces que desea ejecutar el shell
# Por ejemplo:
# sh Ejecuta_archivo_nveces_Lnx.sh 01_Genera_amigos_Lnx.sh 1000


# Variables a ejecutar
arch_ejecutar=$1
nveces=$2

# Se le pasa como parametro el nombre del archivo a ejecutar
echo Se ejecutara el archivo: $arch_ejecutar

# Manda a llamar el archivo solicitado n veces
echo Se ejecutara: $nveces

# Se ejecuta el archivo deseado las n veces solicitadas
for ((i=1; i<=$nveces; i++))
do
    sh $arch_ejecutar
done

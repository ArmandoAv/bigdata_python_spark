:: Ejecuta un archivo que genera datos n veces

@ECHO OFF

:: Se le pasa como parametro el nombre del archivo a ejecutar
echo Poner el nombre del archivo a ejecutar con la extension .bat: 
set /p arch_ejecutar=

:: Manda a llamar el archivo solicitado n veces
echo Cuantas veces se desea ejecutar el archivo, debe ser mas de 1: 
set /p nveces=

:: Se ejecuta el archivo deseado las n veces solicitadas
for /L %%x in (1, 1, %nveces%) do (
   call %arch_ejecutar%
)

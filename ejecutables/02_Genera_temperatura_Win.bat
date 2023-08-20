:: Genera archivo de temperaturas el año 1800

@ECHO OFF

:: Rango de dias enero
set /a min01=101
set /a max01=131
set /a mes01=%max01% - %min01% + 1

:: Rango de dias febrero
set /a min02=201
set /a max02=229
set /a mes02=%max02% - %min02% + 1

:: Rango de dias marzo
set /a min03=301
set /a max03=331
set /a mes03=%max03% - %min03% + 1

:: Rango de dias abril
set /a min04=401
set /a max04=430
set /a mes04=%max04% - %min04% + 1

:: Rango de dias mayo
set /a min05=501
set /a max05=531
set /a mes05=%max05% - %min05% + 1

:: Rango de dias junio
set /a min06=601
set /a max06=630
set /a mes06=%max06% - %min06% + 1

:: Rango de dias julio
set /a min07=701
set /a max07=731
set /a mes07=%max07% - %min07% + 1

:: Rango de dias agosto
set /a min08=801
set /a max08=831
set /a mes08=%max08% - %min08% + 1

:: Rango de dias septiembre
set /a min09=901
set /a max09=930
set /a mes09=%max09% - %min09% + 1

:: Rango de dias octubre
set /a min10=1001
set /a max10=1031
set /a mes10=%max10% - %min10% + 1

:: Rango de dias noviembre
set /a min11=1101
set /a max11=1130
set /a mes11=%max11% - %min11% + 1

:: Rango de dias diciembre
set /a min12=1201
set /a max12=1231
set /a mes12=%max12% - %min12% + 1

:: Rango de temperatura minima
set rmin=0
set rmax=15
set /a tmin=%rmax% - %rmin% + 1

:: Rango de temperatura maxima
set rmmin=25
set rmmax=45
set /a tmax=%rmmax% - %rmmin% + 1

:: Rango de temperatura media
set rmemin=15
set rmemax=30
set /a tmed=%rmemax% - %rmemin% + 1

:: Rango de estaciones
set estmin=10000
set estmax=10030
set /a rangest=%estmax% - %estmin% + 1

:: Genera temperaturas minimas

:: Genera un numero aleatorio hasta del 10000 al 10030
Set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio del -40 al 15
Set /a _temp=(%RANDOM%*%tmin%/32768)+%rmin%
:: Genera dias de enero
set /a diames=(%RANDOM%*%mes01%/32768)+%min01%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMIN,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
Set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio del -40 al 15
Set /a _temp=(%RANDOM%*%tmin%/32768)+%rmin%
:: Genera dias de febrero
set /a diames=(%RANDOM%*%mes02%/32768)+%min02%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMIN,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
Set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio del -40 al 15
Set /a _temp=(%RANDOM%*%tmin%/32768)+%rmin%
:: Genera dias de marzo
set /a diames=(%RANDOM%*%mes03%/32768)+%min03%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMIN,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
Set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio del -40 al 15
Set /a _temp=(%RANDOM%*%tmin%/32768)+%rmin%
:: Genera dias de abril
set /a diames=(%RANDOM%*%mes04%/32768)+%min04%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMIN,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
Set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio del -40 al 15
Set /a _temp=(%RANDOM%*%tmin%/32768)+%rmin%
:: Genera dias de mayo
set /a diames=(%RANDOM%*%mes05%/32768)+%min05%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMIN,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
Set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio del -40 al 15
Set /a _temp=(%RANDOM%*%tmin%/32768)+%rmin%
:: Genera dias de junio
set /a diames=(%RANDOM%*%mes06%/32768)+%min06%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMIN,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
Set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio del -40 al 15
Set /a _temp=(%RANDOM%*%tmin%/32768)+%rmin%
:: Genera dias de julio
set /a diames=(%RANDOM%*%mes07%/32768)+%min07%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMIN,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
Set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio del -40 al 15
Set /a _temp=(%RANDOM%*%tmin%/32768)+%rmin%
:: Genera dias de agosto
set /a diames=(%RANDOM%*%mes08%/32768)+%min08%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMIN,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
Set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio del -40 al 15
Set /a _temp=(%RANDOM%*%tmin%/32768)+%rmin%
:: Genera dias de septiembre
set /a diames=(%RANDOM%*%mes09%/32768)+%min09%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMIN,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
Set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio del -40 al 15
Set /a _temp=(%RANDOM%*%tmin%/32768)+%rmin%
:: Genera dias de octubre
set /a diames=(%RANDOM%*%mes10%/32768)+%min10%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,1800%diames%,TMIN,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
Set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio del -40 al 15
Set /a _temp=(%RANDOM%*%tmin%/32768)+%rmin%
:: Genera dias de noviembre
set /a diames=(%RANDOM%*%mes11%/32768)+%min11%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,1800%diames%,TMIN,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
Set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio del -40 al 15
Set /a _temp=(%RANDOM%*%tmin%/32768)+%rmin%
:: Genera dias de diciembre
set /a diames=(%RANDOM%*%mes12%/32768)+%min12%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,1800%diames%,TMIN,%_temp% >> ..\datos\temp1800.txt


:: Genera temperaturas maximas

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 25 al 45
set /a _temp=(%RANDOM%*%tmax%/32768)+%rmmin%
:: Genera dias de enero
set /a diames=(%RANDOM%*%mes01%/32768)+%min01%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMAX,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 25 al 45
set /a _temp=(%RANDOM%*%tmax%/32768)+%rmmin%
:: Genera dias de febrero
set /a diames=(%RANDOM%*%mes02%/32768)+%min02%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMAX,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 25 al 45
set /a _temp=(%RANDOM%*%tmax%/32768)+%rmmin%
:: Genera dias de marzo
set /a diames=(%RANDOM%*%mes03%/32768)+%min03%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMAX,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 25 al 45
set /a _temp=(%RANDOM%*%tmax%/32768)+%rmmin%
:: Genera dias de abril
set /a diames=(%RANDOM%*%mes04%/32768)+%min04%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMAX,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 25 al 45
set /a _temp=(%RANDOM%*%tmax%/32768)+%rmmin%
:: Genera dias de mayo
set /a diames=(%RANDOM%*%mes05%/32768)+%min05%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMAX,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 25 al 45
set /a _temp=(%RANDOM%*%tmax%/32768)+%rmmin%
:: Genera dias de junio
set /a diames=(%RANDOM%*%mes06%/32768)+%min06%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMAX,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 25 al 45
set /a _temp=(%RANDOM%*%tmax%/32768)+%rmmin%
:: Genera dias de julio
set /a diames=(%RANDOM%*%mes07%/32768)+%min07%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMAX,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 25 al 45
set /a _temp=(%RANDOM%*%tmax%/32768)+%rmmin%
:: Genera dias de agosto
set /a diames=(%RANDOM%*%mes08%/32768)+%min08%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMAX,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 25 al 45
set /a _temp=(%RANDOM%*%tmax%/32768)+%rmmin%
:: Genera dias de septiembre
set /a diames=(%RANDOM%*%mes09%/32768)+%min09%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMAX,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 25 al 45
set /a _temp=(%RANDOM%*%tmax%/32768)+%rmmin%
:: Genera dias de octubre
set /a diames=(%RANDOM%*%mes10%/32768)+%min10%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,1800%diames%,TMAX,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 25 al 45
set /a _temp=(%RANDOM%*%tmax%/32768)+%rmmin%
:: Genera dias de noviembre
set /a diames=(%RANDOM%*%mes11%/32768)+%min11%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,1800%diames%,TMAX,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 25 al 45
set /a _temp=(%RANDOM%*%tmax%/32768)+%rmmin%
:: Genera dias de diciembre
set /a diames=(%RANDOM%*%mes12%/32768)+%min12%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,1800%diames%,TMAX,%_temp% >> ..\datos\temp1800.txt


:: Genera temperaturas medias

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de enero
set /a diames=(%RANDOM%*%mes01%/32768)+%min01%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de enero
set /a diames=(%RANDOM%*%mes01%/32768)+%min01%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de febrero
set /a diames=(%RANDOM%*%mes02%/32768)+%min02%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de febrero
set /a diames=(%RANDOM%*%mes02%/32768)+%min02%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de marzo
set /a diames=(%RANDOM%*%mes03%/32768)+%min03%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de marzo
set /a diames=(%RANDOM%*%mes03%/32768)+%min03%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de abril
set /a diames=(%RANDOM%*%mes04%/32768)+%min04%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de abril
set /a diames=(%RANDOM%*%mes04%/32768)+%min04%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de mayo
set /a diames=(%RANDOM%*%mes05%/32768)+%min05%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de mayo
set /a diames=(%RANDOM%*%mes05%/32768)+%min05%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de junio
set /a diames=(%RANDOM%*%mes06%/32768)+%min06%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de junio
set /a diames=(%RANDOM%*%mes06%/32768)+%min06%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de julio
set /a diames=(%RANDOM%*%mes07%/32768)+%min07%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de julio
set /a diames=(%RANDOM%*%mes07%/32768)+%min07%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de agosto
set /a diames=(%RANDOM%*%mes08%/32768)+%min08%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de agosto
set /a diames=(%RANDOM%*%mes08%/32768)+%min08%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de septiembre
set /a diames=(%RANDOM%*%mes09%/32768)+%min09%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de septiembre
set /a diames=(%RANDOM%*%mes09%/32768)+%min09%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,18000%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de octubre
set /a diames=(%RANDOM%*%mes10%/32768)+%min10%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,1800%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de octubre
set /a diames=(%RANDOM%*%mes10%/32768)+%min10%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,1800%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de noviembre
set /a diames=(%RANDOM%*%mes11%/32768)+%min11%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,1800%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de noviembre
set /a diames=(%RANDOM%*%mes11%/32768)+%min11%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,1800%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de diciembre
set /a diames=(%RANDOM%*%mes12%/32768)+%min12%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,1800%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

:: Genera un numero aleatorio hasta del 10000 al 10100
set /a _esta=(%RANDOM%*%rangest%/32768)+%estmin%
:: Genera un numero aleatorio hasta del 15 al 30
set /a _temp=(%RANDOM%*%tmed%/32768)+%rmemin%
:: Genera dias de diciembre
set /a diames=(%RANDOM%*%mes12%/32768)+%min12%
:: Pega la informacion en el archivo de temperatura
Echo Met%_esta%,1800%diames%,TMED,%_temp% >> ..\datos\temp1800.txt

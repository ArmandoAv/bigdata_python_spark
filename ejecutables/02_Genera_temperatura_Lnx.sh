# Genera archivo de temperaturas el año 1800


# Rango de dias enero
min01=101
max01=131
let mes01=$max01-$min01+1

# Rango de dias febrero
min02=201
max02=229
let mes02=$max02-$min02+1

# Rango de dias marzo
min03=301
max03=331
let mes03=$max03-$min03+1

# Rango de dias abril
min04=401
max04=430
let mes04=$max04-$min04+1

# Rango de dias mayo
min05=501
max05=531
let mes05=$max05-$min05+1

# Rango de dias junio
min06=601
max06=630
let mes06=$max06-$min06+1

# Rango de dias julio
min07=701
max07=731
let mes07=$max07-$min07+1

# Rango de dias agosto
min08=801
max08=831
let mes08=$max08-$min08+1

# Rango de dias septiembre
min09=901
max09=930
let mes09=$max09-$min09+1

# Rango de dias octubre
min10=1001
max10=1031
let mes10=$max10-$min10+1

# Rango de dias noviembre
min11=1101
max11=1130
let mes11=$max11-$min11+1

# Rango de dias diciembre
min12=1201
max12=1231
let mes12=$max12-$min12+1

# Rango de temperatura minima
rmin=0
rmax=15
let tmin=$rmax-$rmin+1

# Rango de temperatura maxima
rmmin=25
rmmax=45
let tmax=$rmmax-$rmmin+1

# Rango de temperatura media
rmemin=15
rmemax=30
let tmed=$rmemax-$rmemin+1

# Rango de estaciones
estmin=10000
estmax=10030
let rangest=$estmax-$estmin+1

# Genera temperaturas minimas

# Genera un numero aleatorio hasta del 10000 al 10030
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio del -40 al 15
temp=$(($(($RANDOM%$tmin))+$rmin))
# Genera dias de enero
diames=$(($(($RANDOM%$mes01))+$min01))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMIN,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio del -40 al 15
temp=$(($(($RANDOM%$tmin))+$rmin))
# Genera dias de febrero
diames=$(($(($RANDOM%$mes02))+$min02))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMIN,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio del -40 al 15
temp=$(($(($RANDOM%$tmin))+$rmin))
# Genera dias de marzo
diames=$(($(($RANDOM%$mes03))+$min03))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMIN,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio del -40 al 15
temp=$(($(($RANDOM%$tmin))+$rmin))
# Genera dias de abril
diames=$(($(($RANDOM%$mes04))+$min04))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMIN,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio del -40 al 15
temp=$(($(($RANDOM%$tmin))+$rmin))
# Genera dias de mayo
diames=$(($(($RANDOM%$mes05))+$min05))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMIN,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio del -40 al 15
temp=$(($(($RANDOM%$tmin))+$rmin))
# Genera dias de junio
diames=$(($(($RANDOM%$mes06))+$min06))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMIN,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio del -40 al 15
temp=$(($(($RANDOM%$tmin))+$rmin))
# Genera dias de julio
diames=$(($(($RANDOM%$mes07))+$min07))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMIN,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio del -40 al 15
temp=$(($(($RANDOM%$tmin))+$rmin))
# Genera dias de agosto
diames=$(($(($RANDOM%$mes08))+$min08))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMIN,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio del -40 al 15
temp=$(($(($RANDOM%$tmin))+$rmin))
# Genera dias de septiembre
diames=$(($(($RANDOM%$mes09))+$min09))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMIN,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio del -40 al 15
temp=$(($(($RANDOM%$tmin))+$rmin))
# Genera dias de octubre
diames=$(($(($RANDOM%$mes10))+$min10))
# Pega la informacion en el archivo de temperatura
echo Met$esta,1800$diames,TMIN,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio del -40 al 15
temp=$(($(($RANDOM%$tmin))+$rmin))
# Genera dias de noviembre
diames=$(($(($RANDOM%$mes11))+$min11))
# Pega la informacion en el archivo de temperatura
echo Met$esta,1800$diames,TMIN,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio del -40 al 15
temp=$(($(($RANDOM%$tmin))+$rmin))
# Genera dias de diciembre
diames=$(($(($RANDOM%$mes12))+$min12))
# Pega la informacion en el archivo de temperatura
echo Met$esta,1800$diames,TMIN,$temp >> ../datos/temp1800.txt


# Genera temperaturas maximas

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 25 al 45
temp=$(($(($RANDOM%$tmax))+$rmmin))
# Genera dias de enero
diames=$(($(($RANDOM%$mes01))+$min01))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMAX,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 25 al 45
temp=$(($(($RANDOM%$tmax))+$rmmin))
# Genera dias de febrero
diames=$(($(($RANDOM%$mes02))+$min02))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMAX,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 25 al 45
temp=$(($(($RANDOM%$tmax))+$rmmin))
# Genera dias de marzo
diames=$(($(($RANDOM%$mes03))+$min03))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMAX,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 25 al 45
temp=$(($(($RANDOM%$tmax))+$rmmin))
# Genera dias de abril
diames=$(($(($RANDOM%$mes04))+$min04))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMAX,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 25 al 45
temp=$(($(($RANDOM%$tmax))+$rmmin))
# Genera dias de mayo
diames=$(($(($RANDOM%$mes05))+$min05))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMAX,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 25 al 45
temp=$(($(($RANDOM%$tmax))+$rmmin))
# Genera dias de junio
diames=$(($(($RANDOM%$mes06))+$min06))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMAX,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 25 al 45
temp=$(($(($RANDOM%$tmax))+$rmmin))
# Genera dias de julio
diames=$(($(($RANDOM%$mes07))+$min07))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMAX,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 25 al 45
temp=$(($(($RANDOM%$tmax))+$rmmin))
# Genera dias de agosto
diames=$(($(($RANDOM%$mes08))+$min08))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMAX,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 25 al 45
temp=$(($(($RANDOM%$tmax))+$rmmin))
# Genera dias de septiembre
diames=$(($(($RANDOM%$mes09))+$min09))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMAX,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 25 al 45
temp=$(($(($RANDOM%$tmax))+$rmmin))
# Genera dias de octubre
diames=$(($(($RANDOM%$mes10))+$min10))
# Pega la informacion en el archivo de temperatura
echo Met$esta,1800$diames,TMAX,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 25 al 45
temp=$(($(($RANDOM%$tmax))+$rmmin))
# Genera dias de noviembre
diames=$(($(($RANDOM%$mes11))+$min11))
# Pega la informacion en el archivo de temperatura
echo Met$esta,1800$diames,TMAX,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 25 al 45
temp=$(($(($RANDOM%$tmax))+$rmmin))
# Genera dias de diciembre
diames=$(($(($RANDOM%$mes12))+$min12))
# Pega la informacion en el archivo de temperatura
echo Met$esta,1800$diames,TMAX,$temp >> ../datos/temp1800.txt


# Genera temperaturas medias

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de enero
diames=$(($(($RANDOM%$mes01))+$min01))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de enero
diames=$(($(($RANDOM%$mes01))+$min01))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de febrero
diames=$(($(($RANDOM%$mes02))+$min02))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de febrero
diames=$(($(($RANDOM%$mes02))+$min02))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de marzo
diames=$(($(($RANDOM%$mes03))+$min03))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de marzo
diames=$(($(($RANDOM%$mes03))+$min03))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de abril
diames=$(($(($RANDOM%$mes04))+$min04))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de abril
diames=$(($(($RANDOM%$mes04))+$min04))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de mayo
diames=$(($(($RANDOM%$mes05))+$min05))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de mayo
diames=$(($(($RANDOM%$mes05))+$min05))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de junio
diames=$(($(($RANDOM%$mes06))+$min06))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de junio
diames=$(($(($RANDOM%$mes06))+$min06))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de julio
diames=$(($(($RANDOM%$mes07))+$min07))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de julio
diames=$(($(($RANDOM%$mes07))+$min07))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de agosto
diames=$(($(($RANDOM%$mes08))+$min08))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de agosto
diames=$(($(($RANDOM%$mes08))+$min08))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de septiembre
diames=$(($(($RANDOM%$mes09))+$min09))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de septiembre
diames=$(($(($RANDOM%$mes09))+$min09))
# Pega la informacion en el archivo de temperatura
echo Met$esta,18000$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de octubre
diames=$(($(($RANDOM%$mes10))+$min10))
# Pega la informacion en el archivo de temperatura
echo Met$esta,1800$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de octubre
diames=$(($(($RANDOM%$mes10))+$min10))
# Pega la informacion en el archivo de temperatura
echo Met$esta,1800$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de noviembre
diames=$(($(($RANDOM%$mes11))+$min11))
# Pega la informacion en el archivo de temperatura
echo Met$esta,1800$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de noviembre
diames=$(($(($RANDOM%$mes11))+$min11))
# Pega la informacion en el archivo de temperatura
echo Met$esta,1800$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de diciembre
diames=$(($(($RANDOM%$mes12))+$min12))
# Pega la informacion en el archivo de temperatura
echo Met$esta,1800$diames,TMED,$temp >> ../datos/temp1800.txt

# Genera un numero aleatorio hasta del 10000 al 10100
esta=$(($(($RANDOM%$rangest))+$estmin))
# Genera un numero aleatorio hasta del 15 al 30
temp=$(($(($RANDOM%$tmed))+$rmemin))
# Genera dias de diciembre
diames=$(($(($RANDOM%$mes12))+$min12))
# Pega la informacion en el archivo de temperatura
echo Met$esta,1800$diames,TMED,$temp >> ../datos/temp1800.txt

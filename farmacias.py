import csv
import sqlite3

FileName="Farmacias.csv"
File = open(FileName,"r")
reader = csv.reader(File)

ConnexionBD = sqlite3.connect('farmaciasDb.db')
query = ConnexionBD.cursor()

sql= """ CREATE TABLE IF NOT EXISTS farmaciaschile(
id_Local INTERGER NOT NULL,
local_nombre VARCHAR(200),
comuna_nombre VARCHAR(200),
local_direccion VARCHAR(200),
funcionamiento_hora_apertura VARCHAR(200),
funcionamiento_hora_cierre VARCHAR(200),
local_telefono  VARCHAR(200)

)
"""
if (query.execute(sql)):
	print'Tabla creada con exito'
else: print 'Error, Tabla no creada'

array=[]
for row in reader:
	array.append(row)

for row in array:
	query.execute("Insert into farmaciaschile values('%s','%s','%s','%s','%s','%s','%s')"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
query.close()
ConnexionBD.commit()
ConnexionBD.close()

import pymongo

#imagenes
logginFondo = "fondoLoggin.png" #imagen de fondo

myClient = pymongo.MongoClient('mongodb://localhost:27017/')

MONGO_BASED = 'digiconnect_db'
COLECCION_USUARIOS = "usuarios"

baseDatos = myClient[MONGO_BASED]
coleccion = baseDatos[COLECCION_USUARIOS]



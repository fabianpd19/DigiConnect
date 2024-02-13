from logicaDeNegocios import *

usuario1 = {"username": "usuario1", "password": "contraseña1"}
#coleccion.insert_one(usuario1)

usuario = {
    "username": "jcgonzales",
    "password": "contrasena",
    "nombres": "Juan Carlos",
    "apellidos": "Pérez González",
    "cedula": "1723456789",
    "correo_electronico": "juan.perez@example.com",
    "rol": "docente",
    "estado": "en proceso"
}

estudiante = {
    "username": "kaloor",
    "password": "contrasena",
    "nombres": "Kevin Alejando",
    "apellidos": "Loor Zambrano",
    "cedula": "1534512561",
    "correo_electronico": "kevin.loor@ejemplo.com",
    "rol": "estudiante",
    "estado": "estudiando"
}

admin = {
    "username": "fapalma1",
    "password": "contrasena",
    "nombres": "Fabián Alexander",
    "apellidos": "Palma Dueñas",
    "cedula": "2300284342",
    "correo_electronico": "fabian@eeeeee.edu.com",
    "rol": "admin",
    "estado": "admin"
}

#resultado = coleccion.insert_one(usuario)
#resultado = coleccion.insert_one(estudiante)
resultado = coleccion.insert_one(admin)

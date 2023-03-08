import tkinter as tk
from pymongo import MongoClient
from logicaDeNegocios import *
from tkinter import messagebox

# Configuración de MongoDB

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("CRUD MongoDB")

        # Creación de widgets
        self.label_nombre = tk.Label(self.master, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, padx=5, pady=5)
        self.entry_nombre = tk.Entry(self.master)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        self.label_apellido = tk.Label(self.master, text="Apellido:")
        self.label_apellido.grid(row=1, column=0, padx=5, pady=5)
        self.entry_apellido = tk.Entry(self.master)
        self.entry_apellido.grid(row=1, column=1, padx=5, pady=5)

        self.label_cedula = tk.Label(self.master, text="Cédula:")
        self.label_cedula.grid(row=2, column=0, padx=5, pady=5)
        self.entry_cedula = tk.Entry(self.master)
        self.entry_cedula.grid(row=2, column=1, padx=5, pady=5)

        self.label_correo = tk.Label(self.master, text="Correo:")
        self.label_correo.grid(row=3, column=0, padx=5, pady=5)
        self.entry_correo = tk.Entry(self.master)
        self.entry_correo.grid(row=3, column=1, padx=5, pady=5)

        self.label_rol = tk.Label(self.master, text="Rol:")
        self.label_rol.grid(row=4, column=0, padx=5, pady=5)
        self.entry_rol = tk.Entry(self.master)
        self.entry_rol.grid(row=4, column=1, padx=5, pady=5)

        self.label_estado = tk.Label(self.master, text="Estado:")
        self.label_estado.grid(row=5, column=0, padx=5, pady=5)
        self.entry_estado = tk.Entry(self.master)
        self.entry_estado.grid(row=5, column=1, padx=5, pady=5)

        self.btn_agregar = tk.Button(self.master, text="Agregar", command=self.agregar)
        self.btn_agregar.grid(row=6, column=0, padx=5, pady=5)

        self.btn_actualizar = tk.Button(self.master, text="Actualizar", command=self.actualizar)
        self.btn_actualizar.grid(row=6, column=1, padx=5, pady=5)

        self.btn_eliminar = tk.Button(self.master, text="Eliminar", command=self.eliminar)
        self.btn_eliminar.grid(row=6, column=2, padx=5, pady=5)

        self.btn_mostrar = tk.Button(self.master, text="Mostrar", command=self.mostrar)
        self.btn_mostrar.grid(row=7, column=0, padx=5, pady=5)

        self.lista_usuarios = tk.Listbox(self.master)
        self.lista_usuarios.grid(row=8, column=0, columnspan=3, padx=5, pady=5)

    def agregar(self):
        """
        Crea un usuario nuevo en la base de datos.
        """
        # Obtenemos los valores de los campos de entrada.
        nombre = self.entry_nombre.get()
        apellidos = self.entry_apellido.get()
        cedula = self.entry_cedula.get()
        correo = self.entry_correo.get()
        rol = self.entry_rol.get()
        estado = self.entry_estado.get()

        # Creamos el objeto usuario.
        usuario = {
            "nombre": nombre,
            "apellidos": apellidos,
            "cedula": cedula,
            "correo": correo,
            "rol": rol,
            "estado": estado
        }

        # Insertamos el usuario en la base de datos.
        coleccion.insert_one(usuario)

        # Mostramos un mensaje de éxito.
        messagebox.showinfo("Éxito", "Usuario creado correctamente.")

        # Limpiamos los campos de entrada.
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_cedula.delete(0, tk.END)
        self.entry_correo.delete(0, tk.END)


    def mostrar(self):
        """
        Lee un usuario de la base de datos y lo muestra en los campos de entrada.
        """
        # Obtenemos el valor del campo de entrada de la cédula.
        cedula = self.entry_cedula.get()

        # Buscamos el usuario en la base de datos.
        usuario = coleccion.find_one({"cedula": cedula})

        # Si el usuario no existe, mostramos un mensaje de error.
        if not usuario:
            messagebox.showerror("Error", "No se encontró ningún usuario con la cédula especificada.")
            return

        # Mostramos los datos del usuario en los campos de entrada.
        self.entry_nombre.delete(0, tk.END)
        self.entry_nombre.insert(0, usuario["nombre"])

        self.entry_apellido.delete(0, tk.END)
        self.entry_apellido.insert(0, usuario["apellidos"])

        self.entry_correo.delete(0, tk.END)
        self.entry_correo.insert(0, usuario["correo"])

        self.entry_rol.set(usuario["rol"])
        self.entry_estado.set(usuario["estado"])


    def actualizar(self):
        """
        Actualiza los datos de un usuario en la base de datos.
        """
        # Obtenemos los valores de los campos de entrada.
        nombre = self.entry_nombre.get()
        apellidos = self.entry_apellido.get()
        cedula = self.entry_cedula.get()
        correo = self.entry_correo.get()
        rol = self.entry_rol.get()
        estado = self.entry_estado.get()

        # Creamos el objeto usuario actualizado.
        usuario_actualizado = {
            "$set": {
                "nombre": nombre,
                "apellidos": apellidos,
                "correo": correo,
                "rol": rol,
                "estado": estado
            }
        }

        # Actualizamos el usuario en la base de datos.
        coleccion.update_one({"cedula": cedula}, usuario_actualizado)

        # Mostramos un mensaje de éxito.
        messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")


    def eliminar(self):
        usuario = self.entry_cedula.get()

        # Buscar el usuario en la base de datos
        resultado = coleccion.find_one({'cedula': usuario})

        if resultado:
            # Eliminar el usuario de la base de datos
            coleccion.delete_one({'cedula': usuario})
            messagebox.showinfo("Eliminar usuario", "Usuario eliminado correctamente.")
        else:
            messagebox.showerror("Eliminar usuario", "El usuario no existe en la base de datos.")


if __name__ == '__main__':
    root = tk.Tk()
    login_form = App(root)
    root.mainloop()
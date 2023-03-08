import tkinter as tk
import tkinter as tk
import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import hashlib
from logicaDeNegocios import *
from CRUD import *

class LoginForm:
    def __init__(self, master):
        self.master = master
        self.master.title('Inicio de Sesión')
        self.master.geometry("600x600")
        
        #Color de fondo de la ventana
        self.master.config(bg="white")
        #Tamaño de la ventana
        self.master.geometry("600x600")
        #No poder modificar el tamaño de la ventana
        self.master.resizable(width="False", height="False")
        
        #fondo del programa
        self.img = tkinter.PhotoImage(file = logginFondo)
        Label(self.master, image = self.img).pack()

        self.username_label = tk.Label(master, text='Usuario:')
        self.username_label.config(bg= "white", highlightthickness=0, highlightcolor="white", font=font.Font(family="Arial", size = "10"))
        self.username_label.place(x=160, y=272)
        self.username_entry = tk.Entry(master, font=font.Font(family="Arial", size = "10"),textvar="", width=32, relief="flat")
        self.username_entry.place(x=160, y=302)
        
        self.password_label = tk.Label(master, text='Contraseña:')
        self.password_label.config(bg= "white",highlightthickness=0, highlightcolor="white", font=font.Font(family="Arial", size = "10"))
        self.password_label.place(x=160, y=335)
        self.password_entry = tk.Entry(master, show = "*",font=font.Font(family="Arial", size = "10"),textvar="", width=32, relief="flat")
        self.password_entry.place(x=160, y=365)
        
        
        self.login_button = tk.Button(master, 
                                      text='Iniciar Sesión', 
                                      command=self.login, 
                                      fg= "white", 
                                      bg = "#112545", 
                                      height=1,
                                      relief="flat")
        
        self.login_button.place(x = 260,  y = 410)
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        #hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        user = coleccion.find_one({'username': username, 'password': password})
        #print(user)
        
        if user is not None:
            self.master.destroy()
            app = Application(user['rol'])
        else:
            # Mostrar mensaje de error
            tk.messagebox.showerror('Error', 'Usuario o contraseña incorrectos')

class Application:
    def __init__(self, role):
        self.master = tk.Tk()
        self.master.title('Habilidades Digitales')
        self.master.geometry("600x600")
        self.master.resizable(width="False", height="False")
        
        # Aquí se agregarían las funcionalidades de la aplicación dependiendo del rol del usuario
        # Por ejemplo:
        if role == 'estudiante':
            self.label = tk.Label(self.master, text='Bienvenido Estudiante')
            self.label.pack()
        elif role == 'docente':
            self.label = tk.Label(self.master, text='Bienvenido Docente')
            self.label.pack()
            
            #botón
            self.login_button = tk.Button(self.master, 
                                      text='Abrir CRUD - docente', 
                                      command=self.crudWindow, 
                                      fg= "white", 
                                      bg = "#112545", 
                                      height=1,
                                      relief="flat")
        
            self.login_button.place(x = 260,  y = 410)
            
        elif role == 'admin':
            self.label = tk.Label(self.master, text='Bienvenido Administrador')
            self.label.pack()

            #botón
            self.login_button = tk.Button(self.master, 
                                      text='Abrir CRUD - admin', 
                                      command=self.crudWindow, 
                                      fg= "white", 
                                      bg = "#112545", 
                                      height=1,
                                      relief="flat")
        
            self.login_button.place(x = 260,  y = 410)
    
        self.master.mainloop()
    
    def crudWindow(self):
            #self.master.withdraw()
            self.crud = tk.Toplevel()
            self.crud_window = App(self.crud)
        

if __name__ == '__main__':
    root = tk.Tk()
    login_form = LoginForm(root)
    root.mainloop()

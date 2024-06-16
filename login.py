import tkinter as tk
from tkinter import ttk,messagebox

class login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x130")
        self.title("Login")
        self.iconbitmap("logo.ico")
        self.resizable(False, False)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=3)

        self.crear_componentes()

    def crear_componentes(self):
        Label_Usuario = ttk.Label(self, text = "Usuario:")
        Label_Usuario.grid(row=0, column=0, sticky= tk.E, padx=5, pady=5)
        self.Entry_Usuario = ttk.Entry(self)
        self.Entry_Usuario.grid(row=0, column=1, sticky= tk.W, padx=5, pady=5)
        Label_Contraseña = ttk.Label(self, text = "Contraseña:")
        Label_Contraseña.grid(row=1, column=0, sticky= tk.E, padx=5, pady=5)
        self.Entry_Contraseña = ttk.Entry(self, show="*")
        self.Entry_Contraseña.grid(row=1, column=1, sticky= tk.W, padx=5, pady=5)
        Boton_Login = ttk.Button(self, text="Ingresar", command=self._login)
        Boton_Login.grid(row=2, column=1, sticky= tk.W, padx=5, pady=5)

    def _login(self):
        if self.Entry_Usuario.get() == "" or self.Entry_Contraseña.get() == "":
            messagebox.showerror("Error", "Debe llenar todos los campos")
        else:
            messagebox.showinfo("Bienvenido", "Bienvenido")

if __name__ == "__main__":
    app = login()
    app.mainloop()
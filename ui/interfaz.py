import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from contactos import gestor

class InterfazContactos:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Contactos")
        self.root.geometry("500x400")

        self.lista = tk.Listbox(root, width=60)
        self.lista.pack(pady=10)

        # Botones
        tk.Button(root, text="Agregar", command=self.agregar).pack()
        tk.Button(root, text="Eliminar", command=self.eliminar).pack()
        tk.Button(root, text="Buscar", command=self.buscar).pack()
        tk.Button(root, text="Actualizar", command=self.cargar_contactos).pack()

        self.cargar_contactos()

    def cargar_contactos(self):
        self.lista.delete(0, tk.END)
        contactos = gestor.cargar_contactos()
        for i, c in enumerate(contactos):
            self.lista.insert(tk.END, f"{i + 1}. {c['nombre']} - {c['correo']} - {c['telefono']}")

    def agregar(self):
        nombre = simpledialog.askstring("Nombre", "Ingrese el nombre:")
        correo = simpledialog.askstring("Correo", "Ingrese el correo:")
        telefono = simpledialog.askstring("Teléfono", "Ingrese el número:")
        if nombre and correo and telefono:
            gestor.agregar_contacto(nombre, correo, telefono)
            self.cargar_contactos()

    def eliminar(self):
        seleccion = self.lista.curselection()
        if seleccion:
            indice = seleccion[0]
            gestor.eliminar_contacto(indice)
            self.cargar_contactos()
        else:
            messagebox.showwarning("Eliminar", "Seleccione un contacto para eliminar.")

    def buscar(self):
        texto = simpledialog.askstring("Buscar", "Ingrese el nombre a buscar:")
        if texto:
            resultados = gestor.buscar_contactos(texto)
            self.lista.delete(0, tk.END)
            for i, c in enumerate(resultados):
                self.lista.insert(tk.END, f"{i + 1}. {c['nombre']} - {c['correo']} - {c['telefono']}")

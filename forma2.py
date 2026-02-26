import tkinter as tk
from tkinter import messagebox

class AplicacionNumeros:
    def __init__(self, master):
        """
        Constructor de la clase AplicacionNumeros
        :param master: ventana principal
        """
        self.master = master
        master.title("Sumadora de Números")
        master.geometry("300x200")
        
        # Lista para almacenar los números ingresados
        self.numeros = []
        
        # Configuración de la interfaz
        self.configurar_interfaz()
    
    def configurar_interfaz(self):
        """Configura los elementos de la interfaz gráfica"""
        # Frame principal
        self.frame = tk.Frame(self.master, padx=20, pady=20)
        self.frame.pack(expand=True)
        
        # Etiqueta de título
        self.titulo = tk.Label(
            self.frame, 
            text="Ingrese números y luego súmelos",
            font=("Arial", 12)
        )
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Botón para ingresar números
        self.boton_ingresar = tk.Button(
            self.frame,
            text="Ingresar Número",
            command=self.ingresar_numero,
            width=15,
            height=2
        )
        self.boton_ingresar.grid(row=1, column=0, padx=5, pady=10)
        
        # Botón para sumar números
        self.boton_sumar = tk.Button(
            self.frame,
            text="Sumar Números",
            command=self.sumar_numeros,
            width=15,
            height=2,
            state=tk.DISABLED  # Inicialmente deshabilitado
        )
        self.boton_sumar.grid(row=1, column=1, padx=5, pady=10)
        
        # Área para mostrar los números ingresados
        self.lista_numeros = tk.Listbox(
            self.frame,
            width=30,
            height=5
        )
        self.lista_numeros.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Etiqueta para mostrar el resultado
        self.resultado = tk.Label(
            self.frame,
            text="",
            font=("Arial", 10, "bold")
        )
        self.resultado.grid(row=3, column=0, columnspan=2)
    
    def ingresar_numero(self):
        """Método para ingresar un nuevo número"""
        # Ventana emergente para ingresar el número
        dialogo = tk.Toplevel()
        dialogo.title("Ingresar Número")
        dialogo.geometry("250x120")
        
        # Etiqueta y campo de entrada
        tk.Label(dialogo, text="Ingrese un número:").pack(pady=5)
        entrada_numero = tk.Entry(dialogo)
        entrada_numero.pack(pady=5)
        entrada_numero.focus()
        
        # Función interna para procesar el número ingresado
        def procesar_numero():
            try:
                numero = float(entrada_numero.get())
                self.numeros.append(numero)
                self.actualizar_lista()
                dialogo.destroy()
                
                # Habilitar el botón de sumar si hay números
                if len(self.numeros) > 0:
                    self.boton_sumar.config(state=tk.NORMAL)
            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese un número válido")
        
        # Botón para confirmar
        tk.Button(
            dialogo,
            text="Aceptar",
            command=procesar_numero
        ).pack(pady=5)
    
    def actualizar_lista(self):
        """Actualiza la lista visual con los números ingresados"""
        self.lista_numeros.delete(0, tk.END)
        for numero in self.numeros:
            self.lista_numeros.insert(tk.END, str(numero))
    
    def sumar_numeros(self):
        """Método para sumar todos los números ingresados"""
        if not self.numeros:
            messagebox.showwarning("Advertencia", "No hay números para sumar")
            return
        
        suma = sum(self.numeros)
        self.resultado.config(text=f"La suma total es: {suma}")
        
        # Opcional: limpiar la lista después de sumar
        # self.numeros = []
        # self.actualizar_lista()
        # self.boton_sumar.config(state=tk.DISABLED)

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionNumeros(root)
    root.mainloop()
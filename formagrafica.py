import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Sumar dos números")
ventana.geometry("400x300")

fuente = ("Arial",12)

#crear etiquetas y campos
etiqueta_num1 = tk.Label(ventana, text="Ingrese el primemr número", font=fuente)
etiqueta_num1.pack()

entrada_num1 = tk.Entry(ventana)
entrada_num1.pack()

etiqueta_num2 = tk.Label(ventana, text="Segundo número")
etiqueta_num2.pack()

entrada_num2 = tk.Entry(ventana)
entrada_num2.pack()

#crear botón suma
#boton_sumar = tk.Button(ventana, text="Sumar", command=lambda: resultado.config(text="Resultado: " + str(float(entrada_num1.get()) + float(entrada_num2.get())))

boton_sumar = tk.Button(ventana, text="Sumar", command=lambda: resultado.config(text="Resultado: " + str(float(entrada_num1.get()) + float(entrada_num2.get()))))
boton_sumar.pack(pady=10)
resultado = tk.Label(ventana,text="Resultado")
resultado.pack()

ventana.mainloop()
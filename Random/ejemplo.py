import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para crear la gráfica
def create_plot():
    # Datos
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    # Crear la figura y los ejes
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')

    # Títulos y etiquetas
    ax.set_title("Gráfica de Líneas Sencilla")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")

    # Mostrar la gráfica en la ventana de tkinter
    canvas = FigureCanvasTkAgg(fig, master=window)  
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Crear la ventana principal de tkinter
window = tk.Tk()
window.title("Interfaz Gráfica con Matplotlib")

# Crear un botón para mostrar la gráfica
btn_plot = ttk.Button(window, text="Mostrar Gráfica", command=create_plot)
btn_plot.pack(side=tk.TOP)

# Iniciar el bucle principal de la interfaz gráfica
window.mainloop()

# Librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Seaborn para visualizaciones más estilizadas
import seaborn as sns
import os
from analisis import DataAnalyzer
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText

data = pd.read_csv("adult.csv")
analizar = DataAnalyzer(data)
analizar.summary()
analizar.correlation_matrix()
analizar.categorical_analisis()


data = pd.read_csv("vehicles.csv")
analizar = DataAnalyzer(data)
analizar.summary()
analizar.correlation_matrix()
analizar.categorical_analisis()



# --- Interfaz gráfica ---
root = tk.Tk()
root.title("Análisis de Datos con Pandas")

btn_load = tk.Button(root, text="Cargar CSV")
btn_load.pack(pady=10)

text_area = ScrolledText(root, width=100, height=30)
text_area.pack()

btns_frame = tk.Frame(root)
btns_frame.pack(pady=10)

tk.Button(btns_frame, text="Resumen Básico").grid(row=0, column=0, padx=5)
tk.Button(btns_frame, text="Análisis Categórico").grid(row=0, column=1, padx=5)
tk.Button(btns_frame, text="Análisis Numérico").grid(row=0, column=2, padx=5)

root.mainloop()
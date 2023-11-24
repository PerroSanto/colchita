import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk
import io
import os
import sys
from analizador_lexico import analizador_lexico_log, analizador_lexico
from analizador_sintactico import analizador_sintactico, analizador_sintactico_log
from funciones import procesar, sew, turn

class Colchita:
    def __init__(self, root):
        self.root = root
        self.root.title("ColchitaPy")
        root.geometry("1000x845")
        root.resizable(0, 0)
        root.configure(background="#535466")

        self.images = []  # Lista para almacenar miniaturas de imágenes
        self.result_image = None
        self.labels = []

        # Establecer el título de la ventana
        label_retazos = tk.Label(root, text="Retazos", font=("System", 16))
        label_retazos.grid(row=0, column=0)
        label_retazos.config(bg="#535466")
        
        label_codigo = tk.Label(root, text="Codigo", font=("System", 16))
        label_codigo.grid(row=0, column=1, columnspan=5)
        label_codigo.config(bg="#535466")
        
        label_acciones = tk.Label(root, text="Acciones", font=("System", 16))
        label_acciones.grid(row=0, column=6)
        label_acciones.config(bg="#535466")
        
        label_logs = tk.Label(root, text="Logs", font=("System", 16))
        label_logs.grid(row=9, column=1,  columnspan=5)
        label_logs.config(bg="#535466")
        
        # Crear un canvas para mostrar miniaturas en la barra lateral
        self.thumbnail_canvas = tk.Canvas(root,  width=110, height=800, bg="#242527", scrollregion=(0, 0, 0, 10000))
        self.thumbnail_canvas.grid(row=1, column=0, rowspan=20, padx=5, pady=5)
        
        # Crear ventana para mostrar el código "colchita"
        self.code_window = tk.Text(root, font=("System", 14), fg="green",  width=80, height=30, bg="#000000")
        self.code_window.grid(row=1, column=1, rowspan=8, columnspan=3, padx=5, pady=5)
        
        # Crear ventana para mostrar el log
        self.logs_window = scrolledtext.ScrolledText(root, width=100, height=19, bg="#000000", fg="#C0C0C0")
        self.logs_window.grid(row=10, column=1, rowspan=8, columnspan=3, padx=5, pady=5)
        
        # Redirigir stdout
        self.output_redirector = OutputRedirector(self.logs_window)
        sys.stdout = self.output_redirector
        sys.stderr = self.output_redirector
        
        # Boton cargar retazos
        self.btn_retazo = tk.Button(root, text="Cargar Retazos", command=self.load_directory)
        self.btn_retazo.grid(row=1, column=6, rowspan=1, columnspan=1, padx=5, pady=5)
        self.btn_retazo.config(width=10, height=2)
        
        # Boton cargar codigo
        self.btn_codigo = tk.Button(root, text="Cargar Codigo", command=self.load_code_from_file)
        self.btn_codigo.grid(row=2, column=6, rowspan=1, columnspan=1, padx=5, pady=5)
        self.btn_codigo.config(width=10, height=2)
        
        # Boton guardar codigo
        self.btn_guardar = tk.Button(root, text="Guardar Codigo", command=self.save_code_from_file)
        self.btn_guardar.grid(row=3, column=6, rowspan=1, columnspan=1, padx=5, pady=5)
        self.btn_guardar.config(width=10, height=2)
        
        # Boton Lexico
        self.btn_compilar = tk.Button(root, text="Analisis Lexico", command=self.analisis_lexico)
        self.btn_compilar.grid(row=4, column=6, rowspan=1, columnspan=1, padx=5, pady=5)
        self.btn_compilar.config(width=10, height=2)
        
        # Boton Sintactico
        self.btn_compilar = tk.Button(root, text="Analisis Sintactico", command=self.analisis_sintactico)
        self.btn_compilar.grid(row=5, column=6, rowspan=1, columnspan=1, padx=5, pady=5)
        self.btn_compilar.config(width=10, height=2)
        
        # Boton Semantico
        #self.btn_compilar = tk.Button(root, text="Analisis Semantico", command=self.analisis_semantico)
        #self.btn_compilar.grid(row=6, column=6, rowspan=1, columnspan=1, padx=5, pady=5)
        #self.btn_compilar.config(width=10, height=2)
        
        # Boton compilar codigo
        self.btn_compilar = tk.Button(root, text="Compilar", command=self.compilar)
        self.btn_compilar.grid(row=6, column=6, rowspan=1, columnspan=1, padx=5, pady=5)
        self.btn_compilar.config(width=10, height=2)
        
        # Boton salir
        self.btn_Salir = tk.Button(root, text="Salir", command=exit)
        self.btn_Salir.grid(row=7, column=6, rowspan=1, columnspan=1, padx=5, pady=5)
        self.btn_Salir.config(width=10, height=2)

    def analisis_lexico(self):
        # Obtener el código de la ventana de código
        code = self.code_window.get("1.0", tk.END)
        # limpiar la consola
        self.logs_window.delete("1.0", tk.END)
        # Analizar el código
        analizador_lexico_log(code)
    
    def analisis_sintactico(self):
        # Obtener el código de la ventana de código
        code = self.code_window.get("1.0", tk.END)
        # limpiar la consola
        self.logs_window.delete("1.0", tk.END)
        # Analizar el código
        analizador_sintactico_log(code)
        
    #def analisis_semantico(self):
    #    # Obtener el código de la ventana de código
    #    code = self.code_window.get("1.0", tk.END)
    #    # Analizar el código
    #    print("Analisis Semantico")

    def compilar(self):
        # Obtener el código de la ventana de código
        code = str(self.code_window.get("1.0", tk.END))
        # limpiar la consola
        self.logs_window.delete("1.0", tk.END)
        
        # Realizar analisis lexico
        if analizador_lexico(code) and analizador_sintactico(code):
            # Analizar el código
            print("Compilando...")
            print("Codigo: " + code)
            procesar(code)

        
    def save_code_from_file(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with io.open(file_path, "w", encoding="utf-8") as file:
                code = self.code_window.get("1.0", tk.END)
                file.write(code)

    def load_code_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with io.open(file_path, "r", encoding="utf-8") as file:
                code = file.read()
                self.code_window.delete("1.0", tk.END)
                self.code_window.insert(tk.END, code)

    def load_directory(self, directory="./retazos"):
        #directory = filedialog.askdirectory()
        if directory:
            image_files = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.ppm'))]

            for image_file in image_files:
                file_path = os.path.join(directory, image_file)
                img = Image.open(file_path)
                img = img.resize((100, 100))
                img = ImageTk.PhotoImage(img)

                # Obtener el nombre del archivo sin extensión
                file_name = os.path.splitext(image_file)[0]

                label = tk.Label(self.root, text=file_name)
                label.image = img

                # Configurar el color del texto y el borde
                label.config(fg="white", bd=3, relief="solid")

                # Mostrar miniatura en el canvas de la barra lateral
                self.thumbnail_canvas.create_image(5, len(self.images) * 110 + 5, anchor="nw", image=img)
                self.thumbnail_canvas.create_window(60, len(self.images) * 110 + 55, window=label, anchor="center")

                self.images.append(img)
                self.labels.append(label)
                
                print("Retazo cargado: " + file_name)
                

class OutputRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END)
               
if __name__ == "__main__":
    root = tk.Tk()
    app = Colchita(root)
    root.mainloop()

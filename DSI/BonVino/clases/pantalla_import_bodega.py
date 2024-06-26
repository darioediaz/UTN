import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk

class PantallaImportBodega:
    def __init__(self, gestor):
        self.gestor = gestor
        self.ventana = tk.Tk()
        self.ventana.title("Importación de Bodegas")

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#f7f7f7")
        style.configure("TLabel", background="#f7f7f7", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12))
        style.configure("Header.TLabel", font=("Arial", 16, "bold"))

        self.frame_bodegas = ttk.Frame(self.ventana, padding=20)
        self.frame_bodegas.pack(fill=tk.BOTH, expand=True)

 
        self.label_titulo = ttk.Label(self.frame_bodegas, text="Bodegas con actualizaciones pendientes", style="Header.TLabel")
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.label_subtitulo = ttk.Label(self.frame_bodegas, text="Seleccione una bodega del siguiente listado")
        self.label_subtitulo.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        self.lista_bodegas_frame = ttk.Frame(self.frame_bodegas)
        self.lista_bodegas_frame.grid(row=2, column=0, columnspan=2, pady=(0, 20))

        self.lista_bodegas_scroll = ttk.Scrollbar(self.lista_bodegas_frame, orient=tk.VERTICAL)
        self.lista_bodegas = tk.Listbox(self.lista_bodegas_frame, width=40, height=10, font=("Arial", 12), yscrollcommand=self.lista_bodegas_scroll.set)
        self.lista_bodegas_scroll.config(command=self.lista_bodegas.yview)

        self.lista_bodegas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.lista_bodegas_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.boton_actualizar = ttk.Button(self.frame_bodegas, text="Actualizar", command=self.actualizar_bodega)
        self.boton_actualizar.grid(row=3, column=0, columnspan=2)
    
    # setters
    def set_gestor(self, gestor):
        self.gestor = gestor
        
    def set_ventana(self, ventana):
        self.ventana = ventana
        
    def set_frame_bodegas(self, frame_bodegas):
        self.frame_bodegas = frame_bodegas
        
    def set_label_titulo(self, label_titulo):
        self.label_titulo = label_titulo
        
    def set_label_subtitulo(self, label_subtitulo):
        self.label_subtitulo = label_subtitulo
    
    def set_lista_bodegas(self, lista_bodegas):
        self.lista_bodegas = lista_bodegas
        
    def set_lista_bodegas_scroll(self, lista_bodegas_scroll):
        self.lista_bodegas_scroll = lista_bodegas_scroll
        
    def set_lista_bodegas_frame(self, lista_bodegas_frame):
        self.lista_bodegas_frame = lista_bodegas_frame
        
    def set_boton_actualizar(self, boton_actualizar):
        self.boton_actualizar = boton_actualizar    
        
    # getters
    def get_gestor(self):
        return self.gestor
    
    def get_ventana(self):
        return self.ventana   
    
    def get_frame_bodegas(self, frame_bodegas):
        return self.frame_bodegas
        
    def get_label_titulo(self, label_titulo):
        return self.label_titulo
        
    def get_label_subtitulo(self, label_subtitulo):
        return self.label_subtitulo
    
    def get_lista_bodegas(self, lista_bodegas):
        return self.lista_bodegas
        
    def get_lista_bodegas_scroll(self, lista_bodegas_scroll):
        return self.lista_bodegas_scroll
        
    def get_lista_bodegas_frame(self, lista_bodegas_frame):
        return self.lista_bodegas_frame
        
    def get_boton_actualizar(self, boton_actualizar):
        return self.boton_actualizar
            
    # funcion del metodo op_importar_a_actualizacion_vinos_bodega
    def op_importar_a_actualizacion_vinos_bodega(self):
        self.habilitar_ventana()

    # funcion del metodo habilitar_ventana
    def habilitar_ventana(self):
        self.solicitar_seleccionar_bodega()
        
    # funcion del metodo actualizar_bodega
    def actualizar_bodega(self):
        # Obtener la bodega seleccionada
        seleccion = self.lista_bodegas.curselection()
        if not seleccion:
            messagebox.showinfo("Error", "Debe seleccionar una bodega.")
        else:
            bodega_seleccionada = seleccion[0]
            self.tomar_seleccion_bodega(bodega_seleccionada)
    
    def solicitar_seleccionar_bodega(self):
        # Obtener las bodegas a actualizar
        bodegas_a_actualizar = self.gestor.importar_actualizacion_vinos_bodega()
        
        # mensaje para la alternativa A1: <NO HAY BODEGAS CON ACTUALIZACIONES DISPONIBLES>
        if len(bodegas_a_actualizar) == 0:
            messagebox.showinfo("Error", "No hay bodegas con actualizaciones pendientes.")
            
        for bodega in bodegas_a_actualizar:
            self.lista_bodegas.insert(tk.END, f"►\t{bodega.nombre}")

        # Centrar la ventana en la pantalla
        window_width = 460
        window_height = 460
        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.ventana.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.ventana.mainloop()
            
    # funcion del metodo tomar_seleccion_bodega
    def tomar_seleccion_bodega(self, bodega):
        try:
            self.gestor.tomar_seleccion_bodega(bodega)
        except Exception as e:
            # mensaje para la alternativa A3: <EL SISTEMA EXTERNO DE BODEGAS NO RESPONDE>
            messagebox.showerror("Error", f"El sistema externo para la bodega seleccionada no responde.")

    # funcion del metodo mostrar_resumen_vinos_importados
    @staticmethod
    def mostrar_resumen_vinos_importados(bodega, vinos_actualizados, vinos_creados):
        # titulos de resumen
        titulo_vinos_actualizados = f"\n{'═' * 10}\tVinos ACTUALIZADOS para: {bodega.nombre}\t{'═' * 10}\n"
        titulo_vinos_creados = f"\n{'═' * 10}\tVinos CREADOS para: {bodega.nombre}\t{'═' * 10}\n"
        
        # ventana de resumen
        resumen_ventana = tk.Toplevel()
        resumen_ventana.title("Resumen de actualizaciones de bodegas")

        # Texto de desplazamiento
        scroll_text = scrolledtext.ScrolledText(resumen_ventana, width=80, height=20, font=("Arial", 12))
        scroll_text.pack(padx=10, pady=10)

        # texto del resumen
        resumen_actualizados = titulo_vinos_actualizados
        scroll_text.insert(tk.END, resumen_actualizados, "negrita")
        for idx, vino in enumerate(vinos_actualizados, start=1):
            scroll_text.insert(tk.END, f"{idx}. {vino}\n")

        resumen_creados = titulo_vinos_creados
        scroll_text.insert(tk.END, resumen_creados, "negrita")
        for idx, vino in enumerate(vinos_creados, start=1):
            scroll_text.insert(tk.END, f"{idx}. {vino}\n")
            
                # Cconfiguracion de etiquetas
        scroll_text.tag_configure("negrita", font=("Arial", 12, "bold"))
        
        resumen_ventana.mainloop()

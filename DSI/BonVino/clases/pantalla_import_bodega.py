'''Version por terminal'''
# class PantallaImportBodega():
#     def __init__(self, gestor):
#         self.gestor = gestor

#     # funcion para el metodo habilitar_ventana
#     def habilitar_ventana(self):
#         bodegas_a_actualizar = self.gestor.importar_actualizacion_vinos_bodega()
#         self.solicitar_seleccion_bodegas(bodegas_a_actualizar)

#     # funcion para el metodo solicitar_seleccion_bodegas
#     def solicitar_seleccion_bodegas(self, bodegas_a_actualizar):
#         i = 1
#         print("\nBodegas con actualizaciones pendientes:\n")
#         for bodega in bodegas_a_actualizar:
#             print(f"{i})-{bodega.nombre}")
#             i = i + 1
#         print("0) Salir\n")
        
#         # menu para seleccionar bodegas
#         while True:
#             seleccion = int(input("Seleccione el numero de la bodega que desea actualizar (0 para salir): "))
#             if seleccion == 0:
#                 print("Saliendo...\n")
#                 break
#             elif seleccion < 1 or seleccion > i - 1:
#                 print("Esa opcion no es valida. Intente nuevamente.\n")
#             else:
#                 self.tomar_seleccion_bodega(bodegas_a_actualizar[(seleccion) - 1])
        
#     # funcion para el metodo tomar_seleccion_bodegas()
#     def tomar_seleccion_bodega(self, bodega):
#         self.gestor.tomar_seleccion_bodega(bodega)

#     # funcion para el metodo mostrar_resumen_vinos_importados()
#     def mostrar_resumen_vinos_importados(bodega, vinos_actualizados, vinos_creados):
#         print(f"\nVinos ACTUALIZADOS para: {bodega.nombre}")
#         for vino in vinos_actualizados:
#             print(vino)
#         print(f"\nVinos CREADOS para: {bodega.nombre}")
#         for vino in vinos_creados:
#             print(vino)

'''Version por GUI'''
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

class PantallaImportBodega:
    def __init__(self, gestor):
        self.gestor = gestor
        self.ventana = tk.Tk()
        self.ventana.title("Importación de Bodegas")

        # Configuración del marco principal
        self.frame_bodegas = tk.Frame(self.ventana, padx=20, pady=20)
        self.frame_bodegas.pack()

        # Etiqueta de título
        self.label_bodegas = tk.Label(self.frame_bodegas, text="Bodegas con actualizaciones pendientes", font=("Arial", 14, "bold"))
        self.label_bodegas.grid(row=0, column=0, columnspan=2, pady=10)

        # Lista de bodegas
        self.lista_bodegas = tk.Listbox(self.frame_bodegas, width=30, height=10, font=("Arial", 12))
        self.lista_bodegas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botón de actualizar
        self.boton_actualizar = tk.Button(self.frame_bodegas, text="Actualizar", command=self.actualizar_bodega, font=("Arial", 12))
        self.boton_actualizar.grid(row=2, column=0, columnspan=2, pady=10)

    def habilitar_ventana(self):
        # Obtener las bodegas a actualizar
        bodegas_a_actualizar = self.gestor.importar_actualizacion_vinos_bodega()
        for bodega in bodegas_a_actualizar:
            self.lista_bodegas.insert(tk.END, bodega.nombre)

        # Centrar la ventana en la pantalla
        window_width = 420
        window_height = 420
        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.ventana.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.ventana.mainloop()

    def actualizar_bodega(self):
        # Obtener la bodega seleccionada
        seleccion = self.lista_bodegas.curselection()
        if not seleccion:
            messagebox.showinfo("Error", "Debe seleccionar una bodega.")
        else:
            bodega_seleccionada = seleccion[0]
            self.tomar_seleccion_bodega(bodega_seleccionada)

    def tomar_seleccion_bodega(self, bodega):
        self.gestor.tomar_seleccion_bodega(bodega)

    @staticmethod
    def mostrar_resumen_vinos_importados(bodega, vinos_actualizados, vinos_creados):
        # titulos para la ventana de resumen
        titulo_vinos_actualizados = f"Vinos ACTUALIZADOS para: {bodega.nombre}"
        titulo_vinos_creados = f"Vinos CREADOS para: {bodega.nombre}"
        
        # Crear el texto del resumen
        resumen = titulo_vinos_actualizados + "\n"
        for idx, vino in enumerate(vinos_actualizados, start=1):
            resumen += f"{idx}. {vino}\n"
            
        resumen += titulo_vinos_creados + "\n"
        for idx, vino in enumerate(vinos_creados, start=1):
            resumen += f"{idx}. {vino}\n"

        # Crear la ventana de resumen
        resumen_ventana = tk.Toplevel()
        resumen_ventana.title("Resumen de actualizaciones de bodegas")

        # Texto de desplazamiento
        scroll_text = scrolledtext.ScrolledText(resumen_ventana, width=80, height=20, font=("Arial", 12))
        scroll_text.insert(tk.END, resumen)
        scroll_text.pack(padx=10, pady=10)

        resumen_ventana.mainloop()



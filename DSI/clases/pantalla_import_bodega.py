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

        self.frame_bodegas = tk.Frame(self.ventana)
        self.frame_bodegas.pack()

        self.label_bodegas = tk.Label(self.frame_bodegas, text="Bodegas con actualizaciones pendientes:")
        self.label_bodegas.pack()

        self.lista_bodegas = tk.Listbox(self.frame_bodegas)
        self.lista_bodegas.pack()

        self.boton_actualizar = tk.Button(self.frame_bodegas, text="Actualizar", command=self.actualizar_bodega)
        self.boton_actualizar.pack()

    # funcion para el metodo habilitar_ventana
    def habilitar_ventana(self):
        bodegas_a_actualizar = self.gestor.importar_actualizacion_vinos_bodega()
        for bodega in bodegas_a_actualizar:
            self.lista_bodegas.insert(tk.END, bodega.nombre)
        
        # Tamaño del textarea de la lista de bodegas a actualizar 
        listbox_width = 30
        listbox_height = 10
        self.lista_bodegas.config(width=listbox_width, height=listbox_height)

        # Tamaño de la ventana
        window_width = 250
        window_height = 250
        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.ventana.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.ventana.mainloop()

    # funcion para el metodo solicitar_seleccion_bodegas
    def actualizar_bodega(self):
        seleccion = self.lista_bodegas.curselection()
        if not seleccion:
            messagebox.showinfo("Error", "Debe seleccionar una bodega.")
        else:
            bodega_seleccionada = seleccion[0]
            self.tomar_seleccion_bodega(bodega_seleccionada)


    # funcion para el metodo tomar_seleccion_bodegas
    def tomar_seleccion_bodega(self, bodega):
        self.gestor.tomar_seleccion_bodega(bodega)

    # funcion para el metodo mostrar_resumen_vinos_importados
    def mostrar_resumen_vinos_importados(bodega, vinos_actualizados, vinos_creados):
        resumen = f"\nVinos ACTUALIZADOS para: {bodega.nombre}\n"
        for vino in vinos_actualizados:
            resumen += str(vino) + "\n"
        resumen += f"\nVinos CREADOS para: {bodega.nombre}\n"
        for vino in vinos_creados:
            resumen += str(vino) + "\n"

        resumen_ventana = tk.Toplevel()
        resumen_ventana.title("Resumen")

        scroll_text = scrolledtext.ScrolledText(resumen_ventana, width=120, height=50)
        scroll_text.insert(tk.END, resumen)
        scroll_text.pack()

        resumen_ventana.mainloop()


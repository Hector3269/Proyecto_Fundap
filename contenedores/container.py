from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

from objetos.Imagen_resize import Imagen_resize
from objetos.alto import ALTO
from objetos.ancho import ANCHO
from objetos.colores import COLORES
from objetos.fill import FILL
from objetos.tamaño import GEOMETRIA
from objetos.tamaño_letra import Tamaño_letra
from objetos.tamaño_x import TAMAÑO_X
from objetos.tamaño_y import TAMAÑO_Y
from objetos.tipo_letra import Tipo_Letra
from views.inventario import INVENTARIO
from views.ventas import VENTAS
import objetos.titulos as TITULOS
import objetos.imagen as img


class Container(tk.Frame):
    def __init__(self, padre, controloador):
        super().__init__(padre)
        self.controlador = controloador
        self.pack()
        self.widgets()
        self.place(
            x=TAMAÑO_X.TAMAÑO_ZERO_X.value,
            y =TAMAÑO_Y.TAMAÑO_ZERO_Y.value,
            width = ANCHO.ANCHO_CONTAINER.value,
            height =ALTO.ALTO_CONTAINER.value
        )
        self.config(
            bg=COLORES.HEX.value
        )
    def show_frames(self,container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(
            bg=COLORES.HEX.value
        )
        frame.pack(
            fill=FILL.BOTH.value,
            expand=True
        )
        top_level.geometry(
            GEOMETRIA.GEOMETRIA_VENTANA2.value
        )
        top_level.resizable(
            False,
            False
        )

    def ventas(self):
        self.show_frames(VENTAS)

    def inventario(self):
        self.show_frames(INVENTARIO)

    def widgets(self):
        frame1 = tk.Frame(
            self,
            bg= COLORES.HEX.value
        )
        frame1.pack()
        frame1.place(
            x=TAMAÑO_X.TAMAÑO_ZERO_X.value,
            y=TAMAÑO_Y.TAMAÑO_ZERO_Y.value,
            width=ANCHO.ANCHO_CONTAINER.value,
            height=ALTO.ALTO_CONTAINER.value

        )
    # botones

        btn_ventas = Button(
            frame1,
            font=(
                Tipo_Letra.ARIAL,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            bg=COLORES.LAWNGREEN.value,
            fg=COLORES.WHITE.value,
            text=TITULOS.TITULO_VENTAS,
            command=self.ventas
        )
        btn_ventas.place(
            x= TAMAÑO_X.TAMAÑO_BOTON_X.value,
            y=TAMAÑO_Y.TAMAÑO_BOTON_Y.value,
            width = ANCHO.ANCHO_BOTON.value,
            height =ALTO.ALTO_BOTON.value
        )

        btn_inventario= Button(
            frame1,
            font=(
                Tipo_Letra.ARIAL,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            bg=COLORES.ORANGEGERED.value,
            fg=COLORES.WHITE.value,
            text=TITULOS.TITULO_INVENTARIO,
            command=self.inventario
        )
        btn_inventario.place(
            x=TAMAÑO_X.TAMAÑO_BOTON_X.value,
            y=TAMAÑO_Y.TAMAÑO_BOTON_2_Y.value,
            width=ANCHO.ANCHO_BOTON.value,
            height=ALTO.ALTO_BOTON.value
        )

        self.logo_imagen = Image.open(
            img.IMAGEN_CAJA_REGISTRADORA
        )
        self.logo_imagen = self.logo_imagen.resize((
            Imagen_resize.IMAGEN_TAMAÑO_RESIZE.value
        ))
        self.logo_imagen = ImageTk.PhotoImage(
            self.logo_imagen
        )
        self.logo_label = tk.Label(
            frame1,
            image=self.logo_imagen,
            bg=COLORES.HEX.value
        )
        self.logo_label.place(
            x=TAMAÑO_X.LOGO_X.value,
            y=TAMAÑO_Y.LOGO_Y.value,
        )

        copyright_label = tk.Label(
            frame1,
            text=TITULOS.COPYRIGHT_L,
            font=(
                Tipo_Letra.ARIAL,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            ),
            bg=COLORES.HEX.value,
            fg=COLORES.GRAY.value
        )
        copyright_label.place(
            x=TAMAÑO_X.COPYRIGHT_X.value,
            y=TAMAÑO_Y.COPYRIGHT_Y.value
        )



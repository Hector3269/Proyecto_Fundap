from tkinter import *
import tkinter as tk

from objetos.alto import ALTO
from objetos.ancho import ANCHO
from objetos.colores import COLORES
from objetos.tamaño import GEOMETRIA
from objetos.tamaño_letra import Tamaño_letra
from objetos.tamaño_x import TAMAÑO_X
from objetos.tamaño_y import TAMAÑO_Y
from objetos.tipo_letra import Tipo_Letra
from views.inventario import INVENTARIO
from views.ventas import VENTAS
import objetos.titulos as TITULOS


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
            fill="both",
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

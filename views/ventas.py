from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

from objetos.alto import ALTO
from objetos.ancho import ANCHO
from objetos.anchor import ANCHOR1
from objetos.colores import COLORES
from objetos.highlightthickness import HGCKNESS
from objetos.tamaño_letra import Tamaño_letra
from objetos.tamaño_x import TAMAÑO_X
from objetos.tamaño_y import TAMAÑO_Y
from objetos.tipo_letra import Tipo_Letra
import objetos.titulos as TITULOS


class VENTAS(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(
            self ,
            bg=COLORES.ORANGE.value,
            highlightbackground=COLORES.GRAY.value,
            highlightthickness=HGCKNESS.TAMAÑO_NESS.value
        )
        frame1.pack()
        frame1.place(
            x=TAMAÑO_X.TAMAÑO_ZERO_X.value,
            y=TAMAÑO_Y.TAMAÑO_ZERO_Y.value,
            width=ALTO.NORMAL_ALTO.value,
            height=ANCHO.NORMAL_ANCHO.value
        )

        titulo = tk.Label(
            frame1,
            text=TITULOS.TITULO_VENTAS,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.GRANDE_TAMAÑO.value
            ),
            bg=COLORES.LAWNGREEN.value,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        titulo.pack()
        titulo.place(
            x=TAMAÑO_X.TAMAÑO_ZERO_X.value,
            y=TAMAÑO_Y.TAMAÑO_ZERO_Y.value,
            width=ALTO.NORMAL_ALTO.value,
            height=ANCHO.NORMAL_ANCHO.value

        )

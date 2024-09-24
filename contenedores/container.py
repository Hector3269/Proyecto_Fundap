from tkinter import *
import tkinter as tk

from objetos.alto import ALTO
from objetos.ancho import ANCHO
from objetos.colores import COLORES
from objetos.tamaño_x import TAMAÑO_X
from objetos.tamaño_y import TAMAÑO_Y


class Container(tk.Frame):
    def __init__(self, padre, controloador):
        super().__init__(padre)
        self.controlador = controloador
        self.pack()
        self.place(
            x=TAMAÑO_X.TAMAÑO_ZERO_X.value,
            y =TAMAÑO_Y.TAMAÑO_ZERO_Y.value,
            width = ANCHO.ANCHO_CONTAINER.value,
            height =ALTO.ALTO_CONTAINER.value
        )
        self.config(
            bg=COLORES.LAWNGREEN.value
        )
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
import objetos.titulos as TITULOS
from objetos.tipo_letra import Tipo_Letra


class INVENTARIO(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.pack()
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(
            self,
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
            text= TITULOS.TITULO_INVENTARIO,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.GRANDE_TAMAÑO.value
            ),
            bg = COLORES.ORANGEGERED.value,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        titulo.pack()
        titulo.place(
            x=TAMAÑO_X.TAMAÑO_ZERO_X.value,
            y=TAMAÑO_Y.TAMAÑO_ZERO_Y.value,
            width=ALTO.NORMAL_ALTO.value,
            height=ANCHO.NORMAL_ANCHO.value
        )
        # Frame inferior
        frame2 = tk.Frame(
            self,
            bg=COLORES.LIME.value,
            highlightbackground=COLORES.GRAY.value,
            highlightthickness=HGCKNESS.TAMAÑO_NESS.value
        )
        frame2.place(
            x=TAMAÑO_X.TAMAÑO_ZERO_X.value,
            y=TAMAÑO_Y.TAMAÑO_FRAME_2_X.value,
            width=ANCHO.ANCHO_FRAME2.value,
            height=ALTO.ALTO_FRAME2.value
        )

        # LabelFrame Izquierdo
        labelframe = LabelFrame(
            frame2,
            text=TITULOS.PRODUCTOI_NVENTARIO,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.GRANDE_TAMAÑO.value
            ),
            bg=COLORES.RED.value,
            fg=COLORES.BLACK.value
        )
        labelframe.place(
            x=20,
            y=30,
            width=400,
            height=500
        )

        lblnombre = Label(
            labelframe,
            text=TITULOS.NOMBRE,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            bg=COLORES.RED.value,
            fg=COLORES.BLACK.value
        )
        lblnombre.place(
            x=10,
            y=20
        )
        self.nombre = ttk.Entry(
            labelframe,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
        )
        self.nombre.place(
            x=140,
            y=20,
            width=240,
            height=40
        )

        lblproveedor = Label(
            labelframe,
            text=TITULOS.PROVEEDOR,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            bg=COLORES.RED.value,
            fg=COLORES.BLACK.value
        )
        lblproveedor.place(
            x=10,
            y=80
        )
        self.proveedor = ttk.Entry(
            labelframe,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
        )
        self.proveedor.place(
            x=140,
            y=80,
            width=240,
            height=40
        )

        lblprecio = Label(
            labelframe,
            text=TITULOS.PRECIOI_NVENTARIO,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            bg=COLORES.RED.value,
            fg=COLORES.BLACK.value
        )
        lblprecio.place(
            x=10,
            y=140
        )
        self.precio = ttk.Entry(
            labelframe,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
        )
        self.precio.place(
            x=140,
            y=140,
            width=240,
            height=40
        )

        lblcosto = Label(
            labelframe,
            text=TITULOS.COSTO,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            bg=COLORES.RED.value,
            fg=COLORES.BLACK.value
        )
        lblcosto.place(
            x=10,
            y=200
        )
        self.costo = ttk.Entry(
            labelframe,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            )
        )
        self.costo.place(
            x=140,
            y=200,
            width=240,
            height=40
        )

        lblexistencias = Label(
            labelframe,
            text=TITULOS.EXISTENCIAS,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            bg=COLORES.RED.value,
            fg=COLORES.BLACK.value
        )
        lblexistencias.place(
            x=10,
            y=260
        )
        self.existencias = ttk.Entry(
            labelframe,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            )
        )
        self.existencias.place(
            x=140,
            y=260,
            width=240,
            height=40
        )

        boton_agregar = tk.Button(
            labelframe,
            text=TITULOS.BT_INGRESO_INVENTARIO,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            bg=COLORES.GOLD.value,
            fg=COLORES.BLACK.value
        )
        boton_agregar.place(
            x=80,
            y=340,
            width=ANCHO.ANCHO_BOTON_INVENTARIO.value,
            height=ALTO.ALTO_BOTON_INVENTARIO.value
        )

        boton_editar = tk.Button(
            labelframe,
            text=TITULOS.BT_EDITAR_INVENTARIO,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            bg=COLORES.GOLD.value,
            fg = COLORES.BLACK.value
        )
        boton_editar.place(
            x=80,
            y=400,
            width=ANCHO.ANCHO_BOTON_INVENTARIO.value,
            height=ALTO.ALTO_BOTON_INVENTARIO.value
        )

        # TreeView Tabla
        treFrame = Frame(
            frame2,
            bg=COLORES.WHITE.value
        )
        treFrame.place(
            x=440,
            y=50,
            width=620,
            height=400
        )

        # Barra de desplazamiento vertical
        scrol_y = ttk.Scrollbar(
            treFrame
        )
        scrol_y.pack(
            side=RIGHT,
            fill=Y
        )

        # Barra de desplazamiento horizontal
        scrol_x = ttk.Scrollbar(
            treFrame,
            orient=HORIZONTAL
        )
        scrol_x.pack(
            side=BOTTOM,
            fill=X
        )

        # Widget Treeview
        self.tre = ttk.Treeview(
            treFrame,
            yscrollcommand=scrol_y.set,
            xscrollcommand=scrol_x.set,
            height=40,
            columns=(
                "ID",
                "PRODUCTO",
                "PROVEEDOR",
                "PRECIO",
                "COSTO",
                "EXISTENCIAS"
            ),
            show="headings"
        )
        self.tre.pack(
            expand=True,
            fill=BOTH
        )

        scrol_y.config(
            command=self.tre.yview
        )
        scrol_x.config(
            command=self.tre.xview
        )

        self.tre.heading(
            "ID",
            text=TITULOS.ID_COLUM
        )
        self.tre.heading(
            "PRODUCTO",
            text=TITULOS.PRODUCTO_COLUM
        )
        self.tre.heading(
            "PROVEEDOR",
            text=TITULOS.PROVEEDOR_COLUM
        )
        self.tre.heading(
            "PRECIO",
            text=TITULOS.PRECIO_COLUM
        )
        self.tre.heading(
            "COSTO",
            text=TITULOS.COSTO_COLUM
        )
        self.tre.heading(
            "EXISTENCIAS",
            text=TITULOS.EXISTENCIAS_COLUM
        )

        self.tre.column(
            "ID",
            width=70,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        self.tre.column(
            "PRODUCTO",
            width=100,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        self.tre.column(
            "PROVEEDOR",
            width=100,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        self.tre.column(
            "PRECIO",
            width=100,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        self.tre.column(
            "COSTO",
            width=100,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        self.tre.column(
            "EXISTENCIAS",
            width=70,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )


        btn_actualizar = Button(
            frame2,
            text=TITULOS.BT_ACTUALIZAR_INVENTARIO,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            bg=COLORES.GOLD.value,
            fg=COLORES.BLACK.value
        )
        btn_actualizar.place(
            x=440,
            y=480,
            width=ANCHO.ANCHO_BOTON_INVENTARIO.value,
            height=ALTO.ALTO_BOTON_INVENTARIO.value
        )

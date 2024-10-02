from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

# objetos
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
            width=ANCHO.NORMAL_ANCHO.value,
            height=ALTO.NORMAL_ALTO.value
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
            width=ANCHO.NORMAL_ANCHO.value,
            height=ALTO.NORMAL_ALTO.value
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
            width=ANCHO.NORMAL_ANCHO.value,
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
            x=TAMAÑO_X.LABEL_FLAME_1_X.value,
            y=TAMAÑO_Y.LABEL_FLAME_INVENTARIO_Y.value,
            width=ANCHO.ANCHO_LABEL_FLAME.value,
            height=ALTO.ALTO_LABEL_FLAME.value
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
            x=TAMAÑO_X.LABEL_FLAME_COMUN_X.value,
            y=TAMAÑO_Y.LABEL_FLAME_INVENTARIO_Y.value
        )
        self.nombre = ttk.Entry(
            labelframe,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
        )
        self.nombre.place(
            x=TAMAÑO_X.LABEL_FLAME_COMUN_2_X.value,
            y=TAMAÑO_Y.LABEL_FLAME_INVENTARIO_Y.value,
            width=ANCHO.ANCHO_LABEL_FLAME_FORM.value,
            height=ALTO.ALTO_LABEL_FLAME_FORM.value
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
            x=TAMAÑO_X.LABEL_FLAME_COMUN_X.value,
            y=TAMAÑO_Y.LABEL_FLAME_INVENTARIO_2_Y.value,
        )
        self.proveedor = ttk.Entry(
            labelframe,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
        )
        self.proveedor.place(
            x=TAMAÑO_X.LABEL_FLAME_COMUN_2_X.value,
            y=TAMAÑO_Y.LABEL_FLAME_INVENTARIO_2_Y.value,
            width=ANCHO.ANCHO_LABEL_FLAME_FORM.value,
            height=ALTO.ALTO_LABEL_FLAME_FORM.value
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
            x=TAMAÑO_X.LABEL_FLAME_COMUN_X.value,
            y=TAMAÑO_Y.LABEL_FLAME_INVENTARIO_3_Y.value
        )
        self.precio = ttk.Entry(
            labelframe,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
        )
        self.precio.place(
            x=TAMAÑO_X.LABEL_FLAME_COMUN_2_X.value,
            y=TAMAÑO_Y.LABEL_FLAME_INVENTARIO_3_Y.value,
            width=ANCHO.ANCHO_LABEL_FLAME_FORM.value,
            height=ALTO.ALTO_LABEL_FLAME_FORM.value
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
            x=TAMAÑO_X.LABEL_FLAME_COMUN_X.value,
            y=TAMAÑO_Y.LABEL_FLAME_INVENTARIO_4_Y.value
        )
        self.costo = ttk.Entry(
            labelframe,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            )
        )
        self.costo.place(
            x=TAMAÑO_X.LABEL_FLAME_COMUN_2_X.value,
            y=TAMAÑO_Y.LABEL_FLAME_INVENTARIO_4_Y.value,
            width=ANCHO.ANCHO_LABEL_FLAME_FORM.value,
            height=ALTO.ALTO_LABEL_FLAME_FORM.value
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
            x=TAMAÑO_X.LABEL_FLAME_COMUN_X.value,
            y=TAMAÑO_Y.LABEL_FLAME_INVENTARIO_5_Y.value
        )
        self.existencias = ttk.Entry(
            labelframe,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            )
        )
        self.existencias.place(
            x=TAMAÑO_X.LABEL_FLAME_COMUN_2_X.value,
            y=TAMAÑO_Y.LABEL_FLAME_INVENTARIO_5_Y.value,
            width=ANCHO.ANCHO_LABEL_FLAME_FORM.value,
            height=ALTO.ALTO_LABEL_FLAME_FORM.value
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
            x=TAMAÑO_X.BTN_AGREGAR_X.value,
            y=TAMAÑO_Y.BTN_AGREGAR_Y.value,
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
            x=TAMAÑO_X.BTN_EDITAR_X.value,
            y=TAMAÑO_Y.BTN_EDITAR_Y.value,
            width=ANCHO.ANCHO_BOTON_INVENTARIO.value,
            height=ALTO.ALTO_BOTON_INVENTARIO.value
        )

        # TreeView Tabla
        treFrame = Frame(
            frame2,
            bg=COLORES.WHITE.value
        )
        treFrame.place(
            x=TAMAÑO_X.TREEVIEW_X.value,
            y=TAMAÑO_Y.TREEVIEW_Y.value,
            width=ANCHO.ANCHO_TEEVIEW.value,
            height=ALTO.ALTO_TEEVIEW.value
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
            height=ALTO.ALTO_TEEVIEW_WIDGET.value,
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
            width=ANCHO.ANCHO_TEEVIEW_NORMAL_WIDGET.value,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        self.tre.column(
            "PRODUCTO",
            width=ANCHO.ANCHO_TEEVIEW_MEDIANO_WIDGET.value,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        self.tre.column(
            "PROVEEDOR",
            width=ANCHO.ANCHO_TEEVIEW_MEDIANO_WIDGET.value,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        self.tre.column(
            "PRECIO",
            width=ANCHO.ANCHO_TEEVIEW_MEDIANO_WIDGET.value,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        self.tre.column(
            "COSTO",
            width=ANCHO.ANCHO_TEEVIEW_MEDIANO_WIDGET.value,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        self.tre.column(
            "EXISTENCIAS",
            width=ANCHO.ANCHO_TEEVIEW_MEDIANO_WIDGET.value,
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
            x=TAMAÑO_X.BTN_ACTUALIZAR_X.value,
            y=TAMAÑO_Y.BTN_ACTUALIZAR_Y.value,
            width=ANCHO.ANCHO_BOTON_INVENTARIO.value,
            height=ALTO.ALTO_BOTON_INVENTARIO.value
        )

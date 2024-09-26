from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

from objetos.alto import ALTO
from objetos.ancho import ANCHO
from objetos.anchor import ANCHOR1
from objetos.colores import COLORES
from objetos.estado import ESTADO
from objetos.highlightthickness import HGCKNESS
from objetos.tamaño_letra import Tamaño_letra
from objetos.tamaño_x import TAMAÑO_X
from objetos.tamaño_y import TAMAÑO_Y
from objetos.tipo_letra import Tipo_Letra
import objetos.titulos as TITULOS
from objetos.ubicacion import UBICACION


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
        frame2 = tk.Frame(
            self,
            bg= COLORES.RED.value,
            highlightbackground=COLORES.GRAY.value,
            highlightthickness=HGCKNESS.TAMAÑO_NESS.value
        )
        frame2.place(
            x=TAMAÑO_X.TAMAÑO_ZERO_X.value,
            y=TAMAÑO_Y.TAMAÑO_FRAME_2_X.value,
            width=ANCHO.ANCHO_FRAME2.value,
            height=ALTO.ALTO_FRAME2.value

        )

        lblframe = LabelFrame(
            frame2,
            text=TITULOS.FRAME_2_TITULO,
            bg=COLORES.LIME.value,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
        )
        lblframe.place(
            x=TAMAÑO_X.LABEL_FLAME_X.value,
            y=TAMAÑO_Y.LABEL_FLAME_Y.value,
            width=ANCHO.ANCHO_LABEL_FLAME.value,
            height=ALTO.ALTO_LABEL_FLAME.value
        )

        # Número de factura
        label_numero_factura = tk.Label(
            lblframe,
            text=TITULOS.NUMERO_FACTURA,
            bg=COLORES.LIME.value,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            ),
        )
        label_numero_factura.place(
            x=TAMAÑO_X.ENTRI_FACTURA_X.value,
            y=TAMAÑO_Y.ENTRI_FACTURA_Y.value
        )
        self.numero_factura = tk.StringVar()
        self.entry_numero_factura = ttk.Entry(
            lblframe,
            textvariable=self.numero_factura,
            state=ESTADO.LECTURA.value,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            ),
        )
        self.entry_numero_factura.place(
            x=TAMAÑO_X.ENTRI_FACTURA_COMPLEMENTO_X.value,
            y=TAMAÑO_Y.ENTRI_FACTURA_COMPLEMENTO_Y.value,
            width=80
        )
        # Entradas de texto para el nuevo artículo
        label_nombre = tk.Label(
            lblframe,
            text=TITULOS.PRODUCTO,
            bg=COLORES.LIME.value,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            ),
        )
        label_nombre.place(
            x=200,
            y=12
        )
        self.entry_nombre = ttk.Combobox(
            lblframe,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            ),
            state=ESTADO.LECTURA.value
        )
        self.entry_nombre.place(
            x=280,
            y=10,
            width=180
        )

        label_valor = tk.Label(
            lblframe,
            text=TITULOS.PRECIO,
            bg=COLORES.LIME.value,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            )
        )
        label_valor.place(
            x=470,
            y=12
        )
        self.entry_valor = ttk.Entry(
            lblframe,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            ),
            state=ESTADO.LECTURA.value
        )
        self.entry_valor.place(
            x=540,
            y=10,
            width=180
        )

        self.entry_nombre.bind("<<ComboboxSelected>>")

        # Label y Entry para la Cantidad
        label_cantidad = tk.Label(
            lblframe,
            text=TITULOS.CANTIDAD,
            bg=COLORES.LIME.value,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            ),
        )
        label_cantidad.place(
            x=730,
            y=12
        )
        self.entry_cantidad = ttk.Entry(
            lblframe,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.NORMAL_TAMAÑO_LETRA.value
            )
        )
        self.entry_cantidad.place(
            x=820,
            y=10,
            width=180
        )

        # Crear el contenedor del Treeview
        treFrame = tk.Frame(
            frame2,
            bg=COLORES.HEX.value
        )
        treFrame.place(
            x=150,
            y=120,
            width=800,
            height=200
        )

        # Barra de desplazamiento vertical
        scrol_y = ttk.Scrollbar(
            treFrame,
            orient=VERTICAL
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

        # TreeView para mostrar la lista de artículos
        self.tree = ttk.Treeview(
            treFrame,
            columns=(
                TITULOS.COLUM_PRODUCTO,
                TITULOS.COLUM_PRECIO,
                TITULOS.COLUM_CANTIDAD,
                TITULOS.COLUM_SUBTOTAL,
            ),
            show="headings",
            height=10,
            yscrollcommand=scrol_y.set,
            xscrollcommand=scrol_x.set
        )

        scrol_y.config(
            command=self.tree.yview
        )
        scrol_x.config(
            command=self.tree.xview
        )

        self.tree.heading(
            UBICACION.UBI1.value,
            text= TITULOS.COLUM_PRODUCTO
        )
        self.tree.heading(
            UBICACION.UBI2.value,
            text=TITULOS.COLUM_PRECIO
        )
        self.tree.heading(
             UBICACION.UBI3.value,
            text=TITULOS.COLUM_CANTIDAD
        )
        self.tree.heading(
             UBICACION.UBI4.value,
            text=TITULOS.COLUM_SUBTOTAL
        )
        self.tree.column(
            TITULOS.COLUM_PRODUCTO,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        self.tree.column(
            TITULOS.COLUM_PRECIO,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        self.tree.column(
            TITULOS.COLUM_CANTIDAD,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        self.tree.column(
            TITULOS.COLUM_SUBTOTAL,
            anchor=ANCHOR1.ANCHOR_CENTRO.value
        )
        self.tree.pack(
            expand=True,
            fill=BOTH
        )

        #LabelFrame inferior
        lblframe1 = LabelFrame(
            frame2,
            text=TITULOS.OPCIONES,
            bg=COLORES.LIME.value,
            font=(
                Tipo_Letra.NEGRITA,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRAS.value
            )
        )
        lblframe1.place(
            x=10,
            y=380,
            width=1060,
            height=100
        )

        # Botones
        boton_agregar = tk.Button(
            lblframe1,
            text=TITULOS.BT_AGREGAR,
            bg=COLORES.GOLD.value,
            fg=COLORES.WHITE.value,
            font=(
                Tipo_Letra.ARIAL,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            )
        )
        boton_agregar.place(
            x=50,
            y=10,
            width=240,
            height=50
        )

        boton_pagar = tk.Button(
            lblframe1,
            text=TITULOS.BT_PAGAR,
            bg=COLORES.GOLD.value,
            fg=COLORES.WHITE.value,
            font=(
                Tipo_Letra.ARIAL,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            )
        )
        boton_pagar.place(
            x=400,
            y=10,
            width=240,
            height=50
        )

        # Botón para abrir la ventana de facturas
        boton_ver_facturas = tk.Button(
            lblframe1,
            text=TITULOS.BT_VER_FACTURA,
            bg=COLORES.GOLD.value,
            fg=COLORES.WHITE.value,
            font=(
                Tipo_Letra.ARIAL,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            )
        )
        boton_ver_facturas.place(
            x=750,
            y=10,
            width=240,
            height=50
        )


        self.label_suma_total = tk.Label(
            frame2,
            text=TITULOS.LABEL_SUMA,
            bg= COLORES.RED.value,
            font=(
                Tipo_Letra.ARIAL,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            )
        )
        self.label_suma_total.place(
            x=360,
            y=335
        )

        copyright_label = tk.Label(
            frame2,
            text=TITULOS.COPYRIGHT_L,
            font=(
                Tipo_Letra.ARIAL,
                Tamaño_letra.MEDIANA_TAMAÑO_LETRA.value
            ),
            bg= COLORES.RED.value,

        )
        copyright_label.place(
            x=320,
            y=500
        )

from tkinter import Tk, Frame
from ttkthemes import ThemedStyle
from contenedores.container import Container
from objetos.colores import COLORES
from objetos.tamaño import GEOMETRIA
import objetos.titulos as TITULOS


class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(TITULOS.TIULOMANAGER)
        self.resizable(False, False)
        self.configure(bg=COLORES.HEX.value)
        self.geometry(GEOMETRIA.GEOMETRIA_VENTANA.value)

        self.container = Frame(self, bg=COLORES.HEX.value)
        self.container.pack(fill="both", expand=True)

        self.frames = {
            Container: None
        }

        self.load_frames()

        self.show_frame(Container)

        self.set_theme()

    def load_frames(self):
        for FrameClass in self.frames.keys():
            frame = FrameClass(self.container, self)
            self.frames[FrameClass] = frame

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

    def set_theme(self):
        style = ThemedStyle(self)
        style.set_theme("breeze")


def main():
    app = Manager()
    app.mainloop()


if __name__ == "__main__":
    main()
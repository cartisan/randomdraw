from Tkinter import Tk, Canvas

from path import Path

# API
#  General: http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
#  Canvas: http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/canvas.html


class MyCanvas(Canvas):
    def __init__(self, parent, width=600, height=600):
        Canvas.__init__(self, width=width, height=height, bg="#C0C0C0")
        self.width = width
        self.height = height
        self.parent = parent

        self.paths = []

        # TODO: implement aesthetic color choice
        for col in ["red", "green", "blue", "cyan", "yellow"]:
            self.paths.append(Path(width, height, color=col))

        self.after(10, self.step)
        self.pack()

    def step(self):
        for path in self.paths:
            path.step(self)

        self.after(100, self.step)


def main():
    root = Tk()
    root.title("Pretty Stuff")

    MyCanvas(root)

    root.mainloop()


if __name__ == '__main__':
    main()

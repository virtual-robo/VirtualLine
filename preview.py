import tkinter as tk
from map import ParseLine


class PreviewMap(tk.Canvas):
    def __init__(self: tk.Canvas, master: (tk.Tk, tk.Frame, tk.Canvas), n: int):
        tk.Canvas.__init__(self, master, width=400, height=400, bg="white")
        data = open("lvls/%s/line.dat" % (n), encoding="UTF-8")
        line = ParseLine(data.read())
        data.close()
        for rect in line["inversion"]:
            self.create_rectangle(*map(lambda n: n // 2.5, rect), fill="black")
        for vector in line["line"]:
            self.create_line(*map(lambda n: n // 2.5, vector[:4]), fill=vector[6], width=vector[5] // 2.5)
        # del self.create_rectangle, self.create_line, self.create_bitmap, self.create_arc, self.create_image, self.create_oval, self.create_polygon, self.create_text, self.create_window, self.delete


def getLvlName(n):
    f = open("lvls/%s/name.txt" % (n), encoding="UTF-8")
    t = f.read()
    f.close()
    return t


def getLvlDesc(n):
    f = open("lvls/%s/description.txt" % (n), encoding="UTF-8")
    t = f.read()
    f.close()
    return t

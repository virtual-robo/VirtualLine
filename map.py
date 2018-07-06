import tkinter as tk


class ParseLine:
    def __init__(self, t: str):
        self.d = {"line": list(), "inversion": list()}
        for s in t.split("\n"):
            if s:
                if s[0] == "|":
                    s = s.split(" ")
                    self.d["line"].append((*map(float, s[1:5]), "b" if len(s) < 6 or not s[5] else s[5],
                                           5 if len(s) < 7 or not s[6] else int(s[6]),
                                           "black" if len(s) < 8 or not s[7] else s[7]))
                elif s[0] == "^":
                    s = s.split()
                    self.d["inversion"].append(tuple(map(float, s[1:])))

    def __getitem__(self, item):
        return self.d[item]


class Map(tk.Canvas):
    def __init__(self, master, l):
        tk.Canvas.__init__(self, master, width=400, height=400, bg="white")
        f = open("lvls/%s/map.dat" % l)
        f.close()
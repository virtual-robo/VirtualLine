import tkinter as tk
import tkinter.ttk as ttk
from preview import PreviewMap, getLvlDesc, getLvlName


def openprelvl(n):
    global LvlImg, i
    i = n
    if i > 1:
        PrevBtn["state"] = "normal"
        PrevBtn["command"] = lambda: openprelvl(i - 1)
    else:
        PrevBtn["state"] = "disable"
    if i < 2:
        NextBtn["state"] = "normal"
        NextBtn["command"] = lambda: openprelvl(i + 1)
    else:
        NextBtn["state"] = "disable"
    LvlImg.destroy()
    LvlImg = PreviewMap(win, n)
    LvlImg.grid(column=1, row=1)
    LvlName["text"] = getLvlName(n)
    LvlDesc["text"] = getLvlDesc(n)


i = 1
win = tk.Tk()
win.title("VirtualLine")
LvlName = tk.Label(win)
LvlName.grid(column=0, row=0, columnspan=3)
PrevBtn = ttk.Button(win, text="Prev", state="disable")
PrevBtn.grid(column=0, row=1)
LvlImg = tk.Canvas(win)
LvlImg.grid(column=1, row=1)
NextBtn = ttk.Button(win, text="Next", command=lambda: openprelvl(2))
NextBtn.grid(column=2, row=1)
LvlDesc = tk.Label(win)
LvlDesc.grid(column=0, row=2, columnspan=3)
Achv = tk.Frame()
Achv.grid(column=0, columnspan=3, row=3)
openprelvl(1)
win.mainloop()

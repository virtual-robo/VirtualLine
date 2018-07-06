import tkinter as tk
import tkinter.ttk as ttk
from preview import PreviewMap, getLvlDesc, getLvlName
from map import Map
from help import version, check_update


class SelectLevel:
    maxi = 4

    def __init__(self):
        self.i = 1
        self.window = tk.Tk()
        self.window.config(menu=TopMenu(self.window))
        self.window.title("VirtualLine %s > Select level" % version)
        self.name = tk.Label(self.window)
        self.name.grid(column=0, row=0, columnspan=3)
        self.previous = ttk.Button(self.window, text="Prev", state="disable", command=self._previous)
        self.previous.grid(column=0, row=1)
        self.preview = tk.Canvas(self.window)
        self.preview.grid(column=1, row=1)
        self.next = ttk.Button(self.window, text="Next", command=self._next)
        self.next.grid(column=2, row=1)
        self.description = tk.Label(self.window)
        self.description.grid(column=0, row=2, columnspan=3)
        self.progress = tk.Frame()
        self.progress.grid(column=0, columnspan=3, row=3)
        self.select = ttk.Button(self.window, text="Select", command=self._select)
        self.select.grid(row=3, column=1, columnspan=2, sticky="e")
        self.open()
        self.window.mainloop()

    def _previous(self):
        self.i -= 1
        self.open()

    def _next(self):
        self.i += 1
        self.open()

    def open(self):
        self.previous["state"] = "normal" if self.i > 1 else "disable"
        self.next["state"] = "normal" if self.i < self.maxi else "disable"
        self.preview.destroy()
        self.preview = PreviewMap(self.window, self.i)
        self.preview.grid(column=1, row=1)
        self.name["text"] = getLvlName(self.i)
        self.description["text"] = getLvlDesc(self.i)

    def _select(self):
        self.window.destroy()
        Editor(self.i)


class Editor:
    def __init__(self, l):
        self.window = tk.Tk()
        self.window.config(menu=TopMenu(self.window, True))
        self.window.title("VirtualLine %s > %s" % (version, getLvlName(l)))
        self.map = Map(self.window, l)
        self.map.grid(column=1, row=0)

        self.editor = tk.Frame(self.window)
        self.editor.root = tk.Text(self.editor, wrap="none")
        self.editor.root.grid(column=0, row=0, sticky="nsew")
        self.editor.y = tk.Scrollbar(self.editor, orient="v", command=self.editor.root.yview)
        self.editor.y.grid(column=1, row=0, sticky="nsew")
        self.editor.root["yscrollcommand"] = self.editor.y.set
        self.editor.x = tk.Scrollbar(self.editor, orient="h", command=self.editor.root.xview)
        self.editor.x.grid(column=0, row=1, sticky="nsew")
        self.editor.root["xscrollcommand"] = self.editor.x.set
        self.editor.columnconfigure(0, weight=1)
        self.editor.rowconfigure(0, weight=1)
        self.editor.grid(column=0, row=0, rowspan=2, sticky="nsew")

        self.output = tk.Frame(self.window)
        self.output.root = tk.Text(self.output, state="disable", wrap="none", width=1)
        self.output.root.grid(column=0, row=0, sticky="nsew")
        self.output.y = tk.Scrollbar(self.output, orient="v", command=self.output.root.yview)
        self.output.y.grid(column=1, row=0, sticky="nsew")
        self.output.root["yscrollcommand"] = self.output.y.set
        self.output.x = tk.Scrollbar(self.output, orient="h", command=self.output.root.xview)
        self.output.x.grid(column=0, row=1, sticky="nsew")
        self.output.root["xscrollcommand"] = self.output.x.set
        self.output.columnconfigure(0, weight=1)
        self.output.rowconfigure(0, weight=1)
        self.output.grid(column=1, row=1, sticky="nsew")

        self.input = tk.Entry(self.window)
        self.input.grid(column=0, row=2, columnspan=4, sticky="nsew")
        self.state = tk.Label(self.window)
        self.state.grid(column=0, row=3, columnspan=4, sticky="nsew")

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)

        self.window.mainloop()


class TopMenu(tk.Menu):
    def __init__(self, master, editor=False):
        tk.Menu.__init__(self, master)
        if editor:
            self.file = tk.Menu(self, tearoff=False)
            self.file.add_command(label="Сохранить", state="disable")
            self.file.add_command(label="Открыть", state="disable")
            self.file.add_command(label="Выйти", state="disable")
            self.add_cascade(label="Файл", menu=self.file)
            self.edit = tk.Menu(self, tearoff=False)
            self.add_cascade(label="Правка", menu=self.edit)
        else:
            self.level = tk.Menu(self, tearoff=False)
            self.level.add_command(label="Добавить уровень", state="disable")
            self.level.add_command(label="Удалить уровень", state="disable")
            self.add_cascade(label="Уровень", menu=self.level)
        self.add_command(label="Проверить на наличие обновлений", command=check_update)

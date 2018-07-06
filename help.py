from webbrowser import open as web

version = "v0.0.2"


def check_update():
    web("https://virtual-robo.github.io/VirtualLine/update/?%s" % version)

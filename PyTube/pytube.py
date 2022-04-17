import PySimpleGUI as sg

sg.theme('dark')

layout = [
    []
]

window = sg.Window('Youtube Downloader', layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()

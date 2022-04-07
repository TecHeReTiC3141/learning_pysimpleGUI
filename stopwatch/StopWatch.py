import PySimpleGUI as sg

sg.theme('dark')

layout = [
    []
]

window = sg.Window('StopWatch', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()

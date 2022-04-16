import PySimpleGUI as sg

sg.theme('DarkAmber')
table_content = []
layout = [
    [sg.Table(headings=['Observation', 'Result'],
              values=table_content,
              expand_x=True,
              hide_vertical_scroll=True,
              key='-DATA-')]
]

window = sg.Window('Grapher', layout, size=(500, 500))

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()
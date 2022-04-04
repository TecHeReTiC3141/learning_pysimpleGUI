import PySimpleGUI as sg

layout = [
    [sg.Text('Hello, Insert value:'), sg.Input()],
    [sg.Button('Convert!'), sg.Spin(['item1', 'item2'])],
    [sg.Text('Result: ')],
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break




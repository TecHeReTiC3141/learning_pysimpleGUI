import PySimpleGUI as sg

layout = [
    [sg.Text('Hello, Insert value:'), sg.Input()],
    [sg.Button('Convert!')],
    [sg.Text('Result: ')]
]

sg.Window('Converter', layout).read()



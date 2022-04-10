import PySimpleGUI as sg

sg.theme('dark')

layout = [
    [sg.Menu([
        ['File', ['Open', 'Save', '---', 'Exit']],
        ['Edit and tools', ['Stats', 'LowerCase', 'UpperCase']],
        ['Insert', ['Time']]
    ], key='-MENU-')],
    [sg.Text('Untitled', key='-FILENAME-')],
    [sg.Multiline(expand_x=True, expand_y=True, pad=((5, 5), (5, 15)), key='-TEXT-')]

]

window = sg.Window('TecEditor', layout, size=(400, 600))

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()
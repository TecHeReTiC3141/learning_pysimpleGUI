import PySimpleGUI as sg
from string import digits, ascii_letters

sg.theme('dark')

def stats_window(text: str) -> sg.Window:
    symbl = len([i for i in text if digits + ascii_letters])
    layout = [
        [sg.Text(f'Text stats: {len(text.split())} words, {symbl} charachers')]
    ]
    return sg.Window('Stats', layout)

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

    elif event == 'Stats':
        new_window = stats_window(window['-TEXT-'].get())
        new_window.read()



window.close()
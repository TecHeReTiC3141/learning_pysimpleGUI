import PySimpleGUI as sg
from string import digits, ascii_letters
import datetime
from pathlib import Path

sg.theme('dark')

themes = ['menu', ['DarkAmber', 'dark', 'graygraygray', 'random']]
inserts = ['Insert', ['Time']]


def create_main_window(theme: str = 'DarkAmber', content: str = '', filename: str='Untitled') -> sg.Window:
    sg.theme(theme)
    layout = [
        [sg.Menu([
            ['File', ['Open', 'Save', '---', 'Exit']],
            ['Edit and tools', [themes, 'Stats', 'LowerCase', 'UpperCase']],
            inserts
        ], key='-MENU-')],
        [sg.Text(filename, key='-FILENAME-')],
        [sg.Multiline(default_text=content, expand_x=True, expand_y=True,
                      pad=((5, 5), (5, 15)), key='-TEXT-', no_scrollbar=True)]
    ]

    return sg.Window('TecEditor', layout, size=(400, 600))


def stats_window(text: str):
    symbl = len([i for i in text if i in digits + ascii_letters])
    sg.popup(f'Text stats: {len(text.split())} words;\n {symbl} characters', title='Stats')


window = create_main_window()

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    elif event == 'Stats':
        stats_window(values['-TEXT-'])

    elif event == 'Open':
        path = sg.popup_get_file('Select file to open:', no_window=True)
        with open(path) as f:
            window['-TEXT-'].update(f.read())
            name = path[path.rindex('/') + 1:]
            window['-FILENAME-'].update(name)

    elif event == 'Save':
        file = Path(sg.popup_get_file('Select file to open:',
                                      no_window=True, save_as=True) + '.txt')
        file.write_text(window['-TEXT-'].get())
        window['-FILENAME-'].update(file.name)

    elif event in themes[1]:
        window = create_main_window(event, values['-TEXT-'])

    elif event in inserts[1]:
        if event == 'Time':
            text = values['-TEXT-']

            window['-TEXT-'].update(text + ' ' +
                                    datetime.datetime.today().strftime('%M:%H %d.%m.%y'))

window.close()

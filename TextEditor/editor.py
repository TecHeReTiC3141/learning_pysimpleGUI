import PySimpleGUI as sg
from string import digits, ascii_letters

sg.theme('dark')

themes = ['menu', ['DarkAmber', 'dark', 'graygraygray', 'random']]


def create_main_window(theme: str = 'DarkAmber', content: str = '') -> sg.Window:
    sg.theme(theme)
    layout = [
        [sg.Menu([
            ['File', ['Open', 'Save', '---', 'Exit']],
            ['Edit and tools', [themes, 'Stats', 'LowerCase', 'UpperCase']],
            ['Insert', ['Time']]
        ], key='-MENU-')],
        [sg.Text('Untitled', key='-FILENAME-')],
        [sg.Multiline(default_text=content, expand_x=True, expand_y=True,
                      pad=((5, 5), (5, 15)), key='-TEXT-', no_scrollbar=True)]
    ]

    return sg.Window('TecEditor', layout, size=(400, 600))


def stats_window(text: str):
    symbl = len([i for i in text if i in digits + ascii_letters])
    sg.popup(f'Text stats: {len(text.split())} words, {symbl} characters', title='Stats')


window = create_main_window()

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    elif event == 'Stats':
        stats_window(values['-TEXT-'])

    elif event in themes[1]:
        window = create_main_window(event, values['-TEXT-'])

window.close()

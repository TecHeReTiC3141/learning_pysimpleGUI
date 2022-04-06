import PySimpleGUI as sg


def create_themed_window(theme: str):
    sg.theme(theme)
    sg.set_options(font='Calibri 15', )

    def_button_size = (4, 2)
    layout = [
        [sg.Push(), sg.Text('Screen', key='-Screen-', border_width=2, font='Franklin 25', pad=(5, 25), right_click_menu=themes)],
        [sg.Button('Enter', key='-ENTER-', size=def_button_size, expand_x=True),
         sg.Button('Clear', key='-CLEAR-', size=def_button_size, expand_x=True)],
        [sg.Button('7', key='-7-', size=def_button_size), sg.Button('8', key='-8-', size=def_button_size),
         sg.Button('9', key='-9-', size=def_button_size),
         sg.Button('/', key='-DIV-', size=def_button_size)],
        [sg.Button('4', key='-4-', size=def_button_size), sg.Button('5', key='-5-', size=def_button_size),
         sg.Button('6', key='-6-', size=def_button_size),
         sg.Button('*', key='-MULTY-', size=def_button_size)],
        [sg.Button('1', key='-1-', size=def_button_size), sg.Button('2', key='-2-', size=def_button_size),
         sg.Button('3', key='-3-', size=def_button_size),
         sg.Button('-', key='-MINUS-', size=def_button_size)],
        [sg.Button('0', key='-0-', size=def_button_size, expand_x=True),
         sg.Button('.', key='-PERIOD-', size=def_button_size), sg.Button('+', key='-PLUS-', size=def_button_size)]
    ]
    return sg.Window('Calculator', layout)

themes = ['menu', ['DarkAmber', 'dark', 'graygraygray', 'random']]
window = create_themed_window('dark')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        window.close()
        break

    elif event in themes[1]:
        window = create_themed_window(event)

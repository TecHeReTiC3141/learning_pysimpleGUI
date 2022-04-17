import PySimpleGUI as sg
from string import digits


def create_themed_window(theme: str):
    sg.theme(theme)
    sg.set_options(font='Calibri 15', )

    def_button_size = (4, 2)
    layout = [
        [sg.Push(),
         sg.Text('...', key='-SCREEN-', border_width=2, font='Franklin 25', pad=(5, 25),
                 right_click_menu=themes)],
        [sg.Text('Answer', key='-ANS-')],
        [sg.Button('Enter', key='-ENTER-', size=def_button_size, expand_x=True),
         sg.Button('Clear', key='-CLEAR-', size=def_button_size, expand_x=True)],
        [sg.Button('7', size=def_button_size), sg.Button('8', size=def_button_size),
         sg.Button('9', size=def_button_size),
         sg.Button('/', size=def_button_size)],
        [sg.Button('4', size=def_button_size), sg.Button('5', size=def_button_size),
         sg.Button('6', size=def_button_size),
         sg.Button('*', size=def_button_size)],
        [sg.Button('1', size=def_button_size), sg.Button('2', size=def_button_size),
         sg.Button('3', size=def_button_size),
         sg.Button('-', size=def_button_size)],
        [sg.Button('0', size=def_button_size, expand_x=True),
         sg.Button('.', size=def_button_size), sg.Button('+', size=def_button_size)]
    ]
    return sg.Window('Calculator', layout)


def calc(f: float, s: float, op: str) -> float:
    return round(eval(f'f {op} s'), 2)


themes = ['menu', ['DarkAmber', 'dark', 'graygraygray', 'random']]
window = create_themed_window('dark')
cur_dig = []
opers = []

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        window.close()
        break

    elif event in themes[1]:
        window = create_themed_window(event)

    elif event in digits + '.':
        cur_dig.append(event)
        window['-SCREEN-'].update(''.join(cur_dig))

    elif event in '+-/*':
        if cur_dig:
            opers.append(''.join(cur_dig))
        if len(opers) == 3:
            try:
                f, op, s = float(opers[0]), opers[1], float(opers[2])

                opers = [str(calc(f, s, op))]
            except Exception as e:
                window['-ANS-'].update('Invalid input')
                opers.pop()

        opers.append(event)
        cur_dig = []
        print(opers)
        window['-SCREEN-'].update(f'{opers[0] + opers[1]}')

    elif event == '-CLEAR-':
        window['-SCREEN-'].update('...')
        cur_dig = []
        opers = []

    elif event == '-ENTER-':
        if cur_dig:
            opers.append(''.join(cur_dig))
            if len(opers) == 3:
                try:
                    f, op, s = float(opers[0]), opers[1], float(opers[2])

                    opers = [str(calc(f, s, op))]
                except ValueError as e:
                    window['-ANS-'].update('Invalid input')

            cur_dig = []
            print(opers)
            window['-SCREEN-'].update(f'{opers[0]}')

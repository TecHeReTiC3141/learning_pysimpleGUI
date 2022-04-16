import PySimpleGUI as sg

sg.theme('DarkAmber')
sg.set_options(font='Ubuntu 15')

table_content = []
frozen = False
layout = [
    [sg.Text('Insert formula in terms of x:', font='Ubuntu 20 underline')],
    [sg.Input(expand_x=True, key='-FUNCTION-', default_text='Smth like x ** 2 + 1 - 3 * x', ),
     sg.Button('Freeze formula')],
    [sg.Table(headings=['Index', 'Observation', 'Result'],
              values=table_content,
              expand_x=True,
              hide_vertical_scroll=True,
              key='-DATA-', )],
    [sg.Text('Insert value:', font='Ubuntu 20 underline')],
    [sg.Input(key='-INPUT-', expand_x=True), sg.Button('Submit')],
    [sg.Button('Reset')]
]

window = sg.Window('Grapher', layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == 'Submit':
        if not frozen:
            error_window = sg.Window('Error', layout=[[sg.Text('Please freeze formula first')]])
            error_window.read()

        elif values['-INPUT-'].isdigit():
            obs = int(values['-INPUT-'])
            table_content.append((len(table_content) + 1, obs,
                                  eval(values['-FUNCTION-'].replace('x', str(obs)))))
            window['-DATA-'].update(values=table_content)

        else:
            error_window = sg.Window('Error', layout=[[sg.Text('Please insert integer and right formula')]])
            error_window.read()

    elif event == 'Freeze formula':
        frozen = True
        window['-FUNCTION-'].update(disabled=True)

    elif event == 'Reset':
        frozen = False
        window['-FUNCTION-'].update(disabled=False, value='Smth like x ** 2 + 1 - 3 * x')
        window['-INPUT-'].update(value='')
        table_content = []
        window['-DATA-'].update(values=table_content)

window.close()
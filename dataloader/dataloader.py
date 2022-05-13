import PySimpleGUI as sg
import pandas as pd

data = [[]]
sg.theme('DarkAmber')
sg.set_options(font='Ubuntu 15')

table = sg.Table(values=data, key='-DATA-', expand_x=True, auto_size_columns=True)

data_tab = sg.Tab('Data',
                  layout=[

                      [sg.Text('Write query to data:')],
                      [sg.Input(key='-MAKEQUERY-'), sg.Button('Query')]
                  ])

load_tab = sg.Tab('Load', layout=[
    [sg.Button('Load data')]
])

layout = [
    [sg.Text('DataLoader', font='Ubuntu 25 italic')],
    [sg.TabGroup([[data_tab, load_tab]])],
    [table],
]

window = sg.Window('DataLoader', layout=layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == 'Load data':
        try:
            filepath = sg.popup_get_file('', no_window=True, )
            data = pd.read_csv(filepath)
            print(data)
            window['-DATA-'].update(values=data.values.tolist(), )
            print(window['-DATA-'].Values[0], len(window['-DATA-'].Values))
        except Exception as e:
            sg.popup(str(e))

window.close()
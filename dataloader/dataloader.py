import PySimpleGUI as sg
import pandas as pd

data, headings = pd.DataFrame(), []
sg.theme('DarkAmber')
sg.set_options(font='Ubuntu 15')
formats = ['format', ['*.csv', '*.xlsx']]

def create_window(data: pd.DataFrame) -> sg.Window:

    table = sg.Table(values=data.values.tolist(), headings=data.columns.values.tolist(), key='-DATA-', expand_x=True, auto_size_columns=True)

    data_tab = sg.Tab('Data',
                      layout=[

                          [sg.Text('Write query to data:')],
                          [sg.Input(key='-MAKEQUERY-', expand_x=True), sg.Button('Query')]
                      ], key='-DATATAB-', expand_x=True)

    load_tab = sg.Tab('Load', layout=[
        [sg.Button('Load data', right_click_menu=formats)]
    ], expand_x=True)

    layout = [
        [sg.Text('DataLoader', font='Ubuntu 25 italic')],
        [sg.TabGroup([[data_tab, load_tab]])],
        [table],
    ]


    window = sg.Window('DataLoader', layout=layout)
    return window

window = create_window(data)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == 'Load data':
        try:
            filepath = sg.popup_get_file('', no_window=True, )
            data = pd.read_csv(filepath)
            window.close()

            window = create_window(data)
            print(window)
            print(headings, data.columns.values)
            print(window['-DATA-'].Values[0], len(window['-DATA-'].Values))
        except Exception as e:
            print(e)
            sg.popup(str(e))

window.close()
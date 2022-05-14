import PySimpleGUI as sg
import pandas as pd

data, queried = pd.DataFrame(), pd.DataFrame()
query = False
sg.theme('DarkAmber')
sg.set_options(font='Ubuntu 15')
from_formats = ['format', ['*.csv', '*.xlsx']]
to_formats = ['formats', ['to .csv', 'to .xlsx']]
cur_format = '*.csv'


def create_window(data: pd.DataFrame) -> sg.Window:
    table = sg.Table(values=data.values.tolist(),
                     headings=data.columns.values.tolist(), key='-DATA-', expand_x=True, auto_size_columns=True)

    data_tab = sg.Tab('Data',
                      layout=[
                          [sg.Text('Write query to data:')],
                          [sg.Input(key='-MAKEQUERY-', expand_x=True), sg.Button('Query'), sg.Button('Reset')]
                      ], key='-DATATAB-', expand_x=True)

    load_tab = sg.Tab('Load', layout=[
        [sg.Button('Load data', right_click_menu=from_formats), sg.Text(f'Current format: {cur_format}', key='-CURFORM-')],
        [sg.Button('Save data', right_click_menu=to_formats), sg.Text(f'Current format: {cur_format}', key='-CURFORM-')]
    ], expand_x=True)

    layout = [
        [sg.Text('DataLoader', font='Ubuntu 25 italic')],
        [sg.TabGroup([[data_tab, load_tab]])],

        [sg.HorizontalSeparator()],
        [sg.Text(f'Data {data.shape[0]} rows x {data.shape[1]} columns')],
        [table],
    ]

    window = sg.Window('DataLoader', layout=layout, element_justification='center', finalize=True)
    return window


window = create_window(data)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event in to_formats[1]:
        cur_format = event
        window['-CURFORM-'].update(f'Current format: {cur_format}')


    elif event == 'Load data':
        try:
            filepath = sg.popup_get_file('', no_window=True, )
            data = pd.read_csv(filepath)
            window.close()

            window = create_window(data)
            print(window)
            print(data.columns.values)
            print(window['-DATA-'].Values[0], len(window['-DATA-'].Values))
        except Exception as e:
            print(e)
            sg.popup(str(e))


    elif event == 'Query':
        try:
            if len(data):
                query = values['-MAKEQUERY-']
                queried = data.query(query)

                window.close()
                window = create_window(queried)
                window['-MAKEQUERY-'].update(query)
            else:
                sg.popup('Please load some some first')
        except Exception as e:
            print(e)
            sg.popup(str(e))


    elif event == 'Reset':
        window.close()
        window = create_window(data)

window.close()

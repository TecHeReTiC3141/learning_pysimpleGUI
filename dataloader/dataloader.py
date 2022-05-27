import PySimpleGUI as sg
import pandas as pd
import numpy as np

data, queried = pd.DataFrame(), pd.DataFrame()
pd.set_option("display.precision", 3)

is_query = False
sg.theme('DarkAmber')
sg.set_options(font='Ubuntu 15')
from_formats = ['format', ['*.csv', '*.xlsx']]
to_formats = ['formats', ['to .csv', 'to .xlsx']]
cur_format = '*.csv'

# TODO create tab with data categorical stats (pandas.describe)
# TODO implement saving of data and queries
# TODO learn more about getting and changing certain rows
def create_window(data: pd.DataFrame) -> sg.Window:
    table = sg.Table(values=np.hstack((np.array(range(1, data.shape[0] + 1)).reshape((data.shape[0], 1)), data.values)).tolist(),
                     headings=['Id'] + data.columns.values.tolist(), max_col_width=35,
                     key='-DATA-', expand_x=True, auto_size_columns=True, enable_events=True)

    data_tab = sg.Tab('Data',
                      layout=[
                          [sg.Text('Write query to data:')],
                          [sg.Input(key='-MAKEQUERY-', expand_x=True), sg.Button('Query'), sg.Button('Reset')]
                      ], key='-DATATAB-', expand_x=True)

    load_tab = sg.Tab('Load', layout=[
        [sg.Button('Load data', right_click_menu=from_formats), sg.Text(f'Current format: {cur_format}', key='-CURFORM-')],
        [sg.Button('Save data', right_click_menu=to_formats), sg.Text(f'Current format: {cur_format}', key='-CURFORM-')]
    ], expand_x=True)

    if data.shape[1] > 0:
        numer_descr = data.describe().round(3).T
        print(numer_descr)

        print(numer_descr.index.to_numpy().reshape(numer_descr.shape[0], 1), numer_descr.values)

        num_stats_tab = sg.Tab('Numeric Stats',
                           layout=[
                               [sg.Text('Numeric features description')],
                               [sg.HorizontalSeparator()],
                               [sg.Table(values=np.hstack([numer_descr.index.to_numpy().reshape(numer_descr.shape[0], 1),
                                                           numer_descr.values]).tolist(),
                                         headings=['Column'] + numer_descr.columns.tolist())]
                           ])

        features = [['all']] + [[i] for i in data.columns.tolist()]

        tabs = sg.TabGroup([
            [data_tab, load_tab],
            [num_stats_tab]
        ])
    else:
        tabs = sg.TabGroup([
            [data_tab, load_tab],
        ])

        features = [['Nothing here']]

    layout = [
        [sg.Text('DataLoader', font='Ubuntu 25 italic')],
        [sg.Column(layout=[
            [sg.Text('Choose features')],
            [sg.Table(values=features, enable_events=True, headings=['Column'], key='-COLUMNS-')]
        ]), sg.VerticalSeparator(), sg.Column(layout=[[tabs]])],

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
                is_query = True
            else:
                sg.popup('Please load some some first')
        except Exception as e:
            print(e)
            sg.popup(str(e))


    elif event == 'Reset':
        window.close()
        window = create_window(data)
        is_query = False

    elif event == '-DATA-':
        print(values[event])

window.close()

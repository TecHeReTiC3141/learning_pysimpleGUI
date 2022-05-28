import PySimpleGUI as sg
import pandas as pd
import numpy as np

data, queried = pd.read_csv('titanic.csv'), pd.DataFrame()
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
def create_window(data: pd.DataFrame, all_data: pd.DataFrame, columns='all') -> sg.Window:
    if isinstance(columns, list):
        values = np.hstack(
            (np.array(range(1, data.shape[0] + 1)).reshape((data.shape[0], 1)), data.iloc[:, columns].values)).tolist()
    else:
        values = np.hstack((np.array(range(1, data.shape[0] + 1)).reshape((data.shape[0], 1)), data.values)).tolist()

    table = sg.Table(values=values,
                     headings=['Id'] + data.columns.values.tolist(), max_col_width=35,
                     key='-DATA-', expand_x=True, auto_size_columns=True, enable_events=True)

    data_tab = sg.Tab('Data',
                      layout=[
                          [sg.T('Write query to data:')],
                          [sg.Input(key='-MAKEQUERY-', expand_x=True), sg.B('Query'), sg.B('Reset')]
                      ], key='-DATATAB-', expand_x=True)

    load_tab = sg.Tab('Load and save', layout=[
        [sg.B('Load data', right_click_menu=from_formats), sg.T(f'Current format: {cur_format}', key='-CURFORM-')],
        [sg.B('Save data', right_click_menu=to_formats), sg.T(f'Current format: {cur_format}', key='-CURFORM-')]
    ], expand_x=True)

    if data.shape[1] > 0:
        num_cols, cat_cols = [], []
        for col in data.columns:
            if data[col].dtype == np.object or data[col].nunique() <= 5:
                cat_cols.append(col)
            else:
                num_cols.append(col)
        numer_descr = data[num_cols].describe().round(3).T
        cater_descr = data[cat_cols].describe(include=['object', 'float64', 'int']).round(3).T[['count', 'freq',
                                                                                                'unique', 'top', 'mean']]

        print(numer_descr)

        print(numer_descr.index.to_numpy().reshape(numer_descr.shape[0], 1), numer_descr.values)

        num_stats_tab = sg.Tab('Numeric Stats',
                               layout=[
                                   [sg.T('Numeric features description')],
                                   [sg.HSep()],
                                   [sg.Table(
                                       values=np.hstack([numer_descr.index.to_numpy().reshape(numer_descr.shape[0], 1),
                                                         numer_descr.values]).tolist(),
                                       headings=['Column'] + numer_descr.columns.tolist())]
                               ])

        cat_stats_tab = sg.Tab('Caterogical Stats',
                               layout=[
                                   [sg.T('Categorical features description')],
                                   [sg.HSep()],
                                   [sg.Table(
                                       values=np.hstack([cater_descr.index.to_numpy().reshape(cater_descr.shape[0], 1),
                                                         cater_descr.values]).tolist(),
                                       headings=['Column'] + cater_descr.columns.tolist())]
                               ])

        num_features = [['all']] + [[i] for i in num_cols]
        cat_features = [['all']] + [[i] for i in cat_cols]

        plottings = sg.Tab('Visualisations',
                           layout=[
                               [sg.Col(layout=[
                                   [sg.T('Choose features')],
                                   [sg.Fr('Numeric', layout=[
                                       [sg.Table(values=num_features, enable_events=True, headings=['Column'],
                                                 key='-NUMS-')]
                                   ])],
                                   [sg.Fr('Categorical', layout=[
                                       [sg.Table(values=cat_features, enable_events=True, headings=['Column'],
                                                 key='-CATS-')]
                                   ])]
                               ]), sg.VSep(), sg.Col(layout=[
                                   [sg.Canvas(key='-CANVAS-', size=(5, 5))]
                               ])
                               ]])

        tabs = sg.TabGroup([
            [data_tab, load_tab, num_stats_tab, cat_stats_tab, plottings],
        ])
    else:
        tabs = sg.TabGroup([
            [data_tab, load_tab],
        ])

    layout = [
        [sg.T('DataLoader', font='Ubuntu 25 italic')],
        [tabs],
        [sg.HSep()],
        [sg.T(f'Data {data.shape[0]} rows x {data.shape[1]} columns')],
        [table],
    ]

    window = sg.Window('DataLoader', layout=layout, element_justification='center', finalize=True)
    return window


window = create_window(data, data)

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

            window = create_window(data, data)
            print(window)
            print(data.columns.values)
            print(window['-DATA-'].Values[0], len(window['-DATA-'].Values))
        except Exception as e:
            print(e)
            sg.popup(str(e))

    elif event == 'Save data':
        try:
            filepath = sg.popup_get_file('', no_window=True, save_as=True)
            if not filepath.endswith('.csv'):
                filepath += '.csv'
            if is_query:
                queried.to_csv(filepath, index=False)
            else:
                data.to_csv(filepath, index=False)
        except Exception as e:
            sg.popup_error(str(e))

    elif event == 'Query':
        try:
            if len(data):
                query = values['-MAKEQUERY-']
                queried = data.query(query)

                window.close()
                window = create_window(queried, data)
                window['-MAKEQUERY-'].update(query)
                is_query = True
            else:
                sg.popup('Please load some some first')
        except Exception as e:
            print(e)
            sg.popup(str(e))

    elif event == 'Reset':
        window.close()
        window = create_window(data, data)
        is_query = False

    elif event == '-DATA-':
        print(values[event])

    elif event == '-COLUMNS-':
        if 0 in values[event]:
            window.close()
            if is_query:
                window = create_window(queried, data)
            else:
                window = create_window(data, data)
        else:
            cols = [i - 1 for i in values[event]]
            window.close()
            if is_query:
                window = create_window(queried, data, cols)
            else:
                window = create_window(data, data, cols)

window.close()

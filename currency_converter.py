import PySimpleGUI as sg
from getting_info_about_currency import source_data, currency
layout = [
    [sg.Text('Hello, Insert value:', enable_events=True, key='-GREET-'),
     sg.Input(key='-INPUT-')],
    [sg.Button('Convert!', key='-CONV-'), sg.Spin(list(currency.keys()), key='-CURRENCY-'), sg.Spin(['to rouble', 'from rouble'], key='-TYPE-')],
    [sg.Text('Input: ; Result: ', key='-RESULT-'), sg.Button('Reset', key='-RESET-')],
]

window = sg.Window('Converter', layout)
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == '-CONV-':
        print('In progress')
        try:
            inp = float(values["-INPUT-"])
            cur_val = currency[values["-CURRENCY-"]]
            if values["-TYPE-"] == "to rouble":

                window['-RESULT-'].update(f'Input: {inp}; Result: {round(inp * cur_val["Value"] / cur_val["Nominal"], 2)}₽')
            else:
                window['-RESULT-'].update(f'Input: {inp}; Result: {round(inp / cur_val["Value"] * cur_val["Nominal"], 2)} {cur_val["Name"]}')
        except Exception as e:
            window['-RESULT-'].update('Wrong input. Please type a number')
            print(e)


    elif event == '-RESET-':
        print('The result was wiped')
        window['-RESULT-'].update(f'Input: ; Result: ')

    elif event == '-GREET-':
        print(values)

window.close()
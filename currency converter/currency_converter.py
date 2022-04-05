import PySimpleGUI as sg
from getting_info_about_currency import *

sourse_date, curr_data = get_currency_info(['USD', 'EUR', 'PLN', 'UAH', 'JPY'])
pprint(curr_data)

layout = [
    [sg.Text('Hello, Insert value:', enable_events=True, key='-GREET-'),
     sg.Input(key='-INPUT-')],
    [sg.Button('Convert!', key='-CONV-'), sg.Spin(list(curr_data.keys()), key='-CURRENCY-'), sg.Spin(['to rouble', 'from rouble'], key='-TYPE-')],
    [sg.Text('', key='-RESULT-'), sg.Button('Reset', key='-RESET-'), sg.Text(f'Data gathered in {sourse_date}', background_color='White', text_color='Black')],
]

window = sg.Window('Currency Converter', layout)
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == '-CONV-':
        if values['-INPUT-'].isnumeric():
            inp = float(values["-INPUT-"])
            cur_val = curr_data[values["-CURRENCY-"]]
            window['-RESULT-'].update(visible=True)
            if values["-TYPE-"] == "to rouble":

                window['-RESULT-'].update(f'Output: {inp} {cur_val["Name"]} = {round(inp * cur_val["Value"] / cur_val["Nominal"], 2)}₽')
            else:
                window['-RESULT-'].update(f'Output: {inp}₽ = {round(inp / cur_val["Value"] * cur_val["Nominal"], 2)} {cur_val["Name"]}')
        else:
            window['-RESULT-'].update('Wrong input. Please enter a number')


    elif event == '-RESET-':
        print('The result was wiped')
        window['-RESULT-'].update(visible=False)

    elif event == '-GREET-':
        print(values)

window.close()
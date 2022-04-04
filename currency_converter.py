import PySimpleGUI as sg
currency = {'USD': ('$', 83.59), 'EURO': ('€', 92.39), 'Zloty': ("zł", 19.86), 'Hrivna': ('₴', 2.84)}
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
            if values["-TYPE-"] == "to rouble":
                window['-RESULT-'].update(f'Input: {inp}; Result: {round(inp * currency[values["-CURRENCY-"]][1], 2)}₽')
            else:
                window['-RESULT-'].update(f'Input: {inp}; Result: {round(inp / currency[values["-CURRENCY-"]][1], 2)}{currency[values["-CURRENCY-"]][0]}')
        except Exception as e:
            window['-RESULT-'].update('Wrong input. Please type a number')
            print(e)


    elif event == '-RESET-':
        print('The result was wiped')
        window['-RESULT-'].update(f'Input: ; Result: ')

    elif event == '-GREET-':
        print(values)

window.close()

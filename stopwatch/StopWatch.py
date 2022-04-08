import PySimpleGUI as sg
from time import sleep, time

sg.theme('black')

layout = [
    [sg.Push(), sg.Image('m_closing_button.png', pad=0, enable_events=True, key='-EXIT-')],
    [sg.VPush(), ],
    [sg.Text('0.0', key='-TIME-', font='Young 45')],
    [
        sg.Button('Lap', button_color=('white', 'red'), border_width=2),
        sg.Button('Start', button_color=('white', 'red'), border_width=2, key='-STARTSTOP-')
    ],
    [sg.VPush()]
]

window = sg.Window('StopWatch',
                   layout,
                   size=(250, 250),
                   no_titlebar=True,
                   element_justification='center')
beg_time, active = time(), False

while True:
    event, values = window.read(timeout=100)

    if event in [sg.WIN_CLOSED, '-EXIT-']:
        break

    elif event == '-STARTSTOP-':
        if window['-STARTSTOP-'].get_text() == 'Start':
            window['-STARTSTOP-'].update('Reset')
            beg_time, active = time(), True
            window['-TIME-'].update(round(time() - beg_time, 1))

        else:
            window['-STARTSTOP-'].update('Start')
            active = False

    if active:
        window['-TIME-'].update(round(time() - beg_time, 1))

window.close()

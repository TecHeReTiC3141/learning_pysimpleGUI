import PySimpleGUI as sg
from time import sleep

sg.theme('black')

layout = [
    [sg.Push(), sg.Image('m_closing_button.png', pad=0, enable_events=True, key='-EXIT-')],
    [sg.VPush(), ],
    [sg.Text('0.0', key='-TIME-', font='Young 45')],
    [
        sg.Button('Lap', button_color=('white', 'red'), border_width=2),
        sg.Button('Reset', button_color=('white', 'red'), border_width=2)
    ],
    [sg.VPush()]
]

window = sg.Window('StopWatch',
                   layout,
                   size=(250, 250),
                   no_titlebar=True,
                   element_justification='center')
cur_time = 0.

while True:
    event, values = window.read()

    if event in [sg.WIN_CLOSED, '-EXIT-']:
        break

    cur_time = round(cur_time + .1, 1)
    window['-TIME-'].update(cur_time)
    sleep(.1)




window.close()

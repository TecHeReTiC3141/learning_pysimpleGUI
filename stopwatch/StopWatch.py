import PySimpleGUI as sg
from time import sleep, time

sg.theme('black')

def create_start_window():

    layout = [
        [sg.Push(), sg.Image('m_closing_button.png', pad=0, enable_events=True, key='-EXIT-')],
        [sg.VPush(), ],
        [sg.Text('0.0', key='-TIME-', font='Young 45')],
        [
            sg.Button('Lap', button_color=('white', 'red'), border_width=2, key='-LAP-', visible=False),
            sg.Button('Start', button_color=('white', 'red'), border_width=2, key='-STARTSTOP-')
        ],
        [sg.VPush()]
    ]

    window = sg.Window('StopWatch',
                       layout,
                       size=(250, 250),
                       no_titlebar=True,
                       element_justification='center')

    return window


beg_time, active = time(), False
window = create_start_window()

while True:
    event, values = window.read(timeout=10)

    if event in [sg.WIN_CLOSED, '-EXIT-']:
        break

    elif event == '-STARTSTOP-':
        if window['-STARTSTOP-'].get_text() == 'Start':
            window['-STARTSTOP-'].update('Reset')
            beg_time, active = time(), True
            window['-LAP-'].update(visible=True)


        else:
            window['-STARTSTOP-'].update('Start')
            active = False
            window['-TIME-'].update(round(0., 1))
            window['-LAP-'].update(visible=False)

    elif event == '-LAP-':
        pass
        # TODO implement lap button and updating window

    if active:
        window['-TIME-'].update(round(time() - beg_time, 1))

window.close()

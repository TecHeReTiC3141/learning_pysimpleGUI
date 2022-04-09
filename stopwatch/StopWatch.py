import PySimpleGUI as sg
from time import time

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
        [sg.Column([[]], key='-LAPS-')],
        [sg.VPush()]
    ]

    return sg.Window('StopWatch',
                     layout,
                     size=(300, 300),
                     no_titlebar=True,
                     element_justification='center', finalize=True)


beg_time, active = 0, False
cur_laps = 0
window = create_start_window()

while True:
    event, values = window.read(timeout=5)

    if event in [sg.WIN_CLOSED, '-EXIT-']:
        break

    elif event == '-STARTSTOP-':
        if not active:
            window['-STARTSTOP-'].update('Reset')
            beg_time, active = time(), True
            window['-LAP-'].update(visible=True)

        else:
            if beg_time == 0:
                window['-STARTSTOP-'].update('Start')
                active = False
                window['-TIME-'].update(round(0., 1))
                window['-LAP-'].update(visible=False)

            else:
                window.close()
                window = create_start_window()
                beg_time, active, cur_laps = 0, False, 0

    elif event == '-LAP-':
        cur_laps += 1
        window.extend_layout(window['-LAPS-'],
                             [[sg.Text(cur_laps), sg.VSeparator(),
                               sg.Text(round(time() - beg_time, 1), justification='center')]])

    if active:
        window['-TIME-'].update(round(time() - beg_time, 1))

window.close()

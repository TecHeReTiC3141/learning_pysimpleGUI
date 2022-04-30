import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from math import *

sg.theme('DarkAmber')
sg.set_options(font='Ubuntu 15')


def update_scatter(data: list[tuple], function: str):
    axes = figure.axes
    cop = data.copy()
    cop.sort(key=lambda i: i[1])
    axes[0].clear()
    axes[0].grid()
    axes[0].plot([i[1] for i in cop], [i[2] for i in cop])
    axes[0].set_title('y = ' + function)
    figure.axes[0].set_xlabel('X')
    figure.axes[0].set_ylabel('Y')
    figure_canv.draw()
    figure_canv.get_tk_widget().pack()


def update_range(expr: str, data: list[tuple], x0: int, x1: int, step: float):
    x_data = np.linspace(x0, x1, round((x1 - x0) // step))
    y_data = np.array(list(map(lambda i: eval(expr.replace('x', str(i))), x_data)))
    print(f'x - {x_data}')
    print(f'y - {y_data}')

    # TODO fill tables correctly in numpy-like style
    for x, y in np.stack([x_data, y_data], axis=1):
        data.append((len(data) + 1, round(x, 2), round(y, 2)))

    axe = figure.axes[0]
    axe.clear()
    axe.grid()
    axe.plot(x_data, y_data)
    axe.set_title('y = ' + expr)
    figure.axes[0].set_xlabel('X')
    figure.axes[0].set_ylabel('Y')
    figure_canv.draw()
    figure_canv.get_tk_widget().pack()


table_content = []
frozen = False

scatter_tab = sg.Tab('Scatter', layout=[
    [sg.Text('Insert value:', font='Ubuntu 20 underline')],
    [sg.Input(key='-INPUT-', expand_x=True), sg.Button('Submit', key='-SUBMITSCAT-')],

])

range_tab = sg.Tab('Range', layout=[
    [sg.Frame('x0', layout=[
        [sg.Input(size=(10, 50), key='-X0-')]
    ]), sg.Frame('x1', layout=[
        [sg.Input(size=(10, 50), key='-X1-')]
    ]),
     sg.Frame('step', layout=[
         [sg.Input(size=(10, 50), key='-STEP-')]
     ]), sg.Button('Submit', key='-SUBMITRANGE-')
     ]
])

layout = [
    [sg.Text('TecGrapher', font='Young 40 italic')],
    [sg.HorizontalSeparator()],
    [sg.Text('Insert formula in terms of x:', font='Ubuntu 20 underline')],
    [sg.Input(expand_x=True, key='-FUNCTION-', default_text='Smth like x ** 2 + 1 - 3 * x', ),
     sg.Button('Freeze formula', key='-FREEZE-')],
    [sg.Table(headings=['Index', 'Observation', 'Result'],
              values=table_content,
              expand_x=True,
              hide_vertical_scroll=True,
              key='-DATA-')],
    [sg.TabGroup(layout=[
        [scatter_tab, range_tab]
    ], key='-GROUP-')],
    [sg.Canvas(key='-CANVAS-')],
    [sg.Button('Reset')]
]

window = sg.Window('Grapher', layout, finalize=True, return_keyboard_events=True)
sg.popup('TecGrapher is a simple GUI-app created to plot any function\n which can be expressed by Python syntax',
         title='Intro', no_titlebar=True)

figure = matplotlib.figure.Figure(figsize=(6, 4))
figure.add_subplot(1, 1, 1).plot([], [])
figure.axes[0].set_xlabel('X')
figure.axes[0].set_ylabel('Y')

figure_canv = FigureCanvasTkAgg(figure, window['-CANVAS-'].TKCanvas)
figure_canv.draw()

figure_canv.get_tk_widget().pack()

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    elif event == '-SUBMITSCAT-':
        if not frozen:
            sg.popup('Please freeze formula first', title='Error')
            continue

        try:
            obs = float(values['-INPUT-'])
            table_content.append((len(table_content) + 1, obs,
                                  eval(values['-FUNCTION-'].replace('x', str(obs) if obs >= 0 else f'({obs})'))))
            window['-DATA-'].update(values=table_content)
            window['-INPUT-'].update('')
            update_scatter(table_content, values['-FUNCTION-'])

        except Exception as e:
            print(e)
            sg.popup('Please insert integer and right formula', title='Error')

    elif event == '-SUBMITRANGE-':
        if not frozen:
            sg.popup('Please freeze formula first', title='Error')
            continue

        x, y, step = float(values['-X0-']), float(values['-X1-']), float(values['-STEP-'])
        if x and y and step:
            table_content = []
            window['-DATA-'].update(values=table_content)
            update_range(values['-FUNCTION-'], table_content, x, y, step)
            window['-DATA-'].update(values=table_content)
            window['-X0-'].update('')
            window['-X1-'].update('')
            window['-STEP-'].update('')

        else:
            sg.popup('Please enter x, y and step', title='Error')


    elif event == '-FREEZE-':
        frozen = True
        window['-FUNCTION-'].update(disabled=True, text_color='black')
        window['-FREEZE-'].update(disabled=True)

    elif event == 'Reset':
        frozen = False
        window['-FUNCTION-'].update(disabled=False,
                                   text_color='orange')
        window['-INPUT-'].update(value='',)
        table_content = []
        window['-DATA-'].update(values=table_content)

        figure.axes[0].clear()

        window['-FREEZE-'].update(disabled=False)


window.close()

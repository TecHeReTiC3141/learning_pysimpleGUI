import PySimpleGUI as sg
from constants import *

sg.theme('DarkAmber')

game_field = sg.Graph(
    canvas_size=(field_size, field_size),
    graph_bottom_left=(0, 0),
    graph_top_right = (field_size, field_size),
    background_color='black'
)

layout = [
    [game_field]
]

window = sg.Window('Snake', layout, return_keyboard_events=True)

while True:
    event, values = window.read(timeout=10)

    if event == sg.WIN_CLOSED:
        break

    elif event == 'Left:37':
        print('left')
    elif event == 'Up:38':
        print('up')
    elif event == 'Right:39':
        print('right')
    elif event == 'Down:40':
        print('down')

    for i in range(cell_num):
        for j in range(cell_num):
            game_field.DrawRectangle(*pos_to_pixel(i, j), 'red')

window.close()
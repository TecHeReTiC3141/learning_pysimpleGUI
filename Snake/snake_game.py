from random import *
from time import time

import PySimpleGUI as sg

from classes import *

sg.theme('DarkAmber')
sg.set_options(font='Young 40 italic', )

game_field = sg.Graph(
    canvas_size=(field_size, field_size),
    graph_bottom_left=(0, 0),
    graph_top_right=(field_size, field_size),
    background_color='green'
)

snake = Snake([(2, 3), (3, 3), (4, 3)])

apples = [Apple(randint(0, cell_num - 1), randint(0, cell_num - 1)) for i in range(randint(1, 3))]

layout = [
    [sg.Push(), sg.Text('The Snake', justification='center'), sg.Push()],
    [sg.Text('Current score: 0', key='-SCORE-', pad=((5, 5), (10, 10)))],
    [game_field]
]

window = sg.Window('Snake', layout, return_keyboard_events=True)

start_time = time()
while True:
    event, values = window.read(timeout=50)

    if event == sg.WIN_CLOSED:
        break

    elif event in ['Left:37', 'Up:38',
                   'Right:39', 'Down:40']:
        snake.set_dir(event.split(':')[0].lower())

    cur_time = time()
    if not apples:
        apples.extend([Apple(randint(0, cell_num - 1), randint(0, cell_num - 1)) for i in range(randint(1, 3))])
    if cur_time - start_time >= .25:
        start_time = cur_time

        # clearing canvas
        for i in range(cell_num):
            for j in range(cell_num):
                game_field.DrawRectangle(*pos_to_pixel(i, j), 'grey')

        for ind, segm in enumerate(snake.draw_object()):
            game_field.DrawRectangle(*segm, 'green' if ind != 0 else 'yellow')
        snake.move()
        snake.collide(apples)
        window['-SCORE-'].update(f'Current score: {len(snake.segm) - 3}')

        for apple in apples:
            game_field.DrawRectangle(*pos_to_pixel(apple.x, apple.y), 'red')


window.close()

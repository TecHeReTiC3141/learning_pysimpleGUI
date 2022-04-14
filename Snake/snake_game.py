import PySimpleGUI as sg
from classes import *
from time import sleep, time

sg.theme('DarkAmber')

game_field = sg.Graph(
    canvas_size=(field_size, field_size),
    graph_bottom_left=(0, 0),
    graph_top_right=(field_size, field_size),
    background_color='black'
)

snake = Snake([(2, 3), (3, 3), (4, 3)])

layout = [
    [game_field]
]


window = sg.Window('Snake', layout, return_keyboard_events=True)

start_time = time()
while True:
    event, values = window.read(timeout=30)

    if event == sg.WIN_CLOSED:
        break

    elif event in ['Left:37', 'Up:38',
                   'Right:39', 'Down:40']:
        snake.set_dir(event.split(':')[0].lower())
        print(snake.direction)

    cur_time = time()
    if cur_time - start_time >= .35:
        start_time = cur_time

        # clearing canvas
        for i in range(cell_num):
            for j in range(cell_num):
                game_field.DrawRectangle(*pos_to_pixel(i, j), 'grey')

        for ind, segm in enumerate(snake.draw_object()):
            game_field.DrawRectangle(*segm, 'green' if ind != 0 else 'yellow')

        snake.move()


window.close()

import PySimpleGUI as sg
from snake import *
from time import sleep

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
tick = 0

window = sg.Window('Snake', layout, return_keyboard_events=True)

while True:
    event, values = window.read(timeout=30)

    if event == sg.WIN_CLOSED:
        break

    elif event in ['Left:37', 'Up:38',
                   'Right:39', 'Down:40']:
        snake.set_dir(event.split(':')[0].lower())
        print(snake.direction)

    for i in range(cell_num):
        for j in range(cell_num):
            game_field.DrawRectangle(*pos_to_pixel(i, j), 'white')

    for segm in snake.draw_object():
        game_field.DrawRectangle(*segm, 'green')

    sleep(.15)
    snake.move()


window.close()

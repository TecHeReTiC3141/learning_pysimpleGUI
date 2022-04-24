import PySimpleGUI as sg
from bs4 import BeautifulSoup
from PIL import Image, ImageTk

sg.theme('BlueMono')

def update_image(filename: str, key: str, size: tuple):
    im = Image.open(filename).resize(size, Image.Resampling.BICUBIC)
    window[key].update(data=ImageTk.PhotoImage(image=im))


im_col = sg.Column([
    [sg.Image('', size=(300, 300), key='-WEATHER-', background_color='#FFFFFF')]
])

forecast_col = sg.Column([
    [sg.Text('Chusovoy', background_color='red', font='Frank 35', text_color='grey', pad=1, key='-LOC-', visible=False)],
    [sg.Text('Time', background_color='white', font='Frank 35', text_color='black', pad=1, key='-TIME-', visible=False)],
    [sg.Text('Temperature', background_color='red', font='Frank 35', text_color='grey', pad=1, key='-TEMP-', visible=False)]
])

layout = [
    [sg.Input(key='-INPUT-', expand_x=True), sg.Button('Submit', border_width=2)],
    [im_col, sg.VerticalSeparator(), forecast_col],
]

window = sg.Window('Weather Forecast', layout, finalize=True)
update_image('images/sunny.png', '-WEATHER-', (300, 300))

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == 'Submit':
        window['-LOC-'].update(visible=True)
        window['-TIME-'].update(visible=True)
        window['-TEMP-'].update(visible=True)
        update_image('images/sunny.png', '-WEATHER-', (350, 350))

window.close()
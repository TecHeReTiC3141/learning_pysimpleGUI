import PySimpleGUI as sg
from bs4 import BeautifulSoup
from PIL import Image, ImageTk

sg.theme('BlueMono')

def update_image(filename: str, key: str, size: tuple):
    im = Image.open(filename).resize(size, Image.Resampling.BICUBIC)
    window[key].update(data=ImageTk.PhotoImage(image=im))


im_col = sg.Column([
    [sg.Image('', size=(300, 300), key='-SUNNY-')]
])

forecast_col = sg.Column([
    [sg.Text('Chusovoy', background_color='red', font='Frank 35', text_color='grey')]
])

layout = [
    [sg.Input(key='-INPUT-', expand_x=True), sg.Button('Submit')],
    [im_col, sg.VerticalSeparator(), forecast_col],
]

window = sg.Window('Weather Forecast', layout, finalize=True)
update_image('images/sunny.png', '-SUNNY-', (300, 300))

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()
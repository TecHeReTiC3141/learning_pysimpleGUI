import PySimpleGUI as sg
from PIL import Image, ImageTk

from get_data import get_weather_data

sg.theme('BlueMono')


def update_image(filename: str, key: str, size: tuple):
    im = Image.open(filename).resize(size, Image.Resampling.BICUBIC)
    window[key].update(data=ImageTk.PhotoImage(image=im))


im_col = sg.Column([
    [sg.Image('', size=(300, 300), key='-WEATHER-', background_color='#FFFFFF', visible=False)]
])

forecast_col = sg.Column([
    [sg.Text('Chusovoy', background_color='red', font='Frank 35', text_color='grey', pad=1, key='-LOC-', visible=False)],
    [sg.Text('DESCR', background_color='white', font='Frank 35', text_color='black', pad=1, key='-DESCR-', visible=False)],
    [sg.Text('Temperature', background_color='red', font='Frank 35', text_color='black', pad=1, key='-TEMP-', visible=False)]
])

layout = [
    [sg.Input(key='-INPUT-', expand_x=True), sg.Button('Submit', border_width=2)],
    [im_col, sg.VerticalSeparator(key='-SEP-'), forecast_col],
]

window = sg.Window('Weather Forecast', layout, finalize=True)
update_image('images/sunny.png', '-WEATHER-', (300, 300))

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == 'Submit':
        try:
            data = get_weather_data(values['-INPUT-'])
            window['-LOC-'].update(value=f"{data['name']}, {data['sys']['country']}", visible=True)
            window['-DESCR-'].update(value=data['weather'][0]['main'], visible=True)
            window['-TEMP-'].update(value=f"Temp: {data['main']['feels_like']}\u2103", visible=True)
            window['-WEATHER-'].update(visible=True)
            # TODO update images
            update_image('images/sunny.png', '-WEATHER-', (350, 350))
        except Exception as e:
            sg.popup(f'{e} Please enter correct place!')


window.close()

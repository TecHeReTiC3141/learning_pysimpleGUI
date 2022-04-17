import PySimpleGUI as sg
import PIL as pil

image = None


def update_image(image, blur: int, contrasr: int,
                 flx: bool, fly: bool, emboss: bool, edges: bool):
    pass


sg.theme('dark')

contr_col = sg.Column([
    [sg.Frame('Blur', layout=[[sg.Slider(range=(0, 10), orientation='h', key='-BLUR-')]])],
    [sg.Frame('Contrast', layout=[[sg.Slider(range=(0, 10), orientation='h', key='-CONTRAST-')]])],
    [sg.Checkbox('Flip x', key='-FLIPX-'), sg.Checkbox('Flip y', key='-FLIPY-')],
    [sg.Checkbox('Emboss', key='-EMBOSS-'), sg.Checkbox('Edges', key='-EDGES-')],
])

image_col = sg.Column([
    [sg.Frame('Result', layout=[[sg.Image('sunrise_cropped.png')]])]
])


layout = [
    [contr_col, sg.VerticalSeparator(), image_col]
]

window = sg.Window('ImageEditor', layout)

while True:

    event, values = window.read(timeout=100)

    if event == sg.WIN_CLOSED:
        break

    update_image(image, values['-BLUR-'], values['-CONTRAST-'],
                 values['-FLIPX-'], values['-FLIPY-'],
                 values['-EMBOSS-'], values['-EDGES-'])
    print(values)

window.close()

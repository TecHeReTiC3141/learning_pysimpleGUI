import PySimpleGUI as sg
import PIL as pil

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
    [contr_col, image_col]
]

window = sg.Window('ImageEditor', layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()

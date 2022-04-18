import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO

image = Image.open('sunrise_cropped.png')


def update_image(image, blur: int, contrast: int,
                 flx: bool, fly: bool, emboss: bool, edges: bool):

    new_image = image.filter(ImageFilter.GaussianBlur(blur))
    new_image = new_image.filter(ImageFilter.UnsharpMask(contrast))

    if flx:
        new_image = ImageOps.mirror(new_image)
    if fly:
        new_image = ImageOps.flip(new_image)
    if edges:
        new_image = new_image.filter(ImageFilter.FIND_EDGES)
    if emboss:
        new_image = new_image.filter(ImageFilter.EMBOSS)


    bio = BytesIO()
    new_image.save(bio, format='PNG')

    window['-IMAGE-'].update(data=bio.getvalue())


sg.theme('dark')

contr_col = sg.Column([
    [sg.Frame('Blur', layout=[[sg.Slider(range=(0, 10), orientation='h', key='-BLUR-')]])],
    [sg.Frame('Contrast', layout=[[sg.Slider(range=(0, 10), orientation='h', key='-CONTRAST-')]])],
    [sg.Checkbox('Flip x', key='-FLIPX-'), sg.Checkbox('Flip y', key='-FLIPY-')],
    [sg.Checkbox('Emboss', key='-EMBOSS-'), sg.Checkbox('Edges', key='-EDGES-')],
])

image_col = sg.Column([
    [sg.Frame('Result', layout=[[sg.Image('sunrise_cropped.png', key='-IMAGE-')]])]
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

window.close()

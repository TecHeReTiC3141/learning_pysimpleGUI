import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO
image = Image.open('sunrise_cropped.png')



def open_image(image):
    bio = BytesIO()
    image.save(bio, 'PNG')
    window['-IMAGE-'].update(bio.getvalue())


def update_image(image, blur: int, contrast: int,
                 flx: bool, fly: bool, emboss: bool, edges: bool, color: str):
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
    if color != 'N':
        r, g, b = new_image.split()
        if color == 'R':
            new_image = r
        elif color == 'G':
            new_image = g
        else:
            new_image = b

    bio = BytesIO()
    new_image.save(bio, format='PNG')

    window['-IMAGE-'].update(data=bio.getvalue())
    return new_image


sg.theme('dark')

contr_col = sg.Column([
    [sg.Frame('RGB', layout=[[sg.Spin(list('RGBN'), key='-COLORS-', initial_value='N')]], expand_x=True)],
    [sg.Frame('Blur', layout=[[sg.Slider(range=(0, 10), orientation='h', key='-BLUR-')]])],
    [sg.Frame('Contrast', layout=[[sg.Slider(range=(0, 10), orientation='h', key='-CONTRAST-')]])],
    [sg.Checkbox('Flip x', key='-FLIPX-'), sg.Checkbox('Flip y', key='-FLIPY-')],
    [sg.Checkbox('Emboss', key='-EMBOSS-'), sg.Checkbox('Edges', key='-EDGES-')],
    [sg.Button('Open image', key='-OPEN-'), sg.Button('Save image', key='-SAVE-')]
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

    cur_image = update_image(image, values['-BLUR-'], values['-CONTRAST-'],
                             values['-FLIPX-'], values['-FLIPY-'],
                             values['-EMBOSS-'], values['-EDGES-'], values['-COLORS-'])

    if event == '-SAVE-':
        path = sg.popup_get_file('Choose where to save',
                                 no_window=True, save_as=True) + '.png'
        cur_image.save(path, 'PNG')

    elif event == '-OPEN-':
        image = Image.open(sg.popup_get_file('Open', no_window=True)).resize((500, 375),
                                                                             Image.Resampling.HAMMING)
        open_image(image)

window.close()

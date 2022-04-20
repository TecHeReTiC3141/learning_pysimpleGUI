import PySimpleGUI as sg
from pytube import YouTube

sg.theme('Darkred')

info_tab = [
    [sg.Text('Title: ', key='-TITLE-')],
    [sg.Text('Views: ', key='-VIEWS-'), ],
    [sg.Text('Length: ', key='-LEN-'), ],
    [sg.Text('Author: ', key='-AUTHOR-'), ],
    [sg.Text('Description: ', key='-DESCR-'),
     sg.Multiline(default_text='Choose video to download', no_scrollbar=True, disabled=True)],
]

down_tab = [
    [sg.Frame('Best quality', [[sg.Button('Download', key='-DOWNBEST-')]])],
    [sg.Frame('Worst quality', [[sg.Button('Download', key='-DOWNWORST-')]])],
    [sg.Frame('Audio quality', [[sg.Button('Download', key='-AUDIOONLY-')]])],
    [sg.Progress(100, expand_x=True, size=(20, 20), pad=((10, 10), (5, 5)))]
]

# TODO set keys to elements

layout = [
    [sg.Text('YouTube Downloader', font='Young 35')],
    [sg.HorizontalSeparator()],
    [sg.TabGroup([[
        sg.Tab('info', info_tab, expand_x=True),
        sg.Tab('download', down_tab, expand_x=True),
    ]])]
]

window = sg.Window('Youtube Downloader', layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()

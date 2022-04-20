import PySimpleGUI as sg
from pytube import YouTube

sg.theme('dark')

info_tab = [
    [sg.Text('Title: ', key='-TITLE-')],
    [sg.Text('Views: ', key='-VIEWS-'),],
    [sg.Text('Length: ', key='-LEN-'),],
    [sg.Text('Author: ', key='-AUTHOR-'),],
    [sg.Text('Description: ', key='-DESCR-'),
     sg.Multiline(default_text='Choose video to download', no_scrollbar=True, disabled=True)],
]

down_tab = [
    []
]


layout = [
    [sg.Text('YouTube Downloader', font='Young 45')],
    [sg.HorizontalSeparator()],
    [sg.TabGroup([[
        sg.Tab('info', info_tab),
        sg.Tab('info', down_tab),
    ]])]
]

window = sg.Window('Youtube Downloader', layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()

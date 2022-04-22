import PySimpleGUI as sg
from pytube import YouTube

sg.theme('Darkred1')

info_tab = [
    [sg.Text('Title:'), sg.Text('', key='-TITLE-')],
    [sg.Text('Views:'), sg.Text('', key='-VIEWS-'), ],
    [sg.Text('Length:'), sg.Text('', key='-LEN-'), ],
    [sg.Text('Author:'), sg.Text('', key='-AUTHOR-'), ],
    [sg.Text('Description: '),
     sg.Multiline(default_text='Choose video to download', no_scrollbar=True, disabled=True, expand_x=True,
                  expand_y=True, key='-DESCR-')],
]

down_tab = [
    [sg.Frame('Best quality', [[sg.Button('Download', key='-DOWNBEST-'), sg.Text('', key='-BESTSIZE-')]])],
    [sg.Frame('Worst quality', [[sg.Button('Download', key='-DOWNWORST-'), sg.Text('', key='-WORSTSIZE-')]])],
    [sg.Frame('Audio quality', [[sg.Button('Download', key='-AUDIOONLY-'), sg.Text('', key='-AUDIOSIZE-')]])],
    [sg.Progress(100, expand_x=True, size=(20, 20),
                 pad=((10, 10), (5, 5)),
                 key='-PROGRESS-')]
]

start_layout = [
    [sg.Input('', key='-INPUT-'), sg.Button('Submit')]
]

layout = [
    [sg.Text('YouTube Downloader', font='Young 35')],
    [sg.HorizontalSeparator()],
    [sg.TabGroup([[
        sg.Tab('info', info_tab, expand_x=True, expand_y=True),
        sg.Tab('download', down_tab, expand_x=True, expand_y=True),
    ]])]
]

window = sg.Window('Insert ref to video', start_layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == 'Submit':
        try:
            video = YouTube(values['-INPUT-'])
            window.close()

            window = sg.Window('Youtube Downloader', layout, finalize=True)
            window['-TITLE-'].update(video.title)
            window['-VIEWS-'].update(video.views)
            window['-LEN-'].update(f'{round(video.length / 60, 2)} mins')
            window['-AUTHOR-'].update(video.author)
            window['-DESCR-'].update(video.description)

            window['-BESTSIZE-'].update(f'{video.streams.get_highest_resolution().filesize / 2 ** 23} MB')
            window['-WORSTSIZE-'].update(f'{video.streams.get_lowest_resolution().filesize / 2 ** 23} MB')
            window['-AUDIOSIZE-'].update(f'{video.streams.get_audio_only().filesize / 2 ** 23} MB')
        except Exception as e:
            print(e)
            sg.popup('Please, enter a valid ref', title='Error')
window.close()

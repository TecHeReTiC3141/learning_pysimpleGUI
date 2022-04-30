import PySimpleGUI as sg
import cv2

layout = [
    [sg.Image(filename='../Image Editor/green_sunrise.png', key='-IMAGE-')],
    [sg.Text('There is 0 people in the sight')]
]

window = sg.Window('Face Detector', layout, element_justification='c')

capture = cv2.VideoCapture(0)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()
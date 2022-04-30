import PySimpleGUI as sg
import cv2

layout = [
    [sg.Image(filename='../Image Editor/green_sunrise.png', key='-IMAGE1-'),
     sg.Image(filename='../Image Editor/green_sunrise.png', key='-IMAGE2-')],
    [sg.Text('There is 0 people in the sight', key='-COUNT-')]
]

window = sg.Window('Face Detector', layout, element_justification='c')

capture1 = cv2.VideoCapture(1)
capture2 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



while True:
    event, values = window.read(timeout=0)

    if event == sg.WIN_CLOSED:
        break

    _, frame1 = capture1.read()
    frame2 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        frame2,
        scaleFactor=1.3,
        minNeighbors=7,
        minSize=(50, 50)
    )

    print(faces)
    for x, y, w, h in faces:
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    imgbytes1 = cv2.imencode('.png', frame1)[1].tobytes()
    imgbytes2 = cv2.imencode('.png', frame2)[1].tobytes()
    window['-IMAGE1-'].update(data=imgbytes1)
    window['-IMAGE2-'].update(data=imgbytes2)
    window['-COUNT-'].update(f'There are {len(faces)} people in the sight')

window.close()
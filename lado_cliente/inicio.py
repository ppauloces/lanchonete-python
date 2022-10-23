import PySimpleGUI as sg
import conn
import time
import one 

def inicio_screen():

    sg.theme('reddit')
    sg.set_options(font=('Arial 16'),text_color = 'black')

    image = [
        [sg.Image(filename='logo.png')]
    ]

    input = [
        [sg.Button("FAZER PEDIDO",size=(23,1),button_color=('red'))]
    ]

    layout = [
        [
        sg.Column(image),
        sg.VSeparator(),
        sg.Column(input)
        ]

    ]
    window = sg.Window('Pedido', layout=layout,element_justification='c',)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == "FAZER PEDIDO":
            one.step_one()
    window.close()
inicio_screen()
import PySimpleGUI as sg
import conn
import time


def step_one():

    sg.theme('reddit')
    sg.set_options(font=('Arial 16'),text_color = 'black')

    cursor = conn.banco.cursor()
            
    query = "SELECT * FROM lanches WHERE tipo = 'C'"
            
    cursor.execute(query)

    resultado = cursor.fetchall()

    

    text = [
        [sg.Text("O que irá comer?")]
    ]

    checkbox =  [
        [sg.Checkbox("Hamburguer", 'group 2', key='hamburguer',font=('Arial 12'))],
        [sg.Checkbox("BigMac", 'group 2', key='bigmac',font=('Arial 12'))],
        [sg.Checkbox("Lanche Natural", 'group 2', key='lancheNatural',font=('Arial 12'))],
        [sg.Checkbox("Batata Frita", 'group 2', key='batataFrita',font=('Arial 12'))]
        ]
    button = [
        [sg.Button("Continuar")]
    ]

    layout = [
        [sg.Column(text)],
        [sg.Column(checkbox)],
        [sg.Column(button)]
    ]

    window = sg.Window('Pedido', layout=layout,element_justification='l')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        print(values['choice'])
step_one()
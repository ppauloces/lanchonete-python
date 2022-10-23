import PySimpleGUI as sg

data = ['One', 'Two', 'Three', 'Four']

layout = [
    [sg.Combo(data, size=20, enable_events=False, key='COMBO')],
    [sg.Push(), sg.Button('Check')],
]
window = sg.Window('Title', layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event in ('COMBO', 'Check'):
        text = values['COMBO']
        index1 = window['COMBO'].widget.current()
        index2 = data.index(text) if text in data else -1
        print(index1, index2, repr(values['COMBO']))

window.close()
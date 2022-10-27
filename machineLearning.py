import wolframalpha
import PySimpleGUI as sg

apiAccessKey = '4Y8UP4-YUU37UK48U'
client = wolframalpha.Client(apiAccessKey)
layout = [[sg.Text("What Can I do For You?"), sg.InputText()], 
         [sg.Button("Enter")]]
window = sg.Window("Api Access Test", layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    elif event == 'Enter':
        res = client.query(values[0])
        sg.Popup(next(res.results).text)
        

window.close()


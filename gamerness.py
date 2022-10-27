'''
Version 1.0
By: Payton J.
updated 3/4/21
'''
pip install PySimpleGUI
pip install Pillow


#^installing packages
import os
import PySimpleGUI as sg


from PILL import image
images = ['cat', 'dog', 'lizard', 'fish']
images[0] = image.open(C:\Users\pc\Pictures\cat.jpeg)
images[1] = image.open(C:\Users\pc\Pictures\dog.jpeg)
images[2] = image.open(C:\Users\pc\Pictures\lizard.jpeg)
images[3] = image.open(C:\Users\pc\Pictures\fish.jpeg)
command = input('What would you like me to do?')

for x in range(1):
    sg.theme('DarkAmber')   
    layout = [  [sg.Text('You can view several different images with this GUI')],
            [sg.Text('Try typing cat, dog, lizard or fish'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]

    window = sg.Window('PhotoViewer By Payton', layout)
    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

window.close()
    



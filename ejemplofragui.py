import PySimpleGUI as sg

layout = [[sg.Text("Hola Mundo")], [sg.Button("OK")]]
window = sg.Window("Demo", layout)
event, values = window.read()
window.close()

from asyncio import events
from tkinter import font
from PIL import Image, ImageDraw
import PySimpleGUI as sg
import os
import tkinter
import io


def draw_hospital():
    img = Image.open("hospital.jpeg")
    img.thumbnail((1200,800))
    bio = io.BytesIO()
    img.save(bio, format="PNG")

    layout = [[sg.Text("Hospital", font = ("Arial", 25))],[sg.Image(data = bio.getvalue())], [sg.Button("Don't show anymore")]]
    window = sg.Window("Image", layout, size = (1200,800))

    while True:
        event, values = window.read()
        if event == "Don't show anymore" or event == sg.WIN_CLOSED:
            break

    window.close()


   

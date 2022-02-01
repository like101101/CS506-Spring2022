from asyncio import events
from tkinter import font
from PIL import Image, ImageDraw
import PySimpleGUI as sg
import os
import tkinter
import io


def draw_firestation():
    img = Image.open("fire.jpeg")
    img.thumbnail((1200,800))
    bio = io.BytesIO()
    img.save(bio, format="PNG")

    layout = [[sg.Text("FireStation", font = ("Arial", 25))],[sg.Image(data = bio.getvalue())], [sg.Button("Don't show anymore")]]
    window = sg.Window("Image", layout, size = (1200,800))

    while True:
        event, values = window.read()
        if event == "Don't show anymore" or event == sg.WIN_CLOSED:
            break

    window.close()


# Import the required libraries
from tkinter import *
import pygame
import PIL.Image
import PIL.ImageTk
import customtkinter
from PIL import Image, ImageTk
from tkinter.ttk import *
import tkinter as tk
from customtkinter import CTkImage

# Create an instance of tkinter frame or window
win = Tk()

win.configure(background='black')

def play_sound():
   pygame.mixer.music.load("Satisfaction/sound.wav")
   pygame.mixer.music.play()

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# Set the size of the window
win.geometry("700x700")
win.title("Click")

# Load the image
image_path = "Satisfaction/music.jpg"
pil_image = Image.open(image_path)

img_label = Label(image=image_path)

# Convert the PIL Image to a CTkImage
ctk_image = CTkImage(pil_image)

# Set the image for the button
button = Button(master=win, image=ctk_image, text="Click Me!", width=190, height=40, compound="left", command=play_sound)

label = Label(win)
label.place(x=0, y=0)

add_folder_image = ImageTk.PhotoImage(Image.open("Satisfaction/music.jpg").resize((40,40), PIL.Image.Resampling.LANCZOS))

button = Button(master=win, image=add_folder_image, text="Click Me!", width=190, height=40, compound="left", command=play_sound)

button.pack(pady=26, padx=20)
button.pack(expand=True)
button.pack(side='bottom')

# Initialize mixer module in pygame
pygame.mixer.init()

# Define a function to play the music

win.mainloop()
label.place(x=0, y=0)

add_folder_image = ImageTk.PhotoImage(Image.open("Satisfaction/music.jpg").resize((40,40), PIL.Image.Resampling.LANCZOS))

button = customtkinter.CTkButton(master=win, image=add_folder_image, text="Click Me!", width=190, height=40, compound="left", command=play_sound)
button.pack(pady=26, padx=20)
button.pack(expand=True)
button.pack(side='bottom')

# Initialize mixer module in pygame
pygame.mixer.init()

# Define a function to play the music

win.mainloop()


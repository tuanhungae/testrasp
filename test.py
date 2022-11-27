from tkinter import *
from tkinter import messagebox
import pyqrcode
import RPi.GPIO as GPIO
import time
from PIL import ImageTk,Image
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

ws = Tk()
ws.title("PythonGuides")
ws.geometry('1920x1080')
# Tk.attributes("-fullscreen", True)
ws['bg'] ='#FFFFFF'

def generate_QR():
    if len(user_input.get()) != 0:
        global qr, img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data=qr.xbm(scale=16))
        p.ChangeDutyCycle(StringVar())
        time.sleep(0.5)
    try:
        display_code()
    except:
        pass

def display_code():
    img_lbl.config(image=img)
    img_lbl.pack(side = RIGHT)

user_input = StringVar()
entry = Entry(
    ws,
    textvariable=user_input
)
entry.pack(padx=50)

button = Button(
    ws,
    text="generate_QR",
    width=15,
    command=generate_QR

)
button.pack(side=LEFT)

button.pack(pady=10)
img_lbl = Label(
    ws
   )

img_lbl.pack()
# output = Label(
#     ws,
# )
# output.pack()
p.stop()
GPIO.cleanup()
ws.mainloop()
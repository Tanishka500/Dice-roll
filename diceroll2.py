import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")

dice = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window, image=image1)
label2 = tk.Label(window, image=image2)

label1.image = image1
label2.image = image2

label1.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
label2.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

def dice_roll():
    new_image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=new_image1)
    label1.image = new_image1

    new_image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=new_image2)
    label2.image = new_image2

button = tk.Button(window, text="ROLL DICE", bg="gray", fg="black", font="Times 20 bold", command=dice_roll)
button.pack(pady=20)  # Centering the button horizontally

window.mainloop()

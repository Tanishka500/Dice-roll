import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")

dice = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window, image=image1)
label1.image = image1
label1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
 
def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1

button = tk.Button(window, text="ROLL DICE", bg="gray", fg="black", font="Times 20 bold", command=dice_roll)
button.pack(pady=20)  # pady adds vertical space above and below the button

window.mainloop()

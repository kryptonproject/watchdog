import os
import tkinter as tk

def create_defacement_screen():
    root = tk.Tk()
    root.title("You've Been Owned!")
    root.attributes('-fullscreen', True)
    root.configure(bg='black')


    message = tk.Label(
        root, 
        text="You Have Been Hacked By KryptonSec_My\nAll of your data, passwords, login, will be sell on darkweb\nsee ya fuckers HAHAHAH",
        fg="red",
        bg="black",
        font=("Courier", 24, "bold"),
        justify="center"
    )
    message.pack(expand=True)

    
    keys_pressed = set()

    def on_key_press(event):
        keys_pressed.add(event.keysym)

        
        if ('Shift_L' in keys_pressed or 'Shift_R' in keys_pressed) and 'K' in keys_pressed:
            root.destroy()

    def on_key_release(event):
        if event.keysym in keys_pressed:
            keys_pressed.remove(event.keysym)

    root.bind("<KeyPress>", on_key_press)
    root.bind("<KeyRelease>", on_key_release)
    root.mainloop()

if __name__ == "__main__":
    create_defacement_screen()

import tkinter as tk
import subprocess
import customtkinter
from customtkinter import CTkButton

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


def LabelStyle1():
    LabelStyle1 = r'C:\Users\pc\Desktop\Model_Select\test.bat'
    subprocess.run([LabelStyle1])


def LabelStyle2():
    LabelStyle2 = r'C:\Users\pc\Desktop\Model_Select\test.bat'
    subprocess.run([LabelStyle2])


def LabelStyle3():
    LabelStyle3 = r'C:\Users\pc\Desktop\Model_Select\test.bat'
    subprocess.run([LabelStyle3])


def open_popout():
    LabelStyle3 = r'C:\Users\pc\Desktop\Model_Select\test.bat'
    subprocess.run([LabelStyle3])
    # popout = tk.Toplevel(window)
    # popout.title('Popout')
    # popout.geometry('300x200')

    # Add widgets to the popout window here
    # label = tk.Label(popout, text='This is a popout window')
    # label.pack()


window = customtkinter.CTk()
window.title('Select Model')
window.geometry('1366x360')


# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates of the center of the screen
window_width = 1366
window_height = 360
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

# Set the window geometry
window.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)

file_menu.add_command(label='LabelStyle1', command=LabelStyle1)
file_menu.add_command(label='LabelStyle2', command=LabelStyle2)
file_menu.add_command(label='LabelStyle3', command=LabelStyle3)
file_menu.add_command(label='Exit', command=window.quit)
file_menu.add_separator()

# Create a button and place it at the center of the window
button = CTkButton(window, text="QA268", command=open_popout)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


window.mainloop()

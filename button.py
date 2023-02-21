import tkinter as tk

root = tk.Tk()

# Define a function to be called when the button is clicked
def button_click():
    print("Button clicked!")

# Create a button widget and add it to the root window
button = tk.Button(root, text="Click me!", command=button_click)
button.pack()

root.mainloop()

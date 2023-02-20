import tkinter as tk

#from globle import start

# create a window
window = tk.Tk()
window.geometry("400x300")

# add a label to the window
label = tk.Label(window, text="Enter your name: ")
label.pack()

#create entry widget for input
entry = tk.Entry(window)
entry.pack()

#create button for user input when clicked
def get_input():
    user_input = entry.get()
    print("you entered:", user_input)

button = tk.Button(window, text="submit", command=get_input)
button.pack()

#start the event loop
window.mainloop()

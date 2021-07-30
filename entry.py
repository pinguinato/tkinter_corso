import tkinter as tk

root = tk.Tk()
root.title("Entry Example")

e = tk.Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
e.pack()
e.insert(0, "Enter your name here")


def my_click():
    hello = "Hello " + e.get()
    myLabel = tk.Label(root, text=hello)
    myLabel.pack()


# this button execute the function my_click()
myButton3 = tk.Button(root, text="Enter your name", command=my_click, fg="blue", bg="#FFFF00")


myButton3.pack()


root.mainloop()


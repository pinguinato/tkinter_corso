import tkinter as tk

root = tk.Tk()


def my_click():
    myLabel = tk.Label(root, text="Look! I clicked a button!!")
    myLabel.pack()


myButton = tk.Button(root, text="Click Me!", state=tk.DISABLED)
myButton2 = tk.Button(root, text="Click Me!", padx=50, pady=50)
# this button execute the function my_click()
myButton3 = tk.Button(root, text="Click me!", command=my_click, fg="blue", bg="#FFFF00")
myButton3.pack()
myButton2.pack()
myButton.pack()


root.mainloop()


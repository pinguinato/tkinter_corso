import tkinter as tk

root = tk.Tk()

# # creating a label
# myLabel1 = tk.Label(root, text="Hello World!!!")
# myLabel2 = tk.Label(root, text="My name is Roberto Gianotto")
# myLabel3 = tk.Label(root, text=" ")
# # show label to the screen with grid layout
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)
# myLabel3.grid(row=1, column=1)

# sviluppo in un singolo step
myLabel1 = tk.Label(root, text="Hello World!!!").grid(row=0, column=0)
myLabel2 = tk.Label(root, text="My name is Roberto Gianotto").grid(row=1, column=5)
myLabel3 = tk.Label(root, text=" ").grid(row=1, column=1)


root.mainloop()
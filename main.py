from populationData import *
import tkinter as tk

window = tk.Tk()
label = tk.Label(text="Population Data", width=20, height=0)
label.pack()

button = tk.Button(
  text = "Get Data",
  width = 10,
  height = 0
)
button.pack()

window.mainloop()
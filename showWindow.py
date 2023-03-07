from populationData import *
from showData import *
import matplotlib.pyplot as plt
import tkinter as tk

window = tk.Tk()
title = tk.Label(text="Pick any country or region here:")
title.pack()
window.geometry( "600x300" )

def show():
  plt.close('all')
  pageCountry = clicked.get()
  createDataVisuals = showData(pageCountry)
  createDataVisuals.start()
  label.config( text = 'Region name: ' + clicked.get() )
  labelMale.config( text = createDataVisuals.printMale() )
  labelFemale.config( text = createDataVisuals.printFemale() )

clicked = tk.StringVar()
clicked.set( "WORLD" )
drop = tk.OptionMenu( window , clicked , *pageCountry )
drop.pack()
button = tk.Button( window , text = "Click To See Data" , command = show ).pack()

labelTop = tk.Label( window , text = "Previous region basic information:" )
labelTop.pack()
label = tk.Label( window , text = "[NO DATA YET]" )
label.pack()
labelMale = tk.Label( window , text = "[NO DATA YET]" )
labelMale.pack()
labelFemale = tk.Label( window , text = "[NO DATA YET]" )
labelFemale.pack()

window.mainloop()

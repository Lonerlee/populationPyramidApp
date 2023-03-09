from populationData import *
from showData import *
import matplotlib.pyplot as plt
import tkinter as tk

pageCountry = 'WORLD'
window = tk.Tk()
title = tk.Label(text="Pick any country or region here:")
title.pack()
window.geometry( "600x300" )

clicked = tk.StringVar()
clicked.set( "WORLD" )
pageCountry = getCountryList()
drop = tk.OptionMenu( window , clicked , *pageCountry )
drop.pack()

labelTop = tk.Label( window , text = "Previous region basic information:" )
labelTop.pack()
label = tk.Label( window , text = "[NO DATA YET]" )
label.pack()
labelMale = tk.Label( window , text = "[NO DATA YET]" )
labelMale.pack()
labelFemale = tk.Label( window , text = "[NO DATA YET]" )
labelFemale.pack()

def show(): 
  plt.close('all')
  createDataVisuals = showData(pageCountry)
  pageCountry = clicked.get()
  createDataVisuals.calculations()
  label.config( text = 'Region name: ' + clicked.get() )
  labelMale.config( text = createDataVisuals.printMale() )
  labelFemale.config( text = createDataVisuals.printFemale() )
  createDataVisuals.start()

button = tk.Button( window , text = "Click To See Data" , command = show ).pack()
  
window.mainloop()

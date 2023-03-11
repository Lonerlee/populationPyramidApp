from populationData import *
from showData import *
import tkinter as tk

class windowGUI:
  def __init__(self):
    self.window = tk.Tk()
    self.title = tk.Label(text="Pick any country or region here:")
    self.clicked = tk.StringVar()
    self.countryList = getCountryList()
    self.drop = tk.OptionMenu( self.window , self.clicked , *self.countryList )

    self.labelTop = tk.Label( self.window , text = "Previous region basic information:" )
    self.label = tk.Label( self.window , text = "[NO DATA YET]" )
    self.labelMale = tk.Label( self.window , text = "[NO DATA YET]" )
    self.labelFemale = tk.Label( self.window , text = "[NO DATA YET]" )

    self.button = tk.Button( self.window , text = "Click To See Data" , command = self.show )

  def show(self): 
    selectedCountry = self.clicked.get()
    createDataVisuals = showData(selectedCountry, self.countryList)
    self.label.config( text = 'Region name: ' + self.clicked.get() )
    self.labelMale.config( text = createDataVisuals.printMale() )
    self.labelFemale.config( text = createDataVisuals.printFemale() )
    createDataVisuals.start()

  def createWindow(self):
    self.title.pack()
    self.window.geometry( "600x300" )

    self.clicked.set( "WORLD" )
    self.drop.pack()

    self.labelTop.pack()
    self.label.pack()
    self.labelMale.pack()
    self.labelFemale.pack()

    self.button.pack()
      
    self.window.mainloop()
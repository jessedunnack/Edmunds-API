### an interface to plot car data ###

from tkinter import *
from tkinter import ttk
import plot_price_vs_power
import os

class app():
    def __init__(self):
        self.root = Tk()
        self.root.title('Plot Edmunds.com Data')
        self.mainframe = Frame(self.root, height = 800, width = 1200)
        self.mainframe.pack_propagate(0)
        self.mainframe.pack(padx = 10, pady = 10)
        
        intro = Label(self.mainframe, text= 'Welcome to the Edmunds.com Data Plotter.\nPlease select an automaker to explore:')
        intro.pack(side=TOP)

        names = os.listdir('CarData')
        names = [(filename[:-5]).title() for filename in names]


        self.makevar = StringVar()
        self.make = ttk.Combobox(self.mainframe, textvariable = self.makevar, values=names)
        self.make.current()
        self.make.bind('<<ComboboxSelected>>', plot_price_vs_power.plotdata)
        self.make.pack()

app() 

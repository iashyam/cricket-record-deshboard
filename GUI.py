from tkinter import *
from tkinter import ttk
from clean_data import Data
import os
from helper import columns_to_show
class App:

    def __init__(self) -> None:

        self.format="Test"
        self.mode="Batting"
        self.filter = "Runs"

        self.data_path = os.path.join('data', self.mode, self.format+'.csv')

        #number of rows to display
        self.rows = 10

        self.window =  Tk()
        self.window.geometry("800x400")
        self.window.title("Records")
        self.createGUI()

        self.window.call("source", "themes/azure.tcl")
        self.window.call("set_theme", "light")

        self.data_path = os.path.join('data', self.format, self.mode+'.csv')

        self.window.mainloop()


    def createGUI(self):
        self.selectDataFrame = ttk.LabelFrame(self.window, text="Select Record")
        self.selectDataFrame.grid(row=0,column=0, padx=10, pady=15)
        
        self.radioButtons()

    
    def radioButtons(self):
        self.formatVar = StringVar()
        self.modeVar = StringVar()
        self.format_button = Radiobutton(self.selectDataFrame,variable=self.formatVar, 
                                       text="Test", value="Test", command=self.getRadio)
        self.format_button.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        self.format_button = Radiobutton(self.selectDataFrame,variable=self.formatVar, 
                                       text="ODI", value="ODI", command=self.getRadio)
        self.format_button.grid(row=0, column=1, padx=5, pady=10)

        self.format_button = Radiobutton(self.selectDataFrame,variable=self.formatVar, 
                                       text="T20I", value="T20I", command=self.getRadio)
        self.format_button.grid(row=0, column=2, padx=5, pady=10)


        self.mode_button = Radiobutton(self.selectDataFrame, variable=self.modeVar, text="Batting",
                                       value="Batting", command=self.getRadio)
        self.mode_button.grid(row=1,column=0, padx=5, pady=19)

        self.mode_button = Radiobutton(self.selectDataFrame, variable=self.modeVar, text="Bowling",
                                       value="Bowling", command=self.getRadio)
        self.mode_button.grid(row=1,column=2, padx=5, pady=19)

        self.mode_button = Radiobutton(self.selectDataFrame, variable=self.modeVar, text="Fielding",
                                       value="Fielding", command=self.getRadio)
        self.mode_button.grid(row=1,column=1, padx=5, pady=19)

        self.tabel_frame = Frame(self.window)
        self.tabel_frame.grid(row=0, column=1, padx=10, pady=10)

    def filterMenu(self, columns):

        self.filterVar = StringVar()

        self.filter_menu = OptionMenu(self.selectDataFrame,self.filterVar,*columns)
        self.filter_menu.config(width=16)
        self.filter_menu.grid(row=2, column=1, padx=20, pady=20)

        self.update_button = Button(self.selectDataFrame, text="Update", command=self.update)
        self.update_button.grid(row=2, column=2, padx=20, pady=20)

    def update(self):
        
        filter = self.filterVar.get()
        columns_to_show = ["Name", "Innings", filter]
        gata = self.data.sort_values(by=filter,axis=0, ascending=False)
        data = gata[columns_to_show]
        self.treeView(data)


    def getRadio(self):
        self.format = self.formatVar.get()
        self.mode = self.modeVar.get()

        self.data_path = os.path.join('data', self.mode, self.format+'.csv')
        self.data = self.loadData(self.data_path)

        self.filterMenu(self.data.columns[3:])
       

    def loadData(self, path):
        data_obj = Data(path)
        data_obj.clean()
        return data_obj.df

    def treeView(self, data):
        '''
        `data` is a pandas dataframe object
        '''
        # Clear the frame
        for widget in self.tabel_frame.winfo_children():
            widget.destroy()

        self.tree = ttk.Treeview(self.tabel_frame, columns=tuple(data.columns), show="headings")

        for column_name in data.columns:
            self.tree.heading(column_name, text=column_name)
            self.tree.column(column_name, width=100)

        for index in range(self.rows):
            self.tree.insert("", index=END, values=data.head(self.rows).iloc[index].to_list())

        self.tree.grid(row=0, column=1, padx=10, pady=10)
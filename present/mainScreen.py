from os import path
from tkinter import *
from tkinter.filedialog import askopenfilename
from domain import reader

class app:
    def __init__(self, master=None):
        self.defaultFont = ('Calibri','10')
        self.firstContainer = Frame(master)
        self.firstContainer['pady'] = 30
        self.firstContainer['padx'] = 70
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer['pady'] = 20
        self.secondContainer['padx'] = 70
        self.secondContainer.pack()


        self.thirdContainer = Frame(master)
        self.thirdContainer['pady'] = 20
        self.thirdContainer.pack()

        self.fourthContainer = Frame(master)
        self.fourthContainer['pady'] = 20
        self.fourthContainer.pack()
        
        self.title = Label(self.firstContainer, text = 'Importe a tabela para\n realizar a busca dos arquivos.')
        self.title['font'] = self.defaultFont
        self.title.pack()

        self.importedSheet = Label(self.secondContainer, text='', font=self.defaultFont)
        self.importedSheet.pack()

        self.importButton = Button(self.thirdContainer)
        self.importButton['text'] = 'Importar'
        self.importButton['font'] = self.defaultFont
        self.importButton['width'] = 12
        self.importButton['command'] = self.importSheet
        self.importButton.pack()    

        self.buscar = Button(self.fourthContainer)
        self.buscar['text'] = 'Buscar'
        self.buscar['font'] = self.defaultFont
        self.buscar['width'] = 12
        self.buscar['command'] = self.verify
        self.buscar.pack()

    def importSheet(self):
        path = askopenfilename()
        self.importedSheet['text'] = path

    def verify(self):
        path = self.importedSheet.cget('text')
        if path != '':
            print(path)
            #reader.read_excel(path)
        else:
            self.title['text'] = 'Favor informar nome do aquivo\n ou importar tabela.'

    



root = Tk()
root.title('Busca Arquivos')
app(root)
root.mainloop()
        
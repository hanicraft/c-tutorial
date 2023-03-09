from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
import tkinter.font
import re




class Py2C():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#323232')
            self.w1.geometry('440x530')
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg = '#323232')
            self.w1.place(x = 0, y = 0, width = 440, height = 530)
        self.pythoncode = Text(self.w1, bg = "#5e5e5e", fg = "#ffffff", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.pythoncode.place(x = 10, y = 20, width = 420, height = 210)
        self.label1 = Label(self.w1, text = "Enter Python Code Here", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label1.place(x = 10, y = 0, width = 130, height = 22)
        self.convert = Button(self.w1, text = "Convert To C Code", bg = "#313131", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.convert.place(x = 10, y = 240, width = 420, height = 42)
        self.convert['command'] = self.convertcode
        self.ccode = Text(self.w1, bg = "#5e5e5e", fg = "#ffffff", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.ccode.place(x = 10, y = 300, width = 420, height = 220)
        self.label2 = Label(self.w1, text = "Get Converted Python To C Code", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label2.place(x = 10, y = 280, width = 170, height = 22)

    def convertcode(self):
        python_code = self.pythoncode.get("1.0", "end")
        c_code = re.sub(r'print\(', 'printf(', python_code)
        c_code = re.sub(r'print \(', 'printf(', c_code)
        c_code = re.sub(r'def ', 'void ', c_code)
        c_code = re.sub(r':', '', c_code)
        c_code = re.sub(r'return', 'return ', c_code)
        c_code = re.sub(r'True', '1', c_code)
        c_code = re.sub(r'False', '0', c_code)
        c_code = re.sub(r'and', '&&', c_code)
        c_code = re.sub(r'or', '||', c_code)
        c_code = re.sub(r'not', '!', c_code)
        c_code = re.sub(r'    ', '\t', c_code)
        c_code = re.sub(r'\n\t', '\n{\n\t', c_code)
        c_code = re.sub(r'\n\n', '\n}\n\n', c_code)
        self.ccode.insert('1.0',c_code)



if __name__ == '__main__':
    a = Py2C(0)
    a.w1.mainloop()
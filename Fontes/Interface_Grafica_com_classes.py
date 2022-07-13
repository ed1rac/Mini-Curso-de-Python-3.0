from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.bt_sair = Button(frame, text='Sair', fg='red', command = self.quit)
        self.bt_sair.pack(side=LEFT)

        self.bt_hello = Button(frame, text='Olá', fg='black', command = self.hello)
        self.bt_hello.pack(side=LEFT)

    def quit(self):
        root.destroy()

    def hello(self):
        print('Olá Mundo, programação em Python é demais!')
    
        
root = Tk()
app = App(root)
root.mainloop()

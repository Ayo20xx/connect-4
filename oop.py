from tkinter import *

class Application(Frame):
    def __init__(self, master):
       super(Application,self).__init__(master)
       self.grid()
       self.create_widgets()


    def create_widgets(self):
      self.label1 = Label(self,text="first number")
      self.label1.grid(row=0,column=0,sticky=W)


      self.entry1 = Entry(self,width=10)
      self.entry1.grid(row=0, column=1)

      self.label2 = Label(self, text="second number")
      self.label2.grid(row=1, column=0, sticky=W)

      self.entry2 = Entry(self, width=10)
      self.entry2.grid(row=1, column=1)

      self.radioVar1 = StringVar()
      self.radio1 = Radiobutton(self, text="Add",variable=self.radioVar1, value ="Add")
      self.radio1.grid(row=2, column=0, sticky=W)
      self.radio1.select()

      self.radio2 = Radiobutton(self, text="Subtract", variable=self.radioVar1, value="Subtract")
      self.radio2.grid(row=2, column=1, sticky=W)

      self.radio3 = Radiobutton(self, text="Multiply", variable=self.radioVar1, value="Multiply")
      self.radio3.grid(row=2, column=3, sticky=W)

      self.radio4 = Radiobutton(self, text="Divide", variable=self.radioVar1, value="Divide")
      self.radio4.grid(row=2, column=4, sticky=W)

      self.label3 = Label(self, text="answer")
      self.label3.grid(row=3, column=0, sticky=W)

      self.entry3 = Entry(self, width=10)
      self.entry3.grid(row=3, column=1)

      self.button1 = Button(self , text ="Calculate", command=self.calculate)
      self.button1. grid (row=4, column=1)


    def calculate(self):
        operation = self.radioVar1.get()
        if (operation =="Add"):
            total = int(self.entry1.get()) + int(self.entry2.get())
            self.entry3.delete(0, END)
            self.entry3.insert(END, total)
        elif(operation =="Subtract"):
            minus = int(self.entry1.get()) - int(self.entry2.get())
            self.entry3.delete(0, END)
            self.entry3.insert(END, minus)
        elif (operation == "Multiply"):
            product = int(self.entry1.get()) * int(self.entry2.get())
            self.entry3.delete(0, END)
            self.entry3.insert(END, product)
        elif (operation == "Divide"):
            div = int(self.entry1.get()) / int(self.entry2.get())
            self.entry3.delete(0, END)
            self.entry3.insert(END, div)
window = Tk()
window.title("This is a test window")
window.geometry("400x300")
app = Application(window)
window.mainloop()

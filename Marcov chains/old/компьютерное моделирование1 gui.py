# recode as an embeddable class

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror,showinfo
from computer_modeling1 import Pj,myround

class SumGrid(Frame):
    def __init__(self, parent=None, numrow=5, numcol=5):
        f = Frame.__init__(self, parent)
        self.numrow = numrow                       # I am a frame container
        self.numcol = numcol                       # caller packs or grids me
        self.makeWidgets(numrow, numcol)           # else only usable one way

    def makeWidgets(self, numrow, numcol):
        self.rows = []

        self.grid_ = []
        for i in range(numrow):
            cols = []
            self.grid_.append([])
            for j in range(numcol):
                var = StringVar()
                ent = Entry(self, relief=RIDGE, textvariable=var)
                ent.grid(row=i+1, column=j, sticky=NSEW)
                ent.insert(END, '%d.%d' % (i, j))
                cols.append(ent)
                self.grid_[i].append(var)
            self.rows.append(cols)

        self.sums = []
        for i in range(numcol):
            lab = Label(self, text='?', relief=SUNKEN)
            #lab.grid(row=numrow+1, column=i, sticky=NSEW)
            lab.grid(row=i+1,column=numcol+1, sticky=NSEW)
            self.sums.append(lab)

        Button(self, text='Проверка',   command=self.onSum).grid(row=0, column=0)
        self.calc = Button(self, text='Вычислить', command=self.onPrint)
        self.calc.grid(row=0, column=1)
        Button(self, text='Очистить', command=self.onClear).grid(row=0, column=2)
        #Button(self, text='Загрузить',  command=self.onLoad).grid(row=0, column=3)
        Button(self, text='Выход',  command=lambda:root.destroy()).grid(row=0, column=4)
        #Button(self, text='По Умолчанию',  command=lambda:self.setter(list((a,b,c,d,e)))).grid(row=6, column=4)
        Button(self, text='По Умолчанию',  command=lambda:self.setter(list((a,b,c,d,e)))).grid(row=0, column=3)

    def report(self):
        return self.grid_

    def get(self):
        try:
            return [[float(x.get()) for x in elem] for elem in self.report()]
        except ValueError:
            return [[x.get() for x in elem] for elem in self.report()]
        int(1)

    def getSafe(self):
        try:
            return [[float(x.get()) for x in elem] for elem in self.report()]
        except ValueError:
            showerror('Ошибка',"Одно из полей заполнено не верно")
            return None

    def setter(self,table,Round=1):
        if not table:
            showerror('Ошибка',"Одно из полей заполнено не верно!")
            return
        #set = lambda x:round(x.set(),1)
        try:
            [[x.set(round(float(y),2)) for x,y in zip(rcell,lcell)] for rcell,lcell in zip(self.report(),table )]
        except ValueError:
            [[x.set(y) for x,y in zip(rcell,lcell)] for rcell,lcell in zip(self.report(),table )]
##            for rcell,lcell in zip(self.report(),table ):
##                for x,y in zip(rcell,lcell):
##                    x.set(y)
    def onPrint(self):
        for row in self.rows:
            for col in row:
                print(col.get(), end=' ')
            print()
        print()

    def onSum(self,vertical=0):
        if vertical:
            tots = [0] * self.numrow
            for i in range(self.numrow):
                for j in range(self.numcol):
                    tots[i] += eval(self.rows[j][i].get())        # sum current data
            for i in range(self.numrow):
                self.sums[i].config(text=str(tots[i]))
        else:
            matrix = self.getSafe()
            for x,i in zip(matrix,range(self.numcol)):
                self.sums[i].config(text=str( round(sum(x),2)    ))

    def onClear(self):
        for row in self.rows:
            for col in row:
                col.delete('0', END)                          # delete content
                col.insert(END, '0.0')                        # preserve display
        for sum in self.sums:
            sum.config(text='?')

    def onLoad(self):
        file = askopenfilename()
        if file:
            for row in self.rows:
                for col in row: col.grid_forget()             # erase current gui
            for sum in self.sums:
                sum.grid_forget()

            filelines   = open(file, 'r').readlines()         # load file data
            #self.numrow = len(filelines)                      # resize to data
            #self.numcol = len(filelines[0].split())
            #self.makeWidgets(self.numrow, self.numcol)
            tmp = []
            for (row, line) in enumerate(filelines):          # load into gui
                fields = line.split()
                [tmp.append(field+'22') for field in fields ]
            #self.setter(tmp)
##                for col in range(self.numcol):
##                    self.rows[row][col].delete('0', END)
##                    self.rows[row][col].insert(END, fields[col])

def getter(spisok):
    try:
        return [[float(x.get()) for x in elem] for elem in widget.report()]
    except ValueError:
        return [[x.get() for x in elem] for elem in widget.report()]

a = (0.4, 0.25, 0.2, 0.1, 0.05)
b = (0,	0.35,0.3,0.25,0.1)
c = (0,	0, 0.45 ,0.4 ,0.15)
d = (0 ,0 ,0 ,0.4 ,0.6)
e = (0 ,0 ,0 ,0 ,1)
if __name__ == '__main__':
    import sys
    root = Tk()
    root.title('Summer Grid')
    if len(sys.argv) != 3:


        widget = SumGrid(root, numrow=5, numcol=5) #Pj(5,3,list((a,b,c,d,e)) )
        widget.pack()    # .grid() works here too
        widget.setter(list((a,b,c,d,e) ))
        #[[x.set(y) for x,y in zip(rcell,lcell)] for rcell,lcell in zip(widget.report(),list((a,b,c,d,e) ) )]
        #print(list(getter(widget.report() )))
        widget.calc['command']=lambda:widget.setter(Pj(5,3,widget.get() ))

        print([[x.get() for x in elem] for elem in widget.report()])
    else:
        rows, cols = eval(sys.argv[1]), eval(sys.argv[2])
        SumGrid(root, rows, cols).pack()
        print(SumGrid.report())
    mainloop()

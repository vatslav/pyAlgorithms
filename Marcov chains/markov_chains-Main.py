# -*- coding: UTF-8 -*-
# recode as an embeddable class
print('asd')
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror,showinfo
from markov_chains_more import Pj,myround
from copy import deepcopy
def deepworker(obj, func):
    for x in obj:
        for y in x:
            y.func()

def deepworker2(obj, func):
    for x in obj:
        for y in x:
            y = y.func()

class SumGrid(Frame):
    def __init__(self, parent=None, numrow=5, numcol=5):
        f = Frame.__init__(self, parent)
        self.numrow = numrow                       # I am a frame container
        self.numcol = numcol                       # caller packs or grids me
        self.makeWidgets(numrow, numcol)           # else only usable one way

    def makeWidgets(self, numrow, numcol):
        ab = '''Автор: Вацлав Довнар
        Программа расчетывает вероятности нахождения стационарной марковской системы в заданных состояниях,
        если известна матрица переходных вероятностей.
        Входные параметры: число состояний N, значения переходных вероятностей.
        Программа умеет работать с командной строкой и текстывыми файлами (сепаратор - пробел и перевод каретки)'''
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
        #self.onPrint
        #lambda:self.setter(Pj(5,3,self.get() ))
        self.calc = Button(self, text='Вычислить', command=lambda:self.setter(Pj(5,3,self.get() ))  )
        self.calc.grid(row=0, column=1)
        Button(self, text='Очистить', command=self.onClear).grid(row=0, column=2)
        Button(self, text='Загрузить',  command=self.onLoad).grid(row=0, column=3)
        Button(self, text='Выход',  command=lambda:root.destroy()).grid(row=0, column=4)
        #Button(self, text='По Умолчанию',  command=lambda:self.setter(list((a,b,c,d,e)))).grid(row=6, column=4)
        Button(self, text='По Умолчанию',  command=lambda:self.setter(list((a,b,c,d,e)))).grid(row=0, column=4)
        Button(self, text='О программе',  command=lambda:showinfo("О Программе", ab)).grid(row=0, column=6)
        Button(self, text='Синтаксис КС',  command=lambda:showinfo("О Командной строке", errmsg)).grid(row=0, column=5)

    def report(self):
        return self.grid_

    def get(self):
        try:
            return [[float(x.get()) for x in elem] for elem in self.report()]
        except ValueError:
            return [[x.get() for x in elem] for elem in self.report()]


    def getSafe(self):
        try:
            return [[float(x.get()) for x in elem] for elem in self.report()]
        except ValueError:
            showerror('Ошибка',"Одно из полей заполнено не верно")
            return None

    def setter(self,table,Round=1):
        #завидывает таблицу в гуи
        if table==-1:return #если уже окно об ошибки было (не квадратная матрица)
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
        print(self.rows)
        for row in self.rows:
            for col in row:
                1/0#print(col.get(), end=' ')
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
            try:
                for x,i in zip(matrix,range(self.numcol)):
                    self.sums[i].config(text=str( round(sum(x),2)    ))
            except TypeError:pass # нужно это исправлять рефакторингом:)

    def onClear(self):
        for row in self.rows:
            for col in row:
                col.delete('0', END)                          # delete content
                col.insert(END, '0.0')                        # preserve display
        for sum in self.sums:
            sum.config(text='?')

    def onLoad(self,file=None,cl=None):
        #print(len(self.rows)
        #file=None
        if not file:file = askopenfilename()
        #file = 'C:/Users/Vatslav/Documents/GitHub/pyAlgorithms/Marlov chains/1.txt'
        #print('file=',file)
        if file:
##            for row in self.rows:
##                for col in row: col.grid_forget()             # erase current gui хз чо он тут делает
##            for sum in self.sums:
##                sum.grid_forget()
##
##            filelines   = open(file, 'r').readlines()         # load file data
##
##
##            ptr = 0
##            for (x,y) in zip(filelines,self.grid_):
##                del self.grid_[ptr][len(x.strip().split(' ')):len(y)]
##                ptr += 1
##                for (i,j) in zip(x.strip().split(' '),y):
##                    j.set(i)
            for row in self.rows:
                for col in row: col.grid_forget()             # erase current gui
            for sum in self.sums:
                sum.grid_forget()
            try:
                filelines   = open(file, 'r').readlines()         # load file data
            except IOError:
                if not cl:
                    showerror('Упс!..',"Файл не найден\n")
                    return
                else:
                    return -1


            self.numrow = len(filelines)                      # resize to data
            self.numcol = len(filelines[0].split())
            if self.numrow!=self.numcol:
                showerror('Ну как так можно?',"Давайте квадартную матрицу, а не всякое там...")
                return
            self.makeWidgets(self.numrow, self.numcol)


            for (row, line) in enumerate(filelines):          # load into gui
                fields = line.split()
                for col in range(self.numcol):
                    self.rows[row][col].delete('0', END)
                    self.rows[row][col].insert(END, fields[col])



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
    root.title('Марковские цепи v.2.0')
    errmsg = "Запуск без аргументов - по умолчанию\nЗапуск с 1 аргументов - путь к файлу с таблицей переходов\nЗапуск с 2 аргументами - количество строк и столбцов"


    #если не чего не дано или дан размер
    if len(sys.argv) == 1 or len(sys.argv)==3:
        l = len(sys.argv)
        if l==3:
            try:
                rows=int(sys.argv[1])
                cols=int(sys.argv[2])
            except (ValueError,TypeError):
                showerror('Ошибочка командной строки',errmsg)
                root.destroy()
                exit(1)
        else: #или задаем по умолчанию
            rows=5
            cols=5
        widget = SumGrid(root, numrow=rows, numcol=cols) #Pj(5,3,list((a,b,c,d,e)) )
        widget.pack()    # .grid() works here too
        if l==1: widget.setter(list((a,b,c,d,e) ))
        if l==3:widget.onClear()  #убогая заглука, где-то в конструкторе виджета  вызывается заполнение по умолчанию
                        ##[[x.set(y) for x,y in zip(rcell,lcell)] for rcell,lcell in zip(widget.report(),list((a,b,c,d,e) ) )]
                        ##print(list(getter(widget.report() )))
        #widget.calc['command']=lambda:widget.setter(Pj(5,3,widget.get() ))

        #print([[x.get() for x in elem] for elem in widget.report()])

    elif len(sys.argv)==2:
##        widget = SumGrid(root, numrow=5, numcol=5)
##        widget.pack()
        try:
            cols = int(sys.argv[1])
            widget = SumGrid(root, numrow=cols, numcol=cols)
            widget.pack()
        except ValueError:
            widget.onLoad(sys.argv[1])
        finally:
            widget.pack()

        #если дан адрес файла: выполнить то же что и при load_file и после запустить
        pass
    else: #на фоне унылое окно и это плохо, может убрать шапку и размер 0? или методм класса который сделает что надо?
        showerror('Ошибочка командной строки',errmsg)
        root.destroy()
    if len(sys.argv)<=3:
        root.mainloop()






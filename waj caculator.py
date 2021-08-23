
from tkinter import *


root= Tk()
root.title("Calculator")
x=Entry(root,width='40')
x.grid(column=0,row=0,columnspan=3,pady=30,padx=13)
button1=Button(root,text='1',padx=40,pady=25,command=lambda : X(1))
button2=Button(root,text='2',padx=40,pady=25,command=lambda: X(2))
button3=Button(root,text='3',padx=40,pady=25,command=lambda: X(3))
button4=Button(root,text='4',padx=40,pady=25,command=lambda: X(4))
button5=Button(root,text='5',padx=40,pady=25,command=lambda: X(5))
button6=Button(root,text='6',padx=40,pady=25,command=lambda: X(6))
button7=Button(root,text='7',padx=40,pady=25,command=lambda: X(7))
button8=Button(root,text='8',padx=40,pady=25,command=lambda: X(8))
button9=Button(root,text='9',padx=40,pady=25,command=lambda: X(9))
button0=Button(root,text='0',padx=40,pady=25,command=lambda: X(0))
button_add=Button(root,text='+',padx=40,pady=25,command=lambda : Op('+'),state=DISABLED)
button_equal=Button(root,text='=',padx=40,pady=25,command=lambda : result())
button_cleraall=Button(root,text='CLEAR',padx=120,pady=25,command=lambda : Clear())
button_multiply=Button(root,text='*',padx=40,pady=25,command=lambda : Op('*'),state=DISABLED)
button_sub=Button(root,text='-',padx=40,pady=25,command=lambda : Op('-'),state=DISABLED)
button_div=Button(root,text='/',padx=40,pady=25,command=lambda : Op('/'),state=DISABLED)


button1.grid(column=0,row=1)
button2.grid(column=1,row=1)
button3.grid(column=2,row=1)
button4.grid(column=0,row=2)
button5.grid(column=1,row=2)
button6.grid(column=2,row=2)
button7.grid(column=0,row=3)
button8.grid(column=1,row=3)
button9.grid(column=2,row=3)
button0.grid(column=0,row=4)
button_add.grid(column=1,row=4)
button_multiply.grid(column=0,row=5)
button_div.grid(column=1,row=5)
button_sub.grid(column=2,row=5)
button_equal.grid(column=2,row=4)
button_cleraall.grid(column=0,row=6,columnspan=3)



def X(n):
    x.insert(END,n)
    button_add["state"]="normal"
    button_sub["state"]="normal"
    button_div["state"]="normal"
    button_multiply["state"]="normal"
def Op(o):
    x.insert(END,o)
    button_add["state"]="disabled"
    button_sub["state"]="disabled"
    button_div["state"]="disabled"
    button_multiply["state"]="disabled"
def Clear():
    x.delete(0,END)
def result():
    total=0
    y = x.get()
    x.delete(0,END)
    x.insert(END,eval(y))



root.mainloop()

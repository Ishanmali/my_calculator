from tkinter import *

root = Tk()
root.title("calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation += value
    Label_result.config(text=equation)




def clear():
    global equation
    equation = ""
    Label_result.config(text=equation)

def cal():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    Label_result.config(text=result)

Label_result = Label(root, width=25, height=2, text="", font=("arial", 30))
Label_result.pack()

Button(root, width=5, height=1, text="/", font=("arial", 30, "bold"), bd=0, fg="#fff", bg="#2a2d36", command=lambda: show("/")).place(x=10, y=100)
Button(root, width=5, height=1, text="x", font=("arial", 30, "bold"), bd=0, fg="#fff", bg="#2a2d36", command=lambda: show("*")).place(x=150, y=100)
Button(root, width=5, height=1, text="%", font=("arial", 30, "bold"), bd=0, fg="#fff", bg="#2a2d36", command=lambda: show("%")).place(x=290, y=100)
Button(root, width=5, height=1, text="c", font=("arial", 30, "bold"), bd=0, fg="#fff", bg="#2a2d36", command=lambda: clear()).place(x=430, y=100)

Button(root,width=5,height=1,text="1",font=("arial",30,"bold"),bd=0,fg="#fff",bg="#2a2d36",command=lambda:show("1")).place(x=10,y=200)
Button(root,width=5,height=1,text="2",font=("arial",30,"bold"),bd=0,fg="#fff",bg="#2a2d36",command=lambda:show("2")).place(x=150,y=200)
Button(root,width=5,height=1,text="3",font=("arial",30,"bold"),bd=0,fg="#fff",bg="#2a2d36",command=lambda:show("3")).place(x=290,y=200)
Button(root,width=5,height=1,text="-",font=("arial",30,"bold"),bd=0,fg="#fff",bg="#2a2d36",command=lambda:show("-")).place(x=430,y=200)

Button(root,width=5,height=1,text="4",font=("arial",30,"bold"),bd=0,fg="#fff",bg="#2a2d36",command=lambda:show("4")).place(x=10,y=300)
Button(root,width=5,height=1,text="5",font=("arial",30,"bold"),bd=0,fg="#fff",bg="#2a2d36",command=lambda:show("5")).place(x=150,y=300)
Button(root,width=5,height=1,text="6",font=("arial",30,"bold"),bd=0,fg="#fff",bg="#2a2d36",command=lambda:show("6")).place(x=290,y=300)
Button(root,width=5,height=1,text="+",font=("arial",30,"bold"),bd=0,fg="#fff",bg="#2a2d36",command=lambda:show("+")).place(x=430,y=300)

Button(root,width=5,height=1,text="7",font=("arial",30,"bold"),bd=0,fg="#fff",bg="#2a2d36",command=lambda:show("7")).place(x=10,y=400)
Button(root,width=5,height=1,text="8",font=("arial",30,"bold"),bd=0,fg="#fff",bg="#2a2d36",command=lambda:show("8")).place(x=150,y=400)
Button(root,width=5,height=1,text="9",font=("arial",30,"bold"),bd=0,fg="#fff",bg="#2a2d36",command=lambda:show("9")).place(x=290,y=400)
Button(root,width=5,height=3,text="=",font=("arial",30,"bold"),bd=0,fg="#fff",bg="#fe9037",command=lambda:cal()).place(x=430,y=400)

Button(root,width=11,height=1,text="0",font=("arial",30,"bold"),bd=0,fg="#fff",bg="#2a2d36",command=lambda:show("0")).place(x=10,y=500)
Button(root,width=5,height=1,text=".",font=("arial",30,"bold"),bd=0,fg="#fff",bg="#2a2d36",command=lambda:show(".")).place(x=290,y=500)






root.mainloop()
root.mainloop()


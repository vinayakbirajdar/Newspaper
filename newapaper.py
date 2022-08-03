from tkinter import *

root=Tk()
def hello():
    label_3=Label(f4,text="The Deaths On Indian Roads,An India Today Infographic"
        "\nwo-wheelers are the"
        "\n most vulnerable on Indian roads -"
        "\n the video that went"
        "\nviral earlier in the week is not"
        "the only evidence.",fg="white",font=("comicsansms","30"),relief=GROOVE)
    label_3.pack()
def hell():
    label=Label(f2,text="\nAuto mobile price had""\nreached to the peek!",
                font=("comicsansms","30"),relief=GROOVE,fg="white",)
    label.pack()
def hel():
    label_1=Label(f3,text="HURRY !!! get your \nintersting dresses \nby just a"
                  "\nclick! vist myntra",fg="white",relief=GROOVE,font=("comicsansms","30"))
    label_1.pack()
root.geometry("1300x750")
root.minsize(700,550)
root.maxsize(1600,950)

root.title("Newspaper")

f1=Frame(root,borderwidth=4,relief="flat",bg="lightblue",)
f1.pack(fill="x",side="top",)
vb=Label(f1,text="HINDUSTAN NEWS"
         "\n DATE = 08/06/22",font=("comicsansms","40"),bg='red',
         fg='white',borderwidth=9,
         relief=RIDGE,)
vb.pack()
f2 = Frame(root,borderwidth=5,bg="gray",relief="flat",width=250)
f2.pack(fill="y",side="left")
b2=Button(f2,text="    TOP NEWS    ",bg="brown",fg="red",
           borderwidth=3,relief="groove"
           ,font=("comicsansms","30"),command=hell)
b2.pack()
f3=Frame(root,borderwidth=4,relief="groove",bg="gray",width=250)
f3.pack(fill="y",side="right")
b3=Button(f3,text = "ADVERTISEMENT'S",bg="brown",fg="red"
           ,borderwidth=3,relief="groove",font=("comicsansms","30"),
          command=hel)
b3.pack()
f4 = Frame(root,borderwidth=5,bg="red",relief="groove",width=600)
f4.pack(fill="y",side= TOP)
b1=Button(f4,text = "Azaj ki taza khabar!!!",bg="brown",fg="black"
           ,borderwidth=3,font=("comicsansms","40"),command=hello)
b1.pack()
root.mainloop()

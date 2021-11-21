
from tkinter import *
from tkinter import messagebox




def new_window():
    t=Toplevel()
    t.geometry("1250x650")
    t.resizable(0,0)
    t.configure(bg="lightgray")

    
    def show_data():

        txt.delete(0.0,END)
        
        un=uname.get()
        pa=passwd.get()
        chk=c.get()
        tn=tnam.get()
        dj=doj.get()
        cla=ca.get()
        seat=nob.get()
        sta=sf.get()
        tion=st.get()
        board=ba.get()
        reserv=ru.get()
        full=fname.get
        gender=var.get()
        age=ag.get()
        phn=no.get()
        address=e.get("1.0","end")
        che=ch.get()
        coice=[Lb.get(i) for i in Lb.curselection()]
        
        
        output=(">>>UserName is : "+un+"\n>>>Login password is : "
                +pa+"\n"+"\n>>>any medical practitioner is : "+
                chk+"\n"+"\n>>>TrainNo&Name is : "+tn+"\n>>>Date Of Journey is : "
                +dj+"\n>>>Class is : "+cla+"\n>>>No of Berth/Seat is : "+seat+
                "\n>>>Station From : "+sta+"\n>>>Station TO : "+tion+
                "\n>>>Boarding at : "+board+"\n>>>Reservation upto : "+reserv+
                "\n>>>Gender is : "+gender+"\n>>>Age : "+age+"\n>>>Enter a PhoneNO : "+phn+
                "\n>>>Enter a Address : "+address+"\n>>>Check if you are fill the form correct : "+che+
                "\n>>>Choice for premium trains : "+" ,".join(coice))
                
        txt.insert(0.0,output)
        

        messagebox.showinfo("Thank you ","your railway form has been sumbmited successfully")
    




    c=StringVar()
    Lb=StringVar()
    tnam=StringVar()
    doj=StringVar()
    ca=StringVar()
    nob=StringVar()
    sf=StringVar()
    st=StringVar()
    ba=StringVar()
    ru=StringVar()
    var=StringVar()
    ag=StringVar()
    no=StringVar()
    
    ch=StringVar()
    fname= StringVar()
    

    txt=Text(t,width=50,height=38,padx=10,pady=10,wrap="word",fg="Blue",font = ("Verdana",10))
    txt.place(x=820,y=10)
    b= Button(t, text= "SUBMIT",font=("bold",15),bg="lightgray",command=show_data).place(x=600,y=600)
    b= Button(t, text= "CANCEL",font=("bold",15),bg="lightgray",command=t.destroy).place(x=700,y=600)

    l = Label( t, text = "RAILWAY", font = ("Verdana", 20),bg="lightgray" ).place(x=350,y=0)

    l = Label( t, text = "Reservation / Concelltion Requirion Form", font = ("Verdana", 20),bg="lightgray" ).place(x=150,y=40)

    l = Label(t, text= "if you are a Medical practitioner please tick in Box", font=("bold",19),bg="lightgray").place(x=20,y=100)
    che = Checkbutton(t,bg="lightgray",variable=c,offvalue="no",onvalue="yes",font=("bold",9))
    che.place(x=780,y=140)
    l = Label(t, text= "(You could be of help in an emergency)", font=("bold",19),bg="lightgray").place(x=20,y=140)

    l = Label(t, text= "TrainNo&Name",font=("bold",15),bg="lightgray").place(x=20,y=200)
    e=Entry(t,width=35,textvariable=tnam).place(x=170,y=200)


    l = Label(t, text= "Date Of Journey",font=("bold",15),bg="lightgray").place(x=420,y=200)
    e=Entry(t,width=35,textvariable=doj).place(x=590,y=200)

    l = Label(t, text= "Class",font=("bold",15),bg="lightgray").place(x=20,y=230)
    e=Entry(t,width=35,textvariable=ca).place(x=170,y=230)

    l = Label(t, text= "No of Berth/Seat",font=("bold",15),bg="lightgray").place(x=420,y=230)
    e=Entry(t,width=35,textvariable=nob).place(x=590,y=230)

    l = Label(t, text= "Station From",font=("bold",15),bg="lightgray").place(x=20,y=260)
    e=Entry(t,width=35,textvariable=sf).place(x=170,y=260)

    l = Label(t, text= "Station TO",font=("bold",15),bg="lightgray").place(x=420,y=260)
    e=Entry(t,width=35,textvariable=st).place(x=590,y=260)

    l = Label(t, text= "Boarding at",font=("bold",15),bg="lightgray").place(x=20,y=290)
    e=Entry(t,width=35,textvariable=ba).place(x=170,y=290)

    l = Label(t, text= "Reservation upto",font=("bold",15),bg="lightgray").place(x=420,y=290)
    e=Entry(t,width=35,textvariable=ru).place(x=590,y=290)

    l= Label(t, text= "Enter a FullName",font=("bold",15),bg="lightgray").place(x=20,y=330)
    e=Entry(t,width=35,textvariable=fname).place(x=200,y=330)

    l = Label(t, text= "Gender",font=("bold",15),bg="lightgray").place(x=20,y=360)
    r = Radiobutton(t, text= "Male", value="Male",font=("bold",17),variable=var,bg="lightgray").place(x=200,y=360 )
    r = Radiobutton(t, text= "Female", value="Female",font=("bold",17),variable=var,bg="lightgray").place(x=290,y=360 )

    l = Label(t, text= "Age",font=("bold",15),bg="lightgray").place(x=20,y=400)
    e=Entry(t,width=35,textvariable=ag).place(x=200,y=400)

    l = Label(t, text= "Enter a PhoneNO",font=("bold",15),bg="lightgray").place(x=20,y=430)
    e=Entry(t,width=35,textvariable=no).place(x=200,y=430)

    l= Label(t, text= "Enter a Address ",font=("bold",15),bg="lightgray").place(x=20,y=460)
    e=Text(t,width=27,height=6,wrap="word")
    e.place(x=200,y=460)

    che = Checkbutton(t,bg="lightgray",variable=ch,offvalue="no",onvalue="yes")
    che.place(x=50,y=590)
    l= Label(t, text= "Check if you are fill the form correct ",font=("bold",15),bg="lightgray").place(x=100,y=590)

    l = Label(t, text= " Choice for premium trains ",font=("bold",15),bg="lightgray").place(x=480,y=330)

    Lb = Listbox(t,selectmode='multiple', background="white", fg="black",selectbackground="blue",highlightcolor="Red",font=("bold",13),)#textvariable=)
    Lb.place(x=520,y=360)
    Lb.index(0)
    Lb.insert(0, 'Coffee')
    Lb.insert(1, "Black Tea")
    Lb.insert(2, "upma vada")
    Lb.insert(3, "Idli vada")
    Lb.insert(4, "Gulabjamun")
    Lb.insert(5, "chicken manchurian")
    Lb.insert(6, "Butter chicken")
    Lb.insert(8, "Dal Makhani")
    Lb.insert(9, "veg manchurian")
    Lb.insert(10, "sabji puri")





t=Tk()

t.title("IRCTC")
uname=StringVar()
passwd=StringVar()

t.geometry("400x200")

t.configure(bg="lightgray")


l=Label(t,text = "UserName",font=("bold",15),bg="lightgray").place(x=20,y=20)
l= Entry(t,width=25,textvariable=uname).place(x=150,y=20)



l= Label(t,text = "Password",font=("bold",15),bg="lightgray").place(x=20,y=80)
l= Entry(t,width=25, show ="*" ,textvariable=passwd,).place(x=150,y=80)

BU=Button(t,text = "Log in",font=("bold",15),bg="lightgray",command=new_window).place(x=120,y=150)
BU=Button(t,text = "Cancel",font=("bold",15),bg="lightgray",command=t.destroy).place(x=190,y=150)



t.mainloop()

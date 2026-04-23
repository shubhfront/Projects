# Project on Airport Management System

import mysql.connector as M
import tkinter
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
import PIL
from PIL import ImageTk, Image
import time
from datetime import date
import datetime
import random
import pyttsx3
import speech_recognition  as sr
import pywhatkit

global c,cur
c = M.connect(host = 'localhost', user = 'root', password = 'Shubham@123', database = 'Airline_Management')
cur = c.cursor()

pass

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 160)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    global liste
    b = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        b.pause_threshold = 1
        audio = b.listen(source,timeout=2,phrase_time_limit=5)
    try:
        print("Recognizing....")
        liste = 2
        query = b.recognize_google(audio,language='en-in')
        print(f"user said:{query}")
    except Exception as e:
        liste = 3
        speak('Say that again please')
        return 'None'
    return query    

def login():
    username = user.get()
    password = code.get()
    cur.execute('select * from login where user  = "{}" and password = "{}"'.format(username,password))
    cur.fetchall()
    rows = cur.rowcount
    while True:
        if rows!=1:
            speak('invalid username or password')            
            messagebox.showerror('invalid','invalid username or password')
            break
        else:
            speak('login succesful')
            global sm,liste
            log.destroy()
            sm = Tk()
            sm.title('Category')
            sm.geometry('700x400+150+150')
            sm.config(bg = 'white')
            a = tkinter.Label(sm,text = 'Welcome To Global India Airline Booking',fg = '#57a1f8',bg = 'white',font = ('calibiri',23,'bold'))
            a.place(x = 50,y = 30)
            frame = tkinter.Frame(sm, width = 350,height = 350,bg = 'white')
            frame.place(x = 50,y = 70)
            heading = tkinter.Label(frame,text = 'Select Your Category',bg = 'white',font = ('calibiri',15))
            heading.place(x = 10,y = 40)
            cat = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
            cat.place(x = 30,y = 105)
            cat.insert(0,'1. ')
            per = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
            per.place(x = 30,y = 160)
            per.insert(0,'2. ')
            button1 = tkinter.Button(frame,width = 10,text = 'Customer',border = 0,bg = 'white',cursor = 'hand2',command = cust,activeforeground = 'blue',font = ('calibiri',15)) 
            button1.place(x = 50,y = 100)
            button2 = tkinter.Button(frame,width = 6,text = 'Staff',border = 0,bg = 'white',cursor = 'hand2',command = staff,activeforeground = 'blue',font = ('calibiri',15))
            button2.place(x = 50,y = 155)
            b = tkinter.Label(sm,text = '* Select whether you are a customer or a staff member',bg = 'white',font = ('calibiri',10,'bold'))
            b.place(x = 20,y = 350)
            curr_time = time.strftime("%H:%M", time.localtime())
            c=curr_time
            tml=tkinter.Button(sm,text=c, width=10, command=wishme)
            tml.place(x=630,y=350)
            sm.mainloop()
            sm.destroy()
            speak('Are you a customer or a staff member')            
            ln = Tk()
            global lstr
            ln.title('Listening') 
            ln.geometry('200x200+300+200')
            ln.config(bg = 'white')
            lst = tkinter.Label(ln,text='Listening...',fg = '#57a1f8',bg = 'white',font = ('calibiri',25,'bold'))
            lst.place(x=20,y=70)
            lstr = takecommand()
            ln.mainloop()
            ln.destroy()
            liste = 2
            sm = Tk()
            sm.title('Category')
            sm.geometry('700x400+150+150')
            sm.config(bg = 'white')
            a = tkinter.Label(sm,text = 'Welcome To Global India Airline Booking',fg = '#57a1f8',bg = 'white',font = ('calibiri',23,'bold'))
            a.place(x = 50,y = 30)
            frame = tkinter.Frame(sm, width = 350,height = 350,bg = 'white')
            frame.place(x = 50,y = 70)
            heading = tkinter.Label(frame,text = 'Select Your Category',bg = 'white',font = ('calibiri',15))
            heading.place(x = 10,y = 40)
            cat = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
            cat.place(x = 30,y = 105)
            cat.insert(0,'1. ')
            per = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
            per.place(x = 30,y = 160)
            per.insert(0,'2. ')
            button1 = tkinter.Button(frame,width = 10,text = 'Customer',border = 0,bg = 'white',cursor = 'hand2',command = cust,activeforeground = 'blue',font = ('calibiri',15)) 
            button1.place(x = 50,y = 100)
            button2 = tkinter.Button(frame,width = 6,text = 'Staff',border = 0,bg = 'white',cursor = 'hand2',command = staff,activeforeground = 'blue',font = ('calibiri',15))
            button2.place(x = 50,y = 155)
            b = tkinter.Label(sm,text = '* Select whether you are a customer or a staff member',bg = 'white',font = ('calibiri',10,'bold'))
            b.place(x = 20,y = 350)
            curr_time = time.strftime("%H:%M", time.localtime())
            c=curr_time
            tml=tkinter.Button(sm,text=c, width=10, command=wishme)
            tml.place(x=630,y=350)
            sm.mainloop()
            break

def pra():
    speak('You Have To Login Manually First')
def ex():
    cus.destroy()

def ba():
    cus.destroy()

def wishme():
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak(f"Good Morning Sir !  It's {curr_time} ")
    elif hour>=12 and hour <18:
        speak(f"Good Afternoon Sir ! It's {curr_time}")
    else:
        speak(f"Good Evenning Sir !  It's {curr_time}")

def cust():
    global cus
    sm.destroy()
    cus = Tk()
    cus.title('main Menu')
    cus.geometry('700x500+150+100')
    a = tkinter.Label(cus,text = 'Main Menu      ',width = 37,fg = '#57a1f8',bg = 'white',font = ('calibiri',25,'bold'))
    a.place(x = 0,y = 11)
    frame = tkinter.Frame(cus, width = 700,height = 500,bg = 'white')
    frame.place(x = 0,y = 70)
    heading = tkinter.Label(frame,text = 'Select Your Choice',bg = 'white',font = ('calibiri',25))
    heading.place(x = 10,y = 40)
    cat = tkinter.Entry(frame,width = 5,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
    cat.place(x = 30,y = 105)
    cat.insert(0,'1. ')
    per = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
    per.place(x = 30,y = 160)
    per.insert(0,'2. ')
    mm = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
    mm.place(x = 30,y = 215)
    mm.insert(0,'3. ')
    men = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
    men.place(x = 30,y = 270)
    men.insert(0,'4. ')
    button1 = tkinter.Button(frame,width = 7,text = 'Booking',border = 0,bg = 'white',cursor = 'hand2',activeforeground = 'blue',command = form,font = ('calibiri',15)) 
    button1.place(x = 50,y = 100)
    button2 = tkinter.Button(frame,width = 8,text = 'Boarding',border = 0,bg = 'white',cursor = 'hand2',activeforeground = 'blue',command = chb,font = ('calibiri',15))
    button2.place(x = 50,y = 210)
    button3 = tkinter.Button(frame,width = 6,text = 'Check',border = 0,bg = 'white',cursor = 'hand2',activeforeground = 'blue',command = chbi,font = ('calibiri',15))
    button3.place(x = 50,y = 155)
    button4 = tkinter.Button(frame,width = 7,text = 'Enquiry',border = 0,bg = 'white',cursor = 'hand2',activeforeground = 'blue',command = staff,font = ('calibiri',15))
    button4.place(x = 50,y = 265)
    d = '_'*90
    c = tkinter.Label(cus,text = d,bg = 'white',font = ('calibiri',10,'bold'))
    c.place(x = 20,y = 380)
    b = tkinter.Label(cus,text = '* Select the operation you want to perform',bg = 'white',font = ('calibiri',10,'bold'))
    b.place(x = 20,y = 400)
    button5 = tkinter.Button(cus, text = 'exit',width = 7,pady = 7,bg = '#D3D3D3', font = ('calibiri', 10), command = ex)
    button5.place(x = 10,y = 450)
    button6 = tkinter.Button(cus, text = 'Back',width = 10,pady = 7,bg = '#D3D3D3', font = ('calibiri', 10), command = ba)
    button6.place(x = 600,y = 450)
    cus.mainloop()

def staff():
    global stf
    sm.destroy()
    stf = Tk()
    stf.title('main Menu')
    stf.geometry('700x500+150+100')
    a = tkinter.Label(stf,text = 'Main Menu      ',width = 37,fg = '#57a1f8',bg = 'white',font = ('calibiri',25,'bold'))
    a.place(x = 0,y = 11)
    frame = tkinter.Frame(stf, width = 700,height = 500,bg = 'white')
    frame.place(x = 0,y = 70)
    heading = tkinter.Label(frame,text = 'Select Your Choice',bg = 'white',font = ('calibiri',25))
    heading.place(x = 10,y = 40)
    cat = tkinter.Entry(frame,width = 5,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
    cat.place(x = 30,y = 105)
    cat.insert(0,'1. ')
    per = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
    per.place(x = 30,y = 160)
    per.insert(0,'2. ')
    mm = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
    mm.place(x = 30,y = 215)
    mm.insert(0,'3. ')
    men = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
    men.place(x = 30,y = 270)
    men.insert(0,'4. ')
    button1 = tkinter.Button(frame,width = 20,text = 'Modify Flight Detail',border = 0,bg = 'white',cursor = 'hand2',activeforeground = 'blue',command = fdi,font = ('calibiri',15)) 
    button1.place(x = 50,y = 100)
    button2 = tkinter.Button(frame,width = 17,text = 'Add new Flight',border = 0,bg = 'white',cursor = 'hand2',activeforeground = 'blue',command = addn,font = ('calibiri',15))
    button2.place(x = 50,y = 210)
    button3 = tkinter.Button(frame,width = 20,text = 'Print Boarding Pass',border = 0,bg = 'white',cursor = 'hand2',activeforeground = 'blue',command = cm,font = ('calibiri',15))
    button3.place(x = 50,y = 155)
    button4 = tkinter.Button(frame,width = 23,text = 'Find Customer Details',border = 0,bg = 'white',cursor = 'hand2',activeforeground = 'blue',command = detl,font = ('calibiri',15))
    button4.place(x = 50,y = 265)
    d = '_'*90
    c = tkinter.Label(stf,text = d,bg = 'white',font = ('calibiri',10,'bold'))
    c.place(x = 20,y = 380)
    b = tkinter.Label(stf,text = '* Select the operation you want to perform',bg = 'white',font = ('calibiri',10,'bold'))
    b.place(x = 20,y = 400)
    button5 = tkinter.Button(stf, text = 'exit',width = 7,pady = 7,bg = '#D3D3D3', font = ('calibiri', 10), command = exit5)
    button5.place(x = 10,y = 450)
    button6 = tkinter.Button(stf, text = 'Back',width = 10,pady = 7,bg = '#D3D3D3', font = ('calibiri', 10), command = cm)
    button6.place(x = 600,y = 450)
    stf.mainloop()   

def exit5():
    stf.destroy()

def cm():
    print('ok')

def on_entersu(e):
    users.delete(0,'end')

def on_leavesu(e):
    nameu = users.get()
    if nameu == "":
        users.insert(0,'username')

def on_entersp(e):
    codes.delete(0,'end')

def on_leavesp(e):
    namep = codes.get()
    if namep == "":
        codes.insert(0,'password')

def signin():   
    username = users.get()
    password = codes.get()
    query = """INSERT INTO login (user, password) 
               VALUES (%s, %s)"""
    data = (username,password)
    cur.execute(query, data)
    c.commit()
    sin.destroy()

def back():
    sin.destroy()
    run()

def runs():
    global users,codes,sin
    log.destroy()
    sin = Tk()
    sin.title('Signin')
    sin.geometry('400x300+300+200')
    sin.configure(bg = '#fff')
    sin.resizable(False,False)
    frame = tkinter.Frame(sin, width = 350,height = 350,bg = 'white')
    frame.place(x = 10,y = 20)
    heading = tkinter.Label(frame,text = 'Sign In',fg = '#57a1f8',bg = 'white',font = ('calibiri',23,'bold'))
    heading.place(x = 100,y = 5)
    users = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',11))
    users.place(x = 30,y = 80)
    users.insert(0,'username')
    users.bind('<FocusIn>',on_entersu)
    users.bind('<FocusOut>',on_leavesu)
    tkinter.Frame(frame,width = 295,height = 2,bg = 'black').place(x = 25,y = 107)
    codes = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',11))
    codes.place(x = 30,y = 150)
    codes.insert(0,'password')
    codes.bind('<FocusIn>',on_entersp)
    codes.bind('<FocusOut>',on_leavesp) 
    tkinter.Frame(frame,width = 295,height = 2,bg = 'black').place(x = 25,y = 177)
    tkinter.Button(frame,width = 39,pady = 7 ,text = 'sign in', bg = '#57a1f8',fg = 'white',border = 0,command = signin).place(x = 35,y = 204)
    sin.mainloop()

def run():
    global user, code,log
    log = Tk()
    log.title('Login')
    log.geometry('700x350+150+200')
    log.configure(bg = '#fff')
    log.resizable(False,False)
    img = PhotoImage(file = 'login.png')
    tkinter.Label(log, image = img, bg = 'white').place(x = 50,y = 50)
    frame = tkinter.Frame(log, width = 350,height = 350,bg = 'white')
    frame.place(x = 308,y = 20)
    heading = tkinter.Label(frame,text = 'Login',fg = '#57a1f8',bg = 'white',font = ('calibiri',23,'bold'))
    heading.place(x = 100,y = 5)
    user = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',11))
    user.place(x = 30,y = 80)
    user.insert(0,'username')
    user.bind('<FocusIn>',on_enteru)
    user.bind('<FocusOut>',on_leaveu)
    tkinter.Frame(frame,width = 295,height = 2,bg = 'black').place(x = 25,y = 107)
    code = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',11))
    code.place(x = 30,y = 150)
    code.insert(0,'password')
    code.bind('<FocusIn>',on_enterp)
    code.bind('<FocusOut>',on_leavep)
    tkinter.Frame(frame,width = 295,height = 2,bg = 'black').place(x = 25,y = 177)
    tkinter.Button(frame,width = 39,pady = 7,text = 'sign in', bg = '#57a1f8',fg = 'white',border = 0,command = login).place(x = 35,y = 204)
    label = tkinter.Label(frame, text = 'Dont have an account?', fg = 'black',bg = 'white', font = ('calibiri',9))
    label.place(x = 75,y = 270)
    sign_up = tkinter.Button(frame,width = 6,text = 'Sign in',border = 0,bg = 'white',cursor = 'hand2',fg = '#57a1f8',command = runs)
    sign_up.place(x = 215,y = 270)
    if vs==1:
        a='First You have to login manually'
        speak(a)
    log.mainloop()

def on_enteru(e):
    user.delete(0,'end')

def on_leaveu(e):
    name = user.get()
    if name == "":
        user.insert(0,'username')

def on_enterp(e):
    code.delete(0,'end')

def on_leavep(e):
    global name
    name = code.get()
    if name == "":
        code.insert(0,'password')
        print(name)

def thing():
    global a
    master.destroy()
    a='thank You and Have a Nice day'
    print(a)
    speak(a)

def cont():
    global vs
    vs=0
    master.destroy()
    print('yes')
    run()

def vas():
    global vs
    vs=1
    master.destroy()
    run()

def sta():
    global master
    master = Tk()
    master.title('Global india')
    image_0 = Image.open('airr.jpg')
    bck = ImageTk.PhotoImage(image_0)
    master.geometry("800x300+100+200")
    lbl = tkinter.Label(master, image = bck)
    lbl.place(x = 0,y = 0)
    a = "Welcome to Global India Airline Booking System"
    lbl2 = tkinter.Label(master, text = a,fg = '#57a1f8',bg = 'white',font = ('calibiri',23,'bold'))
    lbl2.pack()
    button1 = tkinter.Button(master, text = 'exit',width = 7,pady = 7, font = ('calibiri', 10), command = thing)
    button1.place(x = 10,y = 250)
    button2 = tkinter.Button(master, text = 'Continue',width = 10,pady = 7, font = ('calibiri', 10), command = cont)
    button2.place(x = 700,y = 250)
    button2 = tkinter.Button(master, text = 'Voice Assistance',width = 20,pady = 7, font = ('calibiri', 10), command = vas)
    button2.place(x = 350,y = 250)
    speak('Welcome To Global India Airline Booking System')
    master.mainloop()


def cust_login():
    c_id = input('enter your customer id:- ')
    pas = input('enter your password:- ')
    cur.execute('select * from cust_login where user  = "{}" and password = "{}"'.format(c_id,pas))
    cur.fetchall()
    rows = cur.rowcount
    while True:
        if rows!= 1:
            print('invalid login details.....Try Again')
            break
        else:
             print('login successful........')
             c = input("Press 'c' to continue........")
             break

def tbld():
    dme.destroy()
    today = date.today()
    query = """INSERT INTO cust_det (firstname, lastname, flight_id, company, Dep_from, Arr_to, Dep, bookid, bdate) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    data = (firstname, lastname, Fid, air, fro, too, depa, pi, today)
    cur.execute(query, data)
    c.commit()
    mes()

def exit2():
    pay.destroy()
    msg.destroy()

def mes():
    global msg
    msg = Tk()
    msg.geometry('400x400+300+200')
    msg.title('Message')
    lbl = tkinter.Label(msg,text = 'Booked',fg = '#57a1f8',bg = 'white',width = 18,font = ('calibiri',27,'bold'))
    lbl.place(x = 0,y = 0)
    frame = tkinter.Frame(msg, width = 400,height = 350,bg = 'white')
    frame.place(x = 0,y = 50)
    heading1 = tkinter.Label(frame,text = 'Your Ticket is booked',bg = 'white',font = ('calibiri',15))
    heading1.place(x = 20,y = 40)
    heading2 = tkinter.Label(frame,text = 'What you want to do',bg = 'white',font = ('calibiri',15))
    heading2.place(x = 20,y = 80)
    heading3 = tkinter.Label(frame,text = 'The ticket is confirmed ',bg = 'white',font = ('calibiri',15))
    heading3.place(x = 20,y = 120)
    heading4 = tkinter.Label(frame,text = 'But need details check',bg = 'white',font = ('calibiri',15))
    heading4.place(x = 20,y = 160)
    button1 = tkinter.Button(msg, text = 'exit',width = 7,pady = 7, font = ('calibiri', 10), command = exit2)
    button1.place(x = 10,y = 330)
    button2 = tkinter.Button(msg, text = 'Continue',width = 10,pady = 7, font = ('calibiri', 10),command = fer)
    button2.place(x = 300,y = 330)
    heading5 = tkinter.Label(frame,text = 'You will not lose ticket after exiting',bg = 'white',font = ('calibiri',15))
    heading5.place(x = 20,y = 200)    
    msg.mainloop()

def fer():
    msg.destroy()
    chn()

def fwd():
    cbk.destroy()
    chn()

def on_entera(e):
    adh.delete(0,'end')

def on_leavea(e):
    name = adh.get()
    if name == "":
        adh.insert(0,'Aadhar Number')

def on_entern(e):
    pan.delete(0,'end')

def on_leaven(e):
    global name
    name = pan.get()
    if name == "":
        pan.insert(0,'PAN Number')
        
def on_enterm(e):
    mail.delete(0,'end')

def on_leavem(e):
    global name
    name = mail.get()
    if name == "":
        mail.insert(0,'Email id')
        
def vfr():
    print('ok')

def chn():
    global adh,pan,mail,ckh 
    ckh = Tk()
    ckh.title('Check')
    ckh.geometry('700x350+150+200')
    ckh.configure(bg = '#fff')
    ckh.resizable(False,False)
    aadh = tkinter.Label(ckh,text = 'Aadhar Number :',fg = 'black',bg = 'white',font = ('calibiri',18,'bold'))
    aadh.place(x = 50,y = 105)
    paan = tkinter.Label(ckh,text = 'PAN Number :',fg = 'black',bg = 'white',font = ('calibiri',18,'bold'))
    paan.place(x = 50,y = 170)
    mal = tkinter.Label(ckh,text = 'Email ID :',fg = 'black',bg = 'white',font = ('calibiri',18,'bold'))
    mal.place(x = 50,y = 230)
    frame = tkinter.Frame(ckh, width = 350,height = 350,bg = 'white')
    frame.place(x = 308,y = 20)
    heading = tkinter.Label(frame,text = 'Details',fg = '#57a1f8',bg = 'white',font = ('calibiri',23,'bold'))
    heading.place(x = 20,y = 5)
    adh = tkinter.Entry(frame,width = 25,fg = 'silver',border = 0,bg = 'white',font = ('calibiri',11))
    adh.place(x = 30,y = 80)
    adh.insert(0,'XXXX XXXX XXXX')
    adh.bind('<FocusIn>',on_entera)
    adh.bind('<FocusOut>',on_leavea)
    tkinter.Frame(frame,width = 295,height = 2,bg = 'black').place(x = 25,y = 107)
    pan = tkinter.Entry(frame,width = 25,fg = 'silver',border = 0,bg = 'white',font = ('calibiri',11))
    pan.place(x = 30,y = 150)
    pan.insert(0,'AMPPDXXXXX')
    pan.bind('<FocusIn>',on_entern)
    pan.bind('<FocusOut>',on_leaven)
    tkinter.Frame(frame,width = 295,height = 2,bg = 'black').place(x = 25,y = 177)
    mail = tkinter.Entry(frame,width = 25,fg = 'silver',border = 0,bg = 'white',font = ('calibiri',11))
    mail.place(x = 30,y = 220)
    mail.insert(0,'name@address.com')
    mail.bind('<FocusIn>',on_enterm)
    mail.bind('<FocusOut>',on_leavem)
    tkinter.Frame(frame,width = 300,height = 2,bg = 'black').place(x = 25,y = 247)
    tkinter.Button(frame,width = 39,pady = 7,text = 'Verify', bg = '#57a1f8',fg = 'white',border = 0,command = detchk).place(x = 35,y = 274)
    ckh.mainloop()

def detchk():
    global adhr,panc,mlid
    adhr = adh.get()
    panc = pan.get()
    mlid = mail.get()
    while True:        
        if len(adhr)!= 14:
            tkinter.messagebox.showwarning(title = "Error", message = "Invalid Aadhar number")
            break
        elif panc.startswith('AMPPD') == False:
            tkinter.messagebox.showwarning(title = "Error", message = "Invalid PAN number")
            break                                             
        elif len(panc)!= 10:
            tkinter.messagebox.showwarning(title = "Error", message = "Invalid PAN number")
            break
        elif mlid.endswith('.com') == False:
            tkinter.messagebox.showwarning(title = "Error", message = "Invalid Email ID")
            break
        else:
            vrfr()
            break
   
def on_enterb(e):
    adb.delete(0,'end')

def on_leaveb(e):
    name = adb.get()
    if name == "":
        adb.insert(0,'Book ID')

def on_entero(e):
    ado.delete(0,'end')

def on_leaveo(e):
    name = ado.get()
    if name == "":
        ado.insert(0,'Book ID')

def on_enterf(e):
    udt.delete(0,'end')

def on_leavef(e):
    name = udt.get()
    if name == "":
        udt.insert(0,'Flight ID')

def on_enterd(e):
    add.delete(0,'end')

def on_leaved(e):
    name = add.get()
    if name == "":
        add.insert(0,'Book ID')

def check():
    bid = adb.get()
    cur.execute('select * from cust_det where bookid  = "{}"'.format(bid))
    a = cur.fetchall()
    rows = cur.rowcount
    if rows == 0:
        tkinter.messagebox.showwarning(title = "Error", message = "Invalid Booking ID")
    else:
        global cbk,fi,dep,pi
        for i in a:
            fn,ln = i[0],i[1]
            fi,co = i[2],i[3]
            fr,to = i[4],i[5]
            dep,dt = i[6],i[8]
            nm = fn+' '+ln
            pi = i[7]
            break
        cbk = Tk()
        cbk.title('Book Detail')
        cbk.geometry('400x400+300+200')
        cbk.configure(bg = '#fff')
        a = tkinter.Label(cbk,text = 'Booking Details',width = 20,fg = '#57a1f8',bg = 'white',font = ('calibiri',25,'bold'))
        a.place(x = 0,y = 10)
        frame = tkinter.Frame(cbk, width = 700,height = 400,bg = 'white')
        frame.place(x = 0,y = 50)
        lbl1 = tkinter.Label(frame, text = 'Name : '+nm, bg = 'white', font = ('calibiri', 10))
        lbl1.place(x = 30, y = 50)
        lbl2 = tkinter.Label(frame, text = 'Flight : '+fi, bg = 'white', font = ('calibiri', 10))
        lbl2.place(x = 30, y = 100)
        lbl3 = tkinter.Label(frame, text = 'Company : '+co, bg = 'white', font = ('calibiri', 10))
        lbl3.place(x = 30, y = 150)
        lbl4 = tkinter.Label(frame, text = 'From : '+fr, bg = 'white', font = ('calibiri', 10))
        lbl4.place(x = 30, y = 200)
        lbl5 = tkinter.Label(frame, text = 'To : '+to, bg = 'white', font = ('calibiri', 10))
        lbl5.place(x = 220, y = 50)
        lbl6 = tkinter.Label(frame, text = 'Dep : '+dep, bg = 'white', font = ('calibiri', 10))
        lbl6.place(x = 220, y = 100)
        lbl7 = tkinter.Label(frame, text = 'Book ID : '+bid, bg = 'white', font = ('calibiri', 10))
        lbl7.place(x = 220, y = 150)
        but = tkinter.Button(cbk,width = 40,pady = 7,text = 'Agree', bg = 'silver',fg = 'white',border = 1,command = fwd)
        but.place(x = 40,y = 320)
        cbi.destroy()
        cbk.mainloop()
        
def exit3():
    vfr.destroy()

def cok():
    print('ok')

def sat():
    global st
    st = seat.get()
    query = """Update cust_det set seat = %s where bookid = %s """
    data = (st,pi)
    cur.execute(query, data)
    c.commit()
    vfr.destroy()
    berd()

def vrfr():
    ckh.destroy()
    global seat,tkt,vfr
    vfr = Tk()
    vfr.title('Succesful')
    vfr.geometry('500x400+300+200')
    vfr.config(bg = 'white')
    lbl = tkinter.Label(vfr,text = 'Verified',fg = '#57a1f8',bg = 'white',width = 18,font = ('calibiri',27,'bold'))
    lbl.place(x = 0,y = 0)
    frame = tkinter.Frame(vfr, width = 400,height = 350,bg = 'white')
    frame.place(x = 0,y = 50)
    heading1 = tkinter.Label(frame,text = 'Your Details Verified successfully',bg = 'white',font = ('calibiri',15))
    heading1.place(x = 20,y = 40)
    heading2 = tkinter.Label(frame,text = 'Select Seat',bg = 'white',font = ('calibiri',15))
    heading2.place(x = 20,y = 80)
    heading3 = tkinter.Label(frame,text = 'No. of tickets ',bg = 'white',font = ('calibiri',15))
    heading3.place(x = 20,y = 120)    
    button1 = tkinter.Button(vfr, text = 'exit',width = 7,pady = 7, font = ('calibiri', 10), command = exit3)
    button1.place(x = 10,y = 330)
    button2 = tkinter.Button(vfr, text = 'Continue',width = 10,pady = 7, font = ('calibiri', 10),command = sat)
    button2.place(x = 400,y = 330)
    heading5 = tkinter.Label(frame,text = 'Proceed to Print Boarding pass',bg = 'white',font = ('calibiri',15))
    heading5.place(x = 20,y = 200)
    tkt = tkinter.Spinbox(frame, from_ = 1, to = 10)
    tkt.place(x = 200, y = 120)
    seat = ttk.Combobox(frame, values = ['Window','Corner','Center'])    
    seat.place(x = 200,y = 80)    
    vfr.mainloop()

def fdi():
    global ffi,udt
    ffi = Tk()
    ffi.title('Check')
    ffi.geometry('300x300+350+200')
    ffi.configure(bg = '#fff')
    a = tkinter.Label(ffi,text = 'Modify Flight',width = 15,fg = '#57a1f8',bg = 'white',font = ('calibiri',25,'bold'))
    a.place(x = 0,y = 11)
    aado = tkinter.Label(ffi,text = 'Flight id',fg = 'black',bg = 'white',font = ('calibiri',12,'bold'))
    aado.place(x = 40,y = 105)
    udt = tkinter.Entry(ffi,width = 10,fg = 'black',border = 2,font = ('calibiri',11))
    udt.place(x = 170,y = 105)
    udt.insert(0,'Flight id')
    udt.bind('<FocusIn>',on_enterf)
    udt.bind('<FocusOut>',on_leavef)
    tkinter.Button(ffi,width = 32,pady = 7,text = 'Enter', bg = '#57a1f8',fg = 'white',border = 0,command = bdi).place(x = 35,y = 224)
    ffi.mainloop()

def bdi():
    fdi = udt.get()
    v = "select * from flights where flight_id = %s"
    cur.execute(v, (fdi,))
    b = cur.fetchall()
    row = cur.rowcount
    if row == 0:
        messagebox.showerror('Invalid','Invalid Flight ID')
    else:
        for i in b :
            global Fid
            Fid = i[0]
            break
        mfd()

def chb():
    global cbo,ado
    cbo = Tk()
    cbo.title('Check')
    cbo.geometry('300x300+350+200')
    cbo.configure(bg = '#fff')
    a = tkinter.Label(cbo,text = 'Booking Check',width = 15,fg = '#57a1f8',bg = 'white',font = ('calibiri',25,'bold'))
    a.place(x = 0,y = 11)
    aado = tkinter.Label(cbo,text = 'Booking ID :',fg = 'black',bg = 'white',font = ('calibiri',12,'bold'))
    aado.place(x = 40,y = 105)
    ado = tkinter.Entry(cbo,width = 10,fg = 'black',border = 2,font = ('calibiri',11))
    ado.place(x = 170,y = 105)
    ado.insert(0,'GPXXXXX')
    ado.bind('<FocusIn>',on_entero)
    ado.bind('<FocusOut>',on_leaveo)
    tkinter.Button(cbo,width = 32,pady = 7,text = 'Enter', bg = '#57a1f8',fg = 'white',border = 0,command = bchk).place(x = 35,y = 224)
    cbo.mainloop()

def mfd():
    ffi.destroy()
    global seat,tkt,mfy
    global cmpy,name,From,too,dep,fre,tt
    mfy = Tk()
    mfy.title('Succesful')
    mfy.geometry('500x400+300+200')
    mfy.config(bg = 'white')
    lbl = tkinter.Label(mfy,text = 'Modify Flight Details',fg = '#57a1f8',bg = 'white',width = 18,font = ('calibiri',27,'bold'))
    lbl.place(x = 0,y = 0)
    frame = tkinter.Frame(mfy, width = 400,height = 350,bg = 'white')
    frame.place(x = 0,y = 40)
    heading1 = tkinter.Label(frame,text = 'Flight ID',bg = 'white',font = ('calibiri',12))
    heading1.place(x = 50,y = 40)
    heading2 = tkinter.Label(frame,text = 'Company ',bg = 'white',font = ('calibiri',12))
    heading2.place(x = 50,y = 70)
    heading3 = tkinter.Label(frame,text = 'Name',bg = 'white',font = ('calibiri',12))
    heading3.place(x = 50,y = 100)
    heading4 = tkinter.Label(frame,text = 'From',bg = 'white',font = ('calibiri',12))
    heading4.place(x = 50,y = 130)
    heading5 = tkinter.Label(frame,text = 'To',bg = 'white',font = ('calibiri',12))
    heading5.place(x = 50,y = 160)
    heading6 = tkinter.Label(frame,text = 'Departure',bg = 'white',font = ('calibiri',12))
    heading6.place(x = 50,y = 190)
    heading7 = tkinter.Label(frame,text = 'Time Taken',bg = 'white',font = ('calibiri',12))
    heading7.place(x = 50,y = 220)
    heading8 = tkinter.Label(frame,text = 'Basic',bg = 'white',font = ('calibiri',12))
    heading8.place(x = 50,y = 250)
    heading9 = tkinter.Label(frame,text = Fid ,bg = 'white',font = ('calibiri',12))
    heading9.place(x = 200,y = 40)
    button1 = tkinter.Button(mfy, text = 'exit',width = 7,pady = 7, font = ('calibiri', 10),command = exit6)
    button1.place(x = 10,y = 340)
    button2 = tkinter.Button(mfy, text = 'Continue',width = 10,pady = 7, font = ('calibiri', 10),command = mfdt)
    button2.place(x = 400,y = 340)
    cmpy = tkinter.Entry(frame,border = 2,bg = 'light blue')
    name = tkinter.Entry(frame,borde = 2,bg = 'light blue')
    From = tkinter.Entry(frame,border = 2,bg = 'light blue')
    too = tkinter.Entry(frame,border = 2,bg = 'light blue')
    dep = tkinter.Entry(frame,border = 2,bg = 'light blue')
    tt = tkinter.Entry(frame,border = 2,bg = 'light blue')
    fre = tkinter.Entry(frame,border = 2,bg = 'light blue')
    cmpy.place(x = 200,y = 70)
    name.place(x = 200,y = 100)
    From.place(x = 200,y = 130)
    too.place(x = 200,y = 160)
    dep.place(x = 200,y = 190)
    tt.place(x = 200,y = 220)
    fre.place(x = 200,y = 250)
    mfy.mainloop()

def exit6():
    mfy.destroy()

def mfdt():
    company = cmpy.get()
    nme = name.get()
    Frm = From.get()
    to = too.get()
    dept = dep.get()
    timet = tt.get()
    basc = fre.get()
    query = """Update flights set company = %s,name = %s,Dept_from = %s, Arr_to = %s,Dep_time = %s,time_taken = %s,fare = %s where flight_id = %s """
    data = (company,nme,Frm,to,dept,timet,basc,Fid)
    cur.execute(query, data)
    c.commit()
    mfy.destroy()
    messagebox.showinfo("Successful","Data Modified Successfully")

def bchk():
    bid = ado.get()
    cur.execute('select * from cust_det where bookid  = "{}"'.format(bid))
    a = cur.fetchall()
    rows = cur.rowcount
    if rows == 0:
        tkinter.messagebox.showwarning(title = "Error", message = "Invalid Booking ID")
    else:
        global cbb
        global nm,fi,fr,to,dep,dt,sm,pi
        for i in a:
            fn,ln = i[0],i[1]
            fi,co = i[2],i[3]
            fr,to = i[4],i[5]
            dep,dt = i[6],i[8]
            sm,pi = i[9],i[7]
            nm = fn+' '+ln
            break
        cbb = Tk()
        cbb.title('Book Detail')
        cbb.geometry('400x400+300+200')
        cbb.configure(bg = '#fff')
        a = tkinter.Label(cbb,text = 'Booking Details',width = 20,fg = '#57a1f8',bg = 'white',font = ('calibiri',25,'bold'))
        a.place(x = 0,y = 10)
        frame = tkinter.Frame(cbb, width = 700,height = 400,bg = 'white')
        frame.place(x = 0,y = 50)
        lbl1 = tkinter.Label(frame, text = 'Name : '+nm, bg = 'white', font = ('calibiri', 10))
        lbl1.place(x = 30, y = 50)
        lbl2 = tkinter.Label(frame, text = 'Flight : '+fi, bg = 'white', font = ('calibiri', 10))
        lbl2.place(x = 30, y = 100)
        lbl3 = tkinter.Label(frame, text = 'Company : '+co, bg = 'white', font = ('calibiri', 10))
        lbl3.place(x = 30, y = 150)
        lbl4 = tkinter.Label(frame, text = 'From : '+fr, bg = 'white', font = ('calibiri', 10))
        lbl4.place(x = 30, y = 200)
        lbl5 = tkinter.Label(frame, text = 'To : '+to, bg = 'white', font = ('calibiri', 10))
        lbl5.place(x = 220, y = 50)
        lbl6 = tkinter.Label(frame, text = 'Dep : '+dep, bg = 'white', font = ('calibiri', 10))
        lbl6.place(x = 220, y = 100)
        lbl7 = tkinter.Label(frame, text = 'Book ID : '+bid, bg = 'white', font = ('calibiri', 10))
        lbl7.place(x = 220, y = 150)
        lbl8 = tkinter.Label(frame, text = 'Seat : '+sm, bg = 'white', font = ('calibiri', 10))
        lbl8.place(x = 220, y = 200)
        but = tkinter.Button(cbb,width = 40,pady = 7,text = 'Agree', bg = 'silver',fg = 'white',border = 1,command = board)
        but.place(x = 40,y = 320)
        cbo.destroy()
        cbb.mainloop()

def addn():
    global seat,tkt,add
    global Fi,cmpy,name,From,too,dep,fre,tt
    add = Tk()
    add.title('Succesful')
    add.geometry('500x400+300+200')
    add.config(bg = 'white')
    lbl = tkinter.Label(add,text = 'Add New Flight',fg = '#57a1f8',bg = 'white',width = 18,font = ('calibiri',27,'bold'))
    lbl.place(x = 0,y = 0)
    frame = tkinter.Frame(add, width = 400,height = 350,bg = 'white')
    frame.place(x = 0,y = 40)
    heading1 = tkinter.Label(frame,text = 'Flight ID',bg = 'white',font = ('calibiri',12))
    heading1.place(x = 50,y = 40)
    heading2 = tkinter.Label(frame,text = 'Company ',bg = 'white',font = ('calibiri',12))
    heading2.place(x = 50,y = 70)
    heading3 = tkinter.Label(frame,text = 'Name',bg = 'white',font = ('calibiri',12))
    heading3.place(x = 50,y = 100)
    heading4 = tkinter.Label(frame,text = 'From',bg = 'white',font = ('calibiri',12))
    heading4.place(x = 50,y = 130)
    heading5 = tkinter.Label(frame,text = 'To',bg = 'white',font = ('calibiri',12))
    heading5.place(x = 50,y = 160)
    heading6 = tkinter.Label(frame,text = 'Departure',bg = 'white',font = ('calibiri',12))
    heading6.place(x = 50,y = 190)
    heading7 = tkinter.Label(frame,text = 'Time Taken',bg = 'white',font = ('calibiri',12))
    heading7.place(x = 50,y = 220)
    heading8 = tkinter.Label(frame,text = 'Basic',bg = 'white',font = ('calibiri',12))
    heading8.place(x = 50,y = 250)
    button1 = tkinter.Button(add, text = 'exit',width = 7,pady = 7, font = ('calibiri', 10),command = exit7)
    button1.place(x = 10,y = 340)
    button2 = tkinter.Button(add, text = 'Continue',width = 10,pady = 7, font = ('calibiri', 10),command = addt)
    button2.place(x = 400,y = 340)
    cmpy = tkinter.Entry(frame,border = 2,bg = 'light blue')
    name = tkinter.Entry(frame,borde = 2,bg = 'light blue')
    From = tkinter.Entry(frame,border = 2,bg = 'light blue')
    too = tkinter.Entry(frame,border = 2,bg = 'light blue')
    dep = tkinter.Entry(frame,border = 2,bg = 'light blue')
    tt = tkinter.Entry(frame,border = 2,bg = 'light blue')
    fre = tkinter.Entry(frame,border = 2,bg = 'light blue')
    Fi = tkinter.Entry(frame,border = 2,bg = 'light blue')
    cmpy.place(x = 200,y = 70)
    name.place(x = 200,y = 100)
    From.place(x = 200,y = 130)
    too.place(x = 200,y = 160)
    dep.place(x = 200,y = 190)
    tt.place(x = 200,y = 220)
    fre.place(x = 200,y = 250)
    Fi.place(x = 200,y = 40)
    add.mainloop()

def exit7():
    add.destroy()

def addt():
    flig = Fi.get()
    company = cmpy.get()
    nme = name.get()
    Frm = From.get()
    to = too.get()
    dept = dep.get()
    timet = tt.get()
    basc = fre.get()
    basic = int(basc)
    query = """INSERT INTO flights (flight_id,company,name,Dept_from, Arr_to,Dep_time,time_taken,fare) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    data = (flig,company,nme,Frm,to,dept,timet,basic)
    cur.execute(query,data)
    c.commit()
    add.destroy()
    messagebox.showinfo("Successful","Data Added Successfully")

def exit4():
    bor.destroy()

def detl():
    global cbd,add
    cbd = Tk()
    cbd.title('Check')
    cbd.geometry('300x300+350+200')
    cbd.configure(bg = '#fff')
    a = tkinter.Label(cbd,text = 'Booking Check',width = 15,fg = '#57a1f8',bg = 'white',font = ('calibiri',25,'bold'))
    a.place(x = 0,y = 11)
    aadd = tkinter.Label(cbd,text = 'Booking ID :',fg = 'black',bg = 'white',font = ('calibiri',12,'bold'))
    aadd.place(x = 40,y = 105)
    add = tkinter.Entry(cbd,width = 10,fg = 'black',border = 2,font = ('calibiri',11))
    add.place(x = 170,y = 105)
    add.insert(0,'GPXXXXX')
    add.bind('<FocusIn>',on_enterd)
    add.bind('<FocusOut>',on_leaved)
    tkinter.Button(cbd,width = 32,pady = 7,text = 'Enter', bg = '#57a1f8',fg = 'white',border = 0,command = detfnd).place(x = 35,y = 224)
    cbd.mainloop()

def detfnd():
    global cbf
    bbi = add.get()
    cur.execute('select * from cust_det where bookid  = "{}"'.format(bbi))
    a = cur.fetchall()
    rows = cur.rowcount
    if rows == 0:
        tkinter.messagebox.showwarning(title = "Error", message = "Invalid Booking ID")
    else:
        global cbf
        global nm,fi,fr,to,dep,dt,sm,pi
        for i in a:
            fn,ln = i[0],i[1]
            fi,co = i[2],i[3]
            fr,to = i[4],i[5]
            dep,dt = i[6],i[8]
            sm,pi = i[9],i[7]
            nm = fn+' '+ln
            break
        cbf = Tk()
        cbf.title('Customer Detail')
        cbf.geometry('400x400+300+200')
        cbf.configure(bg = '#fff')
        a = tkinter.Label(cbf,text = 'Customer Details',width = 20,fg = '#57a1f8',bg = 'white',font = ('calibiri',25,'bold'))
        a.place(x = 0,y = 10)
        frame = tkinter.Frame(cbf, width = 700,height = 400,bg = 'white')
        frame.place(x = 0,y = 50)
        lbl1 = tkinter.Label(frame, text = 'Name : '+nm, bg = 'white', font = ('calibiri', 10))
        lbl1.place(x = 30, y = 50)
        lbl2 = tkinter.Label(frame, text = 'Flight : '+fi, bg = 'white', font = ('calibiri', 10))
        lbl2.place(x = 30, y = 100)
        lbl3 = tkinter.Label(frame, text = 'Company : '+co, bg = 'white', font = ('calibiri', 10))
        lbl3.place(x = 30, y = 150)
        lbl4 = tkinter.Label(frame, text = 'From : '+fr, bg = 'white', font = ('calibiri', 10))
        lbl4.place(x = 30, y = 200)
        lbl5 = tkinter.Label(frame, text = 'To : '+to, bg = 'white', font = ('calibiri', 10))
        lbl5.place(x = 220, y = 50)
        lbl6 = tkinter.Label(frame, text = 'Dep : '+dep, bg = 'white', font = ('calibiri', 10))
        lbl6.place(x = 220, y = 100)
        lbl7 = tkinter.Label(frame, text = 'Book ID : '+bbi, bg = 'white', font = ('calibiri', 10))
        lbl7.place(x = 220, y = 150)
        lbl8 = tkinter.Label(frame, text = 'Date : ', bg = 'white', font = ('calibiri', 10))
        lbl8.place(x = 220, y = 200)
        lbl9 = tkinter.Label(frame, text = dt, bg = 'white', font = ('calibiri', 10))
        lbl9.place(x = 260, y = 200)
        cbd.destroy()
        cbf.mainloop()

def board():
    global bor,bk
    tod = date.today()
    bor = Tk()
    bor.title('board Details')
    bor.geometry('600x260+150+200')
    image = Image.open('bpp.jpg')
    bk = ImageTk.PhotoImage(image)   
    img = ImageTk.PhotoImage(Image.open('bpp.jpg'))
    label = tkinter.Label(bor, image = img)
    label.pack()
    lbl2 = tkinter.Label(bor, text = nm, bg = 'white' ,font = ('calibiri',10))
    lbl2.place(x = 160,y = 70)
    lbl3 = tkinter.Label(bor, text = fr, bg = 'white' ,font = ('calibiri',10))
    lbl3.place(x = 160,y = 105)
    lbl10 = tkinter.Label(bor, text = to, bg = 'white' ,font = ('calibiri',10))
    lbl10.place(x = 250,y = 105)
    lbl4 = tkinter.Label(bor, text = fi, bg = 'white' ,font = ('calibiri',10  ))
    lbl4.place(x = 160,y = 140)
    lbl11 = tkinter.Label(bor, text = tod, bg = 'white' ,font = ('calibiri',8))
    lbl11.place(x = 248,y = 141)
    lbl12 = tkinter.Label(bor, text = sm, bg = 'white' ,font = ('calibiri',10))
    lbl12.place(x = 349,y = 140)
    lbl5 = tkinter.Label(bor, text = 'G1', bg = 'white' ,font = ('calibiri',10))
    lbl5.place(x = 160,y = 175)
    lbl13 = tkinter.Label(bor, text = dep, bg = 'white' ,font = ('calibiri',10))
    lbl13.place(x = 302,y = 175)
    lbl6 = tkinter.Label(bor, text = nm, bg = 'white' ,font = ('calibiri',10))
    lbl6.place(x = 475,y = 63)
    lbl7 = tkinter.Label(bor, text = fr, bg = 'white' ,font = ('calibiri',10))
    lbl7.place(x = 475,y = 92)
    lbl8 = tkinter.Label(bor, text = to, bg = 'white' ,font = ('calibiri',10))
    lbl8.place(x = 475,y = 125)
    lbl9 = tkinter.Label(bor, text = tod, bg = 'white' ,font = ('calibiri',8))
    lbl9.place(x = 435,y = 168)
    lbl14 = tkinter.Label(bor, text = dep, bg = 'white' ,font = ('calibiri',8))
    lbl14.place(x = 492,y = 168)
    lbl15 = tkinter.Label(bor, text = fi, bg = 'white' ,font = ('calibiri',8))
    lbl15.place(x = 530,y = 168)
    lbl16 = tkinter.Label(bor, text = sm, bg = 'white' ,font = ('calibiri',8))
    lbl16.place(x = 440,y = 197)
    lbl17 = tkinter.Label(bor, text = 'G1', bg = 'white' ,font = ('calibiri',8))
    lbl17.place(x = 490,y = 197)
    button1 = tkinter.Button(bor, text = 'Exit',width = 13,height = 1, font = ('calibiri', 10), command = exit4)
    button1.place(x = 10,y = 230)
    button2 = tkinter.Button(bor, text = 'Continue',width = 13,height = 1, font = ('calibiri', 10))
    button2.place(x = 490,y = 230)
    bor.mainloop()

def berd():
    #vfr.destroy()
    global bor
    nm = firstname+' '+lastname
    tod = date.today()
    bor = Tk()
    bor.title('board Details')
    bor.geometry('600x260+150+200')
    image = Image.open('bpp.jpg')
    bk = ImageTk.PhotoImage(image)   
    img = ImageTk.PhotoImage(Image.open('bpp.jpg'))
    label = tkinter.Label(bor, image = img)
    label.pack()
    lbl2 = tkinter.Label(bor, text = nm, bg = 'white' ,font = ('calibiri',10))
    lbl2.place(x = 160,y = 70)
    lbl3 = tkinter.Label(bor, text = fro, bg = 'white' ,font = ('calibiri',10))
    lbl3.place(x = 160,y = 105)
    lbl10 = tkinter.Label(bor, text = too, bg = 'white' ,font = ('calibiri',10))
    lbl10.place(x = 250,y = 105)
    lbl4 = tkinter.Label(bor, text = Fid, bg = 'white' ,font = ('calibiri',10))
    lbl4.place(x = 160,y = 140)
    lbl11 = tkinter.Label(bor, text = tod, bg = 'white' ,font = ('calibiri',8))
    lbl11.place(x = 248,y = 141)
    lbl12 = tkinter.Label(bor, text = st, bg = 'white' ,font = ('calibiri',10))
    lbl12.place(x = 349,y = 140)
    lbl5 = tkinter.Label(bor, text = 'G1', bg = 'white' ,font = ('calibiri',10))
    lbl5.place(x = 160,y = 175)
    lbl13 = tkinter.Label(bor, text = depa, bg = 'white' ,font = ('calibiri',10))
    lbl13.place(x = 302,y = 175)
    lbl6 = tkinter.Label(bor, text = nm, bg = 'white' ,font = ('calibiri',10))
    lbl6.place(x = 475,y = 63)
    lbl7 = tkinter.Label(bor, text = fro, bg = 'white' ,font = ('calibiri',10))
    lbl7.place(x = 475,y = 92)
    lbl8 = tkinter.Label(bor, text = too, bg = 'white' ,font = ('calibiri',10))
    lbl8.place(x = 475,y = 125)
    lbl9 = tkinter.Label(bor, text = tod, bg = 'white' ,font = ('calibiri',8))
    lbl9.place(x = 435,y = 168)
    lbl14 = tkinter.Label(bor, text = depa, bg = 'white' ,font = ('calibiri',8))
    lbl14.place(x = 492,y = 168)
    lbl15 = tkinter.Label(bor, text = Fid, bg = 'white' ,font = ('calibiri',8))
    lbl15.place(x = 530,y = 168)
    lbl16 = tkinter.Label(bor, text = st, bg = 'white' ,font = ('calibiri',8))
    lbl16.place(x = 440,y = 197)
    lbl17 = tkinter.Label(bor, text = 'G1', bg = 'white' ,font = ('calibiri',8))
    lbl17.place(x = 490,y = 197)
    button1 = tkinter.Button(bor, text = 'Exit',width = 13,height = 1, font = ('calibiri', 10), command = exit4)
    button1.place(x = 10,y = 230)
    button2 = tkinter.Button(bor, text = 'Continue',width = 13,height = 1, font = ('calibiri', 10))
    button2.place(x = 490,y = 230)
    bor.mainloop()

def chbi():
    cus.destroy()
    global cbi,adb
    cbi = Tk()
    cbi.title('Check')
    cbi.geometry('300x300+350+200')
    cbi.configure(bg = '#fff')
    a = tkinter.Label(cbi,text = 'Booking Check',width = 15,fg = '#57a1f8',bg = 'white',font = ('calibiri',25,'bold'))
    a.place(x = 0,y = 11)
    aadb = tkinter.Label(cbi,text = 'Booking ID :',fg = 'black',bg = 'white',font = ('calibiri',12,'bold'))
    aadb.place(x = 40,y = 105)
    adb = tkinter.Entry(cbi,width = 10,fg = 'black',border = 2,font = ('calibiri',11))
    adb.place(x = 170,y = 105)
    adb.insert(0,'GPXXXXX')
    adb.bind('<FocusIn>',on_enterb)
    adb.bind('<FocusOut>',on_leaveb)
    tkinter.Button(cbi,width = 32,pady = 7,text = 'Enter', bg = '#57a1f8',fg = 'white',border = 0,command = check).place(x = 35,y = 224)
    cbi.mainloop()
   
def enter():
    global firstname, lastname, From, to, nationality
    global category
    global day
    if accept_var.get():
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        if not firstname or not lastname:
            tkinter.messagebox.showwarning(title = "Error", message = "First name and last name are required.")
            return
        From = From_combobox.get()
        to = to_combobox.get()
        nationality = nationality_combobox.get()
        category = category_combobox.get()
        day = day_combobox.get()
    else:
        tkinter.messagebox.showwarning(title = "Error", message = "You have not accepted the terms.")

def form():
    global window
    cus.destroy()
    #print('Enter the data in the data entry form')
    global first_name_entry, From_combobox, nationality_combobox
    global last_name_entry, to_combobox, reg_status_var
    global day_combobox, category_combobox, accept_var
    window = Tk()
    window.geometry('600x400+150+200')
    frame = tkinter.Frame(window)
    frame.pack()
    user_info_frame  = tkinter.LabelFrame(frame, text = "User Information")
    user_info_frame.grid(row =  0, column = 0, padx = 20, pady = 10)
    first_name_label = tkinter.Label(user_info_frame, text = "First Name")
    first_name_label.grid(row = 0, column = 0)
    last_name_label = tkinter.Label(user_info_frame, text = "Last Name")
    last_name_label.grid(row = 0, column = 1)
    first_name_entry = tkinter.Entry(user_info_frame)
    last_name_entry = tkinter.Entry(user_info_frame)
    first_name_entry.grid(row = 1, column = 0)
    last_name_entry.grid(row = 1, column = 1)
    From_label = tkinter.Label(user_info_frame, text = "From")
    From_combobox = ttk.Combobox(user_info_frame, values = ["DEL", "MUM", "KOL","AMR","CHN","HDW","PUN","VIZ","GOA","HYD"])
    From_label.grid(row = 0, column = 2)
    From_combobox.grid(row = 1, column = 2)
    to_label = tkinter.Label(user_info_frame, text = "To")
    to_combobox = ttk.Combobox(user_info_frame, values = ["DEL", "MUM", "KOL","AMR","CHN","JAI","PUN","VIZ","GOA","HYD",'LKW','A&N','AHM','BEN','BHO','IND','J&K','AND','KER'])
    to_label.grid(row = 2, column = 0)
    to_combobox.grid(row = 3, column = 0)
    nationality_label = tkinter.Label(user_info_frame, text = "Nationality")
    nationality_combobox = ttk.Combobox(user_info_frame, values = ["Africa", "Australia", "Asia","Bharat", "Europe", "North America", "Oceania", "South America"])
    nationality_label.grid(row = 2, column = 1)
    nationality_combobox.grid(row = 3, column = 1)
    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx = 10, pady = 5)
    courses_frame = tkinter.LabelFrame(frame)
    courses_frame.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 10)
    registered_label = tkinter.Label(courses_frame, text = "Registration Status")
    reg_status_var = tkinter.StringVar(value = "Not Registered")
    registered_check = tkinter.Checkbutton(courses_frame, text = "Currently Registered",
                                           variable = reg_status_var, onvalue = "Registered", offvalue = "Not registered")
    registered_label.grid(row = 0, column = 0)
    registered_check.grid(row = 1, column = 0)
    category_label = tkinter.Label(courses_frame, text =  "# Category")
    category_combobox = ttk.Combobox(courses_frame, values = ['Domestic','International'])
    category_label.grid(row = 0, column = 1)
    category_combobox.grid(row = 1, column = 1)
    day_label = tkinter.Label(courses_frame, text = "# Day")
    day_combobox = ttk.Combobox(courses_frame, values = ['Daily','Weekend','Special'])
    day_label.grid(row = 0, column = 2)
    day_combobox.grid(row = 1, column = 2)
    for widget in courses_frame.winfo_children():
        widget.grid_configure(padx = 10, pady = 5)
    terms_frame = tkinter.LabelFrame(frame, text = "Terms & Conditions")
    terms_frame.grid(row = 2, column = 0, sticky = "news", padx = 20, pady = 10)    
    accept_var = tkinter.BooleanVar(window)    
    terms_check = tkinter.Checkbutton(window, text = "I accept the terms and conditions.", variable = accept_var)
    terms_check.pack(pady = 10)    
    submit_button = tkinter.Button(window, text = "Enter Data", command = enter)
    submit_button.place(x = 300,y = 330)   
    button2 = tkinter.Button(window, text = 'Continue',pady = 7, font = ('calibiri', 10), command = book)
    button2.place(x = 400,y = 330)
    window.mainloop()

def dne():
    global dme,pi,today,pay
    pay.destroy()
    today = date.today()
    a = random.randint(10000,19999)
    bh = str(a)
    pi = 'GP'+bh
    dme = Tk()
    dme.geometry('400x425+200+150')
    dme.title('Payment')
    image = Image.open('ptmm.png')
    bk = ImageTk.PhotoImage(image)   
    img = ImageTk.PhotoImage(Image.open('ptmm.png'))
    label = tkinter.Label(dme, image = img)
    label.pack()
    lbl2 = tkinter.Label(dme, text = firstname, bg = '#DDF6FD' ,font = ('calibiri',11,'bold'))
    lbl2.place(x = 180,y = 105)
    lbl3 = tkinter.Label(dme, text = b, bg = '#DDF6FD' ,font = ('calibiri',30,'bold'))
    lbl3.place(x = 150,y = 180)
    lbl4 = tkinter.Label(dme, text = lastname, bg = '#DDF6FD' ,font = ('calibiri',11,'bold'))
    lbl4.place(x = 180,y = 125)
    lbl5 = tkinter.Label(dme, text = today, bg = '#DDF6FD' ,fg = '#00CCFD',font = ('calibiri',11,'bold'))
    lbl5.place(x = 180,y = 260)
    lbl5 = tkinter.Label(dme, text = 'Date :', bg = '#DDF6FD' ,fg = '#00CCFD',font = ('calibiri',11,'bold'))
    lbl5.place(x = 130,y = 260)
    lbl5 = tkinter.Label(dme, text = pi, bg = '#DDF6FD' ,fg = '#00CCFD',font = ('calibiri',11,'bold'))
    lbl5.place(x = 190,y = 283)
    button2 = tkinter.Button(dme, text = 'Continue',width = 8,cursor = 'hand2',height = 1,border = 0,bg = 'white', font = ('Times New Roman', 12,'bold'), command = tbld)
    button2.place(x = 279,y = 345)   
    dme.mainloop()
    
def pmt():
    global pay
    cl.destroy()
    pay = Tk()
    pay.title('Payments')
    pay.geometry('400x400+300+150')
    pay.configure(bg = '#fff')
    frame = tkinter.Frame(pay, width = 350, height = 350, bg = 'white')
    frame.place(x = 40, y = 10)
    image_0 = Image.open('pmtt.jpg')
    bck = ImageTk.PhotoImage(image_0)   
    img = ImageTk.PhotoImage(Image.open('pmtt.jpg'))
    label1 = tkinter.Label(pay, image = img)
    label1.place(x = 50,y = 100)
    a = tkinter.Label(pay, text = 'Payments', fg = '#57a1f8', bg = 'white', font = ('calibiri', 23, 'bold'))
    a.place(x = 70, y = 10)
    heading = tkinter.Label(frame, text = 'Select Payment Mode', bg = 'white', font = ('calibiri', 15))
    heading.place(x = 10, y = 50)    
    cat = tkinter.Entry(frame, width = 25, fg = 'black', border = 0, bg = 'white', font = ('calibiri', 15))
    cat.place(x = 30, y = 105)    
    tkinter.Frame(frame, width = 295, height = 2, bg = 'black').place(x = 25, y = 300)
    tkinter.Button(frame, width = 39, pady = 7, text = 'Proceed to Pay Rs. ' + b, bg = '#57a1f8', fg = 'white', border = 0, command = dne).place(x = 35, y = 310)    
    pay.mainloop()

def bus():
    global b
    adm = bs+2000
    b = str(adm)
    pmt()

def snd():
    global b
    adm = bs+1000
    b = str(adm)
    pmt()

def eco():
    global b
    adm = bs
    b = str(adm)
    pmt()

def bo():
    global cl
    fli.destroy()
    cl = Tk()
    cl.title('Seating')
    cl.geometry('700x450+150+200')
    lbl = tkinter.Label(cl,text = 'Bookings',fg = '#57a1f8',bg = 'white',width = 32,font = ('calibiri',27,'bold'))
    lbl.place(x = 0,y = 0)
    frame = tkinter.Frame(cl, width = 700,height = 400,bg = 'white')
    frame.place(x = 0,y = 50)
    heading = tkinter.Label(frame,text = 'Select Your Type',bg = 'white',font = ('calibiri',15))
    heading.place(x = 20,y = 40)
    button1 = tkinter.Button(frame,border = 0, text = 'Business Class', bg = 'white',cursor = 'hand2',command = bus,font = ('calibiri',15))
    button1.place(x = 50,y = 100)
    button2 = tkinter.Button(frame,width = 12,text = 'Second Class',border = 0,bg = 'white',cursor = 'hand2',command = snd,font = ('calibiri',15))
    button2.place(x = 48,y = 155)
    button3 = tkinter.Button(frame,width = 8,text = 'Economy',border = 0,bg = 'white',cursor = 'hand2',command = eco,font = ('calibiri',15))
    button3.place(x = 50,y = 210)
    button4 = tkinter.Button(frame,width = 10,text = 'Private Jet',border = 0,bg = 'white',cursor = 'hand2',font = ('calibiri',15))
    button4.place(x = 47,y = 265)
    image = Image.open("cr.jpg")
    photo = ImageTk.PhotoImage(image)
    label_image = tkinter.Label(cl, image = photo, bg = 'white')
    label_image.image = photo  
    label_image.place(x = 45, y = 128)
    bi = tkinter.Label(frame,text = '+2000 Rs. Additional',bg = 'white',font = ('calibiri',11),border = 10)
    bi.place(x = 400,y = 100)
    sc = tkinter.Label(frame,text = '+1000 Rs. Additional',bg = 'white',font = ('calibiri',11),border = 10)
    sc.place(x = 400,y = 155)
    ec = tkinter.Label(frame,text = 'Additional Charges for services',bg = 'white',font = ('calibiri',11),border = 10)
    ec.place(x = 400,y = 210)
    pr = tkinter.Label(frame,text = '+200 Rs. per Km',bg = 'white',font = ('calibiri',11),border = 10)
    pr.place(x = 400,y = 265)
    d = '_'*90
    c = tkinter.Label(cl,text = d,bg = 'white',font = ('calibiri',10,'bold'))
    c.place(x = 20,y = 380)
    nt = tkinter.Label(frame,text = 'Note :- Business Class might not be available for all flights',fg = '#FF0000',bg = 'white',font = ('calibiri',11),border = 10)
    nt.place(x = 20,y = 350) 
    cl.mainloop()

def exit1():
    fli.destroy()

def book():

    if day == 'Daily':
        a = 'select * from Flights where dept_from = "{}" and arr_to = "{}"'.format(From,to)
    elif day == 'Weekend':
        a = 'select * from Weekend where dept_from = "{}" and arr_to = "{}"'.format(From,to)
    elif day == 'Special':
        a = 'select * from Special where dept_from = "{}" and arr_to = "{}"'.format(From,to)
    else:
        messagebox.showerror('Error','Please enter the right choice')
    
    cur.execute(a)
    b = cur.fetchall()
    row = cur.rowcount
    if row == 0:
        messagebox.showerror('Not Available','This Flight is not available for now\nSorry fro inconvenience')
    else:
        
        for i in b :
            
            global Fid,air,pl,fro,too,depa,took,bs
            Fid,too = i[0],i[4]
            air,depa = i[1],i[5]
            pl,took = i[2],i[6]
            fro,bs = i[3],i[7]
            break
        global fli,bk
        window.destroy()
        
        fli = Tk()
        fli.title('Flight Details')
        fli.geometry('600x407+150+200')
        image = Image.open('bll.jpg')
        bk = ImageTk.PhotoImage(image)   
        img = ImageTk.PhotoImage(Image.open('bll.jpg'))
        label = tkinter.Label(fli, image = img)
        label.pack()
        lbl2 = tkinter.Label(fli, text = Fid, bg = '#FFDDC2' ,font = ('calibiri',11,'bold'))
        lbl2.place(x = 180,y = 160)
        lbl3 = tkinter.Label(fli, text = air, bg = '#FFDDC2' ,font = ('calibiri',11,'bold'))
        lbl3.place(x = 180,y = 203)
        lbl4 = tkinter.Label(fli, text = pl, bg = '#FFDDC2' ,font = ('calibiri',11,'bold'))
        lbl4.place(x = 180,y = 247)
        lbl5 = tkinter.Label(fli, text = depa, bg = '#FFDDC2' ,font = ('calibiri',11,'bold'))
        lbl5.place(x = 180,y = 295)
        lbl6 = tkinter.Label(fli, text = fro, bg = '#FFDDC2' ,font = ('calibiri',11,'bold'))
        lbl6.place(x = 450,y = 152)
        lbl7 = tkinter.Label(fli, text = too, bg = '#FFDDC2' ,font = ('calibiri',11,'bold'))
        lbl7.place(x = 450,y = 200)
        lbl8 = tkinter.Label(fli, text = took, bg = '#FFDDC2' ,font = ('calibiri',11,'bold'))
        lbl8.place(x = 450,y = 248)
        lbl9 = tkinter.Label(fli, text = bs, bg = '#FFDDC2' ,font = ('calibiri',11,'bold'))
        lbl9.place(x = 450,y = 295)
        button1 = tkinter.Button(fli, text = 'Exit',width = 13,height = 1, font = ('calibiri', 10), command = exit1)
        button1.place(x = 21,y = 364)
        button2 = tkinter.Button(fli, text = 'Continue',width = 13,height = 1, font = ('calibiri', 10), command = bo)
        button2.place(x = 473,y = 364)
        fli.mainloop()
    
sta()


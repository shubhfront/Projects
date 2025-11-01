import tkinter 
from tkinter import Tk

def form():
    print("Hello World")

global root
root = Tk()
root.title('Tic Tac Toe')
root.config(bg="lightblue") 
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(False, False)
a = tkinter.Label(root, text='Tic-Tac-Toe', width=37, fg='#57a1f8', bg='white', font=('calibiri', 25, 'bold'))
a.place(x=200, y=11, anchor='n')
textbox = tkinter.Entry(root, width=2, font=("calibri", 25, "bold"), justify="center", fg='red')
textbox.bind("<KeyRelease>", lambda e: textbox.insert(0, textbox.get().upper()))
textbox.place(x=50, y=50)


# frame = tkinter.Frame(cus, width = 700,height = 500,bg = 'white')
# frame.place(x = 0,y = 70)
# heading = tkinter.Label(frame,text = 'Select Your Choice',bg = 'white',font = ('calibiri',25))
# heading.place(x = 10,y = 40)
# cat = tkinter.Entry(frame,width = 5,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
# cat.place(x = 30,y = 105)
# cat.insert(0,'1. ')
# per = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
# per.place(x = 30,y = 160)
# per.insert(0,'2. ')
# mm = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
# mm.place(x = 30,y = 215)
# mm.insert(0,'3. ')
# men = tkinter.Entry(frame,width = 25,fg = 'black',border = 0,bg = 'white',font = ('calibiri',15))
# men.place(x = 30,y = 270)
# men.insert(0,'4. ')
# button1 = tkinter.Button(frame,width = 7,text = 'Booking',border = 0,bg = 'white',cursor = 'hand2',activeforeground = 'blue',command = form,font = ('calibiri',15)) 
# button1.place(x = 50,y = 100)
# button2 = tkinter.Button(frame,width = 8,text = 'Boarding',border = 0,bg = 'white',cursor = 'hand2',activeforeground = 'blue',command = form,font = ('calibiri',15))
# button2.place(x = 50,y = 210)
# button3 = tkinter.Button(frame,width = 6,text = 'Check',border = 0,bg = 'white',cursor = 'hand2',activeforeground = 'blue',command = form,font = ('calibiri',15))
# button3.place(x = 50,y = 155)
# button4 = tkinter.Button(frame,width = 7,text = 'Enquiry',border = 0,bg = 'white',cursor = 'hand2',activeforeground = 'blue',command = form,font = ('calibiri',15))
# button4.place(x = 50,y = 265)
# d = '_'*90
# c = tkinter.Label(cus,text = d,bg = 'white',font = ('calibiri',10,'bold'))
# c.place(x = 20,y = 380)
# b = tkinter.Label(cus,text = '* Select the operation you want to perform',bg = 'white',font = ('calibiri',10,'bold'))
# b.place(x = 20,y = 400)
# button5 = tkinter.Button(cus, text = 'exit',width = 7,pady = 7,bg = '#D3D3D3', font = ('calibiri', 10), command = form)
# button5.place(x = 10,y = 450)
# button6 = tkinter.Button(cus, text = 'Back',width = 10,pady = 7,bg = '#D3D3D3', font = ('calibiri', 10), command = form)
# button6.place(x = 600,y = 450)
root.mainloop()
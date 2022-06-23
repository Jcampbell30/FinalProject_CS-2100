from logging import root
from tkinter import *
from tkinter import font
from turtle import width
from PIL import Image,ImageTk
from Currency import Currency
from tkinter import ttk


infile = open("Exchrate.txt")
countryDict = {}
countries = []
for line in infile:
    info = line.rstrip().split(',')
    currency = Currency(info[1],info[2]=="left",info[3]=="comma",float(info[4]))
    countryDict[info[0]] = currency
infile.close()
for c in countryDict.keys():
    countries.append(c)

window = Tk()
window.title("Currency Converter")

window.geometry('1000x1500')
window.iconbitmap('Conversion.ico')
bg = (PhotoImage(file = "Anotherbackground.png"))
bg2 =(PhotoImage(file='background2.png'))

label1 =Label(window,image=bg)
label1.place(x=0,y=0)

countryFrom = Label(window,text="  Choose a Country  ")
converMssg = Label(window,text=" Convert from ______ to _________ ")
countryTo = Label(window,text=  "  Choose a Country  ")


countryFrom.grid(row=1, column=0, padx=10,pady=10)
converMssg.grid(row=1,column=1,padx=10,pady=10)
countryTo.grid(row=1,column=2,padx=10,pady=10)


buttonFrame = Frame(window)
background_frame = Label(buttonFrame,image=bg2)
background_frame.place(x=0,y=0)
buttonFrame.grid(row=4,column=1,columnspan=3,pady=340)




btn1 = Button(buttonFrame,text="1",width=4,bg='silver',font=('Calibri 18'))
btn1.grid(row=0,column=0,padx=10,pady=5)
btn2 = Button(buttonFrame,text="2",width=4,bg='silver',font=('Calibri 18'))
btn2.grid(row=0,column=1,padx=10,pady=5)
btn3 = Button(buttonFrame,text="3",width=4,bg='silver',font=('Calibri 18'))
btn3.grid(row=0,column=2,padx=10,pady=5)
btn4 = Button(buttonFrame,text="4",width=4,bg='silver',font=('Calibri 18'))
btn4.grid(row=1,column=0,padx=10,pady=5)
btn5 = Button(buttonFrame,text="5",width=4,bg='silver',font=('Calibri 18'))
btn5.grid(row=1,column=1,padx=10,pady=5)
btn6 = Button(buttonFrame,text="6",width=4,bg='silver',font=('Calibri 18'))
btn6.grid(row=1,column=2,padx=10,pady=5)

btn7 = Button(buttonFrame,text="7",width=4,bg='silver',font=('Calibri 18'))
btn7.grid(row=3,column=0,padx=10,pady=5)
btn8 = Button(buttonFrame,text="8",width=4,bg='silver',font=('Calibri 18'))
btn8.grid(row=3,column=1,padx=10,pady=5)
btn9 = Button(buttonFrame,text="9",width=4,bg='silver',font=('Calibri 18'))
btn9.grid(row=3,column=2,padx=10,pady=5)
btn0 = Button(buttonFrame,text="0",width=4,bg='silver',font=('Calibri 18'))
btn0.grid(row=1,column=3,padx=10,pady=5)
btndot = Button(buttonFrame,text=".",width=4,bg='silver',font=('Calibri 18'))
btndot.grid(row=1,column=4,padx=10,pady=5)
btnClear = Button(buttonFrame,text="C",width=4,bg='silver',font=('Calibri 18'))
btnClear.grid(row=1,column=5,padx=10,pady=5)


#Record button
btn_record = Button(buttonFrame,text="Record",width=16,bg='red',font=('Calibri 18'))
btn_record.grid(row=0,column=3,columnspan=3)

#Help button
btn_help = Button(buttonFrame,text="Help?", width=16,bg = 'silver', font=('Calibri 18'))
btn_help.grid(row=3, column=3, columnspan=3)







#infile = open('countries.txt')
#l = [line.rstrip() for line in infile]
#infile.close()
#conOfListBox = StringVar()
#lisList = Listbox(width=25,height=5,listvariable=conOfListBox)
#conOfListBox.set(tuple(l))
#lisList.grid(row=3,column=0,pady=10,padx=10)


conOfCountryFrom = StringVar()
countryFrom = Listbox(window,exportselection=0,listvariable=conOfCountryFrom)    
countryFrom.grid(row=2,column=0,sticky=E)
conOfCountryFrom.set(tuple(countries))





























window.mainloop()
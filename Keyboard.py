from tkinter import *


#NOTE: Some functions are impcomplete or missing code

expression = ''
def record():
    global expression
    expression = 'record'
    expression = str(expression)
    equation.set(expression)
    #Record function to do

def convert():
    print(5*3)
    #Conversion equation to do




def pressNum(num):
    
    global expression
    expression = expression+str(num)
    equation.set(expression)
def clear():
    global expression
    expression = ''
    equation.set(expression)
def help():
    frame = Tk()
    frame.title("Help Window")
    frame.geometry('325x250')
    mssgOne = Label(frame,text="This is a help message")
    mssgOne.grid(row=0,column=0)
    mssgTwo = Label(frame,text='This is another help message')
    mssgTwo.grid(row=1,column=0)
    mssg3 = Label(frame,text="Another help message")
    mssg3.grid(row=2,column=0)
    frame.mainloop()

#Creating root window
window = Tk()
window.geometry('800x300')



#Button Frame inside the window
buttonFrame = Frame(window)
background_frame = Label(buttonFrame)
background_frame.place(x=0,y=0)
buttonFrame.grid(row=4,column=1,sticky=NSEW)





#Entrybox for Buttons
equation = StringVar()
conOfentNum = StringVar(buttonFrame, value = equation)
entName = Entry(buttonFrame, textvariable=equation)
entName.grid(row=4,column=3, columnspan=3,sticky=NSEW)
entName.focus_set()


#Button Layout
btn1 = Button(buttonFrame,text="1",width=4,bg='silver',font=('Calibri 18'),command=lambda: pressNum(1))
btn1.grid(row=0,column=0,padx=10,pady=5)
btn2 = Button(buttonFrame,text="2",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum(2))
btn2.grid(row=0,column=1,padx=10,pady=5)
btn3 = Button(buttonFrame,text="3",width=4,bg='silver',font=('Calibri 18'),command= lambda:pressNum(3))
btn3.grid(row=0,column=2,padx=10,pady=5)
btn4 = Button(buttonFrame,text="4",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum(4))
btn4.grid(row=1,column=0,padx=10,pady=5)
btn5 = Button(buttonFrame,text="5",width=4,bg='silver',font=('Calibri 18'),command= lambda:pressNum(5))
btn5.grid(row=1,column=1,padx=10,pady=5)
btn6 = Button(buttonFrame,text="6",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum(6))
btn6.grid(row=1,column=2,padx=10,pady=5)

btn7 = Button(buttonFrame,text="7",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum(7))
btn7.grid(row=3,column=0,padx=10,pady=5)
btn8 = Button(buttonFrame,text="8",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum(8))
btn8.grid(row=3,column=1,padx=10,pady=5)
btn9 = Button(buttonFrame,text="9",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum(9))
btn9.grid(row=3,column=2,padx=10,pady=5)
btn0 = Button(buttonFrame,text="0",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum(0))
btn0.grid(row=4,column=0,padx=10,pady=5)
btndot = Button(buttonFrame,text=".",width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum('.'))
btndot.grid(row=4,column=1,padx=10,pady=5)
btncm = Button(buttonFrame,text=',',width=4,bg='silver',font=('Calibri 18'),command=lambda:pressNum(','))
btncm.grid(row=4,column=2,padx=10,pady=5)
btnClear = Button(buttonFrame,text="Clear",width=4,bg='silver',font=('Calibri 18'),command=lambda:clear())
btnClear.grid(row=5,column=0,columnspan=3,sticky=NSEW)


#ConvertButton
btnConvert = Button(buttonFrame,text="Convert",width=16,font=('Calibri 18'),bg='silver',command=lambda:convert())
btnConvert.grid(row=0,column=3,columnspan=3)

#Record button
btn_record = Button(buttonFrame,text="Record",width=16,bg='red',font=('Calibri 18'),command=lambda:record())
btn_record.grid(row=1,column=3,columnspan=3)

#Help button
btn_help = Button(buttonFrame,text="Help?", width=16,bg = 'silver', font=('Calibri 18'),command=lambda:help())
btn_help.grid(row=3, column=3, columnspan=3)

window.mainloop()


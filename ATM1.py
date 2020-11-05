from tkinter import*
import sqlite3
import tkinter.messagebox

class ATM1():

    def __init__(self, top):
        self.mOffsets = Toplevel(top)
        self.mOffsets.geometry("1400x900+0+0")
        self.mOffsets.title("STATE BANK OF INDIA")
        self.mOffsets.configure(bg='blue')

        def exit1():
            
            tkinter.messagebox.showinfo('window Title','Do you want to close')
            answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

            if answer == 'yes':
                root.destroy()

        lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
        lblInfo.place(x=320,y=20)

        lblInfo1=Label(self.mOffsets,font=('arial',40),text="Select Language",fg="white",bg="blue",bd=10,anchor='w')
        lblInfo1.place(x=480,y=150)

        #========================= BUTTON ===================================================================

        button1 = Button(self.mOffsets,font=('bold italic',20),text="English",bg="yellow",fg="blue",height=1,width=20,command=CALL2)
        button1.place(x=1005,y=400)

        button2 = Button(self.mOffsets,font=('bold italic',20),text="हिन्दी",bg="yellow",fg="blue",height=1,width=20)
        button2.place(x=1005,y=500)

        button9 = Button(self.mOffsets,font=('bold italic',20),text="Cancel",bg="yellow",fg="blue",height=1,width=20,command = exit1)
        button9.place(x=1005,y=600)
        
#==============================================enter pin for withdraw=====================================================    
       
class ATM2():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()
                
            #==========================================================================
            lblInfo=Label(self.mOffsets ,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)

            lblInfo1=Label(self.mOffsets ,font=('arial',40),text="Please Enter Your Pin",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=430,y=150)

            #========================= BUTTON ===================================================================

            entry1=Entry(self.mOffsets ,font=('arial',24,'bold'),bd=10,insertwidth=8,bg="yellow",justify='left')
            entry1.place(x=520,y=320)

            button1 = Button(self.mOffsets ,font=('bold italic',20),text="Procced",bg="yellow",fg="blue",height=1,width=20,command = CALL3)
            button1.place(x=1005,y=500)

            button2 = Button(self.mOffsets ,font=('bold italic',20),text="Cancel",bg="yellow",fg="blue",height=1,width=20,command = exit1)
            button2.place(x=1005,y=600)
#===========================================================main menu two=====================================================

class ATM3():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')      

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()

            lblInfo=Label(self.mOffsets,font=('arial',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)

            lblInfo1=Label(self.mOffsets,font=('arial',40),text="Select Transaction",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=450,y=150)

            #========================= BUTTON ===================================================================

            button1 = Button(self.mOffsets,font=('bold italic',20),text="DEPOSIT",bg="yellow",fg="blue",height=1,width=20,command=CALL16)
            button1.place(x=30,y=300)

            button2 = Button(self.mOffsets,font=('bold italic',20),text="TRANSFER",bg="yellow",fg="blue",height=1,width=20,command=CALL14)
            button2.place(x=30,y=400)

            button3 = Button(self.mOffsets,font=('bold italic',20),text="PIN CHANGE",bg="yellow",fg="blue",height=1,width=20,command=CALL7)
            button3.place(x=30,y=500)

            button4 = Button(self.mOffsets,font=('bold italic',20),text="CHANGE ACC. DETAIL",bg="yellow",fg="blue",height=1,width=20,command=CALL15)
            button4.place(x=30,y=600)

            button5 = Button(self.mOffsets,font=('bold italic',20),text="FAST CASH",bg="yellow",fg="blue",height=1,width=20)
            button5.place(x=1005,y=300)

            button6 = Button(self.mOffsets,font=('bold italic',20),text="CASH WITHDRAWAL",bg="yellow",fg="blue",height=1,width=20,command=CALL4)
            button6.place(x=1005,y=400)

            button7 = Button(self.mOffsets,font=('bold italic',20),text="BALANCE INQ.",bg="yellow",fg="blue",height=1,width=20,command=CALL11)
            button7.place(x=1005,y=500)

            button8 = Button(self.mOffsets,font=('bold italic',20),text="ACC. DETAIL CHECK",bg="yellow",fg="blue",height=1,width=20,command=CALL20)
            button8.place(x=1005,y=600)

            #================================================= Quit Button ===================================================

            button9 = Button(self.mOffsets,font=('bold italic',20),text="CANCEL",bg="yellow",fg="blue",height=1,width=20,command = exit1)
            button9.place(x=510,y=600)

#=========================================================withdraw current and saving=========================================================
class ATM4():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')      

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()
                    
            lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)

            button1 = Button(self.mOffsets,font=('bold italic',20),text="From Current",bg="yellow",fg="blue",height=1,width=20,command = CALL5)
            button1.place(x=1005,y=400)

            button2 = Button(self.mOffsets,font=('bold italic',20),text="From Saving",bg="yellow",fg="blue",height=1,width=20,command = CALL5)
            button2.place(x=1005,y=500)

#======================================================withdraw amount============================================================
class ATM5():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')      

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()

            lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)

            lblInfo=Label(self.mOffsets,font=('bold italic ',40),text="MONEY WITHDRAW",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=430,y=150)

            lblInfo1=Label(self.mOffsets,font=('arial',30),text="Pin Number :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=50,y=308)

            lblInfo2=Label(self.mOffsets,font=('arial',30),text="Withdrawal Amount :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo2.place(x=50,y=408)

            #========================= BUTTON ===================================================================

            entry1=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Password10,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry1.place(x=430,y=320)

            entry2=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Amount10,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry2.place(x=430,y=420)

            button1 = Button(self.mOffsets,font=('bold italic',20),text="Withdraw",bg="yellow",fg="blue",height=1,width=20,command=Update3)
            button1.place(x=1005,y=400)

            button1 = Button(self.mOffsets,font=('bold italic',20),text="Procced",bg="yellow",fg="blue",height=1,width=20,command=CALL6)
            button1.place(x=1005,y=500)

            button2 = Button(self.mOffsets,font=('bold italic',20),text="Cancel",bg="yellow",fg="blue",height=1,width=20,command=exit1)
            button2.place(x=1005,y=600)

#==========================================================withdraw transaction process========================================================
class ATM6():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')      

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()

                    
            lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)

            lblInfo1=Label(self.mOffsets,font=('arial',40),text="Your Transaction is being processed",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=270,y=200)

            lblInfo1=Label(self.mOffsets,font=('arial',40),text="Please Wait ..... ",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=530,y=300)

            button1 = Button(self.mOffsets,font=('bold italic',20),text="Log In",bg="yellow",fg="blue",height=1,width=20,command = CALL1)
            button1.place(x=1005,y=500)

#=========================================================pin change process=======================================================

class ATM7():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')      

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()

            lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)

            lblInfo1=Label(self.mOffsets,font=('arial',40),text="YOU CAN CHANGE YOUR PIN",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=310,y=150)

            #========================= BUTTON ===================================================================

            lblInfo1=Label(self.mOffsets,font=('arial',30),text="Account No.:",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=50,y=390)

            lblInfo1=Label(self.mOffsets,font=('arial',30),text="New Pin      :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=50,y=490)

            lblInfo1=Label(self.mOffsets,font=('arial',30),text="Renter New : \nPin",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=50,y=590)

            entry1=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Account5,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry1.place(x=320,y=400)

            entry2=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Password5,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry2.place(x=320,y=500)

            entry3=Entry(self.mOffsets,font=('arial',24,'bold'),bd=10,insertwidth=8,bg="yellow",justify='left')
            entry3.place(x=320,y=600)


            button1 = Button(self.mOffsets,font=('bold italic',20),text="Submit",bg="yellow",fg="blue",height=1,width=20,command = Update1)
            button1.place(x=1005,y=400)

            button2 = Button(self.mOffsets,font=('bold italic',20),text="Procced",bg="yellow",fg="blue",height=1,width=20,command = CALL8)
            button2.place(x=1005,y=500)

            button3 = Button(self.mOffsets,font=('bold italic',20),text="Cancel",bg="yellow",fg="blue",height=1,width=20,command = exit1)
            button3.place(x=1005,y=600)

#===================================================pin changed sucessfull==============================================================
class ATM8():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')      

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()

                    
            lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)

            lblInfo1=Label(self.mOffsets,font=('arial',40),text="Your Pin Has Changed ",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=420,y=150)

            lblInfo1=Label(self.mOffsets,font=('arial',40),text="Please Log In With New Pin",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=360,y=280)

            button1 = Button(self.mOffsets,font=('bold italic',20),text="Log In",bg="yellow",fg="blue",height=1,width=20,command = CALL1)
            button1.place(x=1005,y=500)

            button2 = Button(self.mOffsets,font=('bold italic',20),text="Cancel",bg="yellow",fg="blue",height=1,width=20,command = exit1)
            button2.place(x=1005,y=600)

#=======================================================deposite transaction  process==========================================================
class ATM10():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')      

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()

                    
            lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)

            lblInfo1=Label(self.mOffsets,font=('arial',40),text="Your Transaction is being processed",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=270,y=200)

            lblInfo1=Label(self.mOffsets,font=('arial',40),text="Please Wait ..... ",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=530,y=300)

            lblInfo1=Label(self.mOffsets,font=('arial',40),text="Your amount has been deposited in your account",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=130,y=400)

            button1 = Button(self.mOffsets,font=('bold italic',20),text="Log In",bg="yellow",fg="blue",height=1,width=20,command = CALL1)
            button1.place(x=1005,y=500)

            button2 = Button(self.mOffsets,font=('bold italic',20),text="Cancel",bg="yellow",fg="blue",height=1,width=20,command = exit1)
            button2.place(x=1005,y=600)

#======================================================balance inquiary process===========================================================
class ATM11():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')      

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()

            lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)

            lblInfo1=Label(self.mOffsets,font=('arial',40),text="Balance Inquery ",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=480,y=130)

            lblInfo1=Label(self.mOffsets,font=('arial',30),text="Please Enter Your Pin Number : ",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=100,y=300)

            lblInfo1=Label(self.mOffsets,font=('arial',30),text="Your Transaction is being processed .... ",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=100,y=410)

            lblInfo1=Label(self.mOffsets,font=('arial',30),text="your current Account balance is :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=100,y=510)

            entry3=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Password21,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry3.place(x=780,y=310)

            entry4=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Amount23,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry4.place(x=480,y=600)

            button1 = Button(self.mOffsets,font=('bold italic',20),text="Procced",bg="yellow",fg="blue",height=1,width=20,command = Update5)
            button1.place(x=1005,y=400)

            button2 = Button(self.mOffsets,font=('bold italic',20),text="Log In",bg="yellow",fg="blue",height=1,width=20,command = CALL1)
            button2.place(x=1005,y=500)

            button3 = Button(self.mOffsets,font=('bold italic',20),text="Cancel",bg="yellow",fg="blue",height=1,width=20,command = exit1)
            button3.place(x=1005,y=600)

#==================================================registration form===============================================================
class ATM12():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')      

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()

            lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)

            lblInfo=Label(self.mOffsets,font=('bold italic ',40),text="REGISTRATION FORM",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=400,y=150)

            lblInfo1=Label(self.mOffsets,font=('arial',30),text="Account No. :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=50,y=308)

            lblInfo2=Label(self.mOffsets,font=('arial',30),text="First Name   :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo2.place(x=50,y=408)

            lblInfo3=Label(self.mOffsets,font=('arial',30),text="Password    :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo3.place(x=50,y=508)

            lblInfo4=Label(self.mOffsets,font=('arial',30),text="Amount       :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo4.place(x=50,y=608)

            #========================= BUTTON ===================================================================

            entry1=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Account1,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry1.place(x=420,y=320)

            entry2=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Firstname1,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry2.place(x=420,y=420)

            entry3=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Password1,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry3.place(x=420,y=520)

            entry4=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Amount1,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry4.place(x=420,y=620)

            button1 = Button(self.mOffsets,font=('bold italic',20),text="Submit",bg="yellow",fg="blue",height=1,width=20,command = Insert)
            button1.place(x=1005,y=400)

            button2 = Button(self.mOffsets,font=('bold italic',20),text="Procced",bg="yellow",fg="blue",height=1,width=20,command = CALL13)
            button2.place(x=1005,y=500)

            button3 = Button(self.mOffsets,font=('bold italic',20),text="Cancel",bg="yellow",fg="blue",height=1,width=20,command = exit1)
            button3.place(x=1005,y=600)


#========================================================registration successfull=========================================================
class ATM13():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')      

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()

            lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)

            lblInfo=Label(self.mOffsets,font=('bold italic ',30),text="REGISTRATION SUCCESSFULL",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=385,y=150)

            lblInfo1=Label(self.mOffsets,font=('arial',30),text="Please Again Log In",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=500,y=250)

            button1 = Button(self.mOffsets,font=('bold italic',20),text="Log In",bg="yellow",fg="blue",height=1,width=20,command = CALL1)
            button1.place(x=1005,y=500)

            button2 = Button(self.mOffsets,font=('bold italic',20),text="Cancel",bg="yellow",fg="blue",height=1,width=20,command = exit1)
            button2.place(x=1005,y=600)


#==================================================transfer form===============================================================
class ATM14():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')      

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()

            lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)            

            lblInfo=Label(self.mOffsets,font=('bold italic ',40),text="MONEY TRANSFER",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=450,y=150)

            lblInfo1=Label(self.mOffsets,font=('arial',30),text="From Account No. :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=50,y=308)

            lblInfo2=Label(self.mOffsets,font=('arial',30),text="To Account No.   :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo2.place(x=50,y=408)

            lblInfo3=Label(self.mOffsets,font=('arial',30),text="Amount    :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo3.place(x=50,y=508)

            #========================= BUTTON ===================================================================

            entry1=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Account13,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry1.place(x=420,y=320)

            entry2=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Account14,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry2.place(x=420,y=420)

            entry3=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Amount15,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry3.place(x=420,y=520)

            button1 = Button(self.mOffsets,font=('bold italic',20),text="Transfer",bg="yellow",fg="blue",height=1,width=20,command = Update4)
            button1.place(x=1005,y=400)

            button2 = Button(self.mOffsets,font=('bold italic',20),text="Procced",bg="yellow",fg="blue",height=1,width=20,command = CALL18)
            button2.place(x=1005,y=500)

            button3 = Button(self.mOffsets,font=('bold italic',20),text="Cancel",bg="yellow",fg="blue",height=1,width=20,command = exit1)
            button3.place(x=1005,y=600)

#============================================detail change=============================================================

class ATM15():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')      

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()

            lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)

            lblInfo=Label(self.mOffsets,font=('bold italic ',40),text="DETAILED UPDATION FORM",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=300,y=150)

            lblInfo1=Label(self.mOffsets,font=('arial',30),text="Old Acc. No.:",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=50,y=308)

            lblInfo2=Label(self.mOffsets,font=('arial',30),text="First Name   :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo2.place(x=50,y=408)

            lblInfo3=Label(self.mOffsets,font=('arial',30),text="Password    :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo3.place(x=50,y=508)

            #========================= BUTTON ===================================================================

            entry1=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Account3,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry1.place(x=420,y=320)

            entry2=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Firstname3,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry2.place(x=420,y=420)

            entry3=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Password3,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry3.place(x=420,y=520)

            button1 = Button(self.mOffsets,font=('bold italic',20),text="Update",bg="yellow",fg="blue",height=1,width=20,command = Update)
            button1.place(x=1005,y=500)

            button2 = Button(self.mOffsets,font=('bold italic',20),text="Procced",bg="yellow",fg="blue",height=1,width=20,command = CALL13)
            button2.place(x=1005,y=600)

            button3 = Button(self.mOffsets,font=('bold italic',20),text="Cancel",bg="yellow",fg="blue",height=1,width=20,command = exit1)
            button3.place(x=1005,y=700)

#=============================================Deposit menu=======================================================

class ATM16():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')      

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()


            lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)

            lblInfo=Label(self.mOffsets,font=('bold italic ',40),text="MONEY DEPOSIT FORM",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=370,y=150)

            lblInfo1=Label(self.mOffsets,font=('arial',30),text="Account No. :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=50,y=308)

            lblInfo2=Label(self.mOffsets,font=('arial',30),text="Deposit Amount   :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo2.place(x=50,y=408)

            #========================= BUTTON ===================================================================

            entry1=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Account7,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry1.place(x=430,y=320)

            entry2=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Amount7,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry2.place(x=430,y=420)

            button1 = Button(self.mOffsets,font=('bold italic',20),text="Deposit",bg="yellow",fg="blue",height=1,width=20,command=Update2)
            button1.place(x=1005,y=400)

            button2 = Button(self.mOffsets,font=('bold italic',20),text="Procced",bg="yellow",fg="blue",height=1,width=20,command=CALL10)
            button2.place(x=1005,y=500)

            button3 = Button(self.mOffsets,font=('bold italic',20),text="No",bg="yellow",fg="blue",height=1,width=20,command = exit1)
            button3.place(x=1005,y=600)


#=======================================================Transfer transaction  process==========================================================
class ATM18():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')      

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()

                    
            lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)

            lblInfo1=Label(self.mOffsets,font=('arial',40),text="Your Transaction is being processed",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=270,y=200)

            lblInfo1=Label(self.mOffsets,font=('arial',40),text="Please Wait ..... ",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=530,y=300)

            lblInfo1=Label(self.mOffsets,font=('arial',40),text="Your amount has been transfered in another account",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=130,y=400)

            button1 = Button(self.mOffsets,font=('bold italic',20),text="Log In",bg="yellow",fg="blue",height=1,width=20,command = CALL1)
            button1.place(x=1005,y=500)

            button2 = Button(self.mOffsets,font=('bold italic',20),text="Cancel",bg="yellow",fg="blue",height=1,width=20,command = exit1)
            button2.place(x=1005,y=600)


#======================================================Services process===========================================================
class ATM19():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')     

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()

                    
            lblInfo=Label(self.mOffsets,font=('bold italic ',40),text="WELCOME TO STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=200,y=50)

            lblInfo1=Label(self.mOffsets,font=('arial',20),text="Welcome to State Bank Of India. State Bank Of India Is Most Popular Bank Of India.",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=170,y=200)

            lblInfo1=Label(self.mOffsets,font=('arial',20),text="We Are Providing Many Facilites Like Money Transfer,Cash Withdrwal,Mini Statement, ",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=160,y=240)

            lblInfo1=Label(self.mOffsets,font=('arial',20),text="Balance Inquiry,Cash Deposit,you Can Also Open Your Account.you Can Change Your Pin,\n Update your Account Detail. ",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=140,y=280)

            button1 = Button(self.mOffsets,font=('bold italic',20),text="Log In",bg="yellow",fg="blue",height=1,width=20,command = CALL1)
            button1.place(x=1005,y=500)

            button2 = Button(self.mOffsets,font=('bold italic',20),text="Cancel",bg="yellow",fg="blue",height=1,width=20,command = exit1)
            button2.place(x=1005,y=600)
#==================================================registration form===============================================================
class ATM20():

    def __init__(self, top):
            self.mOffsets = Toplevel(top)
            self.mOffsets.geometry("1400x900+0+0")
            self.mOffsets.title("STATE BANK OF INDIA")
            self.mOffsets.configure(bg='blue')      

            def exit1():
                
                tkinter.messagebox.showinfo('window Title','Do you want to close')
                answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

                if answer == 'yes':
                    root.destroy()

            lblInfo=Label(self.mOffsets,font=('bold italic ',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=320,y=20)

            lblInfo=Label(self.mOffsets,font=('bold italic ',40),text="Account Details",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo.place(x=500,y=130)

            lblInfo1=Label(self.mOffsets,font=('arial',30),text="Enter Your Pin :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=50,y=208)

            lblInfo1=Label(self.mOffsets,font=('arial',30),text="Account No. :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo1.place(x=50,y=308)

            lblInfo2=Label(self.mOffsets,font=('arial',30),text="First Name   :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo2.place(x=50,y=408)

            lblInfo3=Label(self.mOffsets,font=('arial',30),text="Password    :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo3.place(x=50,y=508)

            lblInfo4=Label(self.mOffsets,font=('arial',30),text="Amount       :",fg="white",bg="blue",bd=10,anchor='w')
            lblInfo4.place(x=50,y=608)

            #========================= BUTTON ===================================================================

            entry1=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Password25,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry1.place(x=420,y=220)
            
            entry1=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Account26,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry1.place(x=420,y=320)

            entry2=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Firstname27,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry2.place(x=420,y=420)

            entry3=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Password28,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry3.place(x=420,y=520)

            entry4=Entry(self.mOffsets,font=('arial',24,'bold'),textvar=Amount29,bd=10,insertwidth=8,bg="yellow",justify='left')
            entry4.place(x=420,y=620)

            button1 = Button(self.mOffsets,font=('bold italic',20),text="Check",bg="yellow",fg="blue",height=1,width=20,command = Update6)
            button1.place(x=1005,y=400)

            button2 = Button(self.mOffsets,font=('bold italic',20),text="Procced",bg="yellow",fg="blue",height=1,width=20,command = CALL13)
            button2.place(x=1005,y=500)

            button3 = Button(self.mOffsets,font=('bold italic',20),text="Cancel",bg="yellow",fg="blue",height=1,width=20,command = exit1)
            button3.place(x=1005,y=600)

            
#===================================================function call===============================================
            
def CALL1():
    atm = ATM1(root)

def CALL2():
    atm = ATM2(root)

def CALL3():
    atm = ATM3(root)

def CALL4():
    atm = ATM4(root)

def CALL5():
    atm = ATM5(root)

def CALL6():
    atm = ATM6(root)

def CALL7():
    atm = ATM7(root)

def CALL8():
    atm = ATM8(root)

def CALL9():
    atm = ATM9(root)

def CALL10():
    atm = ATM10(root)

def CALL11():
    atm = ATM11(root)

def CALL12():
    atm = ATM12(root)

def CALL13():
    atm = ATM13(root)

def CALL14():
    atm = ATM14(root)

def CALL15():
    atm = ATM15(root)

def CALL16():
    atm = ATM16(root)  

def CALL17():
    atm = ATM17(root)

def CALL18():
    atm = ATM18(root)

def CALL19():
    atm = ATM19(root)

def CALL20():
    atm = ATM20(root)
    
#==============================================================main menu=====================================   
root = Tk()
root.geometry("1400x900+0+0")
root.title("STATE BANK OF INDIA")
root.configure(bg='blue')

#==========================================create table =========================================================
db=sqlite3.connect('ATM.db')
cursor=db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ATMDATA(AccountNumber TEXT,FirstName TEXT,Password TEXT,Amount TEXT)")
db.commit()

#========================================insert data in table ==========================================================

Account1=StringVar()
Firstname1=StringVar()
Password1=StringVar()
Amount1=StringVar()

def Insert():

  Account2=Account1.get()
  Firstname2=Firstname1.get()
  Password2=Password1.get()
  Amount2=Amount1.get()
  
  ins=sqlite3.connect('ATM.db')
  with ins:
          cursor=ins.cursor()
          cursor.execute('INSERT INTO ATMDATA(AccountNumber,FirstName,Password,Amount) VALUES(?,?,?,?)',( Account2,Firstname2,Password2,Amount2))
          db.close()

#=======================================================update data in tabble ============================================= 

Account3=StringVar()
Firstname3=StringVar()
Password3=StringVar()

def Update():

    Account4=Account3.get()
    Firstname4=Firstname3.get()
    Password4=Password3.get()
  
    up=sqlite3.connect('ATM.db')
    cursor=up.cursor()
    cursor.execute("UPDATE ATMDATA SET FirstName = ? ,Password = ? WHERE AccountNumber = ?",(Firstname4,Password4,Account4))
    up.commit()

#================================================update pin ==================================================================

Account5=StringVar()
Password5=StringVar()

def Update1():

    Account6=Account5.get()
    Password6=Password5.get()
  
    up=sqlite3.connect('ATM.db')
    cursor=up.cursor()
    cursor.execute("UPDATE ATMDATA SET Password = ? WHERE AccountNumber = ?",(Password6,Account6))
    up.commit()

#================================================Deposit money ==================================================================

Account7=StringVar()
Amount7=StringVar()

def Update2():

    Account8=Account7.get()
    Amount8=Amount7.get()

    up1=sqlite3.connect('ATM.db')
    cursor=up1.cursor()
    cursor.execute("SELECT * FROM ATMDATA WHERE AccountNumber = ?",(Account8,))
    row=cursor.fetchone()
    Amount9=int(row[3])+int(Amount8)
    up=sqlite3.connect('ATM.db')
    cursor=up.cursor()
    cursor.execute("UPDATE ATMDATA SET Amount = ? WHERE AccountNumber = ?",(int(Amount9),Account8))
    up.commit()

#================================================Withdraw money ==================================================================

Password10=StringVar()
Amount10=StringVar()

def Update3():

    Password11=Password10.get()
    Amount11=Amount10.get()

    up1=sqlite3.connect('ATM.db')
    cursor=up1.cursor()
    cursor.execute("SELECT * FROM ATMDATA WHERE Password = ?",(Password11,))
    row=cursor.fetchone()
    Amount12=int(row[3])-int(Amount11)
    up=sqlite3.connect('ATM.db')
    cursor=up.cursor()
    cursor.execute("UPDATE ATMDATA SET Amount = ? WHERE Password = ?",(int(Amount12),Password11))
    up.commit()

#================================================Transfer money ==================================================================

Account13=StringVar()
Account14=StringVar()
Amount15=StringVar()

def Update4():

    Account16=Account13.get()
    Account17=Account14.get()
    Amount18=Amount15.get()
#===============================================from account========================================================
    up2=sqlite3.connect('ATM.db')
    cursor=up2.cursor()
    cursor.execute("SELECT * FROM ATMDATA WHERE AccountNumber = ?",(Account16,))
    row=cursor.fetchone()
    Amount19=int(row[3])-int(Amount18)
    up3=sqlite3.connect('ATM.db')
    cursor=up3.cursor()
    cursor.execute("UPDATE ATMDATA SET Amount = ? WHERE AccountNumber = ?",(int(Amount19),Account16))
    up3.commit()
#===============================================to account=====================================================
    up4=sqlite3.connect('ATM.db')
    cursor=up4.cursor()
    cursor.execute("SELECT * FROM ATMDATA WHERE AccountNumber = ?",(Account17,))
    row=cursor.fetchone()
    Amount20=int(row[3])+int(Amount18)
    up5=sqlite3.connect('ATM.db')
    cursor=up5.cursor()
    cursor.execute("UPDATE ATMDATA SET Amount = ? WHERE AccountNumber = ?",(int(Amount20),Account17))
    up5.commit()

#================================================Balance inq. ==================================================================

Password21=StringVar()
Amount22=StringVar()
Amount23=StringVar()

def Update5():

    Password24=Password21.get()

    up1=sqlite3.connect('ATM.db')
    cursor=up1.cursor()
    cursor.execute("SELECT * FROM ATMDATA WHERE Password = ?",(Password24,))
    row=cursor.fetchone()
    Amount22=row[3]
    Amount23.set(Amount22)

#================================================Account Detail ==================================================================

Password25=StringVar()
Account26=StringVar()
Firstname27=StringVar()
Password28=StringVar()
Amount29=StringVar()

def Update6():

    Password34=Password25.get()

    up1=sqlite3.connect('ATM.db')
    cursor=up1.cursor()
    cursor.execute("SELECT * FROM ATMDATA WHERE Password = ?",(Password34,))
    row=cursor.fetchone()
    Account30=row[0]
    Account26.set(Account30)
    Firstname31=row[1]
    Firstname27.set( Firstname31)
    Password32=row[2]
    Password28.set(Password32)
    Amount33=row[3]
    Amount29.set(Amount33)
#===================================main menu ====================================================================

def exit1():
    
    tkinter.messagebox.showinfo('window Title','Do you want to close')
    answer = tkinter.messagebox.askquestion('Question 1','Yes for Quit and NO for Continue')

    if answer == 'yes':
        root.destroy()

lblInfo=Label(root,font=('arial',50),text="STATE BANK OF INDIA",fg="white",bg="blue",bd=10,anchor='w')
lblInfo.place(x=320,y=20)

lblInfo1=Label(root,font=('arial',40),text="Please Select Banking",fg="white",bg="blue",bd=10,anchor='w')
lblInfo1.place(x=420,y=150)

#========================= BUTTON ===================================================================

button1 = Button(root,font=('bold italic',20),text="SERVICES",bg="blue",fg="white",height=1,width=20,command = CALL19)
button1.place(x=30,y=300)

button2 = Button(root,font=('bold italic',20),text="MINI STATEMENT",bg="blue",fg="white",height=1,width=20,command = CALL20)
button2.place(x=30,y=400)

button3 = Button(root,font=('bold italic',20),text="REGISTRATION",bg="blue",fg="white",height=1,width=20,command = CALL12)
button3.place(x=30,y=500)

button4 = Button(root,font=('bold italic',20),text="QUICK CASH",bg="blue",fg="white",height=1,width=20)
button4.place(x=30,y=600)

button5 = Button(root,font=('bold italic',20),text="BANKING",bg="blue",fg="white",height=1,width=20,command = CALL1)
button5.place(x=1005,y=300)

button6 = Button(root,font=('bold italic',20),text="BALANCE INQ.",bg="blue",fg="white",height=1,width=20,command = CALL1)
button6.place(x=1005,y=400)

button7 = Button(root,font=('bold italic',20),text="TRANSFER",bg="blue",fg="white",height=1,width=20,command = CALL1)
button7.place(x=1005,y=500)

button8 = Button(root,font=('bold italic',20),text="PIN GENERATION",bg="blue",fg="white",height=1,width=20)
button8.place(x=1005,y=600)

#================================================= Quit Button ===================================================

button9 = Button(root,font=('bold italic',20),text="Cancel",bg="blue",fg="white",height=1,width=20,command = exit1)
button9.place(x=510,y=600)

root.mainloop()

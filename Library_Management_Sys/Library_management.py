import smtplib
import traceback

from tkcalendar import *
from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import random
import pymysql
import time

root = Tk()
root.iconbitmap('LibraryIcon.ico')

root.geometry("1000x562+200+80")
root.resizable(False, False)
root.title("Library Management System")

bg = PhotoImage(file = "loginBg1.png")
bg = bg.subsample(1,1)

can = Canvas(root)
can.place(x=0,y=0,relwidth = 1 ,relheight = 1)
can.create_image(0,0,image = bg ,anchor = 'nw')

#Images Used inside Login Page
ForpassImg = PhotoImage(file = "loginBg1.png")
ForpassImg = ForpassImg.subsample(2,2)

ForXieImg = PhotoImage(file='xielogoblack.png')
ForXieImg = ForXieImg.subsample(10,10)

Xieimg = PhotoImage(file='xielogoblack.png')
Xieimg = Xieimg.subsample(4,4)

logoimg = PhotoImage(file='LoginIcon.png')
logoimg = logoimg.subsample(3, 3)

usernameimg = PhotoImage(file='User.png')
usernameimg = usernameimg.subsample(1, 1)

passwordimg = PhotoImage(file='pass.png')
passwordimg = passwordimg.subsample(1, 1)

calanderimg = PhotoImage(file='Calendar.png')
calanderimg = calanderimg.subsample(1,1)

clockimg = PhotoImage(file='Clock.png')
clockimg = clockimg.subsample(1,1)

libraryimg = PhotoImage(file='bookBackImg.png')
libraryimg = libraryimg.subsample(1,1)

addbookimg = PhotoImage(file='addbookicon1.png')
addbookimg = addbookimg.subsample(6, 6)

issuebookimg = PhotoImage(file='issuebookicon1.png')
issuebookimg = issuebookimg.subsample(13, 12)

editbookimg = PhotoImage(file='editbookicon.png')
editbookimg = editbookimg.subsample(6, 6)

returnbookimg = PhotoImage(file='returnbookicon.png')
returnbookimg = returnbookimg.subsample(3, 3)

deletebookimg = PhotoImage(file='deletebookicon.png')
deletebookimg = deletebookimg.subsample(5, 5)

showbookimg = PhotoImage(file='showbookicon1.png')
showbookimg = showbookimg.subsample(1,1)

AddStudimg = PhotoImage(file='addStd.png')
AddStudimg = AddStudimg.subsample(2,2)

logoutimg = PhotoImage(file='logouticon.png')
logoutimg = logoutimg.subsample(1,1)

backbtnimg = PhotoImage(file='backbtnimg1.png')
backbtnimg = backbtnimg.subsample(5,6)

## Images in other Frames Backgrounds

addbookbg =PhotoImage(file = 'AddbookFrameBg.png')
addbookbg = addbookbg.subsample(2,3)

Issuebookbg =PhotoImage(file = 'IssueBookFrameBg.png')
Issuebookbg = Issuebookbg.subsample(1,1)

Editbookbg =PhotoImage(file = 'EditBookFrameBg.png')
Editbookbg = Editbookbg.subsample(2,3)

showbookbg =PhotoImage(file = 'showBookFrameBg.png')
showbookbg = showbookbg.subsample(1,1)

returnbookbg =PhotoImage(file = 'ReturnBookFrameBg.png')
returnbookbg = returnbookbg.subsample(2,2)

deletebookbg =PhotoImage(file = 'DeleteBookFrameBg.png')
deletebookbg = deletebookbg.subsample(2,3)

addStudbg =PhotoImage(file = 'AddStudentFrameBg.png')
addStudbg = addStudbg.subsample(1,1)

# Label Widget Icons
Idimg =PhotoImage(file = 'IDbook.png')
Idimg = Idimg.subsample(18,18)

Tilt = PhotoImage(file = 'TitleBook.png')
Tilt = Tilt.subsample(3,3)

Auth = PhotoImage(file = 'AuthorBook.png')
Auth = Auth.subsample(13,13)

edition = PhotoImage(file = 'editionBook.png')
edition = edition.subsample(17,17)

price = PhotoImage(file = 'priceBook.png')
price = price.subsample(1,1)

stdId = PhotoImage(file = 'StudentID.png')
stdId = stdId.subsample(1,1)

stdnamimg = PhotoImage(file = 'StdNamImg.png')
stdnamimg = stdnamimg.subsample(1,1)

stdcourseimg = PhotoImage(file = 'StdCoursImg.png')
stdcourseimg = stdcourseimg.subsample(1,1)

stdcontactimg = PhotoImage(file = 'StdphnImg.png')
stdcontactimg = stdcontactimg.subsample(1,1)

stdcollegeimg = PhotoImage(file = 'StdClgImg.png')
stdcollegeimg = stdcollegeimg.subsample(1,1)


#Widget Used inside the login Frame

def loginbtnfunc():                                     #Login Button Function
    global user, passw,Admin_name, con, mycursor
    user = username.get()
    passw = password.get()
    if (user == "" or passw == ""):
        messagebox.showinfo("Notification", "All fields are required", parent=root)
    elif (len(passw) < 8):
        messagebox.showerror("Notification", "Password Must be of 8 Characters!!!", parent=root)
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='')
            mycursor = con.cursor()
            query = 'use library;'
            mycursor.execute(query)
            query = 'select * from admin_logindata where username=%s and password=%s;'
            t = mycursor.execute(query, (user, passw))
            if (t == True):
                root.withdraw()
                data = mycursor.execute("select name from admin_logindata where username=%s;", (user))
                data = mycursor.fetchall()
                for i in data:
                    Admin_name = i[0]
                openTop()
            else:
                messagebox.showerror('Notification', 'Incorrect Username or Password!!!\nPlease try again...',
                                     parent=root)
                loginForgetPassbtn.place(x=500, y=455)

        except :
            messagebox.showerror('Notification', 'Something is wrong!!!\nPlease try again...', parent=root)
            return

# Login Frame Labels

titleLabel = Label(can ,text='LOGIN SYSTEM', font=('Georgia', 20, 'italic bold'), bg='#6D93B1', fg='White' ,height = 2,
                   relief='groove' ,bd=2 )
titleLabel.place(x=1,y=1,relwidth = 1)

titleLabel2 = Label(can,image = Xieimg , bg='azure' ,bd=2,relief='groove' )
titleLabel2.place(x=6,y=8)

can.create_image((430,80),image = logoimg ,anchor = 'nw')

can.create_image((297,275),image = usernameimg ,anchor = 'nw')

can.create_text((370,289),text = "Username :",font=('times', 15, 'italic bold'))

can.create_image((297,358),image = passwordimg ,anchor = 'nw')

can.create_text((370,368),text = "Password :",font=('times', 15, 'italic bold'))

#Login Entry Boxes
username = StringVar()
password = StringVar()

usernameEntry = Entry(root, textvariable=username, width=25, font=('times', 15, 'italic'), bd=5, bg='lightblue')
usernameEntry.place(x=420, y=270)
usernameEntry.focus()

passwordEntry = Entry(root, width=25, show='*', textvariable=password, font=('times', 15, 'italic'), bd=5, bg='lightblue')
passwordEntry.place(x=420, y=350)

#Login Submit Button
loginbtn = Button(root, text='Login', font=('times', 13, 'italic bold'), bg='lightgreen', bd=5, activebackground='green',
                  activeforeground='white', command=loginbtnfunc ,width = 8)
loginbtn.place(x=580, y=410)

def ForGetPass(event):
    root.withdraw()
    Forget = Toplevel()
    Forget.geometry('500x290')
    Forget.resizable(False,False)
    Forget.title('Forget PassWord')

    for_frame =  Frame(Forget,bd= 4,relief ='groove',bg= 'red')
    for_frame.place(x=0,y=0,relwidth=1 ,relheight=1)

    forcan = Canvas(for_frame )
    forcan.place(x=0, y=0, relwidth=1, relheight=1)
    forcan.create_image(0, 0, image=ForpassImg, anchor='nw')

    ForTitle = Label(forcan,text= 'Enter Verified Email ID' ,font= ('serif',15,'italic'), bg='#6D93B1', fg='White' ,bd=3,
                     relief = 'groove')
    ForTitle.place(x= 10 ,y= 5 ,width = 468)

    FortitleLabel2 = Label(forcan, image=ForXieImg, bg='azure', bd=2, relief='groove')
    FortitleLabel2.place(x=16, y=9)

    forcan.create_text((115,125),text = 'Email : ', font= ('Time',12,'bold'))

    Emailval = StringVar()
    ForEmailVal = Entry(for_frame,textvariable = Emailval, font= ('Time',12,'italic') ,bd = 3 ,width = 28)
    ForEmailVal.place(x=145, y=110)

    def SendMail():
        if Emailval.get() == '' :
            messagebox.showerror('Error',"Email Field Cannot be Empty  !!!",parent = for_frame )
        else:
            try:
                conn = pymysql.connect(host='localhost', user='root', password='')
                cursor = conn.cursor()
                query = 'use library;'
                cursor.execute(query)
                query = 'select password from admin_logindata WHERE email = %s;'
                r = cursor.execute(query, (Emailval.get()))
                if r == True:
                    Otp = random.randint(1000,9999)
                    print(Otp)

                    ## Send Mail
                    sender = 'nitingupta2001.ng@gmail.com'
                    reciver = Emailval.get()
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(sender,'Nitin@1906')
                    server.sendmail(sender,reciver,f'These Is Your XIE Library \n\n \tEmail ID : {Emailval.get()} \n\n \tOTP       : {Otp}')
                    server.quit()

                    Otp_frame = Frame(Forget, bd=4 , relief='groove',bg = 'green')
                    Otp_frame.place(x=0, y=0, relwidth=1, relheight=1)

                    forcan = Canvas(Otp_frame)
                    forcan.place(x=0, y=0, relwidth=1, relheight=1)
                    forcan.create_image(0, 0, image=ForpassImg, anchor='nw')

                    ForTitle = Label(forcan, text='Enter OTP send to Email ID', font=('serif', 15, 'italic'),
                                    bg='#6D93B1', fg='White',bd= 3 ,relief= 'groove' )
                    ForTitle.place(x= 10 ,y= 5 ,width = 468)

                    FortitleLabel2 = Label(forcan, image=ForXieImg, bg='azure', bd=2, relief='groove')
                    FortitleLabel2.place(x=16, y=9)

                    forcan.create_text((120,125), text='OTP : ', font=('Time', 12, 'bold'))

                    otpval = StringVar()
                    ForotpVal = Entry(Otp_frame, textvariable=otpval , font= ('Time',12,'italic'), bd=4)
                    ForotpVal.place(x=145, y=110)

                    def NewPass():
                        if otpval.get() == '':
                            messagebox.showinfo('INFORMATION',"OTP Field cannot be Empty !!!" , parent = for_frame)
                        else:
                            if otpval.get() == str(Otp):
                                NewPass_frame = Frame(Forget, bd=4, relief='groove' ,bg = 'yellow')
                                NewPass_frame.place(x=0, y=0, relwidth=1, relheight=1)

                                forcan = Canvas(NewPass_frame)
                                forcan.place(x=0, y=0, relwidth=1, relheight=1)
                                forcan.create_image(0, 0, image=ForpassImg, anchor='nw')

                                NewPassTitle = Label(forcan, text='New PassWord',
                                                 font=('serif', 15, 'italic'),
                                                bg='#6D93B1', fg='White' ,bd= 3 ,relief= 'groove')
                                NewPassTitle.place(x= 10 ,y= 5 ,width = 468)

                                FortitleLabel2 = Label(forcan, image=ForXieImg, bg='azure', bd=2, relief='groove')
                                FortitleLabel2.place(x=16, y=9)

                                forcan.create_text((130,115), text='New Password : ', font=('Time', 12, 'bold'))

                                NewPassval = StringVar()
                                NewPassLabval = Entry(NewPass_frame, textvariable=NewPassval, font=('Times', 12, 'italic'), bd=4)
                                NewPassLabval.place(x=220, y=100)

                                forcan.create_text((142,167), text='Confirm Password : ', font=('Time', 12, 'bold'))

                                ConNewPassval = StringVar()
                                ConNewPassLabval = Entry(NewPass_frame,show = '*',textvariable=ConNewPassval,
                                                      font=('Times', 12, 'italic'), bd=4)
                                ConNewPassLabval.place(x=220, y=150)

                                def ConPass():
                                    if NewPassval.get() != '' and ConNewPassval.get() != '':
                                        if len(NewPassval.get()) >= 8:
                                            if NewPassval.get() == ConNewPassval.get():
                                                query= "select * from admin_logindata ;"
                                                cursor.execute(query)
                                                query = 'UPDATE admin_logindata  SET password = %s WHERE email = %s;'
                                                r = cursor.execute(query,(ConNewPassval.get(),Emailval.get()))
                                                if r == True :
                                                    messagebox.showinfo('INFORMATION',
                                                                           "Password Successfully Updated !!!",
                                                                           parent=for_frame)
                                                    Forget.destroy()
                                                    root.update()
                                                    root.deiconify()
                                                    username.set('')
                                                    password.set('')
                                                else:
                                                    messagebox.showwarning('WARNING',
                                                                           "New Password and Previews Password is Same \nTry Something New Password!!!",
                                                                           parent=for_frame)
                                            else:
                                                messagebox.showwarning('WARNING',
                                                                       "New Password and Confirm Password Must Same!!!",
                                                                       parent=for_frame)
                                        else:
                                            messagebox.showwarning('WARNING',"Password Must contain Atleast 8 Character!!!",
                                                                parent=for_frame)

                                    else :
                                        messagebox.showinfo('INFORMATION',"Any Field cannot be Empty !!!" , parent = for_frame)

                                ConfirmNewPassBtn = Button(NewPass_frame,font = ('Times',13,'bold') ,bd = 4 ,width = 8 ,
                                                           text='Confirm',bg = "sky blue",
                                                           command=ConPass)
                                ConfirmNewPassBtn.place(x=300, y=190)

                            else:
                                messagebox.showwarning("WARNING","Wrong OTP !!!" ,parent = for_frame)


                    ForotpBtn = Button(Otp_frame, text='Next',bg = "sky blue" ,bd= 4 ,font = ('Times',13,'bold'),width = 8,
                                       command = NewPass)
                    ForotpBtn.place(x=300, y=190)

                else:
                    Emailval.set('')
                    messagebox.showwarning('WARNING', "Such Email Id Is Not There In Record !!!", parent=for_frame)
            except:
                print(traceback.format_exc())
                messagebox.showerror('Error', "SomeThing Went Wrong Please Try Again Later!!!", parent=for_frame)

    ForBtn = Button(for_frame , text= 'Submit',font = ('Times',13,'bold'),width = 8,bd= 4 ,bg = 'sky blue',command =SendMail)
    ForBtn.place(x=300, y=190)


    for_frame.place()

loginForgetPassbtn = Label(root, text='Click if Forget Password', font=('times', 9, 'italic bold'), bg='#76ABB6',fg ='red')
loginForgetPassbtn.place_forget()
loginForgetPassbtn.bind( "<Button>", ForGetPass )

def on_enterdeliveredbtn(e):
    loginForgetPassbtn.configure(fg='blue')
def on_leavedeliveredbtn(e):
    loginForgetPassbtn.configure(fg='red')

loginForgetPassbtn.bind('<Enter>',on_enterdeliveredbtn)
loginForgetPassbtn.bind('<Leave>',on_leavedeliveredbtn)

def openTop():

    def Date_Tim():
        time_string = time.strftime("%H:%M:%S")
        date_string = time.strftime("%d/%m/%Y")
        clockdateLabel.configure(text=" Date : " + date_string)
        clocktimLabel.configure(text=" Time : " + time_string )
        clocktimLabel.after(1000, Date_Tim)

    ## TopLevel Frame

    dashwin = Toplevel()
    dashwin.geometry("900x550+300+100")
    # dashwin.resizable(False, False)
    dashwin.iconbitmap('LibraryIcon.ico')
    dashwin.title("Library Management System")

    ## TopLevel Frame Title
    root_title = Label(dashwin, text="DASHBOARD", fg="white", bg='#6D93B1', font=("Courier New", 40, "bold"),relief='groove',bd=2)
    root_title.pack(side = 'top', fill ='x')

    titleLabel2 = Label(dashwin, image=Xieimg, bg='azure', bd=2, relief='groove')
    titleLabel2.place(x=6, y=8)

    ## TopLevel Date Time Admin Frame

    Admin_dateFrame = Frame(dashwin, bg="#E5EACA", height=64 , relief='groove',bd=5)
    Admin_dateFrame.pack(fill ='x')

    nameLabel = Label(Admin_dateFrame, text="Name:", font=("Arial", 13, "bold"),bg="#E5EACA")
    nameLabel.place(x=10, y=0 ,relheight=1)

    nameValLabel = Label(Admin_dateFrame, text = Admin_name, font=("Arial", 14, "italic bold"), fg='red',bg="#E5EACA", padx=5)
    nameValLabel.place(x=68, y=0 ,relheight=1)

    clockdateLabel = Label(Admin_dateFrame,image = calanderimg, font=('times', 14, 'bold'), relief='flat', bg='#E5EACA',compound ='left')
    clockdateLabel.place(x=470, y=0,relheight=1)

    clocktimLabel = Label(Admin_dateFrame,image = clockimg, font=('times', 14, 'bold'), relief='flat', bg='#E5EACA',compound ='left')
    clocktimLabel.place(x=690, y=0, relheight=1)
    Date_Tim()

    ## DashBoard Button Frame and Image
    dashboardframe = Frame(dashwin)
    dashboardframe.pack(fill ='both')

    imageLabel = Label(dashboardframe, image=libraryimg,bd = 5,relief = 'groove', bg="#B07138")
    imageLabel.pack()

    ## Frame Raise Function
    def raise_frame(fm):
        fm.tkraise()

    ## add Widget Inside Add Book Frame
    addbookframe = Frame(dashwin, bg="#D1DEE4",relief = 'ridge' ,bd= 5)
    addbookframe.place(x=0,y=132,relwidth = 1 ,height = 418)

    addbookframeBgImg = Label(addbookframe, image=addbookbg)
    addbookframeBgImg.place(x=0, y=0,relwidth = 1 ,relheight = 1)

    addbookbackbtn = Button(addbookframe, bd=4, image=backbtnimg,
                            command=lambda: raise_frame(dashboardframe),bg = '#D1DEE4')
    addbookbackbtn.place(x=10, y=10)

    ## Add Book Mini Frame
    miniaddbookframe = Frame(addbookframe, bg='#D1DEE4',height =380,width =550 ,relief = 'ridge' ,bd = 4)
    miniaddbookframe.place(x=160, y=20)

    addbookframe_title = Label(miniaddbookframe, text="ADD BOOKS", bg="#006600", font=("Arial", 15, "bold"),relief = 'groove' ,fg='white',width = 41)
    addbookframe_title.place(x=20, y=10)

    idLabelImg = Label(miniaddbookframe, image=Idimg, font=("Arial", 12, "bold"), bg='#D1DEE4')
    idLabelImg.place(x=70, y=65)

    idval = StringVar()
    idLabel = Label(miniaddbookframe, text="Book ID :", font=("Arial", 12, "bold"), bg='#D1DEE4')
    idLabel.place(x=110, y=70)

    idEntry = Entry(miniaddbookframe, textvariable=idval, bg='sky blue', font=("Arial", 12), bd=5, relief=GROOVE, width=10)
    idEntry.place(x=190, y=70)

    TileLabelImg = Label(miniaddbookframe, image=Tilt, font=("Arial", 12, "bold"), bg='#D1DEE4')
    TileLabelImg.place(x=70, y=112)

    titleLabel = Label(miniaddbookframe, text="TITLE :", font=("Arial", 12, "bold"), bg='#D1DEE4')
    titleLabel.place(x=110, y=122)

    titleval = StringVar()
    titleEntry = Entry(miniaddbookframe, textvariable=titleval , bg='sky blue', font=("Arial", 12), bd=5, relief=GROOVE,
                       width=30)
    titleEntry.place(x=190, y=120)

    authorLabelImg = Label(miniaddbookframe, image=Auth, font=("Arial", 12, "bold"), bg='#D1DEE4')
    authorLabelImg.place(x=70, y=160)

    authorLabel = Label(miniaddbookframe, text="Author", font=("Arial", 12, "bold"), bg='#D1DEE4')
    authorLabel.place(x=110, y=170)

    authorval = StringVar()
    authorEntry = Entry(miniaddbookframe, textvariable=authorval, bg='sky blue', font=("Arial", 12), bd=5, relief=GROOVE,
                        width=30)
    authorEntry.place(x=190, y=170)

    editLabelImg = Label(miniaddbookframe, image=edition, font=("Arial", 12, "bold"), bg='#D1DEE4')
    editLabelImg.place(x=71, y=215)

    editionLabel = Label(miniaddbookframe, text="Edition", font=("Arial", 12, "bold"), bg='#D1DEE4')
    editionLabel.place(x=110, y=222)

    editionval = StringVar()
    editionEntry = Entry(miniaddbookframe, textvariable=editionval, bg='sky blue', font=("Arial", 12), bd=5, relief=GROOVE,width=30)
    editionEntry.place(x=190, y=220)

    priceLabelImg = Label(miniaddbookframe, image=price, font=("Arial", 12, "bold"), bg='#D1DEE4')
    priceLabelImg.place(x=70, y=268)

    priceLabel = Label(miniaddbookframe, text="Price", font=("Arial", 12, "bold"), bg='#D1DEE4')
    priceLabel.place(x=110, y=272)

    priceval = StringVar()
    priceEntry = Entry(miniaddbookframe, textvariable=priceval, bg='sky blue', font=("Arial", 12), bd=5, relief=GROOVE,
                       width=10)
    priceEntry.place(x=190, y=270)

    def addbooksubmitbtnfunc():
        if (
                idval.get() == "" or titleval.get() == "" or authorval.get() == "" or editionval.get() == "" or priceval.get() == ""):
            messagebox.showinfo("Info", "All Fields are required...", parent=dashwin)
        else:
            query = "Select bookid,title,author,edition,price from storebook where bookid=%s"
            r = mycursor.execute(query, (idval.get()))
            if (r == True):
                messagebox.showinfo("Info", "Book ID already exists!!!", parent=dashwin)
            else:
                query = "insert into storebook(bookid,title,author,edition,price) values(%s,%s,%s,%s,%s);"
                r = mycursor.execute(query,
                                     (idval.get(), titleval.get(), authorval.get(), editionval.get(), priceval.get()))
                if (r == True):
                    messagebox.showinfo("Notification", "Book Added Successfully...", parent=dashwin)
                con.commit()
                idval.set("")
                titleval.set("")
                authorval.set("")
                editionval.set("")
                priceval.set("")

    def addbookResetbtnfunc():
        idval.set("")
        titleval.set("")
        authorval.set("")
        editionval.set("")
        priceval.set("")

    addbooksubmitbtn = Button(miniaddbookframe, text="Submit", bg='blue2', fg='white', activebackground='red', bd =5,
                              activeforeground='white'
                              , width=8, font=("Arial", 12, "bold"), command=addbooksubmitbtnfunc)
    addbooksubmitbtn.place(x=310, y=320)

    addbookResetbtn = Button(miniaddbookframe, text="Reset", bg='blue2', fg='white', activebackground='red', bd=5,
                              activeforeground='white'
                              , width=8, font=("Arial", 12, "bold"), command=addbookResetbtnfunc)
    addbookResetbtn.place(x=430, y=320)


    ## ADD BOOK Button
    add_booksbtn = Button(dashboardframe, text="Add Books", font=("Arial", 12, "bold italic"), fg='white',
                          bg="#B07138",
                          activebackground='red'
                          , activeforeground='white', bd=10, width=150, height=40, image=addbookimg, compound='left',
                          command=lambda: raise_frame(addbookframe))
    add_booksbtn.place(x= 30 ,y = 35 )

    ## Issue Book Frame
    issuebookframe = Frame(dashwin, bg="plum1", relief='ridge', bd=5)
    issuebookframe.place(x=0, y=132, relwidth=1,height = 418)

    IssuebookframeBgImg = Label(issuebookframe, image=Issuebookbg)
    IssuebookframeBgImg.place(x=0, y=0, relwidth=1, relheight=1)

    def issuebookbackbtnFun():
        #  clearing student id in issue book
        studentidEntry['state'] = 'normal'
        studentidEntry.delete(0, 'end')

        stdnameLabelVal.configure(text='')
        stdcourseLabelVal.configure(text='')
        stdcontactLabelVal.configure(text='')
        stdcollegeLabelVal.configure(text='')
        for child in issuebookminiframe3.winfo_children():
            child.configure(state='disable')

        BookidLabelEntry.delete(0,'end')
        for child in issuebookminiframe2.winfo_children():
            child.configure(state='disable')

        dashboardframe.tkraise()

    issuebookbackbtn = Button(issuebookframe, bd=4, image=backbtnimg,
                            command=issuebookbackbtnFun ,bg= '#EEDE8F')
    issuebookbackbtn.place(x=10, y=10)

    ## Issue Book Mini Frames
    miniissuebookframe1 = Frame(issuebookframe, bg='plum1',relief = 'ridge' ,bd = 4)
    miniissuebookframe1.place(x=30, y=50, width=400, height=200)

    issuebookminiframe3 = Frame(issuebookframe, bg='plum1', relief='ridge', bd=4)
    issuebookminiframe3.place(x=465, y=50, width=400, height=200)

    issuebookminiframe2 = Frame(issuebookframe, bg='plum1', relief='ridge', bd=4)
    issuebookminiframe2.place(x=200, y=255, width=500, height=150)

    ## Issue Book Mini Frames1 widgets
    issuebookframe_title1 = Label(miniissuebookframe1, text="STUDENT INFORMATION", bg="orchid3",relief='sunken',bd =3,
                                  font=("Arial", 15, "bold"),
                                  fg='white', width=30)
    issuebookframe_title1.place(x=13, y=15)

    StdidLabelImg = Label(miniissuebookframe1, image=stdId, font=("Arial", 12, "bold"), bg='plum1')
    StdidLabelImg.place(x=20, y=84)

    studentidLabel = Label(miniissuebookframe1, text="Student ID" , bg='plum1', font=("Arial", 12, "bold"))
    studentidLabel.place(x=60, y=92)

    studentidval = StringVar()
    studentidEntry = Entry(miniissuebookframe1, textvariable=studentidval, bg='orchid1', font=("Arial", 12), bd=5,
                           relief=GROOVE, width=20 ,state = 'normal')
    studentidEntry.place(x=160, y=90)

    def issuebooksubmitbtnfunc1():
        if studentidval == "":
            messagebox.showinfo("Information" ,"Student Id cannot Be Empty  !!!",parent = dashwin)
        else:
            query = 'SELECT * FROM student_data WHERE roll_no=%s;'
            result = mycursor.execute(query,(studentidval.get()))
            if result == True:
                for child in issuebookminiframe3.winfo_children():
                    child.configure(state='normal')
                query = "SELECT * FROM student_data WHERE roll_no=%s;"
                r = mycursor.execute(query, (studentidval.get()))
                data = mycursor.fetchall()
                for i in data:
                    stdnameLabelVal.configure(text = i[1])
                    stdcourseLabelVal.configure(text = i[2])
                    stdcontactLabelVal.configure(text =i[3])
                    stdcollegeLabelVal.configure(text =i[4])

                for child in issuebookminiframe2.winfo_children():
                    child.configure(state='normal')

                studentidEntry['state'] = 'disable'

            else:
                messagebox.showwarning("Warning", "Student Id Doesn't Exist !!!", parent=dashwin)

    ## Issue Book mini frame Submit Button
    issuebooksubmitbtn1 = Button(miniissuebookframe1, text="Submit", bg='blue', fg='white', activebackground='red',bd=5,
                                 activeforeground='white',relief = 'raised'
                                 , width=8, font=("Arial", 12, "bold"), command=issuebooksubmitbtnfunc1)
    issuebooksubmitbtn1.place(x=155, y=145)

    ## Issue Book mini frame 3 widgets

    issuebookminiframe3_title1 = Label(issuebookminiframe3, text="STUDENT INFORMATION", bg="orchid3", relief='sunken',
                                       bd=3,
                                       font=("Arial", 15, "bold"),
                                       fg='white', width=30)
    issuebookminiframe3_title1.place(x=13, y=15)

    ## Student Name Labels in issueBook mini frame 3
    stdnameLabel = Label(issuebookminiframe3, text="Name     : ", font=("Arial", 12, "bold"), bg='plum1')
    stdnameLabel.place(x=20, y=60)

    stdnameLabelVal = Label(issuebookminiframe3, text=" ", bg='plum1',fg = 'red', font=("Arial", 12 ,'italic'),)
    stdnameLabelVal.place(x=130, y=60)

    ## Student Course in issueBook  mini frame 3
    stdcourseLabel = Label(issuebookminiframe3, text="Branch  : ", font=("Arial", 12, "bold"), bg='plum1')
    stdcourseLabel.place(x=20, y=90)

    stdcourseLabelVal = Label(issuebookminiframe3, text=" ", bg='plum1',fg = 'red', font=("Arial", 12,'italic'), )
    stdcourseLabelVal.place(x=130, y=90)

    ## Student Contact in issueBook  mini frame 3
    stdcontactLabel = Label(issuebookminiframe3, text="Contact : ", font=("Arial", 12, "bold"), bg='plum1')
    stdcontactLabel.place(x=20, y=120)

    stdcontactLabelVal = Label(issuebookminiframe3, text=" ", bg='plum1',fg = 'red', font=("Arial", 12 ,'italic'), )
    stdcontactLabelVal.place(x=130, y=120)

    ## Student College in issueBook  mini frame 3
    stdcollegeLabel = Label(issuebookminiframe3, text="College  : ", font=("Arial", 12, "bold"), bg='plum1')
    stdcollegeLabel.place(x=20, y=150)

    stdcollegeLabelVal = Label(issuebookminiframe3, text=" ", bg='plum1',fg = 'red', font=("Arial", 12 ,'italic'), )
    stdcollegeLabelVal.place(x=130, y=150)

    for child in issuebookminiframe3.winfo_children():
        child.configure(state='disable')

    ## Issue Book mini frame2 Submit Button Function
    issuedbooktitle1 = StringVar()
    issuedbookauthor1 = StringVar()
    issuedbookedition1 = StringVar()
    issuedbooktitle2 = StringVar()
    issuedbookauthor2 = StringVar()
    issuedbookedition2 = StringVar()
    issuedbooktitle3 = StringVar()
    issuedbookauthor3 = StringVar()
    issuedbookedition3 = StringVar()
    to_dateval = StringVar()

    ## Issue Book mini frame 2 widgets

    issuebookminiframe2_title1 = Label(issuebookminiframe2, text="BOOK To ISSUE", bg="orchid3", relief='sunken',
                                       bd=3,
                                       font=("Arial", 15, "bold"),
                                       fg='white', width=38)
    issuebookminiframe2_title1.place(x=13, y=15)

    BookidLabelImg = Label(issuebookminiframe2, image=Idimg, font=("Arial", 12, "bold"), bg='plum1')
    BookidLabelImg.place(x=45, y=64)

    BookidLabelLabel = Label(issuebookminiframe2, text="BOOK ID", bg='plum1', font=("Arial", 12, "bold"))
    BookidLabelLabel.place(x=80, y=67)

    Bookidval = StringVar()
    BookidLabelEntry = Entry(issuebookminiframe2, textvariable=Bookidval, bg='orchid1', font=("Arial", 12), bd=5,
                             relief=GROOVE, width=20)
    BookidLabelEntry.place(x=180, y=65)

    def issuebooksubmitbtnfunc2():
        if (Bookidval.get() == ""):
            messagebox.showerror("Error", "Book Id is required!!!", parent=dashwin)
        else:
            query = "select issue_status from storebook where bookid=%s;"
            r = mycursor.execute(query, (Bookidval.get()))
            if r == True:
                data = mycursor.fetchall()
                for i in data:
                    if i[0] == "Issued":
                        messagebox.showinfo("Info", "This book already issued\nTry another one...!!!", parent=dashwin)
                    else:
                        query = "select title,author,edition from storebook where issued_to=%s"
                        mycursor.execute(query,studentidval.get())
                        data = mycursor.fetchall()
                        case = True
                        for i in data:
                            if (issuedbooktitle1.get() == ""):
                                issuedbooktitle1.set(i[0])
                                issuedbookauthor1.set(i[1])
                                issuedbookedition1.set(i[2])

                            elif (issuedbooktitle2.get() == ""):
                                issuedbooktitle2.set(i[0])
                                issuedbookauthor2.set(i[1])
                                issuedbookedition2.set(i[2])

                            elif (issuedbooktitle3.get() == ""):
                                issuedbooktitle3.set(i[0])
                                issuedbookauthor3.set(i[1])
                                issuedbookedition3.set(i[2])

                            else:
                                messagebox.showinfo("Info", "Maximum 3 books can be taken!!!", parent=dashwin)
                                studentidval.set("")
                                stdnameLabelVal.configure(text = '')
                                stdcourseLabelVal.configure(text = '')
                                stdcontactLabelVal.configure(text = '')
                                stdcollegeLabelVal.configure(text = '')
                                Bookidval.set("")

                                issuedbooktitle1.set("")
                                issuedbookauthor1.set("")
                                issuedbookedition1.set("")
                                issuedbooktitle2.set("")
                                issuedbookauthor2.set("")
                                issuedbookedition2.set("")
                                issuedbooktitle3.set("")
                                issuedbookauthor3.set("")
                                issuedbookedition3.set("")
                                to_dateval.set("")
                                case = False


                        query = "select title,author,edition from storebook where bookid=%s"
                        mycursor.execute(query, (Bookidval.get()))
                        data = mycursor.fetchall()
                        for i in data:
                            if (issuedbooktitle1.get() == ""):
                                issuedbooktitle1.set(i[0])
                                issuedbookauthor1.set(i[1])
                                issuedbookedition1.set(i[2])
                            elif (issuedbooktitle2.get() == ""):
                                issuedbooktitle2.set(i[0])
                                issuedbookauthor2.set(i[1])
                                issuedbookedition2.set(i[2])

                            elif (issuedbooktitle3.get() == ""):
                                issuedbooktitle3.set(i[0])
                                issuedbookauthor3.set(i[1])
                                issuedbookedition3.set(i[2])

                            else:
                                messagebox.showinfo("Info", "Maximum 3 books can be taken!!!", parent=dashwin)
                                studentidval.set("")
                                stdnameLabelVal.configure(text='')
                                stdcourseLabelVal.configure(text='')
                                stdcontactLabelVal.configure(text='')
                                stdcollegeLabelVal.configure(text='')
                                Bookidval.set("")

                                issuedbooktitle1.set("")
                                issuedbookauthor1.set("")
                                issuedbookedition1.set("")
                                issuedbooktitle2.set("")
                                issuedbookauthor2.set("")
                                issuedbookedition2.set("")
                                issuedbooktitle3.set("")
                                issuedbookauthor3.set("")
                                issuedbookedition3.set("")
                                to_dateval.set("")
                                case = False


                        if case == True :
                            issuebooksroot = Toplevel()
                            issuebooksroot.geometry("600x400+500+100")
                            issuebooksroot.resizable(False, False)
                            issuebooksroot.title("Issue Books")
                            issuebooksroot.grab_set()
                            issuebooksroot.configure(bg="white")

                            def on_close():
                                issuedbooktitle1.set("")
                                issuedbookauthor1.set("")
                                issuedbookedition1.set("")
                                issuedbooktitle2.set("")
                                issuedbookauthor2.set("")
                                issuedbookedition2.set("")
                                issuedbooktitle3.set("")
                                issuedbookauthor3.set("")
                                issuedbookedition3.set("")
                                issuebooksroot.destroy()

                            issuebooksroot.protocol('WM_DELETE_WINDOW',on_close)

                            issuedtitle1 = Label(issuebooksroot, text="Title : ", bg="white",
                                                 font=("Arial", 13, "bold")).place(x=20, y=20)
                            issuedentry1val = Label(issuebooksroot, textvariable=issuedbooktitle1, bg="white",
                                                    font=("Arial", 12, 'italic')).place(x=100, y=20)

                            issuedauthor1 = Label(issuebooksroot, text="Author : ", bg="white",
                                                  font=("Arial", 13, "bold")).place(x=20, y=60)
                            issuedauthor1val = Label(issuebooksroot, textvariable=issuedbookauthor1, bg="white",
                                                     font=("Arial", 12, 'italic')).place(x=100, y=60)

                            issuededition1 = Label(issuebooksroot, text="Edition : ", bg="white",
                                                   font=("Arial", 13, "bold")).place(x=20, y=100)
                            issuededition1val = Label(issuebooksroot, textvariable=issuedbookedition1, bg="white",
                                                      font=("Arial", 12, 'italic')).place(x=100, y=100)

                            dashLabel1 = Label(issuebooksroot,
                                               text=".....................................................................................",
                                               bg="white")
                            dashLabel1.place(x=20, y=120)

                            issuedtitle2 = Label(issuebooksroot, text="Title : ", bg="white",
                                                 font=("Arial", 13, "bold")).place(x=20, y=140)
                            issuedentry2Val = Label(issuebooksroot, textvariable=issuedbooktitle2, bg="white",
                                                    font=("Arial", 12, 'italic')).place(x=100, y=140)

                            issuedauthor2 = Label(issuebooksroot, text="Author : ", bg="white",
                                                  font=("Arial", 13, "bold")).place(x=20, y=180)
                            issuedauthor2Val = Label(issuebooksroot, textvariable=issuedbookauthor2, bg="white",
                                                     font=("Arial", 12, 'italic')).place(x=100, y=180)

                            issuededition2 = Label(issuebooksroot, text="Edition : ", bg="white",
                                                   font=("Arial", 13, "bold")).place(x=20, y=220)
                            issuededition2Val = Label(issuebooksroot, textvariable=issuedbookedition2, bg="white",
                                                      font=("Arial", 12, 'italic')).place(x=100, y=220)

                            dashLabel2 = Label(issuebooksroot,
                                               text=".....................................................................................",
                                               bg="white")
                            dashLabel2.place(x=20, y=240)

                            issuedtitle3 = Label(issuebooksroot, text="Title : ", bg="white",
                                                 font=("Arial", 13, "bold")).place(x=20, y=260)
                            issuedentry3Val = Label(issuebooksroot, textvariable=issuedbooktitle3, bg="white",
                                                    font=("Arial", 12)).place(x=100, y=260)

                            issuedauthor3 = Label(issuebooksroot, text="Author : ", bg="white",
                                                  font=("Arial", 13, "bold")).place(x=20, y=300)
                            issuedauthor3Val = Label(issuebooksroot, textvariable=issuedbookauthor3, bg="white",
                                                     font=("Arial", 12)).place(x=100, y=300)

                            issuededition3 = Label(issuebooksroot, text="Edition : ", bg="white",
                                                   font=("Arial", 13, "bold")).place(x=20, y=340)
                            issuededition3Val = Label(issuebooksroot, textvariable=issuedbookedition3, bg="white",
                                                      font=("Arial", 12)).place(x=100, y=340)

                            dashLabel3 = Label(issuebooksroot,
                                               text=".....................................................................................",
                                               bg="white")
                            dashLabel3.place(x=20, y=360)

                            cal = Calendar(issuebooksroot, selectmode='day', year=2021, month=1, day=1)
                            cal.place(x=330, y=20)

                            dateLabel = Label(issuebooksroot,
                                              text="Date : ",
                                              bg="white", font=("Times", 15 , 'bold'))
                            dateLabel.place(x=390, y=250)

                            dateLabelval = Label(issuebooksroot,
                                              text="",
                                              bg="white", fg='red', font=("Times", 15))
                            dateLabelval.place(x=450, y=251)

                            def issuedbtnfunc():
                                if (to_dateval.get() == ""):
                                    messagebox.showinfo("Info", "Confirm last date!!!", parent=dashwin)
                                else:
                                    from_date = time.strftime("%y-%m-%d")
                                    query = "insert into bookissued_data(roll_no,from_date,to_date,bookid) values(%s,%s,%s,%s);"
                                    r = mycursor.execute(query, (
                                        studentidval.get(), from_date, to_dateval.get(), Bookidval.get()))
                                    query = "update storebook set issue_status=%s,issued_to=%s where bookid=%s;"
                                    mycursor.execute(query, ("Issued", studentidval.get(), Bookidval.get()))
                                    messagebox.showinfo("Notification","Book Issued Successfully...",
                                                        parent=issuebooksroot)

                                    issuedbooktitle1.set("")
                                    issuedbookauthor1.set("")
                                    issuedbookedition1.set("")
                                    issuedbooktitle2.set("")
                                    issuedbookauthor2.set("")
                                    issuedbookedition2.set("")
                                    issuedbooktitle3.set("")
                                    issuedbookauthor3.set("")
                                    issuedbookedition3.set("")
                                    to_dateval.set('')
                                    issuebooksroot.destroy()

                            def grab_date():
                                date = cal.get_date()
                                date = date.split('/')
                                date[0], date[1], date[2] = date[2], date[0], date[1]
                                s = '-'
                                date = s.join(date)
                                to_dateval.set(date)

                                #label Date
                                date = date.split('-')
                                date[0], date[1], date[2] = date[2], date[1], date[0]
                                ldate = '/'.join(date)
                                dateLabelval['text'] = ldate

                            confirmdatebtn = Button(issuebooksroot, text="Confirm Date", font=("Times", 10 ,'bold'),
                                                    command=grab_date, bg="blue", fg='white', bd=5)
                            confirmdatebtn.place(x=365, y=300)

                            issuedbtn = Button(issuebooksroot, text="Issue", font=("Times", 10,'bold'),
                                               command=issuedbtnfunc,
                                               bg="red", fg='white', bd=5,width=6)
                            issuedbtn.place(x=475, y=300)

            else:
                messagebox.showinfo("INFORMATION", "No Book Available with Such ID", parent=dashwin)
                Bookidval.set('')


    def issuebookAddMorebtn():
        studentidEntry['state'] = 'normal'
        studentidEntry.delete(0, 'end')

        stdnameLabelVal.configure(text='')
        stdcourseLabelVal.configure(text='')
        stdcontactLabelVal.configure(text='')
        stdcollegeLabelVal.configure(text='')
        for child in issuebookminiframe3.winfo_children():
            child.configure(state='disable')

        BookidLabelEntry.delete(0, 'end')
        for child in issuebookminiframe2.winfo_children():
            child.configure(state='disable')

    ## Issue Book mini frame2 Submit Button
    issuebooksubmitbtn2 = Button(issuebookminiframe2, text="ISSUE", bg='blue', fg='white', activebackground='red',
                                 bd=5,
                                 activeforeground='white', relief='raised'
                                 , width=8, font=("Arial", 10, "bold"), command=issuebooksubmitbtnfunc2)
    issuebooksubmitbtn2.place(x = 260, y=100)


    issuebookAddMorebtn1 = Button(issuebookminiframe2, text="Add More Book", bg='Blue', fg='white', activebackground='red',
                                 bd=5,
                                 activeforeground='white', relief='raised'
                                 , width=15, font=("Arial", 10), command=issuebookAddMorebtn)
    issuebookAddMorebtn1.place(x=350, y=100)

    for child in issuebookminiframe2.winfo_children():
        child.configure(state='disable')

    ## Issue BOOK Button
    issue_booksbtn = Button(dashboardframe, text="Issue Books", font=("Arial", 12, "bold italic"), fg='white',
                          bg="#B07138",
                          activebackground='red'
                          , activeforeground='white', bd=10, width=150, height=40, image=issuebookimg, compound='left',
                          command=lambda: raise_frame(issuebookframe))

    issue_booksbtn.place(x=300, y=35)

    # Edit Book Button Function
    editBookframe = Frame(dashwin, bg="#FFD896", relief='ridge', bd=5)
    editBookframe.place(x=0, y=132, relwidth=1,height = 418)

    editbookframeBgImg = Label(editBookframe, image=Editbookbg)
    editbookframeBgImg.place(x=0, y=0, relwidth=1, relheight=1)

    editBookBackbtn = Button(editBookframe, bd=4, image=backbtnimg,
                            command=lambda: raise_frame(dashboardframe),bg='#FFD896')
    editBookBackbtn.place(x=10, y=10)

    ## Edit Book Mini Frame 1
    miniEditbookframe = Frame(editBookframe, bg='#FFD896', height =200, width=550, relief='ridge', bd=4)
    miniEditbookframe.place(x=180, y=100)

    editBookframe_title = Label(miniEditbookframe, text="EDIT BOOKS", bg="#006600", font=("Arial", 15, "bold"),
                               relief='groove', fg='white', width=41)
    editBookframe_title.place(x=20, y=10)

    editBookidLabelImg = Label(miniEditbookframe, image=Idimg, font=("Arial", 12, "bold"), bg='#FFD896')
    editBookidLabelImg.place(x=140, y=70)

    editBookidLabel = Label(miniEditbookframe, text="Book ID :", font=("Arial", 12, "bold"), bg='#FFD896')
    editBookidLabel.place(x=180, y=75)

    editBookidval = StringVar()
    editBookidEntry = Entry(miniEditbookframe, textvariable=editBookidval , font=("Arial", 12), bd=5, relief=GROOVE,
                    width=10)
    editBookidEntry.place(x=270, y=75)

    def editBooksubmitbtnfun():
        if editBookidval.get() == '':
            messagebox.showinfo("INFORMATION","Book ID cannot be Empty !!!" ,parent = dashwin )
        else:
            query = "select title ,author, edition, price from storebook where bookid  = %s;"
            r = mycursor.execute(query,(editBookidval.get()))
            if r == True:
                data = mycursor.fetchall()
                for i in data:

                    editBooktitleval.set(i[0])
                    editBookauthorval.set(i[1])
                    editBookeditionval.set(i[2])
                    editBookpriceval.set(i[3])
                miniEditbookframe.place_forget()
                miniEditbookframe2.place(x=160, y=20)
                editBookidEntry2.configure(state = 'disable')
            else:
                messagebox.showinfo("INFORMATION", "No Book There With Such ID !!!", parent=dashwin)

    editBookbooksubmitbtn = Button(miniEditbookframe, text="Submit", bg='blue2', fg='white', activebackground='red', bd=5,
                              activeforeground='white'
                              , width=8, font=("Arial", 12, "bold"), command=editBooksubmitbtnfun)
    editBookbooksubmitbtn.place(x=310, y=140)

    ## edit Book MiniFrame2

    miniEditbookframe2 = Frame(editBookframe, bg='powder blue', height=380, width=550, relief='groove', bd=4)
    miniEditbookframe2.place_forget()

    editBookframe_title2 = Label(miniEditbookframe2, text="EDIT BOOKS", bg="#006600", font=("Arial", 15, "bold"),
                                relief='groove', fg='white', width=41)
    editBookframe_title2.place(x=20, y=10)

    editBookidLabelImg2 = Label(miniEditbookframe2, image=Idimg, font=("Arial", 12, "bold"), bg='powder blue')
    editBookidLabelImg2.place(x=70, y=65)

    editBookidLabel2 = Label(miniEditbookframe2, text="Book ID :", font=("Arial", 12, "bold"), bg='powder blue')
    editBookidLabel2.place(x=110, y=70)

    editBookidEntry2 = Entry(miniEditbookframe2, textvariable=editBookidval, bg='sky blue', font=("Arial", 12), bd=5,
                            relief=GROOVE,
                            width=10)
    editBookidEntry2.place(x=190, y=70)

    editBookTileLabelImg = Label(miniEditbookframe2, image=Tilt, font=("Arial", 12, "bold"), bg='powder blue')
    editBookTileLabelImg.place(x=70, y=112)

    editBooktitleLabel = Label(miniEditbookframe2, text="TITLE :", font=("Arial", 12, "bold"), bg='powder blue')
    editBooktitleLabel.place(x=110, y=122)

    editBooktitleval = StringVar()
    editBooktitleEntry = Entry(miniEditbookframe2, textvariable=editBooktitleval, bg='sky blue', font=("Arial", 12), bd=5, relief=GROOVE,
                       width=30)
    editBooktitleEntry.place(x=190, y=120)

    editBookauthorLabelImg = Label(miniEditbookframe2, image=Auth, font=("Arial", 12, "bold"), bg='powder blue')
    editBookauthorLabelImg.place(x=70, y=160)

    editBookauthorLabel = Label(miniEditbookframe2, text="Author", font=("Arial", 12, "bold"), bg='powder blue')
    editBookauthorLabel.place(x=110, y=170)

    editBookauthorval = StringVar()
    editBookauthorEntry = Entry(miniEditbookframe2, textvariable=editBookauthorval, bg='sky blue', font=("Arial", 12), bd=5,
                        relief=GROOVE,
                        width=30)
    editBookauthorEntry.place(x=190, y=170)

    editBookeditLabelImg = Label(miniEditbookframe2, image=edition, font=("Arial", 12, "bold"), bg='powder blue')
    editBookeditLabelImg.place(x=71, y=215)

    editBookeditionLabel = Label(miniEditbookframe2, text="Edition", font=("Arial", 12, "bold"), bg='powder blue')
    editBookeditionLabel.place(x=110, y=222)

    editBookeditionval = StringVar()
    editBookeditionEntry = Entry(miniEditbookframe2, textvariable=editBookeditionval, bg='sky blue', font=("Arial", 12), bd=5,
                         relief=GROOVE, width=30)
    editBookeditionEntry.place(x=190, y=220)

    editBookpriceLabelImg = Label(miniEditbookframe2, image=price, font=("Arial", 12, "bold"), bg='powder blue')
    editBookpriceLabelImg.place(x=70, y=268)

    editBookpriceLabel = Label(miniEditbookframe2, text="Price", font=("Arial", 12, "bold"), bg='powder blue')
    editBookpriceLabel.place(x=110, y=272)

    editBookpriceval = StringVar()
    editBookpriceEntry = Entry(miniEditbookframe2, textvariable=editBookpriceval, bg='sky blue', font=("Arial", 12), bd=5, relief=GROOVE,
                       width=10)
    editBookpriceEntry.place(x=190, y=270)

    def editBooksavebtnfun():
        if editBooktitleval.get() == '' or editBookauthorval.get() == '' or editBookeditionval.get() == '' or editBookpriceval.get() == '':
            messagebox.showinfo("INFORMATION", "Any Field Cannot be Empty !!!", parent=dashwin)
        else:
            query = 'UPDATE storebook SET title = %s , author = %s ,edition = %s , price = %s WHERE bookid = %s'
            res = mycursor.execute(query , (editBooktitleval.get() ,editBookauthorval.get() ,editBookeditionval.get() ,editBookpriceval.get(),editBookidval.get()))
            if res == True:
                messagebox.showinfo("INFORMATION", "Book SuccessFully Updated !!!", parent=dashwin)
                editBooktitleval.set('')
                editBookauthorval.set('')
                editBookeditionval.set('')
                editBookpriceval.set('')
                editBookidval.set('')
                miniEditbookframe2.place_forget()
                miniEditbookframe.place(x=180, y=100)

            else:
                messagebox.showerror("ERROR", "Book Failed To Updated !!!", parent=dashwin)
                editBooktitleval.set('')
                editBookauthorval.set('')
                editBookeditionval.set('')
                editBookpriceval.set('')
                editBookidval.set('')
                miniEditbookframe2.place_forget()
                miniEditbookframe.place(x=180, y=100)


    editBookbooksavebtn = Button(miniEditbookframe2, text="SAVE", bg='blue2', fg='white', activebackground='red',
                                   bd=5,
                                   activeforeground='white'
                                   , width=8, font=("Arial", 12, "bold"), command=editBooksavebtnfun)
    editBookbooksavebtn.place(x=310, y=320)

    ## Edit Book button
    edit_booksbtn = Button(dashboardframe, text="Edit Book", font=("Arial", 12, "bold italic"), fg='white',
                          bg="#B07138",
                          activebackground='red'
                          , activeforeground='white', bd=10, width=150, height=40, image=editbookimg, compound='left',
                           command=lambda: raise_frame(editBookframe))
    edit_booksbtn.place(x=30, y=130)

    # Return Book Button Function
    ReturnBookframe = Frame(dashwin, bg="#B0B5B4", relief='ridge', bd=5)
    ReturnBookframe.place(x=0, y=132, relwidth=1,height = 418)

    ReturnbookframeBgImg = Label(ReturnBookframe, image=returnbookbg)
    ReturnbookframeBgImg.place(x=0, y=0, relwidth=1, relheight=1)

    ReturnBookBackbtn = Button(ReturnBookframe, bd=5, font=("Arial", 14, "bold"), image=backbtnimg,
                             command=lambda: raise_frame(dashboardframe),bg ='#B0B5B4')
    ReturnBookBackbtn.place(x=10, y=10)

    ## Return Book Mini Frame 1
    miniReturnbookframe = Frame(ReturnBookframe, bg='#B0B5B4', height=200, width=550, relief='groove', bd=4)
    miniReturnbookframe.place(x=180, y=100)

    ReturnBookframe_title = Label(miniReturnbookframe, text="RETURN BOOKS", bg="#006600", font=("Arial", 15, "bold"),
                                  relief='groove', fg='white', width=41)
    ReturnBookframe_title.place(x=20, y=10)

    ReturnBookidLabelImg = Label(miniReturnbookframe, image=Idimg, font=("Arial", 12, "bold"), bg='#B0B5B4')
    ReturnBookidLabelImg.place(x=140, y=70)

    ReturnBookidLabel = Label(miniReturnbookframe, text="Book ID :", font=("Arial", 12, "bold"), bg='#B0B5B4')
    ReturnBookidLabel.place(x=180, y=75)

    ReturnBookidEntryval = StringVar()
    ReturnBookidEntry = Entry(miniReturnbookframe, textvariable = ReturnBookidEntryval, font=("Arial", 12),
                              bd=5,bg='snow',
                              relief=GROOVE,
                              width=10)
    ReturnBookidEntry.place(x=270, y=75)

    #Return Book Id Submit Button Function
    def ReturnBooksubmitbtnfun():
        if ReturnBookidEntryval.get() == '':
            messagebox.showinfo("INFORMATION","Book ID cannot be Empty !!!" ,parent = dashwin )
        else:
            query = "select * from storebook where bookid  = %s;"
            r = mycursor.execute(query,(ReturnBookidEntryval.get()))
            if r == True:
                query = 'select to_date from bookissued_data where bookid =%s'
                chk = mycursor.execute(query, (ReturnBookidEntryval.get()))
                if chk == True:
                    data = mycursor.fetchall()
                    for i in data:
                        to_date = i[0]
                    today_date = time.strftime("%y-%m-%d")

                    query = "select datediff(%s,%s);"
                    mycursor.execute(query, (str(today_date), str(to_date)))
                    dif = mycursor.fetchall()
                    for j in dif:
                        difren = j[0]

                    if (difren <= 0):
                        query = "update storebook set issue_status=NULL,issued_to=NULL where bookid=%s"
                        r = mycursor.execute(query, (ReturnBookidEntryval.get()))
                        if r == True:
                            query = "delete from bookissued_data where bookid=%s"
                            r = mycursor.execute(query, (ReturnBookidEntryval.get()))
                            if r == True:
                                messagebox.showinfo("INFORMATION", 'Book Status SuccessFull Updated...', parent=dashwin)
                                ReturnBookidEntryval.set('')
                    else:
                        fineroot = Toplevel()
                        fineroot.title('Late Fine')
                        fineroot.geometry('250x260')
                        fineroot.resizable(False, False)

                        fineframe = Frame(fineroot, bd=5, relief='groove', bg='powder blue')
                        fineframe.place(x=0, y=0, relwidth=1, relheight=1)

                        Duedatelabel = Label(fineframe, font=("Times", 13, "bold"), bg='powder blue',
                                             text='Due Date : ')
                        Duedatelabel.place(x=20, y=20)

                        d = to_date.split('-')
                        d[0], d[1], d[2] = d[2], d[1], d[0]
                        d = '-'.join(d)
                        Duedatelabelval = Label(fineframe, font=("Times", 13, "bold"), bg='powder blue', text=d,
                                                fg='red')
                        Duedatelabelval.place(x=120, y=20)

                        Todaydatelabel = Label(fineframe, font=("Times", 13, "bold"), bg='powder blue',
                                               text='Today Date : ')
                        Todaydatelabel.place(x=20, y=70)

                        Todaydatelabelval = Label(fineframe, font=("Times", 13, "bold"), bg='powder blue',
                                                  text=time.strftime("%d-%m-%y"), fg='red')
                        Todaydatelabelval.place(x=120, y=70)

                        finedatelabel = Label(fineframe, font=("Times", 13, "bold"), bg='powder blue',
                                              text='Late Fine : ')
                        finedatelabel.place(x=20, y=120)

                        fin = difren * 2
                        finedatelabelval = Label(fineframe, font=("Times", 13, "bold"), bg='powder blue', text=fin,
                                                 fg='red')
                        finedatelabelval.place(x=120, y=120)

                        def FinePaidfun():
                            query = "update storebook set issue_status=NULL,issued_to=NULL where bookid=%s"
                            r = mycursor.execute(query, (ReturnBookidEntryval.get()))
                            if r == True:
                                query = "delete from bookissued_data where bookid=%s"
                                r = mycursor.execute(query, (ReturnBookidEntryval.get()))
                                if r == True:
                                    fineroot.destroy()
                                    messagebox.showinfo("INFORMATION", 'Book Status SuccessFull Updated...',
                                                        parent=dashwin)
                                    ReturnBookidEntryval.set('')

                        finebutton = Button(fineframe, text='Paid', font=("Arial", 12, "bold"), bd=5, bg='blue',
                                            fg='white',
                                            command=FinePaidfun)
                        finebutton.place(x=150, y=190)
                else:
                    messagebox.showinfo("INFORMATION", "These Book is Not Issued Yet... !!!", parent=dashwin)
                    ReturnBookidEntry.delete(0,'end')
            else:
                messagebox.showinfo("INFORMATION", "No Book There With Such ID !!!", parent=dashwin)
                ReturnBookidEntry.delete(0, 'end')

    ReturnBookbooksubmitbtn = Button(miniReturnbookframe, text="Submit", bg='blue2', fg='white', activebackground='red', bd=5,
                              activeforeground='white'
                              , width=8, font=("Arial", 12, "bold"), command=ReturnBooksubmitbtnfun)
    ReturnBookbooksubmitbtn.place(x=310, y=140)

    return_booksbtn = Button(dashboardframe, text="Return Book", font=("Arial", 12, "bold italic"), fg='white',
                          bg="#B07138",
                          activebackground='red'
                          , activeforeground='white', bd=10, width=150, height=40, image=returnbookimg, compound='left',
                             command=lambda: raise_frame(ReturnBookframe))
    return_booksbtn.place(x=300, y=130)

    # Delete Book Button Frame
    deleteBookframe = Frame(dashwin, bg="#FEBDAB", relief='ridge', bd=5)
    deleteBookframe.place(x=0, y=132, relwidth=1,height = 418)

    deletebookframeBgImg = Label(deleteBookframe, image=deletebookbg)
    deletebookframeBgImg.place(x=0, y=0, relwidth=1, relheight=1)

    DeleteBookBackbtn = Button(deleteBookframe, bd=5, font=("Arial", 14, "bold"), image=backbtnimg,
                             command=lambda: raise_frame(dashboardframe),bg='#FEBDAB')
    DeleteBookBackbtn.place(x=10, y=10)

    ## Delete Book Mini Frame 1
    miniDeletebookframe = Frame(deleteBookframe, bg='#FEBDAB', height=200, width=550, relief='ridge', bd=4)
    miniDeletebookframe.place(x=180, y=100)

    deleteBookframe_title = Label(miniDeletebookframe, text="DELETE BOOK", bg="#006600", font=("Arial", 15, "bold"),
                                relief='groove', fg='white', width=41)
    deleteBookframe_title.place(x=20, y=10)

    deleteBookidLabelImg = Label(miniDeletebookframe, image=Idimg, font=("Arial", 12, "bold"), bg='#FEBDAB')
    deleteBookidLabelImg.place(x=140, y=70)

    deleteBookidLabel = Label(miniDeletebookframe, text="Book ID :", font=("Arial", 12, "bold"), bg='#FEBDAB')
    deleteBookidLabel.place(x=180, y=75)

    deleteBookidEntryval = StringVar()
    deleteBookidEntry = Entry(miniDeletebookframe, textvariable=deleteBookidEntryval, font=("Arial", 12), bd=5,
                            relief=GROOVE,
                            width=10)
    deleteBookidEntry.place(x=270, y=75)

    def deleteBooksubmitbtnfun():
        if deleteBookidEntryval.get() == '':
            messagebox.showinfo("INFORMATION","Book ID cannot be Empty !!!" ,parent = dashwin )
        else:
            query = "select title ,author, edition, price from storebook where bookid  = %s;"
            r = mycursor.execute(query,(deleteBookidEntryval.get()))
            if r == True:
                data = mycursor.fetchall()
                for i in data:
                    pass
                    deleteBooktitleval.set(i[0])
                    deleteBookauthorval.set(i[1])
                    deleteBookeditionval.set(i[2])
                    deleteBookpriceval.set(i[3])
                miniDeletebookframe.place_forget()
                miniDeletebookframe2.place(x=160, y=20)
                deleteBookidEntry2.configure(state = 'disable')
                deleteBooktitleEntry.configure(state = 'disable')
                deleteBookauthorEntry.configure(state = 'disable')
                deleteBookeditionEntry.configure(state = 'disable')
                deleteBookpriceEntry.configure(state = 'disable')

            else:
                messagebox.showinfo("INFORMATION", "No Book There With Such ID !!!", parent=dashwin)

    deleteBookbooksubmitbtn = Button(miniDeletebookframe, text="Submit", bg='blue2', fg='white', activebackground='red', bd=5,
                              activeforeground='white'
                              , width=8, font=("Arial", 12, "bold"), command=deleteBooksubmitbtnfun)
    deleteBookbooksubmitbtn.place(x=310, y=140)

    ## edit Book MiniFrame2

    miniDeletebookframe2 = Frame(deleteBookframe, bg='#FEBDAB', height=380, width=550, relief='ridge', bd=4)
    miniDeletebookframe2.place_forget()

    deleteBookframe_title2 = Label(miniDeletebookframe2, text="DELETE BOOK", bg="#006600", font=("Arial", 15, "bold"),
                                 relief='groove', fg='white', width=41)
    deleteBookframe_title2.place(x=20, y=10)

    deleteBookidLabelImg2 = Label(miniDeletebookframe2, image=Idimg, font=("Arial", 12, "bold"), bg='#FEBDAB')
    deleteBookidLabelImg2.place(x=70, y=65)

    deleteBookidLabel2 = Label(miniDeletebookframe2, text="Book ID :", font=("Arial", 12, "bold"), bg='#FEBDAB')
    deleteBookidLabel2.place(x=110, y=70)

    deleteBookidEntry2 = Entry(miniDeletebookframe2, textvariable=deleteBookidEntryval, bg='sky blue', font=("Arial", 12), bd=5,
                             relief=GROOVE,
                             width=10)
    deleteBookidEntry2.place(x=190, y=70)

    deleteBookTileLabelImg = Label(miniDeletebookframe2, image=Tilt, font=("Arial", 12, "bold"), bg='#FEBDAB')
    deleteBookTileLabelImg.place(x=70, y=112)

    deleteBooktitleLabel = Label(miniDeletebookframe2, text="TITLE :", font=("Arial", 12, "bold"), bg='#FEBDAB')
    deleteBooktitleLabel.place(x=110, y=122)

    deleteBooktitleval = StringVar()
    deleteBooktitleEntry = Entry(miniDeletebookframe2, textvariable=deleteBooktitleval, bg='sky blue', font=("Arial", 12),
                               bd=5, relief=GROOVE,
                               width=30)
    deleteBooktitleEntry.place(x=190, y=120)

    deleteBookauthorLabelImg = Label(miniDeletebookframe2, image=Auth, font=("Arial", 12, "bold"), bg='#FEBDAB')
    deleteBookauthorLabelImg.place(x=70, y=160)

    deleteBookauthorLabel = Label(miniDeletebookframe2, text="Author", font=("Arial", 12, "bold"), bg='#FEBDAB')
    deleteBookauthorLabel.place(x=110, y=170)

    deleteBookauthorval = StringVar()
    deleteBookauthorEntry = Entry(miniDeletebookframe2, textvariable=deleteBookauthorval, bg='sky blue', font=("Arial", 12),
                                bd=5,
                                relief=GROOVE,
                                width=30)
    deleteBookauthorEntry.place(x=190, y=170)

    deleteBookeditLabelImg = Label(miniDeletebookframe2, image=edition, font=("Arial", 12, "bold"), bg='#FEBDAB')
    deleteBookeditLabelImg.place(x=71, y=215)

    deleteBookeditionLabel = Label(miniDeletebookframe2, text="Edition", font=("Arial", 12, "bold"), bg='#FEBDAB')
    deleteBookeditionLabel.place(x=110, y=222)

    deleteBookeditionval = StringVar()
    deleteBookeditionEntry = Entry(miniDeletebookframe2, textvariable=deleteBookeditionval, bg='sky blue', font=("Arial", 12),
                                 bd=5,
                                 relief=GROOVE, width=30)
    deleteBookeditionEntry.place(x=190, y=220)

    deleteBookpriceLabelImg = Label(miniDeletebookframe2, image=price, font=("Arial", 12, "bold"), bg='#FEBDAB')
    deleteBookpriceLabelImg.place(x=70, y=268)

    deleteBookpriceLabel = Label(miniDeletebookframe2, text="Price", font=("Arial", 12, "bold"), bg='#FEBDAB')
    deleteBookpriceLabel.place(x=110, y=272)

    deleteBookpriceval = StringVar()
    deleteBookpriceEntry = Entry(miniDeletebookframe2, textvariable=deleteBookpriceval, bg='sky blue', font=("Arial", 12),
                               bd=5, relief=GROOVE,
                               width=10)
    deleteBookpriceEntry.place(x=190, y=270)

    def BookDeletebtnfun():
        delCon = messagebox.askyesno("CONFIRM","Do You Really Want To Delete These Book  !!!",parent = dashwin)
        if delCon == True :
            query = 'DELETE FROM storebook  WHERE bookid = %s'
            res = mycursor.execute(query, (deleteBookidEntryval.get()))
            if res == True:
                messagebox.showinfo("INFORMATION", "Book SuccessFully Deleted !!!", parent=dashwin)
                deleteBooktitleval.set('')
                deleteBookauthorval.set('')
                deleteBookeditionval.set('')
                deleteBookpriceval.set('')
                deleteBookidEntryval.set('')
                miniDeletebookframe2.place_forget()
                miniDeletebookframe.place(x=180, y=100)
            else:
                messagebox.showerror("ERROR", "Book Failed To Delete !!!", parent=dashwin)
                deleteBooktitleval.set('')
                deleteBookauthorval.set('')
                deleteBookeditionval.set('')
                deleteBookpriceval.set('')
                deleteBookidEntryval.set('')
                miniDeletebookframe2.place_forget()
                miniDeletebookframe.place(x=180, y=100)

    DeleteBookbookdeletebtn = Button(miniDeletebookframe2, text="DELETE", bg='blue2', fg='white', activebackground='red',
                                 bd=5,
                                 activeforeground='white'
                                 , width=8, font=("Arial", 12, "bold"), command = BookDeletebtnfun)
    DeleteBookbookdeletebtn.place(x=310, y=320)



    delete_booksbtn = Button(dashboardframe, text="Delete Book", font=("Arial", 12, "bold italic"), fg='white',
                          bg="#B07138",
                          activebackground='red',
                          activeforeground='white', bd=10, width=150, height=40, image=deletebookimg, compound='left',
                          command=lambda: raise_frame(deleteBookframe))
    delete_booksbtn.place(x=30, y=225)

    def showAll():
        ## Search Book Frame
        showBookframe = Frame(dashwin, bg="#AAC8C6", relief='ridge', bd=4)
        showBookframe.place(x=0, y=132, relwidth=1,height =418)

        ShowbookframeBgImg = Label(showBookframe, image=showbookbg)
        ShowbookframeBgImg.place(x=0, y=0, relwidth=1, relheight=1)

        showbookbackbtn = Button(showBookframe, bd=5, font=("Arial", 14, "bold"), image=backbtnimg,
                                   command=lambda: raise_frame(dashboardframe),bg= '#AAC8C6')
        showbookbackbtn.place(x=10, y=10)

        MinisearchbookFrame = Frame(showBookframe, width=400, height=70, bd=5, relief='ridge', bg='#AAC8C6')
        MinisearchbookFrame.place(x=250, y=10)

        SearchBookidLabelImg = Label(MinisearchbookFrame, image=Idimg, font=("Arial", 12, "bold"), bg='#AAC8C6')
        SearchBookidLabelImg.place(x=20, y=10)

        SearchBookidLabel = Label(MinisearchbookFrame, text="Book ID :", font=("Arial", 12, "bold"), bg='#AAC8C6')
        SearchBookidLabel.place(x=60, y=15)

        SearchBookidEntryval = StringVar()
        SearchBookidEntry = Entry(MinisearchbookFrame, textvariable=SearchBookidEntryval, bg='snow',
                                  font=("Arial", 12), bd=5,
                                  relief=GROOVE,
                                  width=10)
        SearchBookidEntry.place(x=150, y=13)

        def SecBooksubmitbtnfun():
            if SearchBookidEntryval.get() == '':
                messagebox.showinfo('INFORMATION', 'Search Book Id cannot Be Empty...', parent=dashwin)
            else:
                query = 'SELECT bookid,title,author,edition,price FROM storebook WHERE bookid = %s ;'
                r = mycursor.execute(query, SearchBookidEntryval.get())
                if r == True:
                    query = 'select bookid,title,author,edition,price from storebook WHERE bookid = %s ;'
                    mycursor.execute(query, SearchBookidEntryval.get())
                    data = mycursor.fetchall()
                    for i in data:
                        allBookinfoTable.delete(*allBookinfoTable.get_children())
                        tabVal = [i[0], i[1], i[2], i[3], i[4]]
                        allBookinfoTable.insert('', END, values=tabVal)
                else:
                    messagebox.showinfo('INFORMATION', 'No Book Available With Such Book Id...', parent=dashwin)

        SearchBookbooksubmitbtn = Button(MinisearchbookFrame, text="Search", bg='blue2', fg='white',
                                         activebackground='red',
                                         bd=5,
                                         activeforeground='white'
                                         , width=8, font=("Arial", 12, "bold"), command=SecBooksubmitbtnfun)
        SearchBookbooksubmitbtn.place(x=270, y= 10)

        MinishowbookFrame = Frame(showBookframe, width=850, height=10, bd=4, relief='ridge',bg = '#AAC8C6')
        MinishowbookFrame.place(x=25, y=90)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', font=('times', 15, 'italic'),fieldbackground = '#AAC8C6',
                        background = '#AAC8C6',foreground='red',rowheight = 25)
        style.configure('Treeview.Heading', font=('times', 15, 'italic'), background='sky blue')
        style.map('Treeview',background = [('selected','blue2')])

        Scroll_x = Scrollbar(MinishowbookFrame, orient=HORIZONTAL)
        Scroll_y = Scrollbar(MinishowbookFrame, orient=VERTICAL )

        allBookinfoTable = Treeview(MinishowbookFrame, columns=('Book ID', 'Name', 'Author', 'Edition', 'Price'),
                                    xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM, fill=X ,anchor = W)
        Scroll_y.pack(side=RIGHT, fill=Y ,anchor = N)
        Scroll_x.configure(command=allBookinfoTable.xview)
        Scroll_y.configure(command=allBookinfoTable.yview)

        # Treeview Column Formate
        allBookinfoTable.column('Book ID', width=100, anchor=CENTER)
        allBookinfoTable.column('Name', width=260, anchor=W)
        allBookinfoTable.column('Author', width=200, anchor=W)
        allBookinfoTable.column('Edition', width=120, anchor=CENTER)
        allBookinfoTable.column('Price', width=150, anchor=CENTER)

        # Treeview Heading Tect
        allBookinfoTable.heading('Book ID', text='BOOK ID')
        allBookinfoTable.heading('Name', text='NAME')
        allBookinfoTable.heading('Author', text='AUTHOR')
        allBookinfoTable.heading('Edition', text='EDITION')
        allBookinfoTable.heading('Price', text='PRICE')


        allBookinfoTable.configure(show='headings')

        allBookinfoTable.pack(fill='both')

        query = 'select bookid,title,author,edition,price from storebook;'
        mycursor.execute(query)
        data = mycursor.fetchall()
        for i in data:
            tabVal = [i[0], i[1], i[2], i[3], i[4]]
            allBookinfoTable.insert('', END, values = tabVal)


    show_booksbtn = Button(dashboardframe, text="Show Book", font=("Arial", 12, "bold italic"), fg='white',
                           bg="#B07138",
                           activebackground='red'
                           , activeforeground='white', bd=10, width=150, height=40, image=showbookimg,
                           compound='left',command=showAll)
    show_booksbtn.place(x=300, y=225)

    ## add Widget Inside Add Book Frame
    AddStudframe = Frame(dashwin, bg="#D6D1AE", relief='ridge', bd=5)
    AddStudframe.place(x=0, y=132, relwidth=1,height = 418)

    addStudframeBgImg = Label(AddStudframe, image= addStudbg)
    addStudframeBgImg.place(x=0, y=0, relwidth=1, relheight=1)

    addStdbackbtn = Button(AddStudframe, bd=5, font=("Arial", 14, "bold"),bg= '#D6D1AE', image=backbtnimg,
                            command=lambda: raise_frame(dashboardframe))
    addStdbackbtn.place(x=10, y=10)

    ## Add Student Mini Frame
    miniaddStudframe = Frame(AddStudframe, bg='#D6D1AE', height=380, width=550, relief='ridge', bd=4)
    miniaddStudframe.place(x=160, y=20)

    addStudframe_title = Label(miniaddStudframe, text="ADD STUDENT", bg="#006600", font=("Arial", 15, "bold"),
                               relief='groove', fg='white', width=41)
    addStudframe_title.place(x=20, y=10)

    StudidLabelImg = Label(miniaddStudframe, image=stdId, font=("Arial", 12, "bold"), bg='#D6D1AE')
    StudidLabelImg.place(x=70, y=62)

    StudidLabel = Label(miniaddStudframe, text="Student ID :", font=("Arial", 12, "bold"), bg='#D6D1AE')
    StudidLabel.place(x=108, y=70)

    Studidval = StringVar()
    StudidEntry = Entry(miniaddStudframe, textvariable=Studidval, bg='#F0F5D3', font=("Arial", 12), bd=5, relief=GROOVE,
                    width=10)
    StudidEntry.place(x=210, y=70)

    StudNameLabelImg = Label(miniaddStudframe, image=stdnamimg, font=("Arial", 12, "bold"), bg='#D6D1AE')
    StudNameLabelImg.place(x=70, y=116)

    StudNameLabel = Label(miniaddStudframe, text="Name :", font=("Arial", 12, "bold"), bg='#D6D1AE')
    StudNameLabel.place(x=110, y=122)

    StudNameval = StringVar()
    StudNameEntry = Entry(miniaddStudframe, textvariable = StudNameval, bg='#F0F5D3', font=("Arial", 12), bd=5, relief=GROOVE,
                       width=20)
    StudNameEntry.place(x=210, y=120)

    StudCourseLabelImg = Label(miniaddStudframe, image=stdcourseimg, font=("Arial", 12, "bold"), bg='#D6D1AE')
    StudCourseLabelImg.place(x=75, y=169)

    StudCourseLabel = Label(miniaddStudframe, text="Course : ", font=("Arial", 12, "bold"), bg='#D6D1AE')
    StudCourseLabel.place(x=110, y=170)

    StudCourseval = StringVar()
    StudCourseEntry = Entry(miniaddStudframe, textvariable = StudCourseval, bg='#F0F5D3', font=("Arial", 12), bd=5,
                        relief=GROOVE,
                        width=20)
    StudCourseEntry.place(x=210, y=170)

    StudPhoneLabelImg = Label(miniaddStudframe, image=stdcontactimg, font=("Arial", 12, "bold"), bg='#D6D1AE')
    StudPhoneLabelImg.place(x=80, y=219)

    StudPhoneLabel = Label(miniaddStudframe, text="Contact : ", font=("Arial", 12, "bold"), bg='#D6D1AE')
    StudPhoneLabel.place(x=110, y=222)

    StudPhoneval = StringVar()
    StudPhoneEntry = Entry(miniaddStudframe, textvariable = StudPhoneval, bg='#F0F5D3', font=("Arial", 12), bd=5,
                         relief=GROOVE, width=20)
    StudPhoneEntry.place(x=210, y=220)

    StudClgLabelImg = Label(miniaddStudframe, image=stdcollegeimg, font=("Arial", 12, "bold"), bg='#D6D1AE')
    StudClgLabelImg.place(x=72, y=266)

    StudClgLabel = Label(miniaddStudframe, text="College", font=("Arial", 12, "bold"), bg='#D6D1AE')
    StudClgLabel.place(x=110, y=272)

    StudClgval = StringVar()
    StudClgEntry = Entry(miniaddStudframe, textvariable = StudClgval, bg='#F0F5D3', font=("Arial", 12), bd=5, relief=GROOVE,
                       width=30)
    StudClgEntry.place(x=210, y=270)

    def addStudsubmitbtnfunc():
        if (
                Studidval.get() == "" or StudNameval.get() == "" or StudCourseval.get() == "" or StudPhoneval.get() == "" or StudClgval.get() == ""):
            messagebox.showinfo("Info", "All Fields are required...", parent=dashwin)
        else:
            if len(StudPhoneval.get()) == 10:
                query = "Select roll_no ,student_name ,student_course ,phone ,college_name from student_data where roll_no=%s"
                r = mycursor.execute(query, (Studidval.get()))
                if (r == True):
                    messagebox.showinfo("Info", "Student ID already exists!!!", parent=dashwin)
                else:
                    query = "insert into student_data(roll_no,student_name,student_course,phone,college_name) values(%s,%s,%s,%s,%s);"
                    r = mycursor.execute(query, (
                    Studidval.get(), StudNameval.get(), StudCourseval.get(), StudPhoneval.get(), StudClgval.get()))
                    if (r == True):
                        messagebox.showinfo("Notification", "Student Successfully Added...", parent=dashwin)
                    con.commit()
                    Studidval.set("")
                    StudNameval.set("")
                    StudCourseval.set("")
                    StudPhoneval.set("")
                    StudClgval.set("")
            else:
                messagebox('INFORMATION','Student Contact Must Contain 10 digits' ,parent = dashwin)


    def addStudResetbtnfunc():
        Studidval.set("")
        StudNameval.set("")
        StudCourseval.set("")
        StudPhoneval.set("")
        StudClgval.set("")

    AddStudsubmitbtn = Button(miniaddStudframe, text="Submit", bg='blue2', fg='white', activebackground='red', bd =5,
                              activeforeground='white'
                              , width=8, font=("Arial", 12, "bold"), command=addStudsubmitbtnfunc)
    AddStudsubmitbtn.place(x=310, y=320)

    AddStudResetbtn = Button(miniaddStudframe, text="Reset", bg='blue2', fg='white', activebackground='red', bd=5,
                              activeforeground='white'
                              , width=8, font=("Arial", 12, "bold"), command=addStudResetbtnfunc)
    AddStudResetbtn.place(x=430, y=320)

    ## ADD Student Dashboard Button
    Add_Studbtn = Button(dashboardframe, text="Add Student", font=("Arial", 12, "bold italic"), fg='white',
                             bg="#B07138",
                             activebackground='red'
                             , activeforeground='white', bd=10, width=150, height=40, image=AddStudimg,
                             compound='left', command=lambda: raise_frame(AddStudframe))
    Add_Studbtn.place(x=30, y=320)

    def logoutbtnfun():
        logres = messagebox.askyesno("Confirmation", "Do you really want to logout?", parent=dashwin)
        if logres == True:
            ##Destroy Top
            dashwin.destroy()
            dashwin.update()
            ## Back to Login Frame
            root.update()
            root.deiconify()
            username.set('')
            password.set('')

    logoutbtn = Button(dashboardframe, text="  Log Out", font=("Arial", 12, "bold italic"), fg='white',
                             bg="#B07138",
                             activebackground='red'
                             , activeforeground='white', bd=10, width=150, height=40, image=logoutimg,
                             compound='left', command=logoutbtnfun)
    logoutbtn.place(x=300, y=320)
    dashboardframe.tkraise()

root.mainloop()

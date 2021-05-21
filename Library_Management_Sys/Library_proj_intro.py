from tkinter import *

nit = Tk()
nit.geometry('500x450')
nit.title("INTRO")
nit.configure(bg= '#D6D1AE' , bd = 5,relief ='ridge')
introLab = Label(nit,text="INTRODUCTION",font = ("Georgia", 20 ,'bold') ,bg = 'light green' , bd=3,relief ='groove')
introLab.place(x=10,y=10,width=470)

ClgLab = Label(nit,text="College : ",font = ("Georgia", 13 ,'bold') ,bg = '#D6D1AE' )
ClgLab.place(x=10,y=80)

ClgLabval = Label(nit,text="XAVIER  INSTITUTE  OF  ENGINEERING",font = ("Georgia", 13 ,'bold') ,bg = '#D6D4AE',fg='red' )
ClgLabval.place(x=90,y=80)

skLab = Label(nit,text="Project : ",font = ("Georgia", 13 ,'bold') ,bg = '#D6D1AE' )
skLab.place(x=10,y=150)

skLabval = Label(nit,text="PYTHON  Skill  Lab ",font = ("Georgia", 13 ,'bold') ,bg = '#D6D1AE',fg='red' )
skLabval.place(x=90,y=150)

TPLab = Label(nit,text="Topic : ",font = ("Georgia", 13 ,'bold') ,bg = '#D6D1AE' )
TPLab.place(x=10,y=220)

TPLab = Label(nit,text="LIBRARY  MANAGEMENT  SYSTEM",font = ("Georgia", 13 ,'bold') ,bg = '#D6D1AE' ,fg='red')
TPLab.place(x=90,y=220)

GpLab = Label(nit,text="Group Members :",font = ("Georgia", 12 ,'bold') ,bg = '#D6D1AE' )
GpLab.place(x=10,y=290)
#
GpMemLab = Label(nit,text="\nNitin Gupta \n\nAmeer Khan \n\nOmkar Ambre",font = ("Georgia", 12 ,'bold') ,bg = '#D6D1AE',fg='red' )
GpMemLab.place(x=160,y=290)


nit.mainloop()
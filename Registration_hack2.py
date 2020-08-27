from tkinter import *
import tkinter.messagebox as message
from tkinter import ttk
import mysql.connector
from PIL import ImageTk, Image
root = Tk()
imag = Image.open('new_bg.jpeg')
image1 = ImageTk.PhotoImage(imag)

def database():
   name1=name.get()
   email=mail_id.get()
   gender=v.get()
   country= st.get()
   phone=ph.get()
   if (name1 == "" or email == "" or gender == "" or country == "" or phone ==""):
      message.showinfo('Insert Status', 'All Fields are required')
   
   else:
      con = mysql.connector.connect(host = 'localhost', user = 'root', password = '12345', database = 'Registration')
      cursor=con.cursor()
      cursor.execute('CREATE TABLE IF NOT EXISTS Student (name1 VARCHAR(255),email VARCHAR(255),gender VARCHAR(255),country VARCHAR(255),phone VARCHAR(255))')
      cursor.execute('INSERT INTO Student (name1,email,gender,country,phone) VALUES(%s,%s,%s,%s,%s)',(name1,email,gender,country,phone))
      con.commit()
      message.showinfo('Status', 'Sussefully Registered')
   fullname_entry.delete(0,END)
   email_entry.delete(0,END)
   idea_entry.delete(0,END)
   st.set(li[0])
   


root.title("Registration Form")

root.geometry('810x500')
root.configure(bg = 'white')
bg_label = Label(root, image = image1, width = 400)
bg_label.grid(row = 0, column=0)

frame1 = Frame(root, width = 400, height = 500, bg = 'blue')
frame1.grid(row =0, column = 1)


heading = Label(frame1, text=" Hackathon Registration",width=20,font=("bold", 20), bg = 'blue', fg= 'white')
heading.place(x=40,y=53)


fullname = Label(frame1, text="Full Name",width=20,font=("bold", 12), bg = 'black', fg = 'white', anchor = W)
fullname.place(x=35,y=130)

name=StringVar()

fullname_entry = Entry(frame1,textvar=name)
fullname_entry.place(x=240,y=130)

mail_id=StringVar()
emailid = Label(frame1, text="E-mail",width=20,font=("bold", 12), bg = 'black', fg = 'white', anchor = W)
emailid.place(x=35,y=180)

email_entry = Entry(frame1,textvar=mail_id)
email_entry.place(x=240,y=180)

Gender = Label(frame1, text="Gender",width=20,font=("bold", 12), bg ='black', fg = 'white', anchor = W)
Gender.place(x=35,y=230)

v = IntVar()
Radiobutton(frame1, text="Male",padx = 5, variable=v, value = 1, bg = 'blue').place(x=235,y=230)
Radiobutton(frame1, text="Female",padx = 20, variable=v, value = 2,bg = 'blue').place(x=290,y=230)

country = Label(frame1, text="country",width=20,font=("bold", 12), bg = 'black', fg = 'white', anchor = W)
country.place(x=35,y=280)



st=StringVar()
droplist=ttk.Combobox(frame1,width= 15,textvariable = st)
li = ['Select','India', 'USA','UK','Germany','Australia','South Africa', 'China']
droplist['values'] = li
st.set(li[0])
droplist.place(x=240,y=280)

ph= StringVar()
ph.set("")

idea = Label(frame1, text="Mobile Number", width=20,font=("bold", 12), bg = 'black', fg = 'white', anchor = W)
idea.place(x=35,y=330)
var2= IntVar()

idea_entry = Entry(frame1, textvar = ph)
idea_entry.place(x = 240, y = 330)



Button(frame1, text='Submit',width=20,bg='brown',fg='white', command= database).place(x = 110,y=400)

root.mainloop()

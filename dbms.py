from  tkinter import *
from tkinter import messagebox
import mysql.connector
d={}
#create table details(Name varchar(20),Qualification varchar(20),Date_of_birth varchar(20),Experience varchar(20) ,Domain varchar(20) ,Interest varchar(20) ,Certifications varchar(20) ,number int ,email varchar(20) ,age int)
try:
    vetha=mysql.connector.connect(host="sql10.freemysqlhosting.net",user="sql10415058",password="J6Rvzpb5Us",database="sql10415058")
except:
    messagebox.showerror("Error","Check your internet connection or database expired");exit()
hi= vetha.cursor()

g={}

def sendmain(mailid):
    print(mailid)


def welcome():
    user_frame.grid_forget()
    welcome_frame.grid(row=0)



def stringfy(ls):
    string="{} who completed his {} and , who is interested in {} \n with experience of about {} years in {} domain \n can be contacted through {} and {}".format(ls[0],ls[1],ls[5],ls[3],ls[4],ls[-3],ls[-2])
    return string


def update_to_db():
    name=inputbox1.get()
    Qulaification=inputbox2.get()
    dob=inputbox3.get()
    experience=inputbox4.get()
    domain=inputbox5.get()
    interest=inputbox6.get()
    Certifications=inputbox7.get()
    num=inputbox8.get()
    email=inputbox9.get()
    age=inputbox10.get()

    qwery= "insert into details(Name,Qualification,Date_of_birth,Experience,Domain,Interest,Certifications,number,email,age) values('{}','{}','{}',{},'{}','{}','{}',{},'{}',{});".format(name,Qulaification,dob,experience,domain,interest,Certifications,num,email,age)
    print(qwery)
    
    hi.execute(qwery)
    
    vetha.commit()
    messagebox.showinfo("showinfo", "Submitted sucessfullly")
    exit()
    #messagebox.showerror("showerror", "Error")
  
def get_user_frame():
    welcome_frame.grid_forget()
    messagebox.showinfo("Info","Welcome user")
    user_frame.grid(row=0)



def get_recuiter_frame():
    welcome_frame.grid_forget()
    messagebox.showinfo("Info","Welcome recuiter")
    recuiter_frame.grid(row=0,column=0)
    
    info_frame.grid(row=0,column=2)


def final_round(qw):
    print(qw)
    messagebox.showinfo("Info",qw)

def sel():
   selection = "You selected the option " + str(v.get())
   label.config(text = selection)


def search():
    a,b,c=e1.get(),e2.get(),e3.get()
    qwery="select * from details where Domain ='{}' and Interest='{}' and Experience = {};".format(a,b,c)
    print(qwery)
    hi.execute(qwery)
    result = hi.fetchall()
    vetha.commit()
    messagebox.showinfo("showinfo", " retriveing from database")
    #print(result)
    v = IntVar()
    i,j=3,3
    if len(result)==0:
        messagebox.showinfo("show info ","No mactches found")
    for details in result:
        qw = stringfy(details)
        d[details[0]]=qw
        print(qw)
        g[details[0]]=qw
    print(g)    
    cou=0
    for (text, value) in g.items():
        Radiobutton(info_frame, text="Option 1", variable=v, value=1,command=sel).grid(row=cou,column=5)
        cou+=1
    print("test")

def show_det(det):
    my_str.set(det)


root = Tk()
root.title("DBMS")
v = StringVar()
#user_frame.geometry("300x150")
welcome_frame=Frame(root)
welcome_frame.config(bg="#FFFF66")
welcome_frame.grid(row=0)

user_frame = Frame(root)
user_frame.config(bg="#CC33FF")
recuiter_frame=Frame(root)
recuiter_frame.config(bg="#CC33FF")
info_frame=Frame(root)
info_frame.config(bg="#CC33FF")
label = Label(info_frame)
label.grid(row=0)
details_lbel=Label(info_frame, text ='Eligible candidates',font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
details_lbel.grid(row=5,column=8)


info = Frame(root)
info.config(bg="#CC33FF")

my_str = StringVar()
l1 = Label(info,  textvariable=my_str, width=10 )
l1.grid(row=14,column=1,columnspan=5)



#Welcome_label = Label(info_frame,text="Who u are??",bg="#FF007F",foreground = 'black',font=("Times", "24", "bold italic")).grid(row=0,column=1,columnspan=3)





#creating and deploying componets for welcome frame


Welcome_label = Label(welcome_frame,text="Who u are??",bg="#FF007F",foreground = 'black',font=("Times", "24", "bold italic")).grid(row=0,column=1,columnspan=3)

#photo = PhotoImage(file = "b1.png")
#photoimage = photo.subsample(7, 7)
b1 = Button(welcome_frame,text="User",command=get_user_frame,bg="black",foreground = 'white',font=("Times", "24", "bold italic")).grid(row=3,column=1,padx=10,pady=10)
b1 = Button(welcome_frame,text="Recruiter",command=get_recuiter_frame,bg="black",foreground = 'white',font=("Times", "24", "bold italic")).grid(row=3,column=3)




l1=Label(recuiter_frame, text ='In which domain do u need to search?',font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
l2=Label(recuiter_frame, text ='Which interest of candidates do u need?',font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
l3=Label(recuiter_frame, text ='what experience do u need?',font=("Times", "24", "bold italic"),bg="black",foreground = 'white')



e1=Entry(recuiter_frame,font=("Times", "24", "bold italic"),bg="#CCFFFF",foreground = 'black')
e2=Entry(recuiter_frame,font=("Times", "24", "bold italic"),bg="#CCFFFF",foreground = 'black')
e3=Entry(recuiter_frame,font=("Times", "24", "bold italic"),bg="#CCFFFF",foreground = 'black')

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)

search_button=Button(recuiter_frame ,text="Search",command=search,font=("Times", "24", "bold italic"),bg="#FF3333").grid(row=4,column=1)



#create components for User frame

label1 = Label(user_frame, text ='Name', font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
label2 = Label(user_frame, text ='Qulaification', font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
label3 = Label(user_frame, text ='DOB', font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
label4 = Label(user_frame, text ='Experience', font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
label5 = Label(user_frame, text ='Domain', font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
label6 = Label(user_frame, text ='Interest', font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
label7 = Label(user_frame, text ='Certifications', font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
label8 = Label(user_frame, text ='Contact number', font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
label9 = Label(user_frame, text ='E-mail', font=("Times", "24", "bold italic"),bg="black",foreground = 'white')
label10 = Label(user_frame, text ='Age:', font=("Times", "24", "bold italic"),bg="black",foreground = 'white')


inputbox1= Entry(user_frame,font=("Times", "24", "bold italic"),bg="#CCFFFF",foreground = 'black')
inputbox2= Entry(user_frame,font=("Times", "24", "bold italic"),bg="#CCFFFF",foreground = 'black')
inputbox3= Entry(user_frame,font=("Times", "24", "bold italic"),bg="#CCFFFF",foreground = 'black')
inputbox4= Entry(user_frame,font=("Times", "24", "bold italic"),bg="#CCFFFF",foreground = 'black')
inputbox5= Entry(user_frame,font=("Times", "24", "bold italic"),bg="#CCFFFF",foreground = 'black')
inputbox6= Entry(user_frame,font=("Times", "24", "bold italic"),bg="#CCFFFF",foreground = 'black')
inputbox7= Entry(user_frame,font=("Times", "24", "bold italic"),bg="#CCFFFF",foreground = 'black')
inputbox8= Entry(user_frame,font=("Times", "24", "bold italic"),bg="#CCFFFF",foreground = 'black')
inputbox7= Entry(user_frame,font=("Times", "24", "bold italic"),bg="#CCFFFF",foreground = 'black')
inputbox9= Entry(user_frame,font=("Times", "24", "bold italic"),bg="#CCFFFF",foreground = 'black')
inputbox10=Entry(user_frame,font=("Times", "24", "bold italic"),bg="#CCFFFF",foreground = 'black')

button1 = Button(user_frame, text ="Submit", font=("Times", "24", "bold italic"),command=update_to_db,bg="#FF3333")
#backbutton= Button(user_frame, text ="Back", font ='50',command=welcome)
#backbutton2= Button(recuiter_frame, text ="Back", font ='50',command=welcome)
#Deploy the componnets

inputbox1.grid(row=0,column=1)
inputbox2.grid(row=1,column=1)
inputbox3.grid(row=2,column=1)
inputbox4.grid(row=3,column=1)
inputbox5.grid(row=4,column=1)
inputbox6.grid(row=5,column=1)
inputbox7.grid(row=6,column=1)
inputbox8.grid(row=7,column=1)
inputbox9.grid(row=8,column=1)
inputbox10.grid(row=9,column=1)



label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
label4.grid(row=3,column=0)
label5.grid(row=4,column=0)
label6.grid(row=5,column=0)
label7.grid(row=6,column=0)
label8.grid(row=7,column=0)
label9.grid(row=8,column=0)
label10.grid(row=9,column=0)



button1.grid(row=12,column=1)
#backbutton.grid(row=13,column=1)


root.mainloop()

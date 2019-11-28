from tkinter import *
import sqlite3

#Email id and password for sending email
sender='Example@gmail.com'
password='password'
#Sinch Rest Api service id and token for sending SMS
service_plan_id='4963f07d6b3f41eda2b1407657f6c69d'
token='a2da539ab75843c6afb1ea19ec1108ec'

def email(reciever,message):
    import smtplib 

    # creates SMTP session 
    s = smtplib.SMTP(host='smtp.gmail.com', port=587) 

    # start TLS for security 
    s.starttls() 

    # Authentication 
    s.login(sender, password) 

    # message to be sent 
    message = "Message_you_need_to_send"

    # sending the mail 
    s.sendmail(sender, reciever, message) 

    # terminating the session 
    s.quit()
# python script for sending message update 




import clx.xms
import requests
def SMS(number,message):
    client = clx.xms.Client(service_plan_id={'4963f07d6b3f41eda2b1407657f6c69d'}, token={'a2da539ab75843c6afb1ea19ec1108ec'})

    create = clx.xms.api.MtBatchTextSmsCreate()
    create.sender = '12345'
    create.recipients = {number}
    create.body = message

    try:
        batch = client.create_batch(create)
    except(requests.exceptions.RequestException,clx.xms.exceptions.ApiException) as ex:
        print('Failed to communicate with XMS: %s' % str(ex))

def Signup_window():
    global top,window
    
    if window==1:
        top.withdraw()
    window=1
    
    global flag,USERNAME,PASSWORD,lbl_text 
    
    top=Toplevel()
    top.geometry("1400x700+0+0")
    top.title("SIGNUP")
    image1 =PhotoImage(file="Signup.png")
    top.wm_attributes('-fullscreen', 'true')
    Form1 = Label(top, image=image1)
    Form1.pack(side='top', fill='both', expand='yes')
    close = PhotoImage(master=top, file="close.png")
    Button(top, bd=0, image=close, command=top.destroy).place(x=1320,y=10)
    USERNAME = StringVar()
    PASSWORD = StringVar()
   

    lbl_username = Label(Form1, text = "Email ID:", font=(14), bd=10)
    lbl_username.place(x=450,y=350)
    lbl_password = Label(Form1, text = "Password:", font=(14), bd=10)
    lbl_password.place(x=450,y=430 )
    lbl_text = Label(Form1)
    lbl_text.place(x=50,y=50)

    
   
    username = Entry(Form1, textvariable=USERNAME, font=(14))
    username.place(x=570, y=360)
    password = Entry(Form1, textvariable=PASSWORD, show="*", font=(14))
    password.place(x=570, y=440)
    
    sign_up = PhotoImage(file="signup_button.png")
    btn_Signup = Button(Form1, text="Sign Up", image=sign_up, command=Signup)
    btn_Signup.place(x=450, y=500)
    btn_Signup.bind('<Return>', Signup)
    sign_in = PhotoImage(file="sign_in.png")
    btn_sign = Button(Form1, text="Sign IN",image=sign_in, command=login_window)
    btn_sign.place(x=1200, y=10)
    btn_sign.bind('<Return>',login_window )
    top.mainloop()
def Signup():
        
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
        USERNAME.set("")
        PASSWORD.set("")
    else:
        Database_Signup()
        lbl_home = Label(root, text="Successfully Registered!", font=(20)).pack()
        login_window()
    
    #lbl_text.config(text="")
       
    
def Database_Signup():
    global conn, cursor,flag,USERNAME,PASSWORD
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("CREATE TABLE member (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        
    except:
        cursor.execute("INSERT INTO member (username, password) VALUES(?,?)",(USERNAME.get(), PASSWORD.get()))
        
    conn.commit()
    cursor.close()
    conn.close()
def login_window():
    global top,window
    if window==1:
        top.withdraw()
    window=1
    global flag,USERNAME,PASSWORD,lbl_text
    top=Toplevel()
    top.geometry("1400x700+0+0")
    top.title("Login")
    image1 =PhotoImage(file="login.png")
    top.wm_attributes('-fullscreen', 'true')
    Form = Label(top, image=image1)
    Form.pack(side='top', fill='both', expand='yes')
    close = PhotoImage(master=top, file="close.png")
    Button(top, bd=0, image=close,  command=top.destroy).place(x=1320,y=10)
    USERNAME = StringVar()
    PASSWORD = StringVar()
    

    lbl_username = Label(Form, text = "Username:", font=(14), bd=10)
    lbl_username.place(x=50,y=450)
    lbl_password = Label(Form, text = "Password:", font=(14), bd=10)
    lbl_password.place(x=50,y=530 )
    lbl_text = Label(Form)
    lbl_text.place(x=50,y=50)

    
   
    username = Entry(Form, textvariable=USERNAME, font=(14))
    username.place(x=170, y=460)
    password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
    password.place(x=170, y=540)
    
    flag=0
    login_button = PhotoImage(file="login_button.png")
    btn_login = Button(Form, text="Login", image=login_button, command=Login)
    btn_login.place(x=50, y=600)
    btn_login.bind('<Return>', Login)
    register_button = PhotoImage(file="register_button.png")
    btn_signup = Button(Form,image=register_button, command=Signup_window)
    btn_signup.place(x=1200, y=10)
    btn_signup.bind('<Return>', Signup_window)
    top.mainloop()

    
def Database():
    global conn,cursor,flag,USERNAME,PASSWORD
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE member (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        
    except:
        cursor.execute("SELECT * FROM member WHERE username = ? AND password = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            flag=1
    conn.commit()
    cursor.close()
    conn.close()

    
    
def Login():
    global flag,USERNAME,PASSWORD   
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
        USERNAME.set("")
        PASSWORD.set("")
    else:
        Database()
        if flag==1:
            lbl_home = Label(top, text="Successfully Login!", font=(20)).pack()
            Check_in_out()
            
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    
    #lbl_text.config(text="")
def Check_in_out():
    global top,window
    if window==1:
        top.withdraw()
    window=1
    top = Toplevel()
    top.title("Input Page")
    top.wm_attributes('-fullscreen', 'true')
    bg = PhotoImage(master=top,file="bg.png")
    Label(top, image=bg).place(relwidth=1, relheight=1)
    close = PhotoImage(master=top, file="close.png")
    check_in1 = PhotoImage(master=top, file="check_in.png")
    check_out1 = PhotoImage(master=top, file="check_out.png")
    Button(top, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=top.destroy).place(x=1320,y=10)
    Button(top, bd=0, image=check_in1, bg=lightBG, activebackground=lightBG, command=check_in).place(x=400,y=300)
    Button(top, bd=0, image=check_out1, bg=lightBG, activebackground=lightBG, command=check_out).place(x=600,y=300)
    top.mainloop()

def check_in():
    #filling_details
    global top,window
    global name,gender,phone,email_address,check_in,host_name,host_phone,host_email
   
    if window==1:
        top.withdraw()
    window=1
    top = Toplevel()
    top.title("Input Page")
    top.wm_attributes('-fullscreen', 'true')
    bg = PhotoImage(master=top,file="bg.png")
    Label(top, image=bg).place(relwidth=1, relheight=1)
    close = PhotoImage(master=top, file="close.png")
    Button(top, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=top.destroy).place(x=1320,y=10)
    Label(top,text="Enter the Details", font=("Courier",30,"bold underline"),bg=lightBG, fg="#27292b").place(x=490,y=130)
    Label(top, text="Name*: ", fg="#27292b",font=("Arial Black",12), bg=lightBG).place(x=520, y=260)
    #gender
    Label(top, text="Gender*: ",fg="#27292b" , font=("Arial Black",12), bg=lightBG). place(x=520, y=290)
    
    Label(top, text="Phone Number*: ", fg="#27292b",font=("Arial Black",12), bg=lightBG).place(x=520, y=320)

    Label(top, text="Email Address*: ",fg="#27292b" ,font=("Arial Black",12), bg=lightBG).place(x=520,y=350)
    
    Label(top, text="Check-in time*: ",fg="#27292b" ,font=("Arial Black",12), bg=lightBG).place(x=520,y=390)
        
    Label(top, text="Host name*: ",fg="#27292b" ,font=("Arial Black",12), bg=lightBG). place(x=520, y=430)

    Label(top, text="Host Phone Number *: ",fg="#27292b" ,font=("Arial Black",12), bg=lightBG). place(x=520, y=470)

    Label(top, text="Host Email Address *: ",fg="#27292b" ,font=("Arial Black",12), bg=lightBG). place(x=520, y=510)

    name = Entry(top, font=("Arial",12)) 
    gender=IntVar()   
    phone = Entry(top, font=("Arial",12))
    check_in = Entry(top, font=("Arial",12))
    email_address = Entry(top, font=("Arial",12))
    host_name = Entry(top, font=("Arial",12))
    host_phone = Entry(top, font=("Arial",12))
    host_email = Entry(top, font=("Arial",12))
    
    name.place(x=720, y=260)
    phone.place(x=720, y=320)
    check_in.place(x=720, y=350)
    email_address.place(x=720, y=390)
    host_name.place(x=720, y=430)
    host_phone.place(x=720, y=470)
    host_email.place(x=720,y=510)
    Radiobutton(top, text="Male",font=("Arial",12),  variable=gender, value=1).place(x=720, y=290)
    Radiobutton(top, text="Female",font=("Arial",12), variable=gender, value=2).place(x=820, y=290)

    lbl_text = Label(top)
    lbl_text.place(x=50,y=50)
    
    start_img = PhotoImage(file="continue.png")
    Button(top, text="Click Here", relief=RIDGE, image=start_img, bg=darkBG, activebackground=darkBG, bd=0, command=Input).place(x=640, y=590)
      
    top.mainloop()
    return
def Input():
    global name,gender,phone,email_address,check_in,host_name,host_phone,host_email
    if host_email.get() == "" or host_phone.get() == "" or host_name.get() == "" or phone.get() == "" or check_in.get() == "" or email_address.get() == "" or name.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
        name.set("")
        host_name.set("")
        phone.set("")
        check_in.set("")
        email.set("")
        host_email.set("")
        host_phone.set("")
    else:
        Input_Database()
        
def Input_Database():
    global conn, cursor,flag,name,host_name,check_in,gender,phone,email_address,host_phone,host_email,check_in_id
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    if(gender.get()==1):
        Gen='male'
    else:
        Gen='female'
    try:
        cursor.execute("INSERT INTO user_details (name,gender,phone,check_in,check_out,email_address,host_name,host_phone,host_email) VALUES(?,?,?,?,?,?,?,?,?)",(name.get(), Gen, phone.get(), check_in.get(),"Nil",email_address.get(), host_name.get(), host_phone.get(),host_email.get()))
        cursor.execute("SELECT mem_id FROM user_details ORDER BY mem_id DESC LIMIT 1")
        check_in_id=cursor.fetchone()
    except:
        cursor.execute("CREATE TABLE user_details (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, name TEXT, gender TEXT, phone TEXT, check_in TEXT, check_out TEXT, email_address TEXT, host_name TEXT, host_phone TEXT, host_email TEXT)")
        cursor.execute("INSERT INTO user_details (name,gender,phone,check_in,check_out,email_address,host_name,host_phone,host_email) VALUES(?,?,?,?,?,?,?,?,?)",(name.get(), Gen, phone.get(), check_in.get(),"Nil",email_address.get(), host_name.get(), host_phone.get(),host_email.get()))
        cursor.execute("SELECT mem_id FROM user_details ORDER BY mem_id DESC LIMIT 1")
        check_in_id=list(cursor.fetchone())[0]
    conn.commit()
    cursor.close()
    conn.close()
    Id_display()

def Id_display():
    global top,window,name,host_name,check_in,gender,phone,email_address,host_phone,host_email,check_in_id
    print("input")
    if window==1:
        top.withdraw()
    window=1
    top = Toplevel()
    top.title("Input Page")
    top.wm_attributes('-fullscreen', 'true')
    bg = PhotoImage(master=top,file="bg.png")
    Label(top, image=bg).place(relwidth=1, relheight=1)
    close = PhotoImage(master=top, file="close.png")
    Button(top, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=top.destroy).place(x=1320,y=10)
    Label(top,text="Your Check In Id is :-"+str(check_in_id), font=("Courier",30,"bold underline"),bg=lightBG, fg="#27292b").place(x=490,y=130)
    start_img = PhotoImage(file="continue.png")
    Button(top, text="Click Here", relief=RIDGE, image=start_img, bg=darkBG, activebackground=darkBG, bd=0, command=Check_in_out).place(x=640, y=590) 
    message="Visitors details:- \n Name"+str(name.get())+"\nEmail "+str(email_address.get())+"\nPhone "+str(phone.get())+"\nCheck in time "+str(check_in.get())
    print(message)
    try:
        email(host_email.get(),message)
        SMS(host_phone.get(),message)
    except:
        print("please enter the email address and password in the starting of the code also the credentials for Sinch application" )
   
        
        
    top.mainloop()
    
def check_out():

    global top,window,ID,check_out
    
    if window==1:
        top.withdraw()
    window=1
    top = Toplevel()
    top.title("Input Page")
    top.wm_attributes('-fullscreen', 'true')
    bg = PhotoImage(master=top,file="bg.png")
    Label(top, image=bg).place(relwidth=1, relheight=1)
    close = PhotoImage(master=top, file="close.png")
    Button(top, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=top.destroy).place(x=1320,y=10)
    Label(top,text="Enter the Details", font=("Courier",30,"bold underline"),bg=lightBG, fg="#27292b").place(x=490,y=130)
    Label(top, text="ID*: ", fg="#27292b",font=("Arial Black",12), bg=lightBG).place(x=520, y=260)
    Label(top, text="Check Out Time*: ", fg="#27292b",font=("Arial Black",12), bg=lightBG).place(x=520, y=290)
    ID = Entry(top, font=("Arial",12))
    ID.place(x=720, y=260)
    check_out = Entry(top, font=("Arial",12))
    check_out.place(x=720, y=290)
    start_img = PhotoImage(file="continue.png")
    Button(top, text="Click Here", relief=RIDGE, image=start_img, bg=darkBG, activebackground=darkBG, bd=0, command=check_database).place(x=640, y=590) 
    top.mainloop()
def check_database():
    global top,window,ID,update_id,det
    print("input")
    if window==1:
        top.withdraw()
    window=1
    top = Toplevel()
    top.title("Input Page")
    top.wm_attributes('-fullscreen', 'true')
    bg = PhotoImage(master=top,file="bg.png")
    Label(top, image=bg).place(relwidth=1, relheight=1)
    close = PhotoImage(master=top, file="close.png")
    Button(top, bd=0, image=close, bg=lightBG, activebackground=lightBG, command=top.destroy).place(x=1320,y=10)
    global conn, cursor,flag,ID
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    update_id=ID.get()
    cursor.execute("SELECT * FROM user_details WHERE mem_id= ? ", (ID.get()))
    det=cursor.fetchone()
    if det is None:
        Label(top,text="User does not exist", font=("Courier",30,"bold underline"),bg=lightBG, fg="#27292b").place(x=490,y=130)
    else:
        det=list(det)
        Label(top, text="Name*: "+str(det[1]), fg="#27292b",font=("Arial Black",12), bg=lightBG).place(x=520, y=260)
        #gender
        Label(top, text="Gender*: "+str(det[2]),fg="#27292b" , font=("Arial Black",12), bg=lightBG). place(x=520, y=290)
        
        Label(top, text="Phone Number*: "+str(det[3]), fg="#27292b",font=("Arial Black",12), bg=lightBG).place(x=520, y=320)

        Label(top, text="Email Address*: "+str(det[4]),fg="#27292b" ,font=("Arial Black",12), bg=lightBG).place(x=520,y=350)
        
        Label(top, text="Check-in time*: "+str(det[6]),fg="#27292b" ,font=("Arial Black",12), bg=lightBG).place(x=520,y=390)
            
        Label(top, text="Host name*: "+str(det[7]),fg="#27292b" ,font=("Arial Black",12), bg=lightBG). place(x=520, y=430)

        Label(top, text="Host Phone Number *: "+str(det[8]),fg="#27292b" ,font=("Arial Black",12), bg=lightBG). place(x=520, y=470)

        Label(top, text="Host Email Address *: "+str(det[9]),fg="#27292b" ,font=("Arial Black",12), bg=lightBG). place(x=520, y=510)
    conn.commit()
    cursor.close()
    conn.close()
    start_img = PhotoImage(file="continue.png")
    Button(top, text="Click Here", relief=RIDGE, image=start_img, bg=darkBG, activebackground=darkBG, bd=0, command=Update_database).place(x=640, y=590) 
    b3=Button(top,justify = LEFT)
    photo3=PhotoImage(file="backbutton.png")
    b3.config(image=photo3,width="200",height="55",activebackground="#f15922",bg="#005367",bd=0,command=check_out)
    b3.place(x=900,y=600)
    top.mainloop()  
def Update_database():
    global conn, cursor,flag,update_id,check_out,det
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE user_details SET check_out = ? WHERE mem_id= ?",(check_out.get(),update_id))
    conn.commit()
    cursor.close()
    conn.close()
    message="Visitors details:- \nName "+str(det[1])+"\nEmail "+str(det[4])+"\nPhone "+str(det[3])+"\nCheck in time "+str(det[6])+"\nCheck out time "+str(check_out.get())+"\nHost details :- "+"\nHost name "+str(det[7])+"\nPhone number "+str(det[8])+"\nEmail address "+str(det[9])
    print(message)
    try:
        email(det[4],message)
        SMS(det[3],message)
    except:
        print("please enter the email address and password in the starting of the code also the credentials for Sinch application" )
   
    Check_in_out()
    
lightBG, darkBG = "#eafde7", "#44484b"    
root=Tk()
root.withdraw()
global window
window=0
login_window()

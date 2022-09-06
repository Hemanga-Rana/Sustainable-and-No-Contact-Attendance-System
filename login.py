from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from turtle import title
from webbrowser import get
from PIL import Image,ImageTk
import mysql.connector
from time import strftime
from tkinter import font
import tkinter
from datetime import datetime
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"college_images\backg1.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1= Image.open(r"college_images\username2.png")
        img1=img1.resize((90,90),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("timmes new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=97,y=100)

        # Label
        username=lbl=Label(frame,text="Usesrname",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=222)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        ############## Icon Images ################
        img2=Image.open(r"college_images\username2.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)


        img3=Image.open(r"college_images\password2.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)


        # LoginButton 
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # RegistrationButton 
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        # ForgetButton 
        registerbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field requird")
        elif self.txtuser.get()=="hemanga" and self.txtpass.get()=="rana":
            messagebox.showinfo("Success","Welcome to the Major Project")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Cs@190032",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                                ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main= messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


    ################ Reset Password ###############
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter the Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Cs@190032",database="face_recognizer")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get().self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login new password",parent=self.root2)
                self.root2.destroy()


    ################## Forgot Password ##################

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset Password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Cs@190032",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+620+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.pllace(x=0,y=10,relwidth=1)


                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        ############# Text Variable ##############
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        ################ bg Image #################
        self.bg=ImageTk.PhotoImage(file=r"college_images\backg3.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        ################ left Image #################
        self.bg1=ImageTk.PhotoImage(file=r"college_images\student5.jpg")
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=50,y=100,width=470,height=550)

        ####### Main Frame #############
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)


        ################# Label and Entry ################

        ###  row1 ####

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)


        ### row2 ####

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)



        ### row3 ####

        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)


        ### row4 ####

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)


        ##################### Check Button #############
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions", font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)


        ############## Button ##############
        img=Image.open(r"college_images\login.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman", 15,"bold"))
        b1.place(x=10,y=420,width=200)

        img1=Image.open(r"college_images\register.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman", 15,"bold"))
        b1.place(x=330,y=420,width=200)


    ################ Function Declearation #################

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Cs@190032",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")


    def return_login(self):
        self.root.destroy()



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        # width_value= self.root.winfo_screenwidth()
        # height_value=self.root.winfo_screenheight()
        # self.root.geometry("%dx%d+0+0" % (width_value, height_value))
        self.root.title("face Recognition System")


        # First Image
        img=Image.open(r"college_images\christmas.jpg")
        img=img.resize((1650,130),Image.ANTIALIAS)# Convert the high level image to low level through ANTIALIAS
        self.photoimg= ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1650,height=130)


        # Second Image
        # img1=Image.open(r"college_images\corona2.jpg")
        # img1=img1.resize((500,130),Image.ANTIALIAS)
        # self.photoimg1= ImageTk.PhotoImage(img1)

        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=500,y=0,width=500,height=130)


        # # Third Image
        # img2=Image.open(r"college_images\corona2.jpg")
        # img2=img2.resize((550,130),Image.ANTIALIAS)
        # self.photoimg2= ImageTk.PhotoImage(img2)

        # f_lbl=Label(self.root,image=self.photoimg2)
        # f_lbl.place(x=1000,y=0,width=550,height=130)


        # BG Image
        img3=Image.open(r"college_images\bg3.jfif")
        img3=img3.resize((1650,710),Image.ANTIALIAS)
        self.photoimg3= ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1650,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="darkred")
        title_lbl.place(x=0,y=0,width=1532,height=45)

        ####################### Time #######################
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(100, time)

        lbl = Label(title_lbl, font = ('times new roman',14, 'bold'),background = 'white',foreground='blue')
        lbl.place(x=0,y=0,width=110, height=50)
        time()


        # Student Button
        img4=Image.open(r"college_images\student.jpg")
        img4=img4.resize((220,230),Image.ANTIALIAS)
        self.photoimg4= ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=100,width=220,height=230)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkred",fg="White")
        b1_1.place(x=150,y=310,width=220,height=40)

        # Train Face Button
        img8=Image.open(r"college_images\setting2.jpg")
        img8=img8.resize((220,230),Image.ANTIALIAS)
        self.photoimg8= ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=150,y=400,width=220,height=230)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkred",fg="White")
        b1_1.place(x=150,y=610,width=220,height=40)


        # Face Detection Botton
        img5=Image.open(r"college_images\face.jpg")
        img5=img5.resize((220,230),Image.ANTIALIAS)
        self.photoimg5= ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=480,y=100,width=220,height=230)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkred",fg="White")
        b1_1.place(x=480,y=310,width=220,height=40)

        # Attendance Face Button
        img6=Image.open(r"college_images\attend.jpg")
        img6=img6.resize((220,230),Image.ANTIALIAS)
        self.photoimg6= ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=480,y=400,width=220,height=230)
        # b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkred",fg="White")
        b1_1.place(x=480,y=610,width=220,height=40)
        # b1_1.place(x=800,y=300,width=220,height=40)



        ######### Right Buttons ###############
        # main_frame=Frame(bg_img,bd=2,bg="white")
        # main_frame.place(x=840,y=100,width=575,height=515)

        # Photoes Face Button
        img9=Image.open(r"college_images\photo1.png")
        img9=img9.resize((120,120),Image.ANTIALIAS)
        self.photoimg9= ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",borderwidth=1,command=self.open_img)
        b1.place(x=850,y=100,width=120,height=120)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",borderwidth=0,command=self.open_img,font=("times new roman",24,"bold"),bg="white",fg="darkred")
        b1_1.place(x=969,y=100,width=400,height=120)


        # Developer Face Button
        img10=Image.open(r"college_images\developer2.jpg")
        img10=img10.resize((120,120),Image.ANTIALIAS)
        self.photoimg10= ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",borderwidth=1,command=self.developer_data)
        b1.place(x=850,y=230,width=120,height=120)

        b1_1=Button(bg_img,text="TEAM DETAILS",cursor="hand2",borderwidth=0,command=self.developer_data,font=("times new roman",24,"bold"),bg="white",fg="darkred")
        b1_1.place(x=969,y=230,width=400,height=120)


        # Help Face Button
        img7=Image.open(r"college_images\help.jpg")
        img7=img7.resize((120,120),Image.ANTIALIAS)
        self.photoimg7= ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",borderwidth=1,command=self.help_data)
        b1.place(x=850,y=400,width=120,height=120)

        b1_1=Button(bg_img,text="Help Face",cursor="hand2",borderwidth=0,command=self.help_data,font=("times new roman",24,"bold"),bg="white",fg="darkred")
        b1_1.place(x=969,y=400,width=400,height=120)


        # Exit Face Button
        img11=Image.open(r"college_images\exit.png")
        img11=img11.resize((120,120),Image.ANTIALIAS)
        self.photoimg11= ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",borderwidth=1,command=self.iExit)
        b1.place(x=850,y=530,width=120,height=120)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",borderwidth=0,command=self.iExit,font=("times new roman",24,"bold"),bg="white",fg="darkred")
        b1_1.place(x=969,y=530,width=400,height=120)


    def open_img(self):
        os.startfile("data")


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    #############Function Buttons###############

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__ == "__main__":
    main()

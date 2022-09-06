from time import strftime
from tkinter import*
from tkinter import ttk
from tkinter import font
import tkinter
from turtle import title
from time import strftime
from datetime import datetime
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


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

        b1_1=Button(bg_img,text="TEAM",cursor="hand2",borderwidth=0,command=self.developer_data,font=("times new roman",24,"bold"),bg="white",fg="darkred")
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
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
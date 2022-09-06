# from cgitb import text
from tkinter import*
from tkinter import ttk
# from tkinter import font
# from turtle import title, width, ycor
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        title_lbl=Label(self.root,text="TEAM DETAILS",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_images\backg2.jpg")
        img_top=img_top.resize((1530,800),Image.ANTIALIAS)
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=800)

        #frame        
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=500,y=30,width=500,height=670)

        img_top1=Image.open(r"college_images\MyProfile.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1= ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        #Developer Label
        dev_label=Label(main_frame,text="Name: Hemanga Rana",font=("times new roman",22,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="(Team Leader)",font=("times new roman",24,"bold"),bg="white")
        dev_label.place(x=22,y=45)

        img2=Image.open(r"college_images\team.jpeg")
        img2=img2.resize((500,460),Image.ANTIALIAS)
        self.photoimg2= ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=460)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
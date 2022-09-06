# from cgitb import text
from tkinter import*
from tkinter import ttk
# from tkinter import font
# from turtle import title, width, ycor
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        title_lbl=Label(self.root,text="Help Section",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_images\backg2.jpg")
        img_top=img_top.resize((1530,800),Image.ANTIALIAS)
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=800)

        #Help Label
        help_label=Label(f_lbl,text="Email: hemanga.rana1@gmail.com",font=("times new roman",18,"bold"),bg="white")
        help_label.place(x=550,y=400)



if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
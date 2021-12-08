from tkinter import*
from PIL import ImageTk #pip install pillow
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        #== Bg Image ==#
        self.bg=ImageTk.PhotoImage(file="Images/login.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #== Bg Image ==#
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Employee Login Form",font=("Gaudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)

        #== UserName Field ==#
        lbl_user=Label(Frame_login,text="UserName",font=("Gaudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        #== Password Field ==#
        lbl_pass=Label(Frame_login,text="Password",font=("Gaudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        #== Login Button ==#
        Login_btn=Button(self.root,text="Login",fg="white",bg="#d77377",font=("times new roman",20)).place(x=300,y=470,width=180,height=40)

    







        root=Tk()
        obj=Login(root)
        root.mainloop()
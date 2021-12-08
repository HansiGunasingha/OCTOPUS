from tkinter import*
class EMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Employee Management System")

        #== Title ==#
        title=Label(self.root,text="Employee Management System",font=("times new roman",40,"bold")bg="#010c48",fg="white").place(x=0,y=0,relwidth=1,height=70)


root=Tk()
obj=EMS(root)
root.mainloop()
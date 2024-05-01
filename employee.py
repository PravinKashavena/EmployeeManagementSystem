from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Employee:
    def __init__(self,root):
        self.root = root 
        self.root.geometry("1520x750+0+0")
        self.root.title("Employee Management System")
        #varibles 
        self.varDept = StringVar()
        self.varName= StringVar()
        self.varPhoneNo=StringVar()
        self.varDesignation = StringVar()
        self.varEmail= StringVar()
        self.varCountry= StringVar()
        self.varAdd= StringVar()
        self.varMS= StringVar()
        self.varCTC= StringVar()
        self.varDOB= StringVar()
        self.varDOJ= StringVar()
        self.varPanId= StringVar()
        self.varGender =StringVar()
        self.varList = [self.varDept,self.varName,self.varPhoneNo,self.varDesignation,
                   self.varEmail,self.varCountry,self.varAdd,self.varMS,self.varCTC,
                   self.varDOB,self.varDOJ,self.varPanId,self.varGender]

        #Adding title :

        projectTitle= Label(self.root,text="Employee Management System",font=('times new roman',30,'bold'),fg='black',bg='skyblue')
        projectTitle.place(x=0,y=0,width=1550,height=60)
        #creatin frame for images to attach

        imageFrame = Frame(self.root,bd=2, relief=RIDGE,bg="white")
        imageFrame.place(x=0,y=60,width=1550,height=160)
        #image one :

        x= Image.open("Images/img1.jpg")
        x=x.resize((520,160),Image.Resampling.LANCZOS)
        self.temp=ImageTk.PhotoImage(x)
        self.logo =Label(self.root,image=self.temp)
        self.logo.place(x=0,y=60,width=520,height=160)
        #image two:

        y= Image.open("Images/img2.jpg")
        y=y.resize((520,160),Image.Resampling.LANCZOS)
        self.temp2=ImageTk.PhotoImage(y)
        self.logo2 =Label(self.root,image=self.temp2)
        self.logo2.place(x=520,y=60,width=520,height=160)
        #image three:

        z= Image.open("Images/img3.jpg")
        z=z.resize((520,160),Image.Resampling.LANCZOS)
        self.temp3=ImageTk.PhotoImage(z)
        self.logo3 =Label(self.root,image=self.temp3)
        self.logo3.place(x=1040,y=60,width=520,height=160)
        #creating main frame :

        mainFrame = LabelFrame(self.root,bd=2, relief=RIDGE,text="Employee Information",font=('times new roman',12,'bold'),fg='red')
        mainFrame.place(x=10,y=220,width=1500,height=260)
        #creating fields insdie mainframe:

        departmentField= Label(mainFrame,text="Department",font=('times new roman',12,'bold'),fg='black')
        departmentField.grid(row=0,column=0,padx=2,sticky=W)
        deptCombo = ttk.Combobox(mainFrame,textvariable=self.varDept,font=('times new roman',12,'bold'),width=20,state='readonly',
                                 values=["Select Department","HR","Technology","Sales","Leadership","Administration"])
        deptCombo.current(0)
        deptCombo.grid(row=0,column=1,padx=2,pady=7,sticky=W)
        

        nameField = Label(mainFrame,text="Name",font=('times new roman',12,'bold'),fg='black')
        nameField.grid(row=0,column=2,padx=2,sticky=W)
        nameEntry = ttk.Entry(mainFrame,textvariable=self.varName,font=('times new roman',12,'bold'),width=22)
        nameEntry.grid(row=0,column=3,padx=2,pady=7,sticky=W)

        DesignationField = Label(mainFrame,text="Designation",font=('times new roman',12,'bold'),fg='black')
        DesignationField.grid(row=1,column=0,padx=2,sticky=W)
        DesignationEntry = ttk.Entry(mainFrame,textvariable=self.varDesignation,font=('times new roman',12,'bold'),width=22)
        DesignationEntry.grid(row=1,column=1,padx=2,pady=7,sticky=W)

        EmailField = Label(mainFrame,text="Email",font=('times new roman',12,'bold'),fg='black')
        EmailField.grid(row=1,column=2,padx=2,sticky=W)
        EmailEntry = ttk.Entry(mainFrame,textvariable=self.varEmail,font=('times new roman',12,'bold'),width=22)
        EmailEntry.grid(row=1,column=3,padx=2,pady=7,sticky=W)

        AddressField = Label(mainFrame,text="Address",font=('times new roman',12,'bold'),fg='black')
        AddressField.grid(row=2,column=0,padx=2,sticky=W)
        AddressEntry = ttk.Entry(mainFrame,textvariable=self.varAdd,font=('times new roman',12,'bold'),width=22)
        AddressEntry.grid(row=2,column=1,padx=2,pady=7,sticky=W)

        MaritialStatusField= Label(mainFrame,text="MaritialStatus",font=('times new roman',12,'bold'),fg='black')
        MaritialStatusField.grid(row=2,column=2,padx=2,sticky=W)
        MaritialStatusCombo = ttk.Combobox(mainFrame,textvariable=self.varMS,font=('times new roman',12,'bold'),width=20,state='readonly',
                                 values=["Select your choice","Married","Unmarried"])
        MaritialStatusCombo.current(0)
        MaritialStatusCombo.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        DOBField = Label(mainFrame,text="DOB",font=('times new roman',12,'bold'),fg='black')
        DOBField.grid(row=3,column=0,padx=2,sticky=W)
        DOBEntry = ttk.Entry(mainFrame,textvariable=self.varDOB,font=('times new roman',12,'bold'),width=22)
        DOBEntry.grid(row=3,column=1,padx=2,pady=7,sticky=W)

        DOJField = Label(mainFrame,text="joining date",font=('times new roman',12,'bold'),fg='black')
        DOJField.grid(row=3,column=2,padx=2,sticky=W)
        DOJEntry = ttk.Entry(mainFrame,textvariable=self.varDOJ,font=('times new roman',12,'bold'),width=22)
        DOJEntry.grid(row=3,column=3,padx=2,pady=7,sticky=W)

        PANField = Label(mainFrame,text="PAN ID",font=('times new roman',12,'bold'),fg='black')
        PANField.grid(row=4,column=0,padx=2,sticky=W)
        PANEntry = ttk.Entry(mainFrame,textvariable=self.varPanId,font=('times new roman',12,'bold'),width=22)
        PANEntry.grid(row=4,column=1,padx=2,pady=7,sticky=W)

        GenderField= Label(mainFrame,text="Gender",font=('times new roman',12,'bold'),fg='black')
        GenderField.grid(row=4,column=2,padx=2,sticky=W)
        GenderCombo = ttk.Combobox(mainFrame,textvariable=self.varGender,font=('times new roman',12,'bold'),width=20,state='readonly',
                                 values=["Select Gender","Male","Female","Others"])
        GenderCombo.current(0)
        GenderCombo.grid(row=4,column=3,padx=2,pady=7,sticky=W)

        PhoneNoField = Label(mainFrame,text="PhoneNo",font=('times new roman',12,'bold'),fg='black')
        PhoneNoField.grid(row=0,column=4,padx=2,sticky=W)
        PhoneNoEntry = ttk.Entry(mainFrame,textvariable=self.varPhoneNo,font=('times new roman',12,'bold'),width=22)
        PhoneNoEntry.grid(row=0,column=5,padx=2,pady=7,sticky=W)

        CountryField = Label(mainFrame,text="Country",font=('times new roman',12,'bold'),fg='black')
        CountryField.grid(row=1,column=4,padx=2,sticky=W)
        CountryEntry = ttk.Entry(mainFrame,textvariable=self.varCountry,font=('times new roman',12,'bold'),width=22)
        CountryEntry.grid(row=1,column=5,padx=2,pady=7,sticky=W)

        CTCField = Label(mainFrame,text="CTC",font=('times new roman',12,'bold'),fg='black')
        CTCField.grid(row=2,column=4,padx=2,sticky=W)
        CTCEntry = ttk.Entry(mainFrame,textvariable=self.varCTC,font=('times new roman',12,'bold'),width=22)
        CTCEntry.grid(row=2,column=5,padx=2,pady=7,sticky=W)

        a= Image.open("Images/vitaLogo.png")
        a=a.resize((250,250),Image.Resampling.LANCZOS)
        self.tempror=ImageTk.PhotoImage(a)
        self.IFLogo =Label(self.root,image=self.tempror)
        self.IFLogo.place(x=850,y=240,width=300,height=220)
        #creating button frame:

        ButtonFrame = Frame(mainFrame,bd=2, relief=RIDGE)
        ButtonFrame.place(x=1270,y=20,width=200,height=174)

        saveBtn = Button(ButtonFrame,text="Save",command=self.addData,font=('times new roman',13,'bold'),width=18,height=1,bg='red',fg='white')
        saveBtn.grid(row=0,column=0,padx=4,pady=4)

        UpdateBtn = Button(ButtonFrame,text="Update",command=self.updateData,font=('times new roman',13,'bold'),width=18,height=1,bg='red',fg='white')
        UpdateBtn.grid(row=1,column=0,padx=4,pady=4)

        ClearBtn = Button(ButtonFrame,text="Clear",font=('times new roman',13,'bold'),width=18,height=1,bg='red',fg='white')
        ClearBtn.grid(row=2,column=0,padx=4,pady=4)

        DeleteBtn = Button(ButtonFrame,text="Delete",command=self.deleteData,font=('times new roman',13,'bold'),width=18,height=1,bg='red',fg='white')
        DeleteBtn.grid(row=3,column=0,padx=4,pady=4)
        #creating information frame :

        informationFrame = LabelFrame(self.root,bd=2, relief=RIDGE,text="Employee Information Table",font=('times new roman',12,'bold'),fg='red')
        informationFrame.place(x=10,y=480,width=1500,height=300)
        #creating search frame

        searchFrame = LabelFrame(informationFrame,bd=2, relief=RIDGE,text="Search Employee",font=('times new roman',12,'bold'),fg='red')
        searchFrame.place(x=10,y=1,width=1475,height=65)

        searchDropField = Label(searchFrame,text="search here:",font=('times new roman',12,'bold'),fg='black')
        searchDropField.grid(row=0,column=0,padx=10,sticky=W)
        searchCombo = ttk.Combobox(searchFrame,font=('times new roman',10,'bold'),width=15,state='readonly',
                                 values=["Search By","PhoneNo","PAN ID"])
        searchCombo.current(0)
        searchCombo.grid(row=0,column=1,padx=2,pady=7,sticky=W)

        searchEntry = ttk.Entry(searchFrame,width=30)
        searchEntry.grid(row=0,column=2,padx=7,pady=5,sticky=W)

        SearchBtn = Button(searchFrame,text="Search",font=('times new roman',13,'bold'),width=10,bg='red',fg='white')
        SearchBtn.grid(row=0,column=3,padx=4,pady=4)

        showAllBtn = Button(searchFrame,text="Show All",font=('times new roman',13,'bold'),width=10,bg='red',fg='white')
        showAllBtn.grid(row=0,column=4,padx=4,pady=4)
        #Creating Table Frame:

        DBFrame = LabelFrame(informationFrame,bd=2, relief=RIDGE)
        DBFrame.place(x=10,y=70,width=1475,height=195)

        hScroll = ttk.Scrollbar(DBFrame,orient=HORIZONTAL)
        vScroll = ttk.Scrollbar(DBFrame,orient=VERTICAL)
        self.employeeTable = ttk.Treeview(DBFrame,columns=('dep','name','desig',
                                                           'email','add','MS','DOB','DOJ',
                                                           'PID','Gen','Phone','Country','Sal',)
                                                           ,xscrollcommand=hScroll.set,yscrollcommand=vScroll.set)
        hScroll.pack(side=BOTTOM,fill=X)
        vScroll.pack(side=RIGHT,fill=Y)
        hScroll.config(command=self.employeeTable.xview)
        vScroll.config(command=self.employeeTable.yview)

        self.employeeTable.heading('dep',text='Department')
        self.employeeTable.heading('name',text='Name')
        self.employeeTable.heading('desig',text='Designation')
        self.employeeTable.heading('email',text='Email')
        self.employeeTable.heading('add',text='Address')
        self.employeeTable.heading('MS',text='Marriage Status')
        self.employeeTable.heading('DOB',text='Birth Date')
        self.employeeTable.heading('DOJ',text='Joining Date')
        self.employeeTable.heading('PID',text='PAN No')
        self.employeeTable.heading('Gen',text='Gender')
        self.employeeTable.heading('Phone',text='Contact')
        self.employeeTable.heading('Sal',text='Salary')
        self.employeeTable.heading('Country',text='Country')

        self.employeeTable["show"]="headings"
        self.employeeTable.pack(fill=BOTH,expand=1)
        self.employeeTable.bind("<ButtonRelease>",self.getCursor)
        self.fetchData()

    def addData(self):
        if self.varPanId.get()=="" or self.varName.get()=="" or self.varDept.get()=="":
            messagebox.showerror("ALl the fields are mandatory ")
        else:
            try:
                con=mysql.connector.connect(host="localhost",username= "root",
                                             password="test@123",database="ems")    
                addCursor = con.cursor()
                addCursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.varDept.get(),
                                                                                                           self.varName.get(),
                                                                                                           self.varDesignation.get(),
                                                                                                           self.varEmail.get(),
                                                                                                           self.varAdd.get(),
                                                                                                           self.varMS.get(),
                                                                                                           self.varDOB.get(),
                                                                                                           self.varDOJ.get(),
                                                                                                           self.varPanId.get(),
                                                                                                           self.varGender.get(),
                                                                                                           self.varPhoneNo.get(),
                                                                                                           self.varCountry.get(),
                                                                                                           self.varCTC.get(),
                                                                                                           ))
                con.commit()
                self.fetchData()
                con.close()
                messagebox.showinfo("success","Employee has been added successfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("error",f'Due to {e}',parent=self.root)

    def fetchData(self):
        con=mysql.connector.connect(host="localhost",username= "root", password="test@123",database="ems")    
        fetchCursor = con.cursor()
        fetchCursor.execute("select * from employee")
        data = fetchCursor.fetchall()
        if len(data)!=0:
            self.employeeTable.delete(*self.employeeTable.get_children())
            for i in data:
                self.employeeTable.insert("",END,values=i)
                con.commit()
            con.close()
    
    def updateData(self):
         if self.varPanId.get()=="" or self.varName.get()=="" or self.varDept.get()=="":
            messagebox.showerror("ALl the fields are mandatory ")
         else:
            try:
                con=mysql.connector.connect(host="localhost",username= "root",
                                             password="test@123",database="ems")    
                updateCursor = con.cursor()
                updateCursor.execute(("update employee set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,'Marriage_Status'=%s,'Birth_Date'=%s,'Joining_Date'=%s,Gender=%s,Contact=%s,Country=%s,Salary=%s where 'PAN_No'=%s"),(self.varDept.get(),
                                                                                                                                                                                                                                  self.varName.get(),
                                                                                                                                                                                                                                  self.varDesignation.get(),
                                                                                                                                                                                                                                  self.varEmail.get(),
                                                                                                                                                                                                                                  self.varAdd.get(),
                                                                                                                                                                                                                                  self.varMS.get(),
                                                                                                                                                                                                                                  self.varDOB.get(),
                                                                                                                                                                                                                                  self.varDOJ.get(),
                                                                                                                                                                                                                                  self.varGender.get(),                                                                                                                                                                                                                                 self.varGender.get(),
                                                                                                                                                                                                                                  self.varPhoneNo.get(),
                                                                                                                                                                                                                                  self.varCountry.get(),
                                                                                                                                                                                                                                  self.varCTC.get(),
                                                                                                                                                                                                                                  self.varPanId.get()
                                                                                                                                                                                                                                        ))
                
                con.commit()
                self.fetchData()
                con.close()
                messagebox.showinfo("Success","Information updated successfully")
            except Exception as e:
                messagebox.showerror("error",f'Due to {e}',parent=self.root)

    def deleteData(self):
        try:
            con=mysql.connector.connect(host="localhost",username= "root",
                                             password="test@123",database="ems")    
            deleteCursor = con.cursor()
            query="delete from employee where PAN_No=%s"
            param= (self.varPanId.get(),)
            deleteCursor.execute(query,param)
            con.commit()
            self.fetchData()
            con.close()
            messagebox.showinfo("Success","Information Deleted successfully")
        except Exception as e:
            messagebox.showerror("error",f'Due to {e}',parent=self.root)

    def getCursor(self,event=""):
        cursorRow = self.employeeTable.focus()
        content = self.employeeTable.item(cursorRow)
        data = content['values']

        self.varDept.set(data[0])
        self.varName.set(data[1])
        self.varDesignation.set(data[2])
        self.varEmail.set(data[3])
        self.varAdd.set(data[4])
        self.varMS.set(data[5])
        self.varDOB.set(data[6])
        self.varDOJ.set(data[7])
        self.varPanId.set(data[8])
        self.varGender.set(data[9])
        self.varPhoneNo.set(data[10])
        self.varCountry.set(data[11])
        self.varCTC.set(data[12])


2
if __name__=="__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
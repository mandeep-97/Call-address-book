from tkinter import *
from tkinter.font import Font
import os

root=Tk()



frame2 = Frame(root, width=600, height=450, bg="#016f82")
canvas = Canvas(frame2, width = 500, height = 500)
canvas.pack()
my_image=PhotoImage(file='C:\\Users\\hp\\Pictures\\logo.png')
canvas.create_image(0,0, anchor = NW, image=my_image)

root.configure(background="green")
count=0

l1=Label(root,text='Call Address Book',fg='black',font='Times')
l2=Label(root,text='Details..',fg='Black')


l3=Label(root,text='Name',fg='black')
l4=Label(root,text='E-mail id',fg='black')
l5=Label(root,text='Adress',fg='black')
l6=Label(root,text='Pin-code',fg='black')
l7=Label(root,text='phone_no',fg='black')
l8=Label(root,text='Enter-phoneNo',fg='black')

s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()

e1=Entry(root,textvariable=s1)
e2=Entry(root,textvariable=s2)
e3=Entry(root,textvariable=s3)
e4=Entry(root,textvariable=s4)
e5=Entry(root,textvariable=s5)
e6=Entry(root,textvariable=s6)

l1.grid(row=0,columns=2)
l2.grid(row=1,column=0,sticky=W)

l3.grid(row=2,sticky=W)
l4.grid(row=3,sticky=W)
l5.grid(row=4,sticky=W)
l6.grid(row=5,sticky=W)
l7.grid(row=6,sticky=W)


e1.grid(row=2,column=1)
e2.grid(row=3,column=1)
e3.grid(row=4,column=1)
e4.grid(row=5,column=1)
e5.grid(row=6,column=1)

b1=Button(root,text='Next_Record',fg='blue')
b1.grid(row=8,column=1,sticky=W)

b2=Button(root,text='Add',fg='blue')
b2.grid(row=7,column=0,sticky=W)

b3=Button(root,text="First_Rec",fg='blue')
b3.grid(row=8,column=0,sticky=W)

b4=Button(root,text='Last_Rec',fg='blue')
b4.grid(row=8,column=2,sticky=E)

b5=Button(root,text='Search',fg='blue')
b5.grid(row=9,column=2,sticky=E)

b7=Button(root,text='Delete',fg='blue')
b7.grid(row=7,column=2,sticky=E)

b8=Button(root,text='Update',fg='blue')
b8.grid(row=9,column=0,sticky=W)


def display(event):
    data=open('mandeep.txt','r')
    data_list=[]
    j=0
    s=data.readlines()
    for i in s:
        l=s[j].split()
        j+=1
        data_list.append(l)
    print(data_list)
    global count
    if count<=len(data_list)-1:
        s1.set(data_list[count][0])
        s2.set(data_list[count][1])
        s3.set(data_list[count][2])
        s4.set(data_list[count][3])
        s5.set(data_list[count][4])
        count+=1
        data.close()
    else:
        count=0


def record_added():
    l8=Label(root,text='Record Added')
    l8.grid(row=20,columns=3)
def updated():
    l8=Label(root,text='Record Updated')
    l8.grid(row=20,columns=3)

def error():
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")
    l8=Label(root,text='**Error**ALL FIELDS ARE NECESSARY')
    l8.grid(row=20,columns=3)
def data_error():
    l8=Label(root,text='INCORRECT DATE')
    l8.grid(row=20,columns=3)
def add(event):
    data=open('mandeep.txt','a')
    name=s1.get()
    email_id=s2.get()
    address=s3.get()
    pincode=s4.get()
    phone_no=s5.get()
    if name=="" or email_id=="" or address=="" or pincode=="" or phone_no=="":
        error()
    else:
        
        for i in range(len(name),14):
            name=name+" "
        for i in range(len(email_id),15):
            email_id=email_id+" "
        for i in range(len(address),14):
            address=address+" "
        for i in range(len(pincode),14):
            pincode=pincode+" "
        for i in range(len(phone_no),14):
            phone_no=phone_no+" "
        
        data.writelines(name+"  "+email_id+" "+address+" "+pincode+" "+phone_no+" "'\n')
        s1.set("")
        s2.set("")
        s3.set("")
        s4.set("")
        s5.set("")
        record_added()
    data.close()

def display_first(event):
    import re
    data=open('mandeep.txt','r')
    s=data.readline()
    string=re.sub(' +',' ',s)
    l=string.split()
    s1.set(l[0])
    s2.set(l[1])
    s3.set(l[2])
    s4.set(l[3])
    s5.set(l[4])
    data.close()
    

def display_last(event):
    data=open('mandeep.txt','r')
    for i in data:
        s=i
    string=re.sub(' +',' ',s)
    l=string.split()
    s1.set(l[0])
    s2.set(l[1])
    s3.set(l[2])
    s4.set(l[3])
    s5.set(l[4])
    data.close()


def ok(event):
    import re
    flag=1
    data=open('mandeep.txt','r')
    phn_no=s6.get()
    for i in data:
        s=i
        string=re.sub(' +',' ',s)
        l=string.split()
        if phn_no==l[4]:
            s1.set(l[0])
            s2.set(l[1])
            s3.set(l[2])
            s4.set(l[3])
            s5.set(l[4])
            flag=1
            break
        else:
            flag=0
            pass
    if flag==0:
        s1.set('**No record Found**')
        s2.set("")
        s3.set("")
        s4.set("")
        s5.set("")
    data.close()

def delete(event):
    data=open('mandeep.txt','r')
    phn_no=s6.get()
    data_list=[]
    j=0
    s=data.readlines()
    for i in s:
        l=s[j].split()
        j+=1
        data_list.append(l)
    print(data_list)
    data.close()
    data=open('mandeep.txt','w')
    for i in range(0,len(data_list)):
        if phn_no!=data_list[i][4]:
            name=data_list[i][0]
            email_id=data_list[i][1]
            address=data_list[i][2]
            pincode=data_list[i][3]
            phone_no=data_list[i][4]
            
            for i in range(len(name),14):
                name=name+" "
            for i in range(len(email_id),15):
                email_id=email_id+" "
            for i in range(len(address),14):
                address=address+" "
            for i in range(len(pincode),14):
                pincode=pincode+" "
            for i in range(len(phone_no),14):
                phone_no=phone_no+" "
            
            data.writelines(name+"  "+email_id+" "+address+" "+pincode+" "+" "+phone_no+" "'\n')
        else:
            pass
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")
    data.close()  


def update(event):
    data=open('mandeep.txt','r')
    phn_no=s6.get()
    data_list=[]
    j=0
    s=data.readlines()
    for i in s:
        l=s[j].split()
        j+=1
        data_list.append(l)
    print(data_list)
    data.close()
    
    data=open('mandeep.txt','w')
    name=s1.get()
    email_id=s2.get()
    address=s3.get()
    pincode=s4.get()
    phone_no=s5.get()
    if name=="" or email_id=="" or address=="" or pincode=="" or phone_no=="":
        error()
    else:
        
        for i in range(len(name),14):
            name=name+" "
        for i in range(len(email_id),15):
            email_id=email_id+" "
        for i in range(len(address),14):
            address=address+" "
        for i in range(len(pincode),14):
            pincode=pincode+" "
        for i in range(len(phone_no),14):
            phone_no=phone_no+" "
        
        for i in range(len(data_list)):
            if phone_no==data_list[i][-2]:
                data.writelines(name+"  "+email_id+" "+address+" "+pincode+" "+" "+phone_no+" "'\n')
            else:
                name1=data_list[i][0]
                email_id1=data_list[i][1]
                address1=data_list[i][2]
                pincode1=data_list[i][3]
                phone_no1=data_list[i][4]
                
                for i in range(len(name1),14):
                    name1=name1+" "
                for i in range(len(email_id1),15):
                    email_id1=email_id1+" "
                for i in range(len(address1),14):
                    address1=address1+" "
                for i in range(len(pincode1),14):
                    pincode1=pincode1+" "
                for i in range(len(phone_no1),14):
                    phone_no1=phone_no1+" "
                
                data.writelines(name1+" "+email_id1+" "+address1+" "+pincode1+" "+" "+phone_no1+" "'\n')            
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")
    updated()
    data.close()

def search(event):
    l8.grid(row=10,column=0)
    e6.grid(row=10,column=1)
    b5.bind('<Button-1>',ok)
    b7.bind('<Button-1>',delete)
    b8.bind('<Button-1>',update)
    
    
b1.bind('<Button-1>',display)
b2.bind('<Button-1>',add)
b3.bind('<Button-1>',display_first)
b4.bind('<Button-1>',display_last)
b5.bind('<Button-1>',search)
b7.bind('<Button-1>',search)
b8.bind('<Button-1>',search)
root.mainloop()



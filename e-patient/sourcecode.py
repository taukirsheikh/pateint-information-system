import time
from threading import *
from tkinter import *
import pyttsx3
import os
from datetime import date
import mysql.connector
import speech_recognition as s
from tkinter import messagebox
import tempfile

#connection to mysql databse

mydb = mysql.connector.connect(host = "localhost",user = "root",password = "sql@123",database = "patient")
my_cursor = mydb.cursor()
today=date.today() #gets the todays date in  yy-mm-dd format
root=Tk()
root.geometry('1000x700+122+0')
root.configure(bg='#8644f4')

#function to print details
def print_details(txt):
    temp_file=tempfile.mktemp('.txt')
    open(temp_file,'w').write(txt)
    os.startfile(temp_file,'print')

#reads the details which is in text when search button is clicked
def talk():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(details.get(1.0, END))
    engine.runAndWait()

#when search button is clicked pateint details shows up with print buttton
def search_details():
    global details


    getspid=str(search_box.get())
    my_cursor.execute('Select PID from patient_tbll where PID="'+getspid+'"')
    try:
        dbpid = my_cursor.fetchone()[0]

        infoframe = Frame(w2, bg='#885f9c')
        infoframe.place(x=300, y=0, height=700, width=700)
        details = Text(infoframe, height=40, width=90)
        details.place(x=0, y=0)
        my_cursor.execute('select * from patient_tbll where PID="'+getspid+'"')

#patient id inserted
        details.insert(1.0,'Patient ID : '+getspid) #puts id infront of patient
#fetching all details from pateint to perform text to speech
#fetch is performed again and again to store it in variable
        tsdate= str(my_cursor.fetchone()[1])

        my_cursor.execute('select * from patient_tbll where PID="' + getspid + '"')

        tsname=str(my_cursor.fetchone()[2])

        my_cursor.execute('select * from patient_tbll where PID="' + getspid + '"')

        tscontact=str(my_cursor.fetchone()[3])

        my_cursor.execute('select * from patient_tbll where PID="' + getspid + '"')

        tsdob=str(my_cursor.fetchone()[4])

        my_cursor.execute('select * from patient_tbll where PID="' + getspid + '"')

        tsaddress=my_cursor.fetchone()[5]

        my_cursor.execute('select * from patient_tbll where PID="' + getspid + '"')

        tsage=str(my_cursor.fetchone()[6])

        my_cursor.execute('select * from patient_tbll where PID="' + getspid + '"')

        tsgender=my_cursor.fetchone()[7]

        my_cursor.execute('select * from patient_tbll where PID="' + getspid + '"')

        tsbg=my_cursor.fetchone()[8]

        my_cursor.execute('select * from patient_tbll where PID="' + getspid + '"')

        tsmail=my_cursor.fetchone()[9]

        my_cursor.execute('select * from patient_tbll where PID="' + getspid + '"')

        tsec=str(my_cursor.fetchone()[10])

        my_cursor.execute('select * from patient_tbll where PID="' + getspid + '"')

        tsrtp=my_cursor.fetchone()[11]

        my_cursor.execute('select * from patient_tbll where PID="' + getspid + '"')

        tspp=my_cursor.fetchone()[12]

        my_cursor.execute('select * from patient_tbll where PID="' + getspid + '"')

        tsaf=my_cursor.fetchone()[13]

    #inserting data in text widget after fetching
        details.insert(2.0,'\nDate of Registration : '+tsdate)
        details.insert(3.0,'\nPatient Name : '+tsname )
        details.insert(4.0,'\nContact  : '+tscontact)
        details.insert(5.0,'\nDate of Birth  : ' +tsdob)
        details.insert(6.0,'\nAddress  : ' +tsaddress)
        details.insert(7.0,'\nAge  : ' +tsage)
        details.insert(8.0,'\nGender  : ' +tsgender)
        details.insert(9.0,'\nBlood Group  : ' +tsbg)
        details.insert(10.0,'\nEmail  : ' +tsmail)
        details.insert(11.0,'\nEmergency Contact  : ' +tsec)
        details.insert(12.0,'\nRelation to Patient  : ' +tsrtp)
        details.insert(13.0,'\nPrimary Physician  : ' +tspp)
        details.insert(14.0,'\nAppointed For  : ' +tsaf)

# print button to print details
        Button(infoframe, text='Print', bg='red', width=25, activebackground='green',command=lambda: print_details(details.get(1.0, END))).place(x=250, y=660)

#used threading so both text and talk can run
        t1=Thread(target=talk) #talk is a function name

        t1.start()
    except Exception as e:
        messagebox.showerror('Error','Enter Valid Patient ID')

#to insert details in databse when save button is clickced for registration
def insert_database():
    gid=l_ID_registere.get()
    gdate=l_date_registere.get()
    gname=l_name_registere.get()
    gcontact=l_contacte.get()
    gdob=l_dobe.get()
    gaddress=l_address_registere.get()
    gage=l_agee.get()
    ggen=l_gendere.get()
    gblood=l_bloodgroupe.get()
    gmail=l_mail_registere.get()
    gemerg=l_emergency_contacte.get()
    grelation=l_relatione.get()
    gdoctor=l_physiciane.get()
    gappoint=l_appointe.get(1.0,END)
    try:
        sql="INSERT INTO patient_tbll(Date,Name,Contact,DOB,Address,Age,Gender,BloodGroup,EmailAddress,EmergencyContact,RelationToPatient,PrimaryPhysician,AppointedFor) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(gdate,gname,gcontact,gdob,gaddress,gage,ggen,gblood,gmail,gemerg,grelation,gdoctor,gappoint)
        my_cursor.execute(sql,val)
        mydb.commit()
        lastid=my_cursor.lastrowid
        messagebox.showinfo("INFORMATION","Details of patient has been added successfullly")
        l_ID_registere.delete(0,END)

        l_ID_registere.insert(END,lastid+1)
    except Exception as e:
        print(e)

#registration form when registration is button is clicked
def registerform():
    global form, l_appointe,l_physiciane,l_relatione,l_emergency_contacte,l_mail_registere,l_bloodgroupe,l_gendere, l_agee,l_address_registere,l_dobe,l_contacte,l_name_registere,l_date_registere,l_ID_registere
    form = Frame(w2, bg='#8081CD')
    form.place(x=300, y=0, height=1000, width=700)

    l_date_register = Label(form, text="Date")
    l_date_register.place(x=10, y=20)

    l_date_registere=Entry(form)
    l_date_registere.place(x=150,y=20)
    l_date_registere.insert(0,today)
    # l_date_registere.configure(state=DISABLED)

    l_ID_register = Label(form, text=" Patient ID")
    l_ID_register.place(x=10,y=50)


#patient id enter
    l_ID_registere=Entry(form)
    l_ID_registere.place(x=150,y=50)
    my_cursor.execute('select * from patient_tbll ORDER BY PID DESC LIMIT 1')
    last=my_cursor.fetchone()[0]

    l_ID_registere.insert(0,last+1)
    l_ID_registere.configure(state=DISABLED)

    l_name_register = Label(form, text="Patient Name")
    l_name_register.place(x=10, y=80)

    l_name_registere=Entry(form,width=30)
    l_name_registere.place(x=150,y=80)

    l_contact=Label(form,text='Contact')
    l_contact.place(x=10,y=110)

    l_contacte=Entry(form)
    l_contacte.place(x=150,y=110)

    l_dob=Label(form, text='DOB')
    l_dob.place(x=10, y=140)

    l_dobe=Entry(form)
    l_dobe.place(x=150,y=140)
    l_dobe.insert(0,'2000-12-12')

    l_address_register= Label(form, text='Address')
    l_address_register.place(x=10, y=170)

    l_address_registere=Entry(form,width=30)
    l_address_registere.place(x=150,y=170)

    l_ag = Label(form, text='Age')
    l_ag.place(x=10, y=200)

    l_agee=Entry(form)
    l_agee.place(x=150, y=200)

    l_gender=Label(form, text='Gender')
    l_gender.place(x=10,y=230)

    l_gendere=Entry(form)
    l_gendere.place(x=150,y=230)

    l_bloodgroup=Label(form,text='Blood Group')
    l_bloodgroup.place(x=10,y=260)

    l_bloodgroupe=Entry(form)
    l_bloodgroupe.place(x=150,y=260)

    l_mail_register = Label(form, text='Email Address')
    l_mail_register.place(x=10, y=290)

    l_mail_registere=Entry(form,width=50)
    l_mail_registere.place(x=150,y=290)

    l_emergency_contact = Label(form, text='Emergency Contact')
    l_emergency_contact.place(x=10, y=320)

    l_emergency_contacte=Entry(form)
    l_emergency_contacte.place(x=150,y=320)

    l_relation=Label(form, text='Relation to Patient')
    l_relation.place(x=10,y=350)

    l_relatione=Entry(form)
    l_relatione.place(x=150,y=350)

    l_physician=Label(form, text='Primary Physician')
    l_physician.place(x=10,y=380)

    l_physiciane=Entry(form,width=30)
    l_physiciane.place(x=150,y=380)

    l_appoint=Label(form, text='Appointed for')
    l_appoint.place(x=10,y=410)

    l_appointe=Text(form,height=8,width=50)
    l_appointe.place(x=150,y=410)
     
        # KEY BINDING PROGRAM
    def datedown(event):
        #print("downkey pressed")
        l_ID_registere.focus()
    def IDupkey(event):
        #print("upkey pressed")
        l_date_registere.focus()
    def IDdown(event):
        l_name_registere.focus()
    def namedown(event):
        l_contacte.focus()
    def contdown(event):
        l_dobe.focus()
    def dobdown(event):
        l_address_registere.focus()
    def addsdown(event):
        l_agee.focus()
    def ageup(event):
        l_address_registere.focus()
    def agedown(event):
        l_gendere.focus()

    def gendown(event):
        l_bloodgroupe.focus()
    def blooddown(event):
        l_mail_registere.focus()
    def maildown(event):
        l_emergency_contacte.focus()
    def emgcdown(event):
        l_relatione.focus()
    def reladown(event):
        l_physiciane.focus()
    def phydown(event):
        l_appointe.focus()

    l_date_registere.bind('<Down>',datedown)
    l_ID_registere.bind('<Up>',IDupkey)
    l_ID_registere.bind('<Down>',IDdown)
    l_name_registere.bind('<Up>',datedown)
    l_name_registere.bind('<Down>',namedown)
    l_contacte.bind('<Up>',IDdown)
    l_contacte.bind('<Down>',contdown)
    l_dobe.bind('<Up>',namedown)
    l_dobe.bind('<Down>',dobdown)
    l_address_registere.bind('<Up>',contdown)
    l_address_registere.bind('<Down>',addsdown)
    l_agee.bind('<Up>',dobdown)
    l_agee.bind('<Down>',agedown)
    l_gendere.bind('<Up>',addsdown)
    l_gendere.bind('<Down>',gendown)
    l_bloodgroupe.bind('<Up>',agedown)
    l_bloodgroupe.bind('<Down>',blooddown)
    l_mail_registere.bind('<Up>',gendown)
    l_mail_registere.bind('<Down>',maildown)
    l_emergency_contacte.bind('<Up>',blooddown)
    l_emergency_contacte.bind('<Down>',emgcdown)
    l_relatione.bind('<Up>',maildown)
    l_relatione.bind('<Down>',reladown)
    l_physiciane.bind('<Up>',emgcdown)
    l_physiciane.bind('<Down>',phydown)
    l_appointe.bind('<Up>',reladown)


#button to save save data into data base
    l_savebutton=Button(form, text='SAVE',cursor='hand2',command=insert_database)
    l_savebutton.place(x=600,y=440)

    
#threading if no voice is detected
def novoice():
    messagebox.showerror('Error','Say Patient ID again')


#speech to text as work on voice recognition
def id_():
    sr=s.Recognizer() #sr  is a vaiable
    messagebox.showinfo('listen','Please Say Patient ID')
    # listen =Label(w2, text='i am listening')
    # listen.place(x=70, y=170)

    with s.Microphone() as m: #m is also a variable

        # messagebox.showinfo('Listening','Say Patient ID')
        audio=sr.listen(m)
        try:
            query=sr.recognize_google(audio,language='eng-in')

            # listen=Label(w2,text='i am listening')
            # listen.place(x=70,y=150)

            search_box.insert(0,query)
        except Exception as er:
            t3=Thread(target=novoice)
            t3.start()

            # messagebox.showerror('Error','Unable to Recognize Speech')

#update details in mysql database when update button is clicked
def updated_details():


    newDate = str(r_date_registere.get())
    my_cursor.execute("update patient_tbll set Date = '" + newDate + "' where PID = '" + getpid + "' ")
    mydb.commit()

    newName = str(r_name_registere.get())
    my_cursor.execute("update patient_tbll set Name = '" + newName + "' where PID = '" + getpid + "' ")
    mydb.commit()

    newContact = str(r_contacte.get())
    my_cursor.execute("update patient_tbll set Contact = '" + newContact + "' where PID = '" + getpid + "' ")
    mydb.commit()

    newDOB = str(r_dobe.get())
    my_cursor.execute("update patient_tbll set DOB = '" + newDOB + "' where PID = '" + getpid + "' ")
    mydb.commit()

    newAddress = str(r_address_registere.get())
    my_cursor.execute("update patient_tbll set Address = '" + newAddress + "' where PID = '" + getpid + "' ")
    mydb.commit()

    newAge = str(r_agee.get())
    my_cursor.execute("update patient_tbll set Age = '" + newAge + "' where PID = '" + getpid + "' ")
    mydb.commit()

    newGender = str(r_gendere.get())
    my_cursor.execute("update patient_tbll set Gender = '" + newGender + "' where PID = '" + getpid + "' ")
    mydb.commit()

    newBloodGroup = str(r_bloodgroupe.get())
    my_cursor.execute("update patient_tbll set BloodGroup = '" + newBloodGroup + "' where PID = '" + getpid + "' ")
    mydb.commit()

    newEmail = str(r_mail_registere.get())
    my_cursor.execute("update patient_tbll set EmailAddress = '" + newEmail + "' where PID = '" + getpid + "' ")
    mydb.commit()

    newEmergencyContact = str(r_emergency_contacte.get())
    my_cursor.execute(
        "update patient_tbll set EmergencyContact = '" + newEmergencyContact + "' where PID = '" + getpid + "' ")
    mydb.commit()

    newRelation = str(r_relatione.get())
    my_cursor.execute("update patient_tbll set RelationToPatient = '" + newRelation + "' where PID = '" + getpid + "' ")
    mydb.commit()

    newPhysician = str(r_physiciane.get())
    my_cursor.execute("update patient_tbll set PrimaryPhysician = '" + newPhysician + "' where PID = '" + getpid + "' ")
    mydb.commit()

    newAppoint = str(r_appointe.get(1.0,END))
    my_cursor.execute("update patient_tbll set AppointedFor = '" + newAppoint + "' where PID = '" + getpid + "' ")
    mydb.commit()
    messagebox.showinfo('Update','Patient Details Has Been Updated')

#to update patient info after clicking on update button
def fetch_details_for_update():
    global getpid
    global patientdt
    global r_date_registere
    global r_name_registere
    global r_contacte
    global r_dobe
    global r_address_registere
    global r_agee
    global r_gendere
    global r_bloodgroupe
    global r_mail_registere
    global r_emergency_contacte
    global r_relatione
    global r_physiciane
    global r_appointe
    getpid = str(search_box.get())
    # select_stmt = "SELECT * FROM patient_tbll WHERE PID = %(getpid)s"
    # rup=my_cursor.execute(select_stmt, { 'getpid': 1 })

    mysql = "select * from patient_tbll where PID = %s"
    my_cursor.execute(mysql, [(getpid)])
    result = my_cursor.fetchall()
    if result:
        patientdt = Frame(w2, bg='#8081CD')
        patientdt.place(x=300, y=0, height=1000, width=700)

        r_date_register = Label(patientdt, text="Date of Registration")
        r_date_register.place(x=10, y=20)
        my_cursor.execute("SELECT * from patient_tbll where PID = '" + getpid + "'")
        exDate = my_cursor.fetchone()[1]

        r_date_registere = Entry(patientdt)
        r_date_registere.place(x=150, y=20)
        r_date_registere.insert(0, exDate)

        r_ID_register = Label(patientdt, text=" Patient ID")
        r_ID_register.place(x=10, y=50)


        r_ID_registere = Entry(patientdt)
        r_ID_registere.place(x=150, y=50)
        r_ID_registere.insert(0, getpid)
        r_ID_registere.configure(state=DISABLED)

        r_name_register = Label(patientdt, text="Patient Name")
        r_name_register.place(x=10, y=80)
        my_cursor.execute("SELECT * from patient_tbll where PID = '" + getpid + "'")
        exName = my_cursor.fetchone()[2]

        r_name_registere = Entry(patientdt, width=30)
        r_name_registere.place(x=150, y=80)
        r_name_registere.insert(0, exName)

        r_contact = Label(patientdt, text='Contact')
        r_contact.place(x=10, y=110)
        my_cursor.execute("SELECT * from patient_tbll where PID = '" + getpid + "'")
        exContact = my_cursor.fetchone()[3]

        r_contacte = Entry(patientdt)
        r_contacte.place(x=150, y=110)
        r_contacte.insert(0, exContact)

        r_dob = Label(patientdt, text='DOB')
        r_dob.place(x=10, y=140)
        my_cursor.execute("SELECT * from patient_tbll where PID = '" + getpid + "'")
        exDOB = my_cursor.fetchone()[4]

        r_dobe = Entry(patientdt)
        r_dobe.place(x=150, y=140)
        r_dobe.insert(0, exDOB)

        r_address_register = Label(patientdt, text='Address')
        r_address_register.place(x=10, y=170)
        my_cursor.execute("SELECT * from patient_tbll where PID = '" + getpid + "'")
        exAddress = my_cursor.fetchone()[5]

        r_address_registere = Entry(patientdt, width=30)
        r_address_registere.place(x=150, y=170)
        r_address_registere.insert(0, exAddress)

        r_ag = Label(patientdt, text='Age')
        r_ag.place(x=10, y=200)
        my_cursor.execute("SELECT * from patient_tbll where PID = '" + getpid + "'")
        exAge = my_cursor.fetchone()[6]

        r_agee = Entry(patientdt)
        r_agee.place(x=150, y=200)
        r_agee.insert(0, exAge)

        r_gender = Label(patientdt, text='Gender')
        r_gender.place(x=10, y=230)
        my_cursor.execute("SELECT * from patient_tbll where PID = '" + getpid + "'")
        exGender = my_cursor.fetchone()[7]

        r_gendere = Entry(patientdt)
        r_gendere.place(x=150, y=230)
        r_gendere.insert(0, exGender)

        r_bloodgroup = Label(patientdt, text='Blood Group')
        r_bloodgroup.place(x=10, y=260)
        my_cursor.execute("SELECT * from patient_tbll where PID = '" + getpid + "'")
        exBloodGroup = my_cursor.fetchone()[8]

        r_bloodgroupe = Entry(patientdt)
        r_bloodgroupe.place(x=150, y=260)
        r_bloodgroupe.insert(0, exBloodGroup)

        r_mail_register = Label(patientdt, text='Email Address')
        r_mail_register.place(x=10, y=290)
        my_cursor.execute("SELECT * from patient_tbll where PID = '" + getpid + "'")
        exEmail = my_cursor.fetchone()[9]

        r_mail_registere = Entry(patientdt, width=50)
        r_mail_registere.place(x=150, y=290)
        r_mail_registere.insert(0, exEmail)

        r_emergency_contact = Label(patientdt, text='Emergency Contact')
        r_emergency_contact.place(x=10, y=320)
        my_cursor.execute("SELECT * from patient_tbll where PID = '" + getpid + "'")
        exEmergencyContact = my_cursor.fetchone()[10]

        r_emergency_contacte = Entry(patientdt)
        r_emergency_contacte.place(x=150, y=320)
        r_emergency_contacte.insert(0, exEmergencyContact)

        r_relation = Label(patientdt, text='Relation to Patient')
        r_relation.place(x=10, y=350)
        my_cursor.execute("SELECT * from patient_tbll where PID = '" + getpid + "'")
        exRelationToPatient = my_cursor.fetchone()[11]

        r_relatione = Entry(patientdt)
        r_relatione.place(x=150, y=350)
        r_relatione.insert(0, exRelationToPatient)

        r_physician = Label(patientdt, text='Primary Physician')
        r_physician.place(x=10, y=380)
        my_cursor.execute("SELECT * from patient_tbll where PID = '" + getpid + "'")
        exPrimaryPhysician = my_cursor.fetchone()[12]

        r_physiciane = Entry(patientdt, width=30)
        r_physiciane.place(x=150, y=380)
        r_physiciane.insert(0, exPrimaryPhysician)

        r_appoint = Label(patientdt, text='Appointed for')
        r_appoint.place(x=10, y=410)
        my_cursor.execute("SELECT * from patient_tbll where PID = '" + getpid + "'")
        exAppointedFor = str(my_cursor.fetchone()[13])

        r_appointe = Text(patientdt, height=8, width=50)
        r_appointe.place(x=150, y=410)
        r_appointe.insert(1.0, exAppointedFor)

        r_updatebutton = Button(patientdt, text='Update', cursor='hand2', command = updated_details)
        r_updatebutton.place(x=600, y=440)
    else:
        messagebox.showerror("Error", "Invalid Patient ID")
        return False

#when back button will be clicked, it will get us to log in panel
def remove_page():
    w2.destroy()

#page after login

def page():
    global w2, search_box
    
    w2=Frame(root,bg='#8644f4')
    w2.place(x=0,y=0, height=1000,width=1500)
    # search and register for patient
    search_PID = Label(w2, text="Patient ID",bg='#8644f4')
    search_PID.place(x=10, y=20)
#search box with patient id
    search_box =Entry(w2,width=30)
    search_box.place(x=70, y=20)
    search_box.focus()

    #search button
    search_info = Button(w2, text='Search',command=search_details,bg='#53e9c1',activebackground='#8ba5d7')
    search_info.place(x=100, y=50,width=100)

    voice_button = Button(w2, text='Voice Search ', command=id_,bg='#617d1f',activebackground='#8ba5d7')
    voice_button.place(x=100, y=90,width=100)
    # update button
    getinfo = Button(w2, text='Update Details', command=fetch_details_for_update,bg='#5cee42',activebackground='#8ba5d7')
    getinfo.place(x=100, y=130,width=100)

    register_button = Button(w2, text='Register', command=registerform,bg='#e6955d',activebackground='#8ba5d7')
    register_button.place(x=100, y=170,width=100)


    back_to_log_button=Button(w2, text= 'Back', command= remove_page, bg='#a2d9c5', activebackground='#8ba5d7')
    back_to_log_button.place(x=50, y=650, width=50)




#--------------------------------------- full login system----------------------------------

def update_passwd():
    New = new_passwd.get()
    Confirm = confirm_passwd.get()

    if New=="" and Confirm=="":
        messagebox.showwarning('Error','Fields are Empty')

    elif New == Confirm:

        mydb = mysql.connector.connect(host="localhost", user="root", password="sql@123", database="patient")
        my_cursor = mydb.cursor()
        my_cursor.execute("update login set Password ='" + New + "' where UserName= 'hospital' ")
        mydb.commit()
        messagebox.showinfo("", "Password Changed")
        change.destroy()
    else:
        messagebox.showerror("", "Password didn't Match")

def change_password():
    global new_passwd,change,confirm_passwd
    change = Frame(root, bg="#6a86af")
    change.place(x=250, y=100, height=500, width=500)
    Label(change, text="New Password").place(x=10, y=20)
    new_passwd = Entry(change)
    new_passwd.place(x=160, y=20)
    new_passwd.config(show="*")

    Label(change, text="Confirm New Password").place(x=10, y=60)
    confirm_passwd = Entry(change)
    confirm_passwd.place(x=160, y=60)
    confirm_passwd.config(show="*")
    Button(change, text="Change Password", command=update_passwd, cursor="hand2").place(x=140, y=100)
def security():
    mydb = mysql.connector.connect(host="localhost", user="root", password="sql@123", database="patient")
    mycursor = mydb.cursor()

    my = "select * from login where Security_Key = %s"
    Security_Key = security_box.get()
    mycursor.execute(my, [(Security_Key)])
    output = mycursor.fetchall()
    if output:
        messagebox.showinfo("", "Valid")
        forge.destroy()
        change_password()
        return True

    else:
        messagebox.showerror("", "Invalid")
        return False

def destroy_forge():
    forge.destroy()
#when forget password button will be clicked it will display another fram to enter security key
def forgot_password():
    global security_box,forge
    forge = Frame(root, bg="#283446")
    forge.place(x=250, y=100, height=500, width=500)
    Label(forge, text="Enter Security Key").place(x=90, y=220)

    security_box = Entry(forge,show='#')
    security_box.place(x=200, y=220)
    Button(forge, text="Confirm Key", command=security, cursor="hand2").place(x=220, y=250)
    Button(forge,text='Back',command=destroy_forge).place(x=0,y=475)

def logcheck():
    uid = str(user_entry.get())
    psw=str(pw_entry.get())
    mydb = mysql.connector.connect(host="localhost", user="root", password="sql@123", database="patient")
    mycursor = mydb.cursor()
    UserName =uid

    Password =psw
    sql = "select * from login where UserName = %s and Password = %s"
    mycursor.execute(sql, [(UserName), (Password)])
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("", "Login Success")
        # root.destroy()
        page()

    else:
        messagebox.showerror("Error", "Incorrect UserName or Password")
        return False








#loginframe
logf=Frame(root,bg='#8081CD')
logf.place(x=250,y=150, height=340, width=500)

logintitle=Label(logf,text='Log in Panel',font=('impact',35,'bold'),bg='#8081CD', fg='darkblue')
logintitle.place(x=119,y=1)

username=Label(logf, text='Username',bg='lightblue')
username.place(x=135,y=110)
user_entry=Entry(logf)
user_entry.place(x=210,y=110)

password=Label(logf, text='Password',bg='lightblue')
password.place(x=135,y=140)

pw_entry=Entry(logf, bg='lightgray',show='*')
pw_entry.place(x=210,y=141)

login=Button(logf,text='Log in',bg='#8644f4',command=logcheck, cursor='hand2')
login.place(x=240,y=180)

Button(root, text="Forgot Password", command=forgot_password, cursor="hand2", font=("times new roman", 8, "bold"),
       fg="red", bg="lightblue").place(x=250, y=470, height=20, width=120)

#log in panel bind
def userdown(event):
    pw_entry.focus()
def pwup(event):
    user_entry.focus()
def pwdown(event):
     login.focus()

def onreturn(event):
#    print("Return Pressed")
    logcheck()




user_entry.focus()

user_entry.bind('<Return>',userdown)
user_entry.bind('<Down>',userdown)
pw_entry.bind('<Up>',pwup)
pw_entry.bind('<Return>',pwdown)
login.bind('<Up>',userdown)

login.bind('<Return>',onreturn)


root.title('Patient Information')
root.mainloop()

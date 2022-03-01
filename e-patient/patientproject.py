from tkinter import *
from datetime import date
import mysql.connector
import speech_recognition as s
from tkinter import messagebox
mydb = mysql.connector.connect(host = "localhost",user = "root",password = "123qwe",database = "patientdb")
my_cursor = mydb.cursor()
today=date.today() #gets the todays date in  yy-mm-dd format
root=Tk()
root.geometry('1000x700+122+1')
root.configure(bg='#8644f4')


#to insert details in databse when save button is clickced
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
    last=my_cursor.lastrowid
    print(last)
    l_ID_registere.insert(0,last+1)
    # l_ID_registere.configure(state=DISABLED)

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
    l_dobe.insert(0,'2054-12-12')

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

#button to save save data into data base
    l_savebutton=Button(form, text='SAVE',cursor='hand2',command=insert_database)
    l_savebutton.place(x=600,y=440)

#work on voice recognition
def id_():
    sr=s.Recognizer()
    print("i am listening you....")
    # listen =Label(w2, text='i am listening')
    # listen.place(x=70, y=170)

    with s.Microphone() as m:
        audio=sr.listen(m)
        query=sr.recognize_google(audio,language='eng-in')
        # listen=Label(w2,text='i am listening')
        # listen.place(x=70,y=150)

    search_box.insert(0,query)

#to get patient info after clicking on search buttton
def details():
    patientdt = Frame(w2, bg='#8081CD')
    patientdt.place(x=300, y=0, height=1000, width=700)

    r_date_register = Label(patientdt, text="Date of Registration")
    r_date_register.place(x=10, y=20)

    r_date_registere = Entry(patientdt)
    r_date_registere.place(x=150, y=20)

    r_ID_register = Label(patientdt, text=" Patient ID")
    r_ID_register.place(x=10, y=50)

    r_ID_registere = Entry(patientdt)
    r_ID_registere.place(x=150, y=50)

    r_name_register = Label(patientdt, text="Patient Name")
    r_name_register.place(x=10, y=80)

    r_name_registere = Entry(patientdt, width=30)
    r_name_registere.place(x=150, y=80)

    r_contact = Label(patientdt, text='Contact')
    r_contact.place(x=10, y=110)

    r_contacte = Entry(patientdt)
    r_contacte.place(x=150, y=110)

    r_dob = Label(patientdt, text='DOB')
    r_dob.place(x=10, y=140)

    r_dobe = Entry(patientdt)
    r_dobe.place(x=150, y=140)

    r_address_register = Label(patientdt, text='Address')
    r_address_register.place(x=10, y=170)

    r_address_registere = Entry(patientdt, width=30)
    r_address_registere.place(x=150, y=170)

    r_ag = Label(patientdt, text='Age')
    r_ag.place(x=10, y=200)

    r_agee = Entry(patientdt)
    r_agee.place(x=150, y=200)

    r_gender = Label(patientdt, text='Gender')
    r_gender.place(x=10, y=230)

    r_gendere = Entry(patientdt)
    r_gendere.place(x=150, y=230)

    r_bloodgroup = Label(patientdt, text='Blood Group')
    r_bloodgroup.place(x=10, y=260)

    r_bloodgroupe = Entry(patientdt)
    r_bloodgroupe.place(x=150, y=260)

    r_mail_register = Label(patientdt, text='Email Address')
    r_mail_register.place(x=10, y=290)

    r_mail_registere = Entry(patientdt, width=50)
    r_mail_registere.place(x=150, y=290)

    r_emergency_contact = Label(patientdt, text='Emergency Contact')
    r_emergency_contact.place(x=10, y=320)

    r_emergency_contacte: Entry = Entry(patientdt)
    r_emergency_contacte.place(x=150, y=320)

    r_relation = Label(patientdt, text='Relation to Patient')
    r_relation.place(x=10, y=350)

    r_relatione = Entry(patientdt)
    r_relatione.place(x=150, y=350)

    r_physician = Label(patientdt, text='Primary Physician')
    r_physician.place(x=10, y=380)

    r_physiciane = Entry(patientdt, width=30)
    r_physiciane.place(x=150, y=380)

    r_appoint = Label(patientdt, text='Appointed for')
    r_appoint.place(x=10, y=410)

    r_appointe = Text(patientdt, height=8, width=50)
    r_appointe.place(x=150, y=410)

    r_savebutton = Button(patientdt, text='SAVE', cursor='hand2')
    r_savebutton.place(x=600, y=440)


#page after login
def page():
    global w2, search_box
    w2=Tk()
    w2.geometry('1000x700+122+1')
    w2.configure(bg='#8644f4')
    # search and register for patient
    search_PID = Label(w2, text="Patient ID", bg='#8644f4')
    search_PID.place(x=10, y=20)

    search_box =Entry(w2)
    search_box.place(x=70, y=20)

    #search button
    getinfo = Button(w2, text='Search', command=details)
    getinfo.place(x=100, y=50)

    voice_button = Button(w2, text='Voice Search ', command=id_)
    voice_button.place(x=85, y=90)

    register_button = Button(w2, text='Register', command=registerform)
    register_button.place(x=95, y=130)



    w2.title('Find And Register Patient Information')
    w2.mainloop()




def logcheck():
    uid = str(user_entry.get())
    psw=str(pw_entry.get())

    if uid =='a':
        if psw=='a':
            messagebox.showinfo('cool', 'login successful')
            root.destroy()
            page()



        else:
            messagebox.showinfo('Error', 'Password Wrong')

    elif uid=='' and psw=='':
        messagebox.showinfo('Error',"All Field are Required")

    else:
        messagebox.showinfo('Error', 'ID and Password Wrong')






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
login.place(x=210,y=180)


root.title('Patient Information')
root.mainloop()

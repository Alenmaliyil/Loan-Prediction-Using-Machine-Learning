# import openpyxl and tkinter modules
import sqlite3
import tkinter as tk
from datetime import time
from tkinter import Tk, StringVar, Label, Button, Text, Canvas, Entry, END, messagebox
import tkinter.ttk as ttk
import pandas as pd
import numpy as np
import smtplib
from sklearn import preprocessing, tree
from sklearn.preprocessing import LabelEncoder
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.model_selection import train_test_split
from reportlab.platypus import Table,TableStyle
from reportlab.lib import colors
#def focus1(event):
    # set focus on the course_field box
    #Id.focus_set()

# Reading the training dataset in a dataframe using Pandas
    
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("train.csv")

df=df.fillna(df.mean())


X= df.iloc[:,6:11]
Y= df.iloc[:,12]

# Reading the test dataset in a dataframe using Pandas
#test = pd.read_csv("test.csv")
#array1=test.values
# X_test= array1[:,6:11]
#y_test = array1[:,12]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)



cat_cols = ['Credit_History','Dependents','Gender','Married','Education','Property_Area','Self_Employed']






# Store total number of observation in training dataset
df_length =len(df)
# Store total number of columns in testing data set
i=1
outcome_lg=''
cat=['Gender','Married','Dependents','Education','Self_Employed','Credit_History','Property_Area']
var_mod = ['Gender','Married','Dependents','Education','Self_Employed','Property_Area','Loan_Status']
le = LabelEncoder()
for i in var_mod:
    df[i] = le.fit_transform(df[i].astype('str'))





#train_modified=fullData[fullData['Type']=='Train']
#test_modified=fullData[fullData['Type']=='Test']
#train_modified["Loan_Status"] = number.fit_transform(train_modified["Loan_Status"].astype('str'))
def decisiontree():

    
    dec_tree = [Appl_income.get(),Co_income.get(),L_Amt.get(),L_Term.get(),C_history.get()]
    
    if(Appl_income.get()== ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "APPLICANT INCOME can't empty !!!")
        Appl_income.focus_set()
    elif (Appl_income.get().isdigit() == False):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Enter APPLICANT INCOME in numbers only !!!")
        Appl_income.focus_set()
    elif(Co_income.get() == ""):
         messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "CO-APPLICANT INCOME can't empty!!!")
         Co_income.focus_set()
    elif (Co_income.get().isdigit() == False):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Enter CO-APPLICANTCINCOME in numbers only !!!")
        L_Amt.focus_set()
    elif (L_Amt.get() == ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "APPLICANT INCOME can't empty!!!")
        L_Amt.focus_set()
    elif (L_Amt.get().isdigit() == False):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Enter LOAN AMOUNT in numbers only !!!")
        L_Amt.focus_set()
    elif (L_Term== ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "LOAN TERM can't empty!!!")
        L_Term.focus_set()
    elif (L_Term.get().isdigit() == False):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Enter LOAN AMOUNT in numbers only !!!")
        L_Term.focus_set()
    # elif(COMBO1 == ""):
        #messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "PROPERTY_AREA can't empty!!!")
        #monthchoosen.focus_set()
    elif(C_history.get()== ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "CREDIT HISTORY can't empty!!!")
        C_history.focus_set()
    else:
        #X_train = X_train.reshape(-1, 1)
        #X_test = X_test.reshape(-1, 1)
        dec_model = tree.DecisionTreeClassifier()
        dec_model = dec_model.fit(X_train, Y_train)
        dec_acc_score=dec_model.score(X_test,Y_test)
        dec_acc_score=dec_acc_score*100
        A_t1.delete("1.0", END)
        A_t1.insert(END, dec_acc_score)
        
        
   
        

        #dec=dec.reshape(1,-1)
    # Train the model using the training sets
        print(dec_tree)
   # Predict Output
        dec_predicted = dec_model.predict([dec_tree])
    # Create logistic regression object
    # Store it to test dataset
        #outcome_dec =  dec_predicted
        # print(outcome_dec)
        P_t1.insert(END,dec_predicted[0])
        print(pd.__version__)
     
def logisticregression():
    
  
     #predi_logi = [Appl_income.get(),Co_income.get(),L_Amt.get(),L_Term.get(),C_history.get()]
    
     if(Appl_income.get()== ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "APPLICANT INCOME can't empty !!!")
        Appl_income.focus_set()
     elif (Appl_income.get().isdigit() == False):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Enter APPLICANT INCOME in numbers only !!!")
        Appl_income.focus_set()
     elif(Co_income.get() == ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "CO-APPLICANT INCOME can't empty!!!")
        Co_income.focus_set()
     elif (Co_income.get().isdigit() == False):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Enter CO-APPLICANTCINCOME in numbers only !!!")
        Co_income.focus_set()
     elif (L_Amt.get() == ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "APPLICANT INCOME can't empty!!!")
        L_Amt.focus_set()
     elif (L_Amt.get().isdigit() == False):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Enter LOAN AMOUNT in numbers only !!!")
        L_Amt.focus_set()
     elif (L_Term.get()== ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "LOAN TERM can't empty!!!")
        L_Term.focus_set()
     elif (L_Term.get().isdigit() == False):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Enter LOAN AMOUNT in numbers only !!!")
        L_Term.focus_set()
    # elif(COMBO1 == ""):
        #messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "PROPERTY_AREA can't empty!!!")
        #monthchoosen.focus_set()
     elif(C_history.get()== ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "CREDIT HISTORY can't empty!!!")
        C_history.focus_set()
    
   
     else:
        
        lg_model = LogisticRegression()
        lg_model = lg_model.fit(X_train, Y_train)
        Lg_acc_score=lg_model.score(X_test,Y_test)
        print(Lg_acc_score)
        Lg_acc_score=Lg_acc_score*100
        A_t2.delete("1.0", END)
        A_t2.insert(END, Lg_acc_score)
        #predi_logi=map(float,[predi_logi])
        #value=outcome_lg
        print(outcome_lg)
        if(outcome_lg=="['N']"):
            P_t2.insert(END,outcome_lg)
           
        else:

   # Train the model using the training sets
    #inp1=[[3013,3033,95.0,300,00.8421985815602837]]
   # Predict Output
            try:
            
               Lg_predicted = lg_model.predict(X_test)
               #Lg_predicted  = map(float,[Lg_predicted])
    # Create logistic regression object
    # Store it to test dataset
        #outcome_lg1 = Lg_predicted
        #print("Output:", outcome_lg1)
               P_t2.insert(END, Lg_predicted[0])
               print(Lg_predicted)
            except Exception as ee:
               print(ee)
               print("hai")
           #print("OutputRE:", Lg_predicted)
           
           
   
    
    
def randomforest():
    ran_fore = [Appl_income.get(),Co_income.get(),L_Amt.get(),L_Term.get(),C_history.get()]
    Rf_model = RandomForestClassifier(n_estimators=100)
    Rf_model = Rf_model.fit(X_train, Y_train)
    Rf_acc_score=Rf_model.score(X_test,Y_test)

    Rf_acc_score=Rf_acc_score*100
    print(Rf_acc_score)
    A_t3.delete("1.0", END)
    A_t3.insert(END, Rf_acc_score)
    
              
    
    

   # Train the model using the training sets
   
   # Predict Output
    Rf_predicted = Rf_model.predict([ran_fore])
    # Create logistic regression object
    # Store it to test dataset
    outcome_lg =  Rf_predicted
    print(outcome_lg)
    p_t3.insert(END,outcome_lg[0])
    return(outcome_lg)



# Function to set focus
def view_reports(): 
    import tkinter as tk1
    from tkinter import Frame
    master2 = Tk()
    master2.geometry("1200x500")
    master2.title("Loan Prediction Report form")
    #w3 = canvas.create_text((600, 40), text="LOAN APPROVAL  PREDICTION SYSTEM", font='Algerian 20 bold', fill="orange")
    heading1 = Label(master2, text="LOAN APPROVAL  PREDICTION SYSTEM", font='Algerian 20 bold')
    heading1.pack()
    heading2 = Label(master2, text="REPORT", font='Algerian 20 bold')
    heading2.pack()
    #Tableheader
    con = sqlite3.connect('LOAN_PREDICTION2.db')
    cur = con.cursor()
    print("Database created and Successfully Connected to SQLite")
    cur.execute("select LOAN_ID, APPLICANT_INCOME,COAPPLICANT_INCOME,LOAN_AMOUNT,LOAN_TERM,CREDIT_HISTORY,DEC_STATUS,DEC_ACCURACY,LOG_STATUS,LOG_ACCURACY,RANDOM_STATUS,RANDOM_ACCURACY  from Loan_predictor" ) 
    rows=cur.fetchall()
    print(rows)
    
    frm = Frame(master2)
    frm.pack(side=tk1.LEFT, padx=20)
    tv=ttk.Treeview(frm,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17),show='headings',height="10")
    tv.pack()
    
    tv.column("1", width = 90, anchor ='c') 
    tv.column("2", width = 90, anchor ='se') 
    tv.column("3", width = 90, anchor ='se')
    tv.column("4", width = 90, anchor ='se')
    tv.column("5", width = 90, anchor ='se')
    tv.column("6", width = 90, anchor ='se')
    tv.column("7", width = 120, anchor ='se')
    tv.column("8", width = 120, anchor ='se')
    tv.column("9", width = 120, anchor ='se')
    tv.column("10", width = 120, anchor ='se')
    tv.column("11", width = 90, anchor ='se')
    horscrlbar = ttk.Scrollbar(master2,  
                           orient ="horizontal",  
                           command = tv.xview) 
  
    # Calling pack method w.r.to verical  
    # scrollbar 
    horscrlbar.pack(side="bottom", fill ='x') 
  
    # Configuring treeview 
    tv.configure(xscrollcommand = horscrlbar.set)
    tv.grid(row=2,column=6,sticky="ns")
    tv.heading(1,text="LOAN_ID")
    tv.heading(2,text="APPLICANT_INCOME")
    tv.heading(3,text="CO-APPLICANT_INCOME")
    tv.heading(4,text="LOAN_AMOUNT")
    tv.heading(5,text="LOAN_TERM")
    tv.heading(6,text="CREDIT_HISTORY")
    tv.heading(7,text="DEC_TREE_PREDICTION")
    tv.heading(8,text="DEC_TREE_ACCURACY")
    tv.heading(9,text="LOG_REG_PREDICTION")
    tv.heading(10,text="LOG_REG_ACCURACY")
    tv.heading(11,text="RAN_FOR_PREDICTION")
    tv.heading(12,text="RAN_FOR_ACCURACY")
    
    for i in rows:
         tv.insert('','end',values=i)
    
    con.commit()
    con.close()
    master2.mainloop()
def close_window():
    root.destroy()
# Function for clearing the
# contents of text entry boxes
def clear_fields():
    # clear the content of text entry box
    Id_field.delete(0, END)
    
    L_Amt.delete(0, END)
    L_Term.delete(0, END)
    Appl_income.delete(0, END)
    Co_income.delete(0, END)
    P_t1.delete(0, END)
    A_t1.delete(0, END)
    P_t2.delete(0, END)
    A_t2.delete(0, END)
    p_t3.delete(0, END)
    A_t3.delete(0, END)
    address_entry.delete(0, END)
    

def send_mail():
    ADDRESS_INFO = address_entry.get()
    got="haii"
    sender_mail="alenabraham143@gmail.com"  
    sender_pass="alenmaliyil12143"
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    server.starttls()
    
    server.login(sender_mail,sender_pass)
    server.sendmail(sender_mail,ADDRESS_INFO,got)
        

def insert():
    # if user not fill any entry
    # then print "empty input"
    LOAN_ID=Id_field.get()
    GENDER=Gender.get()
    MARRIAGE=MarStatus.get()
    EDUCATION=Education.get()
    DEPENDANTS=Dependents.get()
    APP_INCOME=Appl_income.get()
    CAPP_INCOME=Co_income.get()
    LOAN_AMT=L_Amt.get()
    LOAN_TERM=L_Term.get()
   
    
    CRED_HISTORY=C_history.get()
    SELF_EMPLOYED=S_employed.get()
    DEC_STATUS=P_t1.get('1.0', END)
    DEC_ACCURACY=A_t1.get('1.0', END)
    LOG_STATUS=P_t2.get('1.0', END)
    LOG_ACCURACY=A_t2.get('1.0', END)
    RAN_STATUS=p_t3.get('1.0', END)
    RAN_ACCURACY=A_t3.get('1.0', END)


    if(LOAN_ID == "" ) :
        messagebox.showinfo("MACHINE LEARNING DISEASE PREDICTOR.", "NAME can't be empty !!!")
        Id.focus_set()
    elif (LOAN_ID.isdigit() == False):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Enter APPLICANT ID in numbers only !!!")
        Id.focus_set()

    elif(GENDER  == "" ):
         messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Choose GENDER !!!")
         Gender.focus_set()
    elif(MARRIAGE == ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Choose MARITAL STATUS !!!")
        MarStatus.focus_set()
    elif( EDUCATION== "" ):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Choose EDUCATION !!!")
        Education.focus_set()
    elif( DEPENDANTS == "" ):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Choose DEPENDANTS !!!")
        Dependents.focus_set()
    elif(APP_INCOME == ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "APPLICANT INCOME can't empty !!!")
        Appl_income.focus_set()
    elif (APP_INCOME.isdigit() == False):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Enter APPLICANT INCOME in numbers only !!!")
        Appl_income.focus_set()
    elif(CAPP_INCOME == ""):
         messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "CO-APPLICANT INCOME can't empty!!!")
         Co_income.focus_set()
    elif (CAPP_INCOME.isdigit() == False):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Enter CO-APPLICANTCINCOME in numbers only !!!")
        L_Amt.focus_set()
    elif (LOAN_AMT == ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "APPLICANT INCOME can't empty!!!")
        L_Amt.focus_set()
    elif (LOAN_AMT.isdigit() == False):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Enter LOAN AMOUNT in numbers only !!!")
        L_Amt.focus_set()
    elif (LOAN_TERM== ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "LOAN TERM can't empty!!!")
        L_Term.focus_set()
    elif (LOAN_TERM.isdigit() == False):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Enter LOAN AMOUNT in numbers only !!!")
        L_Term.focus_set()
    elif(monthchoosen == ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "PROPERTY_AREA can't empty!!!")
        monthchoosen.focus_set()
    elif(CRED_HISTORY== ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "CREDIT HISTORY can't empty!!!")
        C_history.focus_set()
    elif(SELF_EMPLOYED == ""):
        messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "SELF_EMPLOYED  can't empty!!!")
        S_employed.focus_set()
        
        # clear()
    else :
    
        con = sqlite3.connect('LOAN_PREDICTION2.db')
        cur = con.cursor()
        print("Database created and Successfully Connected to SQLite")
        cur.execute("CREATE TABLE IF NOT EXISTS Loan_predictor(LOAN_ID integer PRIMARY KEY,GENDER varchar(10), MARITAL_STATUS  varchar(10), EDUCATION  varchar(10), DEPENDANTS  varchar(10), APPLICANT_INCOME real,COAPPLICANT_INCOME real, LOAN_AMOUNT real,LOAN_TERM int,CREDIT_HISTORY varchar(20),SELF_EMPLOYED varchar(10),DEC_STATUS varchar(10),DEC_ACCURACY real,LOG_STATUS varchar(10),LOG_ACCURACY real,RANDOM_STATUS varchar(10),RANDOM_ACCURACY real)")
        print ("Table created successfully");
        try:
            cur.execute("""INSERT INTO Loan_predictor(LOAN_ID,GENDER,MARITAL_STATUS,EDUCATION,DEPENDANTS,
                        APPLICANT_INCOME,COAPPLICANT_INCOME,
                        LOAN_AMOUNT,LOAN_TERM,CREDIT_HISTORY,SELF_EMPLOYED,DEC_STATUS,DEC_ACCURACY,LOG_STATUS,LOG_ACCURACY,RANDOM_STATUS,RANDOM_ACCURACY) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?)""",
                        (LOAN_ID,GENDER,MARRIAGE,EDUCATION,DEPENDANTS,APP_INCOME,CAPP_INCOME,
                        LOAN_AMT,LOAN_TERM,CRED_HISTORY,SELF_EMPLOYED,DEC_STATUS,DEC_ACCURACY,LOG_STATUS,LOG_ACCURACY,RAN_STATUS,RAN_ACCURACY))
            messagebox.showinfo("MACHINE LEARNING LOAN PREDICTOR.", "Record added successfully !!!")
            con.commit()
            con.close()
        
        
    
                                        # Driver code
        except sqlite3.DatabaseError as err:
                print(err)
                print("hello error")
                con.close()
        #sender_mail="alenabraham143@gmail.com"  
        #sender_pass="alenmaliyil12143"
        #server = smtplib.SMTP('smtp.gmail.com',587)
    
        #server.starttls()
    
       # server.login(sender_mail,sender_pass)
        #server.sendmail(sender_mail,ADDRESS_INFO,LOG_STATUS)
        
        
        
        
       
         
if __name__ == "__main__":
    # create a GUI window
    root = Tk()

    # set the background colour of GUI window
    # root.configure(background='light green')
    canvas = Canvas(root, height=768, width=1366)
    canvas.pack()
    # set the title of GUI window
    root.title("Loan approval prediction form")
    Symptom1 = StringVar()
    Symptom1.set('Select Symptom')
    '''                       Variables'''

    Gender = StringVar()
    MarStatus = StringVar()
    Dependents = StringVar()
    S_employed = StringVar()
    Education = StringVar()
    C_history = StringVar()

    # set the configuration of GUI window
    # root.geometry("300x250")
    w2 = canvas.create_text((640, 40), text="LOAN APPROVAL  PREDICTION SYSTEM", font='Algerian 20 bold', fill="orange")
    # create a Form label
    heading = Label(root, text="Form", bg="light blue")
    heading.pack()

                          # create a Name label
    Id = canvas.create_text((105,105),  text="Loan id",fill="blue",  font='Arial 13 bold' )
    Id_field = Entry(root, width=42, bg="white", fg="black", font='Arial 11')
    Id_field.place(x=280,y=96)

    '''--------------------------------------Gender------------------------------------------'''
    radio_style = ttk.Style()
    myColor = '#2780d1'
    radio_style.configure('Wild.TRadiobutton', background=myColor, foreground='white', font='Arial 13')

    gender_label = canvas.create_text((104, 150), text="Gender", fill="blue", font='Arial 13 bold')

    R1 = ttk.Radiobutton(root, text="Male", variable=Gender, value="MALE", style='Wild.TRadiobutton')
    R1.place(x=280, y=136)
    R2 = ttk.Radiobutton(root, text="Female", variable=Gender, value="FEMALE", style='Wild.TRadiobutton')
    R2.place(x=350, y=136)

    '''-----------------------Marital Status-------------------------- '''


    radio_style = ttk.Style()
    myColor = '#2780d1'
    radio_style.configure('Wild.TRadiobutton', background=myColor, foreground='white', font='Arial 13')

    gender_label1 = canvas.create_text((798, 110), text="Married", fill="blue", font='Arial 13 bold')

    R3 = ttk.Radiobutton(root, text="Yes", variable=MarStatus, value="Yes", style='Wild.TRadiobutton')
    R3.place(x=980, y=100)
    R4 = ttk.Radiobutton(root, text="No", variable=MarStatus, value="No", style='Wild.TRadiobutton')
    R4.place(x=1050, y=100)

    '''-----------------------------------Education-----------------------------'''

    radio_style = ttk.Style()
    myColor = '#2780d1'
    radio_style.configure('Wild.TRadiobutton', background=myColor, foreground='white', font='Arial 13')

    gender_label4 = canvas.create_text((809, 158), text="Education", fill="blue", font='Arial 13 bold')

    R5 = ttk.Radiobutton(root, text="Graduate", variable=Education, value="Graduate", style='Wild.TRadiobutton')
    R5.place(x=980, y=155)
    R6 = ttk.Radiobutton(root, text="Undergraduate", variable=Education, value="Undergraduate", style='Wild.TRadiobutton')
    R6.place(x=1090, y=155)

    '''---------------------------------Applicant Income------------------------------------'''

    Applicant_income = canvas.create_text((139, 200), text="Applicant income", fill="blue", font='Arial 13 bold')
    Appl_income = Entry(root, width=42, bg="white", fg="black", font='Arial 11')
    Appl_income.place(x=280, y=196)

    '''---------------------------------C0-Applicant Income------------------------------------'''

    Coappl_income = canvas.create_text((149, 250), text="Co-applicant income", fill="blue", font='Arial 13 bold')
    Co_income = Entry(root, width=42, bg="white", fg="black", font='Arial 11')
    Co_income.place(x=280, y=246)

    '''---------------------------------Loan Amount------------------------------------'''

    Loan_amt = canvas.create_text((120, 300), text=" Loan amount", fill="blue", font='Arial 13 bold')
    L_Amt = Entry(root, width=42, bg="white", fg="black", font='Arial 11')
    L_Amt.place(x=280, y=296)

    '''---------------------------------Loan Term------------------------------------'''

    Term = canvas.create_text((139, 350), text=" Loan amount term", fill="blue", font='Arial 13 bold')
    L_Term = Entry(root, width=42, bg="white", fg="black", font='Arial 11')
    L_Term .place(x=280, y=346)

    '''---------------------------------E-mail---------------------------------------'''
    
    address_field = canvas.create_text((127, 400), text="Email Address ",fill="blue", font='Arial 13 bold')
    address_entry = Entry(root, width=42, bg="white", fg="black", font='Arial 11')
    address_entry.place(x=280, y=396)

    
    
    '''---------------------------------Dependants------------------------------------'''

    radio_style = ttk.Style()
    myColor = '#2780d1'
    radio_style.configure('Wild.TRadiobutton', background=myColor, foreground='white', font='Arial 13')

    gender_label2 = canvas.create_text((818, 300), text="Dependants", fill="blue", font='Arial 13 bold')

    R7 = ttk.Radiobutton(root, text="Yes", variable=Dependents, value="1", style='Wild.TRadiobutton')
    R7.place(x=980, y=293)
    R8 = ttk.Radiobutton(root, text="No", variable=Dependents, value="0", style='Wild.TRadiobutton')
    R8.place(x=1050, y=293)

    '''---------------------------------Self-Employed------------------------------------'''

    radio_style = ttk.Style()
    myColor = '#2780d1'
    radio_style.configure('Wild.TRadiobutton', background=myColor, foreground='white', font='Arial 13')

    gender_label3 = canvas.create_text((825, 349), text="Self_Employed", fill="blue", font='Arial 13 bold')

    R9 = ttk.Radiobutton(root, text="Yes", variable=S_employed, value="Yes", style='Wild.TRadiobutton')
    R9.place(x=980, y=345)
    R10 = ttk.Radiobutton(root, text="No", variable=S_employed, value="No", style='Wild.TRadiobutton')
    R10.place(x=1050, y=345)


                                   # Combobox creation
    combostyle = ttk.Style()

    combostyle.theme_create('combostyle', parent='alt',
                            settings={'TCombobox':
                                          {'configure':
                                               {'selectbackground': 'blue',

                                                'background': 'green'
                                                }}}
                            )
    # combostyle.theme_use('combostyle')
    gender_label4 = canvas.create_text((827, 200), text="Property_Area", fill="blue", font='Arial 13 bold')
    n = StringVar()
    monthchoosen = ttk.Combobox(root, width=27 , textvariable = n)

    # Adding combobox drop down list
    monthchoosen['values'] = (' Urban',
                              ' Semiurban',
                              ' Rural',
                              )

    # monthchoosen.grid(column=1, row=5)
    monthchoosen.current(0)
    monthchoosen.place(x=980, y=200)
    radio_style = ttk.Style()
    myColor = '#2780d1'
    radio_style.configure('Wild.TRadiobutton', background=myColor, foreground='white', font='Arial 13')

    gender_label5 = canvas.create_text((825, 250), text="Credit History", fill="blue", font='Arial 13 bold')

    R9 = ttk.Radiobutton(root, text="Yes", variable=C_history, value="1", style='Wild.TRadiobutton')
    R9.place(x=980, y=240)
    R10 = ttk.Radiobutton(root, text="No", variable=C_history, value="0", style='Wild.TRadiobutton')
    R10.place(x=1050, y=240)

    ''' S1Lb = canvas.create_text((360, 550), text="Education", fill="white", font='Arial 13 bold')
    email_id_field=OPTIONS = sorted(oplist)


    S1En = OptionMenu(root, Symptom1,*OPTIONS)
    S1En.place(x=600,y=220)
    S1En.config(width=50,highlightthickness=0,bg="white") '''

    # create a Course label
    # course = canvas.create_text((290,140),  text="Course",fill="blue",  font='Arial 13 bold' )
    # create a Semester label
    # sem = Label(root, text="Semester", bg="red")
    # sem.pack()
    # sem.place(x=50, y=130, height=20, width=50)
    # create a Form No. lable
    # form_no = Label(root, text="Form No.", bg="red")
    # form_no.pack()
    # form_no.place(x=50, y=170, height=20, width=50)
    # create a Contact No. label
    # contact_no = Label(root, text="Contact No.", bg="light green")
    # contact_no.pack()
    # contact_no.place(x=50, y=210, height=20, width=50)
    # create a Email id label
    # email_id = Label(root, text="Email id", bg="light green")
    # email_id.pack()
    # email_id.place(x=50, y=250, height=20, width=50)
    # create a address label
    #  address = Label(root, text="Address", bg="light green")
    # address.pack()
    # address.place(x=50, y=290, height=20, width=50)
    # create a text entry box
    # for typing the information


    '''---------------------------------Decision Tree Accuracy&Time Labels------------------------------------'''

    Pred_Label=canvas.create_text((70, 525), text="Loan_Status", fill="red", font='Arial 13 bold')
    Acc_Label = canvas.create_text((70, 560), text="Accuracy", fill="red", font='Arial 13 bold')

    '''--------------------------------Decision Tree Accuracy&Time Textbox's----------------------------------'''
    P_t1=Text(root, height=1, width=42, bg="yellow", fg="red", font='Arial 11 bold')
    P_t1.place(x=150, y=520)
    A_t1 = Text(root, height=1, width=42, bg="yellow", fg="red", font='Arial 11 bold')
    A_t1.place(x=150, y=550)
   

    '''---------------------------------Logistic Regression Accuracy&Time Textbox's----------------------------------'''
    P_t2 = Text(root, height=1, width=42, bg="yellow", fg="red", font='Arial 11 bold')
    P_t2.place(x=530, y=520)
    A_t2 = Text(root, height=1, width=42, bg="yellow", fg="red", font='Arial 11 bold')
    A_t2.place(x=530, y=550)

   

    '''---------------------------------Random Forest Accuracy&Time Textbox's----------------------------------'''
    p_t3 = Text(root, height=1, width=42, bg="yellow", fg="red", font='Arial 11 bold')
    p_t3.place(x=910, y=520)
    A_t3 = Text(root, height=1, width=42, bg="yellow", fg="red", font='Arial 11 bold')
    A_t3.place(x=910, y=550)
    

    '''---------------------------------Buttons-------------------------------------------'''
    Save_b1 = Button(root, text="SAVE", bg="#59E817", command=insert, fg="blue", font='Arial 11 bold', width=12)
    Save_b1.place(x=500, y=630)
    Dec_Tree = Button(root, text="Decision Tree", command=decisiontree, bg="#d70000", fg="white", font='Arial 11 bold',
                      width=20)
    Dec_Tree.place(x=220, y=450)
    Log_Reg = Button(root, text="Logistic Regression", command=logisticregression, bg="#d70000", fg="white",
                     font='Arial 11 bold', width=20)
    Log_Reg.place(x=600, y=450)
    Ran_For = Button(root, text="Random Forest", command=randomforest, bg="#d70000", fg="white", font='Arial 11 bold',
                     width=20)
    Ran_For.place(x=970, y=450)
    clear_b1 = Button(root, text="CLEAR", bg="#59E817", command=clear_fields, fg="blue", font='Arial 11 bold', width=12)
    clear_b1.place(x=800, y=630)
    view_b1 = Button(root, text="VIEW REPORT", bg="#59E817", command= view_reports, fg="blue", font='Arial 11 bold', width=12)
    view_b1.place(x=650, y=630)
    close_b1 = Button(root, text="CLOSE", bg="#59E817", command=close_window, fg="blue", font='Arial 11 bold', width=12)
    close_b1.place(x=1150, y=30)
    
    view_b1 = Button(root, text="SEND MAIL", bg="#59E817", command= send_mail, fg="blue", font='Arial 11 bold', width=12)
    view_b1.place(x=950, y=830)
    
    

    # bind method of widget is used for
    # the binding the function with the events

    # whenever the enter key is pressed
    # then call the focus1 function
    #Id.bind("<Return>", focus1)

    # whenever the enter key is pressed
    # then call the focus2 function
    #S_employed.bind("<Return>", focus2)

    # whenever the enter key is pressed
    # then call the focus3 function
    #Appl_income.bind("<Return>", focus3)

    # whenever the enter key is pressed
    # then call the focus4 function
    #Coappl_income.bind("<Return>", focus4)

    # whenever the enter key is pressed
    # then call the focus5 function
    # L_Term.bind("<Return>", focus5)

    # whenever the enter key is pressed
    # then call the focus6 function
    # L_Amt.bind("<Return>", focus6)
    # create a Submit Button and place into the root window



    # start the GUI
    root.mainloop()
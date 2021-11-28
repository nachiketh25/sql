from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,MetaData,Column,Integer,String,Table,Boolean
from sqlalchemy.sql.expression import true
engine = create_engine('sqlite:///college.db', echo = True)
meta= MetaData()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///college.db'
db = SQLAlchemy(app)

students = Table(
    'students',meta,
    Column( ' USN',Integer,primary_key=True),
    Column('student_name',String),
    Column('gender',String),
    Column('entry_type',String),
    Column('YOA',Integer),
    Column('migrated',Boolean),
    Column ('Details_of_transfer',String),
    Column('admission_in_separate_division',Boolean),
    Column('Details_of_admission_in_seperate_division',String),
    Column('pu_marks',Integer),
    Column('YOP',Integer),
    Column( 'degree_type',String),

 )

meta.create_all(engine)
conn = engine.connect()




def create():
    N=int(input ("enter the number of students :"))
    for i in range (N):
        uid = input("enter the usn of student :")
        n=input("enter the name of the students :")
        g=input("enter the gender of the student :")
        E=input ("enter whether the students are Normal Entry / Lateral Entry :")
        y=input("enter the year of admission of the student  :")
        v= input("enter the year of passing :")
        d= input ("enter the degree type the student is studying :")
        m=input("enter the pu marks of the student :")
        z=input("enter wether the student is migrated to other program :")
        if z=="yes":
            z=True
        elif z=="no":
            z=False
        f=input("enter the details of transfer :")
        r=input("does the student have admission in seapreate division :")
        if r=="yes":
            r=True
        elif  r=="no":
            r=False
        x=input("enter the details of admission in seprate division :")
        result = conn.execute(students.insert(),[{'USN':uid,'student_name':n,'gender':g,'enter_type':E,'YOA':y,'YOP':v,
        'degree_type':d,'pu_marks':m,'migrated':z,'Details_of_transfer':f,'admission_in_separate_division':r,
        'Details_of_admission_in_seperate_division':x}])
    

def read():
    n=students.select()
    result=conn.execute(n)
    for row in result:
        print (row)
def update():
    option=int(input("select 1 to update the parameters of the students :\n select 2 to update the range :"))
    if option==1:
        select=input("enter the usn of the student to be updated :")
        print ("please seclect the parameter to be updated :")
        while(true):
            parameter=int(input(""" 
            select 1 to update name
            selcet 2 to update gender
            select 3 to update entry_type
            select 4 to update YOA
            select 5 to update migrated
            select 6 to update details of transfer
            select 7 to update admission_in_separate_division
            select 8 to update Details_of_admission_in_seperate_division
            select 9 to update pu_marks
            select 10 to update YOP 
            select 11 to update degree_type
            select 0 to stop updating"""))
            pram_dict = {1:'student_name', 2:'Gender', 3: 'entry_type', 4:'YOA', 5:'migrated', 6:'details of migration',
                    7: 'admission_in_separate_division', 8:'Details_of_admission_in_seperate_division', 9: 'pu_marks', 10: 'pu_marks', 11: 'degree_type'}
            if parameter != 0:
                selection = parameter_dict[parameter]
                stripped = selection.strip('')
                new = input("Enter the "+ selection+ " values: ")
                updated = students.update().where(students.c.USN==select).values(stripped = new)
                result = conn.execute(updated)
            elif parameter == 0:
                break        
    elif option == 2:
        dict_input = input("Input the dictionary: ")
        dict_input = eval(dict_input)
        match = dict_input['USN']
        for key, value in dict_input.items():
            print(key,value)
            updated = students.update().where(students.c.USN==match).values(key = value)
        result = conn.execute(updated)        
def delete():
    j=input("enter the usn of the student to be deleted")
    stmt = students.delete().where(students.c.USN==j)
    conn.execute(stmt)
    s = students.select()
    conn.execute(s).fetchall()

operation_dict = {1: create, 2: read, 3: update, 4: delete}

while(True):
    operation = int(input("""To perform the following operations: 
          Press 1 to enter new values:
          Press 2 to view the table: 
          Press 3 to update the records: 
          Press 4 to delete a record: \nselect no : """))
    performing = operation_dict[operation]()

from sqlalchemy import create_engine,MetaData,Column,Integer,String,Table,Boolean
engine = create_engine('sqlite:///college.db', echo = True)
meta= MetaData()

students = Table(
    'students',meta,
    Column( ' USN',Integer,primary_key=True),
    Column('student_name',String),
    Column('gender',String),
    Column('entry_type',String),
    Column('YOA',Integer),
    Column('migrated',Boolean, default=False),
    Column ('Details_of_transfer',String),
    Column('admission_in_separate_division',Boolean,defalut=False),
    Column('Details_of_admission_in_seperate_division',string),
    Column('YOP',Integer),
    Column( 'degree_type',String),
    Column('degree_type',Integer)
 )


conn = engine.connect()

def create():
    N=int(input ("enter the number of students:"))
    for i in range (N):
        uid = input("enter the usn of student")
        n=input("enter the name of the students")
        g=input("enter the gender of the student")
        E=input ("enter whether the students are Normal Entry / Lateral Entry")
        y=input("enter the year of admission of the student ")
        v= input("enter the year of passing")
        d= input ("enter the degree type the student is studying")
        m=input("enter the pu marks of the student")
        result = conn.execute(data.insert(),[{'USN':uid,'student_name':n,'gender':g,'enter_type':E,'YOA':y,'YOP':V,'degree_type':d,'pu_marks':m}])
        z=input("enter wether the student is migrated to other program")
        if migrated=="yes":
            migrated=True
            f=("enter the details of transfer")
        else :
            migrated=False
            Details_of_transfer=" "
        r=input("does the student have admission in seapreate division")
        if admission_in_separate_division=="yes":
            admission_in_separate_division=True
            x=("enter the details of admission in seprate division")
        else:
            admission_in_separate_division=False
            Details_of_admission_in_seperate_division==" "
        result = conn.execute(data.insert(),[{'migrated':f,'Details_of_transfer':f,'admission_in_separate_division':y,'Details_of_admission_in_seperate_division':x}])


def read():
    n=students.select()
    result=conn.execute(n)
    for row in result:
        print (row)
def update():
    p=int(input("Enter the USN of the student: "))
    change=(input("enter the changed name of the students"))
    stmt=students.update().where(students.c.USN==p).values(student_name=new)
    conn.execute(stmt)
    s = students.select()
    conn.execute(s).fetchall()
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
          Press 4 to delete a record: """))
    performing = operation_dict[operation]()


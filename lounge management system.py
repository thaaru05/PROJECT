import mysql.connector as sql
mycon=sql.connect(host='localhost',user='root',passwd='thaaru',database='Project')
cursor=mycon.cursor()
def Add_records():
    a=input("Enter the Customer's Name:")
    b=int(input("Enter the Customer's Age:"))
    print("For Male --> Type M")
    print("For Female ---> Type F")
    print("For Others ---> Type Others")
    c=input("Enter the Customer's Gender:")
    d=input("Enter the Customer's Address:")
    e=input("Enter the Customer's Nationality:")
    f=input("Enter the Customer's Aadhar Card number(If Non-Indian-Type NULL):")
    g=input("Enter the Customer's Visa number(If Indian-Type NULL):")
    h=input("Enter the Customer's Mail ID:")
    i=input("Enter the Customer's Phone number:")
    j=input("Enter the Customer's Check-In date(YYYY/MM/DD):")
    k=input("Enter the Customer's Check-Out date(YYYY/MM/DD):")
    print("Types of rooms available are(for ONE DAY AND ONE NIGHT):")
    print("Superior--> â‚¹10,000/-")
    print("Premium--> â‚¹18,000")
    print("Room with a view(Sea view,Pool view,Garden view,City view,Mountain view)--> â‚¹22,000")
    print("Room with Lounge/Club access--> â‚¹31,000")
    print("Junior Suite--> â‚¹40,000")
    print("The Suite--> â‚¹50,000")
    print("The Presidential Suite--> â‚¹80,000")
    l=input("Enter the Customer's room type:")
    x=int(input("Enter the number of days and nights:"))
    y=input("Enter the Customer's door number:")
    m=j+"/"+y
    print("The Customer's room number is:",m)
    if l=='Superior' or l=='superior' or l=='SUPERIOR':
        n=10000*x
    elif l=='Premium' or l=='premium' or l=='PREMIUM':
        n=18000*x
    elif l=='Room with a view' or l=='Room with view' or l=='ROOM WITH A VIEW' or l=='ROOM WITH VIEW' or l=='room with view' or l=='room with a view':
        n=22000*x
    elif l=='ROOM WITH LOUNGE/CLUB ACCESS' or l=='room with lounge/club access':
        n=31000*x
    elif l=='JUNIOR SUITE' or l=='junior suite' or l=='Junior Suite':
        n=40000*x
    elif l=='THE SUITE' or l=='the suite' or l=='The Suite':
        n=50000*x
    elif l=='The Presidential Suite' or l=='THE PRESIDENTIAL SUITE' or l=='the presidential suite':
        n=80000*x
    else:
        n=0
    query='insert into Project values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    value=(a,b,c,d,e,f,g,h,i,j,k,l,x,y,m,n)
    cursor.execute(query,value)
    if cursor.rowcount!=0:
        mycon.commit()
        print("---x---x---x---")
        print("UPDATE SUCCESSFUL")
        print("---x---x---x---x")
    else:
        print("---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("---x---x---x---x")
        
def Search_name():
    Name=input("Enter the Customer's name:")
    inp=(Name,)
    query='SELECT * FROM Project WHERE(Name=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")
        
def search_age():
    Age=int(input("Enter the Customer's age:"))
    inp=(Age,)
    query='SELECT * FROM Project WHERE(Age=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")

#x------------------------x---------------------------x--------------------x---------------------x
def search_gender():
    print("For Male --> Type M")
    print("For Female ---> Type F")
    print("For Others ---> Type Others")
    Gender=input("Enter the Customer's gender:")
    inp=(Gender,)
    query='SELECT * FROM Project WHERE(Gender=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")
        
#x------------------------x---------------------------x--------------------x---------------------x
def search_add():
    Address=input("Enter the Customer's address:")
    inp=(Address,)
    query='SELECT * FROM Project WHERE(Address=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")   
     
#x------------------------x---------------------------x--------------------x---------------------x
def search_nationality():
    A=input("Enter the Customer's Nationality:")
    inp=(A,)
    query='SELECT * FROM Project WHERE(Nationality=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")
#x------------------------x---------------------------x--------------------x---------------------x
def search_Aadhar():
    A=input("Enter the Customer's Aadhar card number:")
    inp=(A,)
    query='SELECT * FROM Project WHERE(Aadhar_card_number=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")
#x------------------------x---------------------------x--------------------x---------------------x
def search_Visa():
    A=input("Enter the Customer's Visa number:")
    inp=(A,)
    query='SELECT * FROM Project WHERE(Visa_number=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")
#x------------------------x---------------------------x--------------------x---------------------x
def search_Mail():
    A=input("Enter the Customer's Mail-ID:")
    inp=(A,)
    query='SELECT * FROM Project WHERE(Mail_ID=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")
   
#x------------------------x---------------------------x--------------------x---------------------x
def search_Phone():
    A=input("Enter the Customer's Phone number:")
    inp=(A,)
    query='SELECT * FROM Project WHERE(Phone_number=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")
#x------------------------x---------------------------x--------------------x---------------------x
def search_In():
    A=input("Enter the Customer's Check-In date(YYYY/MM/DD):")
    inp=(A,)
    query='SELECT * FROM Project WHERE(Check_in=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")
#x------------------------x---------------------------x--------------------x---------------------x
def search_Out():
    A=input("Enter the Customer's Check-Out date(YYYY/MM/DD):")
    inp=(A,)
    query='SELECT * FROM Project WHERE(Check_Out=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")
#x------------------------x---------------------------x--------------------x---------------------x
def search_Type_room():
    A=input("Enter the Customer's room type:")
    inp=(A,)
    query='SELECT * FROM Project WHERE(Type_of_Room=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")
#x------------------------x---------------------------x--------------------x---------------------x
def search_room_number():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    inp=(A,)
    query='SELECT * FROM Project WHERE(Room_number=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")        
#x------------------------x---------------------------x--------------------x---------------------x
def search_bill_amount():
    A=float(input("Enter the Customer's total bill amount:"))
    inp=(A,)
    query='SELECT * FROM Project WHERE(Bill_amount=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")
#x------------------------x---------------------------x--------------------x---------------------x
def search_no_stay():
    A=int(input("Enter the Customer's number of days and nights stay:"))
    inp=(A,)
    query='SELECT * FROM Project WHERE(NO_OF_DAYS_NIGHTS=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")
#x------------------------x---------------------------x--------------------x---------------------x
def search_door():
    A=int(input("Enter the Customer's door number:"))
    inp=(A,)
    query='SELECT * FROM Project WHERE(Room_door=%s)'  
    cursor.execute(query,inp)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")

#x------------------------x---------------------------x--------------------x---------------------x
def search_all():
    query='SELECT * FROM Project'  
    cursor.execute(query)
    data=cursor.fetchall()
    if len(data)!=0:
        for x in data:
            print("Name:",x[0])
            print("Age:",x[1])
            print("Gender:",x[2])
            print("Address:",x[3])
            print("Nationality:",x[4])
            print("Aadhar Card number:",x[5])
            print("Visa number:",x[6])
            print("Mail ID:",x[7])
            print("Phone number:",x[8])
            print("Check-In date:",x[9])
            print("Check-Out date:",x[10])
            print("Type of room:",x[11])
            print("Number of days and nights stay:",x[12])
            print("Door number:",x[13])
            print("Room number:",x[14])
            print("Total Bill amount:",x[15])
            print("----x----x----x----x----x----x----")
    else:
        print("---x---x---x---")
        print("No record found")
        print("---x---x---x---x")
        
def search():
    print("1. To search data based on Customer's Name")
    print("2. To search data based on Customer's Age")
    print("3. To search data based on Customer's Gender")
    print("4. To search data based on Customer's Address")
    print("5. To search data based on Customer's Nationality")
    print("6. To search data based on Customer's Aadhar card number")
    print("7. To search data based on Customer's Visa number")
    print("8. To search data based on Customer's Mail-ID")
    print("9. To search data based on Customer's Phone number")
    print("10. To search data based on Customer's Check-In date")
    print("11. To search data based on Customer's Check-Out date")
    print("12. To search data based on Customer's room type")
    print("13. To search data based on Customer's room number")
    print("14. To search data based on Customer's bill amount")
    print("15. To search data based on Customer's number of days and nights stay")
    print("16. To search data based on Customer's door number")
    print("17. To search all data")
    n=int(input("Enter the choice:"))
    if n==1:
        Search_name()
    elif n==2:
        search_age()
    elif n==3:
        search_gender()
    elif n==4:
        search_add()
    elif n==5:
        search_nationality()
    elif n==6:
        search_Aadhar()
    elif n==7:
        search_Visa()
    elif n==8:
        search_Mail()
    elif n==9:
        search_Phone()
    elif n==10:
        search_In()
    elif n==11:
        search_Out()
    elif n==12:
        search_Type_room()
    elif n==13:
        search_room_number()
    elif n==14:
        search_bill_amount()
    elif n==15:
        search_no_stay()
    elif n==16:
        search_door()
    elif n==17:
        search_all()
    else:
        print("Invalid")

def update_name():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified Customer's name:")
    inp=B,A
    query='UPDATE project set Name=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")
#----------------------------x----------------------------------x-----------------------------x------------------------------------x
def update_Age():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified Customer's age:")
    inp=B,A
    query='UPDATE project set Age=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")
#----------------------------x----------------------------------x-----------------------------x------------------------------------x
def update_Gender():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified Customer's gender:")
    inp=B,A
    query='UPDATE project set Gender=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")
#----------------------------x----------------------------------x-----------------------------x------------------------------------x
def update_Address():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified Customer's address:")
    inp=B,A
    query='UPDATE project set Address=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")
#----------------------------x----------------------------------x-----------------------------x------------------------------------x
def update_nationality():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified Customer's nationality:")
    inp=B,A
    query='UPDATE project set Nationality=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")
#----------------------------x----------------------------------x-----------------------------x------------------------------------x
def update_aadhar():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified Customer's Aadhar card number:")
    inp=B,A
    query='UPDATE project set Aadhar_card_number=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")

#----------------------------x----------------------------------x-----------------------------x------------------------------------x
def update_visa():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified Customer's Visa number:")
    inp=B,A
    query='UPDATE project set Visa_number=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")
#----------------------------x----------------------------------x-----------------------------x------------------------------------x
def update_mail():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified Customer's Mail ID:")
    inp=B,A
    query='UPDATE project set Mail_ID=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")
#----------------------------x----------------------------------x-----------------------------x------------------------------------x
def update_phone():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified Customer's Phone number:")
    inp=B,A
    query='UPDATE project set Phone_number=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")
#----------------------------x----------------------------------x-----------------------------x------------------------------------x
def update_IN():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified Customer's check-in date:")
    inp=B,A
    query='UPDATE project set Check_in=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")
#----------------------------x----------------------------------x-----------------------------x------------------------------------x
def update_Out():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified Customer's check-out date:")
    inp=B,A
    query='UPDATE project set Check_Out=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")
#----------------------------x----------------------------------x-----------------------------x------------------------------------x
def update_type_room():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified Customer's room type:")
    inp=B,A
    query='UPDATE project set Type_of_Room=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")
#----------------------------x----------------------------------x-----------------------------x------------------------------------x
def update_room_number():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified Customer's room number:")
    inp=B,A
    query='UPDATE project set Room_number=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")
update_room_number()
#----------------------------x----------------------------------x-----------------------------x------------------------------------x
def update_bill():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified Customer's bill amount:")
    inp=B,A
    query='UPDATE project set Bill_Amount=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")

def update_no():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified number of days and nights stay:")
    inp=B,A
    query='UPDATE project set NO_OF_DAYS_NIGHTS=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")

def update_door():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    B=input("Enter the Modified door number:")
    inp=B,A
    query='UPDATE project set Room_door=%s WHERE Room_number=%s'
    cursor.execute(query,inp)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("UPDATE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("UPDATE UNSUCCESSFUL")
        print("x---x---x---x---x")        


def update():
    print("1. To update data based on Customer's Name")
    print("2. To update data based on Customer's Age")
    print("3. To update data based on Customer's Gender")
    print("4. To update data based on Customer's Address")
    print("5. To update data based on Customer's Nationality")
    print("6. To update data based on Customer's Aadhar card number")
    print("7. To update data based on Customer's Visa number")
    print("8. To update data based on Customer's Mail-ID")
    print("9. To update data based on Customer's Phone number")
    print("10. To update data based on Customer's Check-In date")
    print("11. To update data based on Customer's Check-Out date")
    print("12. To update data based on Customer's room type")
    print("13. To update data based on Customer's room number")
    print("14. To update data based on Customer's bill amount")
    print("15. To update data based on Customer's number of days and nights stay")
    print("16. To update data based on Customer's door number")
    n=int(input("Enter the choice:"))
    if n==1:
        update_name()
    elif n==2:
        update_Age()
    elif n==3:
        update_Gender()
    elif n==4:
        update_Address()
    elif n==5:
        update_nationality()
    elif n==6:
        update_aadhar()
    elif n==7:
        update_visa()
    elif n==8:
        update_mail
    elif n==9:
        update_phone()
    elif n==10:
        update_IN
    elif n==11:
        update_Out()
    elif n==12:
        update_type_room()
    elif n==13:
        update_room_number()
    elif n==14:
        update_bill()
    elif n==15:
        update_no()
    elif n==16:
        update_door()
    else:
        print("Invalid")

def dele_room():
    A=input("Enter the Customer's room number(Format->Check-In date(YYYY/MM/DD)/xxxxx(door number)):")
    query="DELETE FROM Project WHERE Room_number=%s";
    cursor.execute(query,(A,))
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("DELETE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("DELETE UNSUCCESSFUL")
        print("x---x---x---x---x")


def dele_all():
    query="DELETE FROM Project";
    cursor.execute(query,)
    if cursor.rowcount!=0:
        mycon.commit()
        print("x---x---x---x---x")
        print("DELETE SUCCESSFUL")
        print("x---x---x---x---x")
    else:
        print("x---x---x---x---")
        print("DELETE UNSUCCESSFUL")
        print("x---x---x---x---x")

def dele():
    print("1. Delete records based on room number")
    print("2. Delete all records")
    n=int(input("Enter the choice:"))
    if n==1:
        dele_room()
    elif n==2:
        dele_all()
    else:
        print("Invalid")

def exist():
    mycon.close()

while True:
    print("1.Add records")
    print("2.Search records")
    print("3.Update records")
    print("4.Delete records")
    print("5.Close SQL-PYTHON Connection")
    print("Stop-Exist")
    n=input("Enter the choice:")
    if n=='1':
        Add_records()
    elif n=='2':
        search()
    elif n=='3':
        update()
    elif n=='4':
        dele()
    elif n=='5':
        exist()
    elif n=='Stop' or n=='STOP':
        break
    else:
        print("Invalid")
        

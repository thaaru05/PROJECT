import mysql.connector as sql
# establishing a connection with the project database
mycon=sql.connect(host="localhost",user="root",passwd="thaaru",database="Project")
if mycon.is_connected()==False:
 print('Error connecting to MySQL database')
cursor=mycon.cursor()
### creating a table called Project with fields Med_no,Product_name,Availability,Selling_Price_One_unit,Expiry_date 
#def table():
#    sql=""" Create table Project(Med_no INT NOT NULL PRIMARY KEY,Product_name varchar(30),Availability varchar(50) NOT NULL, 
#    Selling_Price_One_unit decimal(10,2) NOT NULL,Expiry_date varchar(10) NOT NULL);"""
#    cursor.execute(sql)
#table()
#display all the records in the table
def SelectAll():
    cursor.execute("select * from Project")
    A=cursor.fetchall()
    count=cursor.rowcount
    print("Total number of Records:",count)
    for x in A:
        print('--------------------------------')
        print('Medicine number:',x[0])
        print('Product name:',x[1])
        print('Availability:',x[2])
        print('Selling price of one unit(in rupees):',x[3])
        print('Expiry Date:',x[4])
        print('---------------------------------')
##insert_records() function allows one to insert a record into the function
def insert_records():
    cursor.reset()
    while True:
        r=int(input("Enter the Medicine number:"))
        n=input("Enter Product name:")
        m=input("Enter availability:")
        p=float(input("Enter the price of one unit of quantity(in rupees):"))
        t=input('Enter the Expiry date:')
        query="INSERT INTO Project VALUES(%s,%s,%s,%s,%s)"
        value=(r,n,m,p,t)
        cursor.execute(query,value)
        mycon.commit()
        ch=input("Do you want to insert another record (Yes/No):")
        if ch=='No' or ch=='NO' or ch=='no':
            break
    SelectAll()
##DisplayMany() function allows to display records from table
def DisplayMany():
    n=int(input("Enter the number of records to be displayed:"))
    cursor.reset()
    cursor.execute("select * from Project")
    d=cursor.fetchmany(n)
    count=cursor.rowcount
    print("Total number of rows retrieved from table:",count)
    for x in d:
        print('--------------------------------')
        print('Medicine number:',x[0])
        print('Product name:',x[1])
        print('Availability:',x[2])
        print('Selling price of one unit(in rupees):',x[3])
        print('Expiry Date:',x[4])
        print('---------------------------------')

##Update_records() function allows to update the record
def update_record():
    cursor.reset()
    while True:
        a=int(input("Enter the medicine number of the record you want to modify:"))
        n=input("Enter the name:")
        m=input("Enter the new Availablity amount:")
        s=float(input("Enter the selling price(in rupees):"))
        t=input('Enter the expiry date:')
        query1=("update Project set Product_name='%s',Availability='%s',Selling_Price_One_unit=%s,Expiry_date='%s' where Med_no=%s")%(n,m,s,t,a)
        cursor.execute(query1)
        if cursor.rowcount!=0:
            mycon.commit()
        else:
            print('No record found')
        ch=input("Do you want to modify another record (Yes/No):")
        if ch=='No' or ch=='NO' or ch=='no':
            break
    SelectAll()    
# a record can be deleted
def delete_record():
    cursor.reset()
    while True:
        c=int(input("Enter the medicine number that you want to delete:"))
        cursor.execute("delete from Project where Med_no=%s"%(c))
        if cursor.rowcount!=0:
            mycon.commit()
            print('DELETED THE RECORD')
        else:
            print('DELETION UNSUCCESFUL')
            print('---------------------')
            print('Record not found')
        ch=input("Do you want to delete another record{Yes/No}:")
        if ch=='No' or ch=='NO' or ch=='no':
            break
# looks for the product availability
def search():
    cursor.reset()
    while True:
        p=input("Which product are you looking for(Enter the medicine number):")
        query1="select *from Project where Med_no='%s'"%p
        cursor.execute(query1)
        data=cursor.fetchmany()
        if data!=None:
            print("The product is available in the store")
            for x in data:
                print('--------------------------------')
                print('Medicine number:',x[0])
                print('Product name:',x[1])
                print('Availability:',x[2])
                print('Selling price of one unit(in rupees):',x[3])
                print('Expiry Date:',x[4])
                print('---------------------------------')
        elif data==None:
            print("Sorry the product is not available")
        ch=input("Do you want to look for another product{Yes/No}:")
        if ch=='No' or ch=='NO' or ch=='no':
            break
def clean():
    mycon.close()

ch=0
while ch!=6:
    print("MENU")
    print('1.Display records')
    print('2.Insert new records')
    print('3.Update record')
    print('4.Delete record')
    print('5.Search record')
    print('6.Quit')
    ch=int(input('Enter your choice:'))
    if ch>8:
        print("Error,choose a number between 1-6")
        ch=int(input("Enter a valid choice:"))
    elif ch==1:
        print('1.Display all the records')
        print('2.Display certain number of records')
        c=int(input('Enter your choice:'))
        if c==1:
            SelectAll()
        elif c==2:
            DisplayMany()
        else:
            print('Enter the correct option')
    elif ch==2:
        insert_records()
    elif ch==3:
        update_record()
    elif ch==4:
        delete_record()
    elif ch==5:
        search()
    else:
        clean()
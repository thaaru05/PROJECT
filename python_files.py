23rd March, 2021

1. Write a menu driven program using functions to do the following:
a) Reverse a number
b) Checks whether a number is palindrome or not
c) Checks whether a number is an Armstrong number or not
d) Prints the multiplication table of a number
e) Checks whether a number is a prime or not
The number is passed as an argument to the function. The program should repeat till users enter Y or y.
Program:
def rev(z):
        rev=0
        while (z>0):
            dig=z%10
            rev=rev*10+dig
            z=z//10
        print("Reverse of the number:",rev)
def pal(z):
    temp=z
    rev=0
    while (z>0):
        dig=z%10
        rev=rev*10+dig



Output:

Reverse the number:Type a
Check whether the number is palindrome or not:Type b
Check whether the number is armstrong number or not:Type c
Multiplication table:Type d
Check whether the number is prime number or not:Type e
To continue the program:Type y

Enter the number:59

Enter your choice:b
The number you have entered is: 59
The number is not Palindrome

To continue(enter y or Y):y
Reverse the number:Type a
Check whether the number is palindrome or not:Type b
Check whether the number is armstrong number or not:Type c
Multiplication table:Type d
Check whether the number is prime number or not:Type e
To continue the program:Type y

Enter the number:23



       z=z//10
        if temp==rev:
            print('The number is Palindrome')
            break
        else:
            print('The number is not Palindrome')
            break
def Arm(z):
    sum=0
    temp = z
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
        if z == sum:
            print(z,"is an Armstrong number")
            break
        else:
            print(z,"is not an Armstrong number")
            break
def multi(z):
    for i in range(1,11):
            print(z,"X",i,"=",i*z)
def prime(z):
    if z > 1:
        for i in range(1,z):

Enter your choice:a
The number you have entered is: 23
Reverse of the number: 32

To continue(enter y or Y):t
Thank you!





















            if (z % i) == 0:
                print(z, "is not a prime number")
                break
            else:
                print(z, "is a prime number")
                break
choice='y' or 'Y'


while (choice=='y' or choice=='Y'):
    
    print("Reverse the number:Type a")
    print("Check whether the number is palindrome or not:Type b")
    print("Check whether the number is armstrong number or not:Type c")
    print("Multiplication table:Type d")
    print("Check whether the number is prime number or not:Type e")
    print("To continue the program:Type y")
    z=int(input('Enter the number:'))
    y=input('Enter your choice:')
    print("The number you have entered is:",z)
    if y=="a":
        rev(z)
    elif y=="b":
        pal(z)
    elif y=="c":
        Arm(z)

Reverse the number:Type a
Check whether the number is palindrome or not:Type b
Check whether the number is armstrong number or not:Type c
Multiplication table:Type d
Check whether the number is prime number or not:Type e
To continue the program:Type y

Enter the number:8

Enter your choice:d
The number you have entered is: 8
8 X 1 = 8
8 X 2 = 16
8 X 3 = 24
8 X 4 = 32
8 X 5 = 40
8 X 6 = 48
8 X 7 = 56
8 X 8 = 64
8 X 9 = 72
8 X 10 = 80

To continue(enter y or Y):f
Thank you!



    elif y=="d":
        multi(z)
    elif y=="e":
        prime(z)    
    else:
        print("Enter the correct option")
    choice=input('To continue(enter y or Y):')

print('Thank you!')













































30th March, 2021
2. Write an interactive menu driven program using functions which does the following:
 a) Searches for an element in a list of values
 b) Display the frequency of a particular element
 c) Find the smallest and biggest value among a list of values
 d) Find the mean of the list of values
Program:

def search():
    n=int(input("Enter the element that you want to search:"))
    if n in l:
        print(n,'is a element in the list')
    else:
        print(n,'is not a element in the list')
def count():
    n=int(input("Enter the element that you want to count:"))
    if n in l:
        x=l.count(n)
        print('The frequency of',n,'is:',x)
    else:
        print('The element is not in the list!')
def value():
    x=min(l)
    print("The smallest value in the list is:",x)
    y=max(l)


Output:

To search for an element in a list of values:-Type a
To display the frequency of a particular element:-Type b
Find the smallest and biggest value among a list of values:-Type c
Find the mean of the list of values:-Type d
To continue the program : Type y

Enter the list:[2,3,8,9]

Enter your choice:c
The list is: [2, 3, 8, 9]
The smallest value in the list is: 2
The biggest value in the list is: 9

To continue(enter y or Y):d
Thank you!









    print('The biggest value in the list is:',y)
def mean():
    import statistics
    c=statistics.mean(l)
    print("The mean of the list is:",c)
choice='Y' or 'y'
while (choice=='Y' or choice=='y'):
    print('To search for an element in a list of values:-Type a')
    print('To display the frequency of a particular element:-Type b')
    print('Find the smallest and biggest value among a list of values:-Type c')
    print('Find the mean of the list of values:-Type d')
    print("To continue the program : Type y")
    l=eval(input("Enter the list:"))
    y=input('Enter your choice:')
    print('The list is:',l)
    if y=='a':
        search()
    elif y=='b':
        count()
    elif y=='c':
        value()
    elif y=='d':
        mean()
    else:
        print("Enter the correct option")


To search for an element in a list of values:-Type a
To display the frequency of a particular element:-Type b
Find the smallest and biggest value among a list of values:-Type c
Find the mean of the list of values:-Type d
To continue the program : Type y

Enter the list:[1,3,56,9,8,9,71,5]

Enter your choice:d
The list is: [1, 3, 56, 9, 8, 9, 71, 5]
The mean of the list is: 20.25

To continue(enter y or Y):g
Thank you!












       
choice=input('To continue(enter y or Y):')
    
print('Thank you!')



















































6th April, 2021
3.Define functions for the following:- 
a) To input list elements. 
b) To display list elements. 
c) To delete an element from the list. 
                      Write a menu driven program.
Program:
def input_list():
    global l
    l=eval(input("Enter the list:"))
    return l

def dis(l):
    print("The list is:",l)

def delete(l):
    n=int(input("Enter the element that you want to delete from the list:"))
    if n in l:
        l.remove(n)
    else:
        print(n,"is not in the list or the list is empty")
return l
l=[]
choice='y' or 'Y'
while (choice=='y' or choice=='Y'):
print("To input list elements:Type a")

Output:
To input list elements:Type a
To display list elements:Type b
To delete an element from the list:Type c
To continue the program : Type y

Enter your choice:a

Enter the list:[1,2,3,56,1]

To continue(enter y or Y):y
To input list elements:Type a
To display list elements:Type b
To delete an element from the list:Type c
To continue the program : Type y

Enter your choice:b
The list is: [1, 2, 3, 56, 1]

To continue(enter y or Y):u
Thank you!!






print("To display list elements:Type b")
    print("To delete an element from the list:Type c")
    print("To continue the program : Type y")
  
    ch=input("Enter your choice:")
    if ch=="a":
        l = input_list()
    elif ch=="b":
        dis(l)
    elif ch=="c":
        delete(l)
    else:
        print("Enter the correct option")
    choice=input('To continue(enter y or Y):')
print("Thank you!!")












To input list elements:Type a
To display list elements:Type b
To delete an element from the list:Type c
To continue the program : Type y

Enter your choice:b
The list is: []

To continue(enter y or Y):k
Thank you!!

















13th April, 2021
                 
4. Write a python script to take input for a limit and define functions for the following. 
a) Calculate and print the sum of all the numbers upto the limit 
b) Calculate and print its factorial 
c) Print Fibonacci series upto the limit 

Program:
limit=int(input("Enter the limit:"))
def Calculate_sum():
    sum=0
    for i in range(1,limit+1):
        sum=sum+i
    print("The sum of all the numbers upto limit is:",sum)
Calculate_sum()        
def factorial():
    fact=1
    a=1
    while a<=limit:
        fact*=a
        a+=1
    print("The factorial is:",fact) 
factorial()


Output:
Enter the limit:5
The sum of all the numbers upto limit is: 15
The factorial is: 120
The Fibonacci series is:
1
2
3
5
8
13















def  Fibonacci():
   print("The Fibonacci series is:")
    a=0
    b=1
    for i in range(limit+1):
        c=a+b
        print(c)
        a=b
        b=c
Fibonacci()












































17th April, 2021
5. Repeatedly ask the user to enter a team name and how many games the team has won and how many they lost. Store this information in a dictionary where the keys are the team names and the values are list of the form [wins, losses].
(i) using the dictionary created above , allow the user to enter a team name and print out the teams winning percentage.
(ii) using dictionary create a list whose entries are the number of wins of each team.
(iii) using the dictionary , create a list of all those teams that have winning records.

Program:
d={}
win=[]
R=[]
choice='y' or 'Y'
while (choice=='y' or choice=='Y'):
    name=input("Enter the name of the team:")
    win1=int(input('Enter the number of wins:'))
    loss=int(input('Enter the number of loss:'))
    d[name]=[win1,loss]
    win+=[win1]
    if win1>0:
        R+=[name]
choice=input('To continue(enter y or Y):')
n=input('Enter the name of the team that you want to know the percentage of winning:')

Output:
Enter the name of the team:CK

Enter the number of wins:10

Enter the number of loss:5

To continue(enter y or Y):Y

Enter the name of the team:MI

Enter the number of wins:2

Enter the number of loss:13

To continue(enter y or Y):Y

Enter the name of the team:RR

Enter the number of wins:3

Enter the number of loss:12

To continue(enter y or Y):T



if n in d:
    print('The percentage of',n,'winning is:',d[n][0]*100/(d[n][0]+d[n][1]),"%")
else:
    print('Team',n,'not found')
print("The number of wins of each team is:",win)
print("Teams having winning records:",R)























Enter the name of the team that you want to know the percentage of winning:CSK
Team CSK not found
The number of wins of each team is: [10, 2, 3]
Teams having winning records: ['CK', 'MI', 'RR']




















22nd April, 2021
6. Create a dictionary whose keys are month name and whose values are number of days in the corresponding month :
(a) ask the user to enter the month name and use the dictionary to tell how many days are in month .
(b) print out all of the keys in alphabetical order  .
(c) print out all of the month with 31 days
(d) print out the (key - value) pair sorted  by the number of the days in each month .
Program:
M={'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
A=input('Enter a month for which you want to know the number of days:')
if A in M:
    print('Number of days in',A,'is',M[A])
else:
    print(A,'not found')
print()
X=[]
for i in M:
    X+=list([i])
X.sort()
for i in X:
    print(i)
print()



Output:
Enter a month for which you want to know the number of days:June
Number of days in June is 30

April
August
December
February
January
July
June
March
May
November
October
September

Months with 31 days are:
January
March
May
July
August
October
December


print("Months with 31 days are:")
for C in M:
    if M[C]==31:
        print(C)
print()
for y in M:
    if M[y] == 28:
        print("The key-value pair is %s and %s" %(y, 28))
for x in M:
    if M[x] == 30:
        print("The key-value pair is %s and %s" %(x, 30))
for z in M:
    if M[z] == 31:
        print("The key-value pair is %s and %s" %(z, 31))













The key-value pair is February and 28
The key-value pair is April and 30
The key-value pair is June and 30
The key-value pair is September and 30
The key-value pair is November and 30
The key-value pair is January and 31
The key-value pair is March and 31
The key-value pair is May and 31
The key-value pair is July and 31
The key-value pair is August and 31
The key-value pair is October and 31
The key-value pair is December and 31















27th April, 2021
7. Write a menu driven program to do the followings:
a) To add admission number, name and marks of students into the text file student.txt
b) To display the details of all the students 
c) To search and display the details of a student by asking the user to enter the admission number.
Program:
def A():
    count=int(input("How many students are there in the Class?"))
    f=open("student.txt","w")
    for i in range(count):
        print("Enter details for students",(i+1),"below:")
        admin=input("Admission number:")
        name=input("Name:")
        marks=input("Marks:")
        rec=admin+","+name+","+marks+'\n'
        f.write(rec)
    f.close()
def B():
        F=open("student.txt","r")
        k=str
        while k:
            k=F.readline()
            print(k)
        F.close()
  

Output:
To add data enter A
To display the details enter B
To search and display the details enter C
To continue enter Y

Enter your choice:A

How many students are there in the Class?3
Enter details for students 1 below:

Admission number:1

Name:Ann

Marks:20
Enter details for students 2 below:

Admission number:2

Name:Ben

Marks:25
Enter details for students 3 below:

Admission number:3
def C():
    C=input("Enter the admission number:")
    search=open("student.txt")
    for line in search:
        if C in line:
            print(line)
    search.close()            
 
choice='y' or 'Y'
while (choice=='y' or choice=='Y'):
    print("To add data enter A")
    print("To display the details enter B")
    print("To search and display the details enter C")
    print("To continue enter Y")
    
    y=input('Enter your choice:')
    if y=="A":
        A()
    elif y=="B":
        B()
    elif y=="C":
        C()
    else:
        print("ERROR")
    choice=input('To continue(enter y or Y):')


Name:Max

Marks:24

To continue(enter y or Y):y
To add data enter A
To display the details enter B
To search and display the details enter C
To continue enter Y

Enter your choice:C

Enter the admission number:3
3,Max,24


To continue(enter y or Y):d










3rd May, 2021
8. Write an interactive menu driven program with the following four functions:
a) To create a text file called ‘Information.txt’ with some countries and capitals.
b) To display the file contents.
c) Create another file called ‘Copy.txt’ to store all the countries and capitals in uppercase string from ‘Information.txt’.
d) Display the contents of ‘Information.txt’ and ‘Copy.txt’ files.
Program:
def A():
    F=open("Information.txt","w")
    N=int(input("Enter the number of countries:"))
    for i in range(N):
        con=input("Enter the name of the country:")
        cap=input("Enter the capital:")
        F.write(con)
        F.write('\t')
        F.write(cap)
        F.write('\n')
    F.close()
def B():
    F=open("Information.txt","r")
    k=str
    while k:
        k=F.readline()
        print(k)
    F.close()
Output:
To create text file with some countries and capitals-Enter A
To display the file contents-Enter B
To create another text file to store all the countries and capitals in uppercase-Enter C
To display the file contents of both thr files-Enter D

Enter your choice:0
ERROR

To continue(enter y or Y):O

To create text file with some countries and capitals-Enter A
To display the file contents-Enter B
To create another text file to store all the countries and capitals in uppercase-Enter C
To display the file contents of both thr files-Enter D
To continue-Enter Y

Enter your choice:A

Enter the number of countries:3

Enter the name of the country:India



def C():
    with open("Information.txt") as F1,open("Copy.txt","w") as F2:
        line=F1.read()
        k=line.upper()
        F2.write(k)
    F1.close()
    F2.close()

def D():
    F=open("Information.txt","r")
    k=str
    while k:
        k=F.readline()
        print(k)
    F.close()
    F1=open("Copy.txt","r")
    t=str
    while t:
        t=F1.readline()
        print(t)
    F1.close()






Enter the capital:New Delhi

Enter the name of the country:Kuwait

Enter the capital:Kuwait City

Enter the name of the country:Germany

Enter the capital:Berlin

To continue(enter y or Y):Y
To create text file with some countries and capitals-Enter A
To display the file contents-Enter B
To create another text file to store all the countries and capitals in uppercase-Enter C
To display the file contents of both thr files-Enter D
To continue-Enter Y

Enter your choice:C

To continue(enter y or Y):Y
To create text file with some countries and capitals-Enter A
To display the file contents-Enter B
To create another text file to store all the countries and capitals in uppercase-Enter C
To display the file contents of both thr files-Enter D
To continue-Enter Y
choice='y' or 'Y'
while (choice=='y' or choice=='Y'):
    print("To create text file with some countries and capitals-Enter A")
    print("To display the file contents-Enter B")
    print("To create another text file to store all the countries and capitals in uppercase-Enter C")
    print("To display the file contents of both thr files-Enter D")
    print("To continue-Enter Y")
    
    y=input('Enter your choice:')
    if y=="A":
        A()
    elif y=="B":
        B()
    elif y=="C":
        C()
    elif y=="D":
        D()
    else:
        print("ERROR")
    choice=input('To continue(enter y or Y):')







Enter your choice:D
India   New Delhi

Kuwait  Kuwait City

Germany Berlin


INDIA   NEW DELHI

KUWAIT  KUWAIT CITY

GERMANY BERLIN



To continue(enter y or Y):S









23rd May, 2021
9. Write an interactive menu driven program with the following functions:
a) To create a text file called ‘WEATHER.TXT’ and add some lines of text into it.
b) To count and display the number of lines, alphabets, digits and spaces present in the file ‘WEATHER.TXT’. File name must be passed as an argument to the function.
c) To copy only those lines starting with uppercase letter from the file ‘WEATHER.TXT’ to another file ‘climate.txt’.
d) To count the number of occurrence of the words “the” and “THE” in the file ‘climate.txt’.
Program:
def A():
    F=open("WEATHER.TXT","w")
    I=input("Enter the lines:")
    F.write(I)
    F.close()
def B(fname):
    fname=open(fname)
    L=S=A=D=0
    while 1:
        line=fname.readline()
        if not line:
            break
        else:
            L+=1
            for k in line:
                if k.isspace():
                    S+=1
Output:
To create and add data into the file-Enter A
To count and display the number of lines, alphabets, digits and spaces present in the file-Enter B
To copy only those lines starting with uppercase letter from the file to another file-Enter C
To count the number of occurrence of the words the and THE in the file climate.txt-Enter D
To continue-Enter Y

Enter your choice:A

Enter the lines:THE cat is sitting under the table.

To continue(enter y or Y):Y
To create and add data into the file-Enter A
To count and display the number of lines, alphabets, digits and spaces present in the file-Enter B
To copy only those lines starting with uppercase letter from the file to another file-Enter C
To count the number of occurrence of the words the and THE in the file climate.txt-Enter D
To continue-Enter Y

Enter your choice:C




                if k.isalpha():
                    A+=1
                if k.isdigit():
                    D+=1
    print('Line:',L)
    print('Space:',S)
    print('Alphabets:',A)
    print('Digits:',D)
    fname.close()
def C():
    f1=open("WEATHER.TXT")
    f2=open("climate.TXT","w")
    while 1:
        line=f1.readline()
        if not line:
            break
        else:
            if line[0].isupper():
                f2.write(line)
    f1.close()
    f2.close()
def D():
      f=open("climate.TXT")
      c=0
      while 1:
          line=f.readline()
          if not line:
To continue(enter y or Y):Y
To create and add data into the file-Enter A
To count and display the number of lines, alphabets, digits and spaces present in the file-Enter B
To copy only those lines starting with uppercase letter from the file to another file-Enter C
To count the number of occurrence of the words the and THE in the file climate.txt-Enter D
To continue-Enter Y

Enter your choice:D
2 times

To continue(enter y or Y):F              














                break
          else:
              for k in line.split():
                  if 'the' in k or 'THE' in k:
                      c+=1
              print(c, 'times')
      f.close()
choice='y' or 'Y'
while (choice=='y' or choice=='Y'):
    print("To create and add data into the file-Enter A")
    print("To count and display the number of lines, alphabets, digits and spaces present in the file-Enter B")
    print("To copy only those lines starting with uppercase letter from the file to another file-Enter C")
    print("To count the number of occurrence of the words the and THE in the file climate.txt-Enter D")
    print("To continue-Enter Y")


    y=input('Enter your choice:')
    if y=="A":
        A()
    elif y=="B":
        B("WEATHER.TXT")
    elif y=="C":
        C()
    elif y=="D":
        D()
To create and add data into the file-Enter A
To count and display the number of lines, alphabets, digits and spaces present in the file-Enter B
To copy only those lines starting with uppercase letter from the file to another file-Enter C
To count the number of occurrence of the words the and THE in the file climate.txt-Enter D
To continue-Enter Y

Enter your choice:B
Line: 1
Space: 6
Alphabets: 28
Digits: 0

To continue(enter y or Y):c    












else:
        print("ERROR")

choice=input('To continue(enter y or Y):')


















































27th May, 2021
10. A binary file ‘CUSTOMER.DAT’ contains customer’s names and telephone numbers. Write functions to do the following:
a) Append record in the file
b) Display the content of the file.
c) Display the name for a given telephone number.
Telephone number is passed as an argument.
If the telephone number does not exist, then display the error message, Record not found.
Write a menu driven program.
Program:
import pickle
def set_data():
    name=input("Enter the name of the customer:")
    number=int(input("Enter the phone number:"))
    print()
    
    customer={}
    customer['name']=name
    customer['number']=number
    return customer

def display_data(customer):
    print('Name:',customer['name'])
    print('Phone number:',customer['number'])
    print()

Output:
1. Append Record
2. Display Records
3. Search a Record
4. Exit

Enter choice(1-4): 1


Enter the name of the customer:	Max

Enter the phone number:55159624

1. Append Record
2. Display Records
3. Search a Record
4. Exit

Enter choice(1-4): 1


Enter the name of the customer:Lena

Enter the phone number:55156825

1. Append Record
2. Display Records
def write_record():
    f=open('CUSTOMER.DAT','ab')
    pickle.dump(set_data(),f)
    f.close()

def read_records():
    F1=open('CUSTOMER.DAT','rb')
    while True:
        try:
            customer=pickle.load(F1)
            display_data(customer)
        except EOFError:
            break
    F1.close()
        
def search_record():
    F=open('CUSTOMER.DAT','rb')
    number=int(input("Enter the phone number:"))
    flag=False
    while True:
        try:
            customer=pickle.load(F)
            if customer['number']==number:
                display_data(customer)
                flag=True
                break
        except EOFError:
3. Search a Record
4. Exit

Enter choice(1-4): 2

Name:   Max
Phone number: 55159624

Name: Lena
Phone number: 55156825

1. Append Record
2. Display Records
3. Search a Record
4. Exit

Enter choice(1-4): 4










             break
  if flag==False:
            print('Record not found')
            print()
    F.close()
    
def show_choices():
    print('1. Append Record')
    print('2. Display Records')
    print('3. Search a Record')
    print('4. Exit')
while True:
        show_choices()
        choice = input('Enter choice(1-4): ')
        print()
        
        if choice == '1':
            write_record()    
        elif choice == '2':
            read_records()
        elif choice == '3':
            search_record()
        elif choice == '4':
            break
        else:
            print('Invalid input')




























2nd June, 2021
11. Write a menu driven program to do the following on the file hospital.dat which contains admission number, name of patient, patient type (in-patient or out-patient), department, doctor name, bill amount.
 a) Insert records
b) Display records
c) Search for a particular record based on admission number
d) Search for all records under a department
e) Search for all patient either in-patient or out-patient
f) Modify doctor name based on admission number
Program:
import pickle
def Data():
    admin=int(input("Enter the admission number :"))
    name=input("Enter the name of the patient:")
    patient_type=input("Enter the patient's type:")
    department=input("Enter department: ")
    doc_name=input("Enter the doctor's name:")
    bill_amount=input("Enter the bill amount in USD:")
    print()    
    D={}
    D['admin']=admin
    D['name']=name
    D['patient_type']=patient_type
    D['department']=department
    D['doc_name']=doc_name
    D['bill_amount']=bill_amount
Output:
1. Append Record
2. Display Records
3. Search admission number
4. Search department
5. Patient's type
6. Modify doctor's name
Stop - Exit

Enter choice: 1


Enter the admission number :12345

Enter the name of the patient:Luna

Enter the patient's type:Out

Enter department: E.N.T

Enter the doctor's name:Dr.Ryans

Enter the bill amount in USD:60.00

1. Append Record
2. Display Records
3. Search admission number
return D

def display_data(D):
    print('Admission number:',D['admin'])
    print('Name of the patient:',D['name'])
    print("Patient's type:",D['patient_type'])
    print('Department:',D['department'])
    print("Doctor's name:",D['doc_name'])
    print('Bill amount',D['bill_amount'])
    print()
    
def write_record():
    f=open('hospital.dat','ab+')
    pickle.dump(Data(),f)
    f.close()

def read_records():
    F1=open('hospital.dat','rb')
    while True:
        try:
            D=pickle.load(F1)
            display_data(D)
        except EOFError:
            break
    F1.close()


4. Search department
5. Patient's type
6. Modify doctor's name
Stop - Exit

Enter choice: 1


Enter the admission number :65412

Enter the name of the patient:Tom

Enter the patient's type:In

Enter department: Cardiology

Enter the doctor's name:Dr.Max Goodwell

Enter the bill amount in USD:100.00

1. Append Record
2. Display Records
3. Search admission number
4. Search department
5. Patient's type
6. Modify doctor's name
Stop-Exit
def search_admin():
    F=open('hospital.dat','rb')
    number=int(input("Enter the admission number of the patient:"))
    flag=False
    while True:
        try:
            D=pickle.load(F)
            if D['admin']==number:
                display_data(D)
                flag=True
                break
        except EOFError:
            break
    if flag==False:
            print('Record not found')
            print()
    F.close()
    
def search_department():
    F1=open('hospital.dat','rb')
    depart=input("Enter the department:")
    flag=False
    while True:
        try:
            D=pickle.load(F1)
            if D['department']==depart:
                display_data(D)
 
Enter choice: 1


Enter the admission number :78925

Enter the name of the patient:Chris 

Enter the patient's type:Out

Enter department: Neurology

Enter the doctor's name:Dr.Vijay Kapoor

Enter the bill amount in USD:250.00

1. Append Record
2. Display Records
3. Search admission number
4. Search department
5. Patient's type
6. Modify doctor's name
Stop - Exit           

Enter choice: 3


                flag=True
                break
        except EOFError:
            break
    if flag==False:
            print('Record not found')
            print()
    F1.close()   
    
def search_type():
    F=open('hospital.dat','rb')
    p_type=input("Enter the patient's type:")
    flag=False
    while True:
        try:
            D=pickle.load(F)
            if D['patient_type']==p_type:
                display_data(D)
                flag=True
                break
        except EOFError:
            break
    if flag==False:
            print('Record not found')
            print()
    F.close()

Enter the admission number of the patient:65412
Admission number: 65412
Name of the patient: Tom
Patient's type: In
Department: Cardiology
Doctor's name: Dr.Max Goodwell
Bill amount 100.00

1. Append Record
2. Display Records
3. Search admission number
4. Search department
5. Patient's type
6. Modify doctor's name
Stop - Exit

Enter choice: Stop










def change_doc():
    Admin=int(input("Enter the admission number:"))
    F=open('hospital.dat','rb+')
    
    try:
        while True:
            rpos=F.tell()
            D=pickle.load(F)
            if D['admin']==Admin:
                doc=input("Enter the modified name of the doctor:")
                D['doc_name']=doc
                F.seek(rpos)
                pickle.dump(D,F)
                found=True
    except EOFError:
        if found==False:
            print("No record found")
        else:
            print("Record successfully modified!")
    F.close()
def show_choices():
    print('1. Append Record')
    print('2. Display Records')
    print('3. Search admission number')
    print('4. Search department')
    print("5. Patient's type")
    print("6. Modify doctor's name")
 1. Append Record
2. Display Records
3. Search admission number
4. Search department
5. Patient's type
6. Modify doctor's name
Stop - Exit

Enter choice: 4


Enter the department:Cardiology
Admission number: 65412
Name of the patient: Tom
Patient's type: In
Department: Cardiology
Doctor's name: Dr.Max Goodwell
Bill amount 100.00

1. Append Record
2. Display Records
3. Search admission number
4. Search department
5. Patient's type
6. Modify doctor's name
Stop - Exit

    print('Stop - Exit')
while True:
        show_choices()
        choice = input('Enter choice: ')
        print()
        
        if choice == '1':
            write_record()            
        elif choice == '2':
            read_records()
        elif choice == '3':
            search_admin()
        elif choice=='4':
            search_department()
        elif choice=='5':
            search_type()
        elif choice=='6':
            change_doc()
        elif choice == 'Stop':
            break
        else:
            print('Invalid')






Enter the admission number :65425

Enter the name of the patient:Shan

Enter the patient's type:In

Enter department: Radiology

Enter the doctor's name:Dr.Helen Sharpe

Enter the bill amount in USD:500.00

1. Append Record
2. Display Records
3. Search admission number
4. Search department
5. Patient's type
6. Modify doctor's name
Stop - Exit

Enter choice: Stop





8th June, 2021
12. Write a menu driven program to create a file Book.dat which contains the following details Book ID, Book name, author name and Price. The program should be able to do the following:
a)Write records into the file
b) Read the content of the file
c) Append records to the file
d) Search for books priced in the range of 100 and 500
c) Modify the price of the book with book name as C++
Program:
import pickle
def Data():
    global L
    Book_ID=input("Enter the book id:")
    Book_name=input("Enter the name of the book:")
    Author=input("Enter the name of the Author:")
    Price=int(input("Enter the price of the book in INR:"))
    L=[Book_ID,Book_name,Author,Price]
    return L

def display(L):
    print('Book ID:',L[0])
    print('Book name:',L[1])
    print('Author:',L[2])
    print('Price:',L[3])


Output:
1.Write records into the file
2.Read the content of the file
3.Appeand records
4.Search for books priced range 100 to 500
5.Modify the price of the book with book name as C++
6.Stop-Exit

Enter the choice:1

Enter the book id:B014369

Enter the name of the book:Pride and Prejudice

Enter the name of the Author:Jane Austen

Enter the price of the book in INR:150

Would you like to add more(Yes/No):yes

Enter the book id:B963258

Enter the name of the book:The Fault in Our Stars

Enter the name of the Author:John Green

Enter the price of the book in INR:750
def write():
    ch='Yes'
    while ch=='Yes' or ch== 'yes':
        f=open('Book.dat','ab')
        pickle.dump(Data(),f)
        f.close()
        ch=input("Would you like to add more(Yes/No):")
        f.close()

def read_records():
    F1=open('Book.dat','rb')
    while True:
        try:
            D=pickle.load(F1)
            display(D)
        except EOFError:
            break
    F1.close()

def write_record():
    f=open('Book.dat','ab')
    pickle.dump(Data(),f)
    f.close()





Would you like to add more(Yes/No):no
1.Write records into the file
2.Read the content of the file
3.Appeand records
4.Search for books priced range 100 to 500
5.Modify the price of the book with book name as C++
6.Stop-Exit

Enter the choice:4
Details are:
Book ID: B014369
Book name: Pride and Prejudice
Author: Jane Austen
Price: 150
1.Write records into the file
2.Read the content of the file
3.Appeand records
4.Search for books priced range 100 to 500
5.Modify the price of the book with book name as C++
6.Stop-Exit

Enter the choice:2
Details are:
Book ID: B014369
Book name: Pride and Prejudice
Author: Jane Austen
def search():
    F=open('Book.dat','rb')
    flag=False
    while True:
        try:
            D=pickle.load(F)
            if D[3] in range(100,501):
                display(D)
                flag=True
        except EOFError:
            break
    if flag==False:
            print('Record not found')
            print()
    F.close()

def change():
    Book_name='C++'
   Found=False
    F=open('Book.dat','rb+')
    try:
        while True:
            rpos=F.tell()
            D=pickle.load(F)
            if D[1]==Book_name:
                Price=int(input("Enter the modified cost:"))
                D[3]=Price
Price: 750
1.Write records into the file
2.Read the content of the file
3.Appeand records
4.Search for books priced range 100 to 500
5.Modify the price of the book with book name as C++
6.Stop-Exit

Enter the choice:Stop


















                F.seek(rpos)
                pickle.dump(D,F)
                found=True
    except EOFError:
        if found==False:
            print("No record found")
        else:
            print("Record successfully modified!")
    F.close()
def show_choices():
    print('1.Write records into the file')
    print('2.Read the content of the file')
    print('3.Appeand records')
    print('4.Search for books priced range 100 to 500')
    print('5.Modify the price of the book with book name as C++')
    print('6.Stop-Exit')
    
    
while True:
    show_choices()
    choice=input("Enter the choice:")
    if choice=='1':
        write()  
    elif choice=='2':
        print("Details are:")
        read_records()

1.Write records into the file
2.Read the content of the file
3.Appeand records
4.Search for books priced range 100 to 500
5.Modify the price of the book with book name as C++
6.Stop-Exit

Enter the choice:3

Enter the book id:B987450

Enter the name of the book:C++

Enter the name of the Author:Shan K

Enter the price of the book in INR:780
1.Write records into the file
2.Read the content of the file
3.Appeand records
4.Search for books priced range 100 to 500
5.Modify the price of the book with book name as C++
6.Stop-Exit

Enter the choice:5

Enter the modified cost:560
Record successfully modified!
    elif choice=='3':
        write_record()
    elif choice=='4':
        print("Details are:")
        search()
    elif choice=='5':
        change()
    elif choice=="Stop":
        break
    else:
        print("ERROR!")
















1.Write records into the file
2.Read the content of the file
3.Appeand records
4.Search for books priced range 100 to 500
5.Modify the price of the book with book name as C++
6.Stop-Exit

Enter the choice:Stop



















15th June, 2021
13. Write a menu driven program to create a file Book.dat which contains the following details Book ID, Book name, author name and Price in the form of Dictionary. The program should be able to do the following:
a) Write records into the file
b) Read the content of the file
c) Append records to the file
d) Search for books priced in the range of 100 and 500
c) Modify the price of the book with book name as C++
Program:
import pickle
def Data():
    Book_ID=input("Enter the book id:")
    Book_name=input("Enter the name of the book:")
    Author=input("Enter the name of the Author:")
    Price=int(input("Enter the price of the book in INR:"))
    print()
    
    D={}
    D['Book_ID']=Book_ID
    D['Book_name']=Book_name
    D['Author']=Author
    D['Price']=Price
    return D

def display_data(D):
    print('Book ID:',D['Book_ID'])
Output:
1.Write records into the file
2.Read the content of the file
3.Appeand records
4.Search for books priced range 100 to 500
5.Modify the price of the book with book name as C++
6.Stop-Exit

Enter the choice:1

Enter the book id:B963147

Enter the name of the book:Pride and Prejudice

Enter the name of the Author:Jane Austen

Enter the price of the book in INR:750


Would you like to add more(Yes/No):yes

Enter the book id:B321789

Enter the name of the book:The Fault in Our Stars

Enter the name of the Author:John Green

    print('Book name:',D['Book_name'])
    print('Author:',D['Author'])
    print('Price:',D['Price'])
    
def write():
    ch='Yes'
    while ch=='Yes' or ch=='yes':
        f=open('Book.dat','ab')
        pickle.dump(Data(),f)
        f.close()
        ch=input("Would you like to add more(Yes/No):")
        f.close()
        
def read_records():
    F1=open('Book.dat','rb')
    while True:
        try:
            D=pickle.load(F1)
            display_data(D)
        except EOFError:
            break
    F1.close()
def write_record():
    f=open('Book.dat','ab')
    pickle.dump(Data(),f)
    f.close()



Enter the price of the book in INR:300


Would you like to add more(Yes/No):No
1.Write records into the file
2.Read the content of the file
3.Appeand records
4.Search for books priced range 100 to 500
5.Modify the price of the book with book name as C++
6.Stop-Exit

Enter the choice:100
ERROR!
1.Write records into the file
2.Read the content of the file
3.Appeand records
4.Search for books priced range 100 to 500
5.Modify the price of the book with book name as C++
6.Stop-Exit

Enter the choice:4
Details are:
Book ID: B321789
Book name: The Fault in Our Stars
Author: John Green
def search():
    F=open('Book.dat','rb')
    flag=False
    while True:
        try:
            D=pickle.load(F)
            if D['Price'] in range(100,501):
                display_data(D)
                flag=True
        except EOFError:
            break
    if flag==False:
            print('Record not found')
            print()
    F.close()
    
def change():
    Book_name='C++'
    F=open('Book.dat','rb+')
    found=False
    try:
        while True:
            rpos=F.tell()
            D=pickle.load(F)
            if D['Book_name']==Book_name:
                Price=int(input("Enter the modified cost:"))
                D['Price']=Price

Price: 300
1.Write records into the file
2.Read the content of the file
3.Appeand records
4.Search for books priced range 100 to 500
5.Modify the price of the book with book name as C++
6.Stop-Exit

Enter the choice:2
Details are:
Book ID: B963147
Book name: Pride and Prejudice
Author: Jane Austen
Price: 750
Book ID: B321789
Book name: The Fault in Our Stars
Author: John Green
Price: 300
1.Write records into the file
2.Read the content of the file
3.Appeand records
4.Search for books priced range 100 to 500
5.Modify the price of the book with book name as C++
6.Stop-Exit

Enter the choice:Stop
                F.seek(rpos)
                pickle.dump(D,F)
                found=True
    except EOFError:
        if found==False:
            print("No record found")
        else:
            print("Record successfully modified!")
    F.close()
def show_choices():
    print('1.Write records into the file')
    print('2.Read the content of the file')
    print('3.Appeand records')
    print('4.Search for books priced range 100 to 500')
    print('5.Modify the price of the book with book name as C++')
    print('6.Stop-Exit')
    
while True:
    show_choices()
    choice=input("Enter the choice:")
    if choice=='1':
        write()  
    elif choice=='2':
        print("Details are:")
        read_records()
    elif choice=='3':
        write_record()
1.Write records into the file
2.Read the content of the file
3.Appeand records
4.Search for books priced range 100 to 500
5.Modify the price of the book with book name as C++
6.Stop-Exit

Enter the choice:3

Enter the book id:B5846213

Enter the name of the book:C++

Enter the name of the Author:Shak N

Enter the price of the book in INR:789

1.Write records into the file
2.Read the content of the file
3.Appeand records
4.Search for books priced range 100 to 500
5.Modify the price of the book with book name as C++
6.Stop-Exit




elif choice=='4':
        print("Details are:")
        search()
    elif choice=='5':
        change()
    elif choice=="Stop":
        break
    else:
        print("ERROR!")

        

















Enter the choice:5

Enter the modified cost:500
Record successfully modified!
1.Write records into the file
2.Read the content of the file
3.Appeand records
4.Search for books priced range 100 to 500
5.Modify the price of the book with book name as C++
6.Stop-Exit

Enter the choice:Stop














23rd June, 2021
14. Write a menu driven program to do the following:
a) To add product ID, product name, company name, dealer name, quantity and price into the file PRODUCT.CSV
b) To display the details of all the products
Program:
import csv
def write():
    F=open('PRODUCT.CSV','a',newline='\r\n')
    wobject=csv.writer(F)
    id=input("Enter the Product id:")
    P_name=input("Enter the Product's name:")
    C_name=input("Enter the Company name:")
    D_name=input("Enter the Dealer name:")
    Quan=input("Enter the Quantity:")
    Price=input("Enter the Price in USD:")
    P_details=[id,P_name,C_name,D_name,Quan,Price]
    wobject.writerow(P_details)
    F.close()  
def display():
    try:
        with open('PRODUCT.CSV','r',newline='\r\n') as fh:
            ereader=csv.reader(fh)
            print("File PRODUCT.CSV contains:")
            print("'Product ID','Product name','Company name','Dealer name','Quantity','Price'")
            for rec in ereader:
Output:
==========================
1.Add records
2.Display details
3.Exit
--------------------------

Enter the choice:1

Enter the Product id:P08596

Enter the Product's name:iPad Air

Enter the Company name:Apple

Enter the Dealer name:Shan K chan

Enter the Quantity:5

Enter the Price in USD:1000
==========================
1.Add records
2.Display details
3.Exit
--------------------------


                print(rec)
    except:
        print("No record found")
def show_choices():
    print("=" * 26)
    print("1.Add records")
    print("2.Display details")
    print("3.Exit")
    print("-" * 26)
while True:
    show_choices()
    choice=input("Enter the choice:")
    if choice=='1':
        write()
    elif choice=='2':
        display()
    elif choice=='3':
        print("Exiting the program")
        break
    else:
        print("Invalid Input!")






Enter the choice:2
File PRODUCT.CSV contains:
'Product ID','Product name','Company name','Dealer name','Quantity','Price'
['P08596', 'iPad Air', 'Apple', 'Shan K chan', '5', '1000']
==========================
1.Add records
2.Display details
3.Exit
--------------------------

Enter the choice:3
Exiting the program














30th June, 2021
15. Write a random number generator that generates random numbers between 1 and 6 (simulates a dice).
Program:
import random
def ran():
    s=random.randint(1,6)
    return s
print('The number is:',ran())
















Output:
The number is: 2

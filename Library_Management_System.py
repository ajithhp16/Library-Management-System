# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 14:31:04 2023

@author: Ajith
"""

"-------------------------- Library Management System -------------------------------"

import pymysql
import datetime

def userProfile(user_id):
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        cur.execute("Select name,father_name,gender,phone_number,original_address,present_address,books_count_allowed from users where id=(%s)",(user_id))
        res=cur.fetchone()
        name,father_name,gender,phone_number,original_address,present_address,books_count_allowed=res
        print("\nName:-",name,"\nFather Name:-",father_name,"\nGender:-",gender,"\nPhone Number:-",phone_number,"\nOriginal Address:-",original_address,"\nPresent Address:-",present_address,"\nBooks Count Allowed:-",books_count_allowed)
    except:
        myconn.rollback()
    myconn.close()

def checkLibrary():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        cur.execute("Select address,city,state,pincode from libraries")
        res=cur.fetchall()
        flag=1
        while(flag):
            inp=input("\n1. Show all Libraries.\n2. Show Libraries based on City.\n3. Show Libraries based on State.\n4. Show Libraries based on Pinconde.\n5. Exit.\n\nEnter Your Choice: ")
            if inp=='1':
                print("\n----------Adress----------City----------State----------Pincode----------")
                print("************************************************************************")
                for i in res:
                    print("\n")
                    for j in i:
                        print("----------",j,end='')
            elif inp=='2':
                city=input("Enter the CITY name you want to search for: ")
                print("\n----------Adress----------City----------State----------Pincode----------")
                print("************************************************************************")
                for i in res:
                    if i[1]==city:
                        print("\n")
                        for j in i:
                            print("----------",j,end='')
            elif inp=='3':
                state=input("Enter the STATE name you want to search for: ")
                print("\n----------Adress----------City----------State----------Pincode----------")
                print("************************************************************************")
                for i in res:
                    if i[2]==state:
                        print("\n")
                        for j in i:
                            print("----------",j,end='')
            elif inp=='4':
                pincode=input("Enter the PINCODE you want to search for: ")
                print("\n----------Adress----------City----------State----------Pincode----------")
                print("************************************************************************")
                for i in res:
                    if i[3]==pincode:
                        print("\n")
                        for j in i:
                            print("----------",j,end='')
            elif inp=='5':
                print("\nExiting from Library Search Page.!!!")
                flag=0 
            else:
                print("\nPlease re-enter the value given in the options only..!")
    except:
        myconn.rollback()
    myconn.close()

def booksAvailable():
    flag=1
    while(flag):
        inp=input("\n1. Search book based on name.\n2. Search book based on author.\n3. Search book based on Language.\n4. Exit.\n\nEnter Your Choice: ")
        if inp=='1':
            book_name=input("Enter the Book Name you wish to search for: ")
            myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
            cur=myconn.cursor()
            try:
                cur.execute("Select a.name,c.name,a.publication_date,d.name,b.count_available,concat(e.address,' , ',e.city,' , ',e.state,' - ',e.pincode) as Address from (Select id, name, author_id, language_id, publication_date from books WHERE lower(name)=lower((%s))) a join books_available b on a.id=b.book_id join authors c on a.author_id=c.id join languages d on a.language_id=d.id join libraries e on b.library_id=e.id",(book_name))
                res=cur.fetchall()
                print("\n----------Book Name----------Author Name----------Publication Date----------Language----------Book Count Available----------Library Address")
                print("*******************************************************************************************************************************************")
                for i in res:
                    print("\n")
                    for j in i:
                        print("----------",j,end='')
            except:
                myconn.rollback()
            myconn.close()
        elif inp=='2':
            author=input("Enter the Author you wish to search for: ")
            myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
            cur=myconn.cursor()
            try:
                cur.execute("Select b.name,a.name,b.publication_date,e.name,c.count_available,concat(d.address,' , ',d.city,' , ',d.state,' - ',d.pincode) as Address from (Select id, name from authors where lower(name)=lower((%s))) a join books b on a.id=b.author_id join books_available c on b.id=c.book_id join libraries d on c.library_id=d.id join languages e on b.language_id=e.id",(author))
                res=cur.fetchall()
                print("\n----------Book Name----------Author Name----------Publication Date----------Language----------Book Count Available----------Library Address")
                print("*******************************************************************************************************************************************")
                for i in res:
                    print("\n")
                    for j in i:
                        print("----------",j,end='')
            except:
                myconn.rollback()
            myconn.close()
        elif inp=='3':
            language=input("Enter the Language you wish to search for: ")
            myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
            cur=myconn.cursor()
            try:
                cur.execute("Select b.name,e.name,b.publication_date,a.name,c.count_available,concat(d.address,' , ',d.city,' , ',d.state,' - ',d.pincode) as Address from (Select id, name from languages where lower(name)=lower((%s))) a join books b on a.id=b.language_id join books_available c on b.id=c.book_id join libraries d on c.library_id=d.id join authors e on b.author_id=e.id",(language))
                res=cur.fetchall()
                print("\n----------Book Name----------Author Name----------Publication Date----------Language----------Book Count Available----------Library Address")
                print("*******************************************************************************************************************************************")
                for i in res:
                    print("\n")
                    for j in i:
                        print("----------",j,end='')
            except:
                myconn.rollback()
            myconn.close()
        elif inp=='4':
            print("\nExiting from Book Search Page.!!!")
            flag=0 
        else:
            print("\nPlease re-enter the value given in the options only..!")

def booksBorrowed(user_id):
    flag=1
    while(flag):
        inp=input("\n1. Show Books you've borrowed previously and returned.\n2. Show Books you've borrowed and to be returned.\n3. Exit.\n\nEnter Your Choice: ")
        if inp=='1':
            myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
            cur=myconn.cursor()
            try:
                cur.execute("Select b.name,c.name,a.issued_date,a.due_date,a.collected_date,a.fine_collected,a.status,concat(d.address,' , ',d.city,' , ',d.state,' - ',d.pincode) as Address from (Select issued_date,book_id,due_date,collected_date,fine_collected,library_id,status from books_borrowed where user_id=(%s) and status='Collected') a join books b on a.book_id=b.id join authors c on c.id=b.author_id join libraries d on a.library_id=d.id",(user_id))
                res=cur.fetchall()
                print("\n----------Book Name----------Author Name----------Issued Date----------Due Date----------Collected Date----------Fine Collected----------Status----------Library Address")
                print("************************************************************************************************************************************************************************")
                for i in res:
                    print("\n")
                    for j in i:
                        print("----------",j,end='')
            except:
                myconn.rollback()
            myconn.close()
        elif inp=='2':
            myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
            cur=myconn.cursor()
            try:
                cur.execute("Select b.name,c.name,a.issued_date,a.due_date,a.status,concat(d.address,' , ',d.city,' , ',d.state,' - ',d.pincode) as Address from (Select issued_date,book_id,due_date,collected_date,fine_collected,library_id,status from books_borrowed where user_id=(%s) and status='Pending') a join books b on a.book_id=b.id join authors c on c.id=b.author_id join libraries d on a.library_id=d.id",(user_id))
                res=cur.fetchall()
                print("\n----------Book Name----------Author Name----------Issued Date----------Due Date----------Status----------Library Address")
                print("************************************************************************************************************************")
                for i in res:
                    print("\n")
                    for j in i:
                        print("----------",j,end='')
            except:
                myconn.rollback()
            myconn.close()
        elif inp=='3':
            print("\nExiting from Book Search Page.!!!")
            flag=0 
        else:
            print("\nPlease re-enter the value given in the options only..!")

def userProfileUpdate(user_id):
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        flag=1
        while(flag):
            inp=input("\n1. Update Phone Number.\n2. Update Mail ID.\n3. Update Password.\n4. Update Address.\n5. Exit.\n\nEnter Your Choice: ")
            if inp=='1':
                phone_number=input("Enter Phone Number to be Updated: ")
                res=cur.execute("Update users set phone_number=(%s) where id=(%s)",(phone_number,user_id))
                if res==True:
                    print("Phone Number Updated Successfully.")
                else:
                    print("Unable to Update Phone Number. Please try again.")
            elif inp=='2':
                mail_id=input("Enter Mail ID to be Updated: ")
                res=cur.execute("Update users set mail_id=(%s) where id=(%s)",(mail_id,user_id))
                if res==True:
                    print("Mail ID Updated Successfully.")
                else:
                    print("Unable to Update Mail ID. Please try again.")
            elif inp=='3':
                user_password=input("Enter Password to be Updated: ")
                res=cur.execute("Update users set user_password=(%s) where id=(%s)",(user_password,user_id))
                if res==True:
                    print("Password Updated Successfully.")
                else:
                    print("Unable to Update Password. Please try again.")
            elif inp=='4':
                ch=input("\n1. Update Original Address only.\n2. Update Present Address only.\n3. Update both Original and Present Address.\n4. Exit\n\nEnter your Choice: ")
                if ch=='1':
                    original_address=input("Enter Original Address to be Updated: ")
                    res=cur.execute("Update users set original_address=(%s) where id=(%s)",(original_address,user_id))
                    if res==True:
                        print("Original Address Updated Successfully.")
                    else:
                        print("Unable to Update Original Address. Please try again.")
                elif ch=='2':
                    present_address=input("Enter Present Address to be Updated: ")
                    res=cur.execute("Update users set present_address=(%s) where id=(%s)",(present_address,user_id))
                    if res==True:
                        print("Present Address Updated Successfully.")
                    else:
                        print("Unable to Update Present Address. Please try again.")
                elif ch=='3':
                    address=input("Enter Address to be Updated: ")
                    res=cur.execute("Update users set original_address=(%s) and present_address=(%s) where id=(%s)",(address,address,user_id))
                    if res==True:
                        print("Address Updated Successfully.")
                    else:
                        print("Unable to Update Address. Please try again.")
                elif inp=='4':
                    break
            elif inp=='5':
                print("\nExiting from User Profile Update Page.!!!")
                flag=0
            else:
                print("\nPlease re-enter the value given in the options only..!")
    except:
        myconn.rollback()
    myconn.close()

def authorProfileUpdate():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        name=input("Enter Author Name whose details to be Updated: ")
        cur.execute("Select id from authors where name=(%s)",(name))
        res1=cur.fetchone()
        flag=1
        while(flag):
            inp=input("\n1. Update Phone Number.\n2. Update Address.\n3. Exit.\n\nEnter Your Choice: ")
            if inp=='1':
                phone_number=input("Enter Phone Number to be Updated: ")
                res=cur.execute("Update authors set phone_number=(%s) where id=(%s)",(phone_number,res1[0]))
                if res==True:
                    print("Phone Number Updated Successfully.")
                else:
                    print("Unable to Update Phone Number. Please try again.")
            elif inp=='2':
                address=input("Enter Address to be Updated: ")
                res=cur.execute("Update authors set address=(%s) where id=(%s)",(address,res1[0]))
                if res==True:
                    print("Address Updated Successfully.")
                else:
                    print("Unable to Update Address. Please try again.")
            elif inp=='3':
                print("\nExiting from Author Profile Update Page.!!!")
                flag=0
            else:
                print("\nPlease re-enter the value given in the options only..!")
    except:
        myconn.rollback()
    myconn.close()

def publisherProfileUpdate():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        name=input("Enter Publisher Name whose details to be Updated: ")
        cur.execute("Select id from publishers where name=(%s)",(name))
        res1=cur.fetchone()
        flag=1
        while(flag):
            inp=input("\n1. Update Phone Number.\n2. Update Address.\n3. Exit.\n\nEnter Your Choice: ")
            if inp=='1':
                phone_number=input("Enter Phone Number to be Updated: ")
                res=cur.execute("Update publishers set phone_number=(%s) where id=(%s)",(phone_number,res1[0]))
                if res==True:
                    print("Phone Number Updated Successfully.")
                else:
                    print("Unable to Update Phone Number. Please try again.")
            elif inp=='2':
                address=input("Enter Address to be Updated: ")
                res=cur.execute("Update publishers set address=(%s) where id=(%s)",(address,res1[0]))
                if res==True:
                    print("Address Updated Successfully.")
                else:
                    print("Unable to Update Address. Please try again.")
            elif inp=='3':
                print("\nExiting from Publisher Profile Update Page.!!!")
                flag=0
            else:
                print("\nPlease re-enter the value given in the options only..!")
    except:
        myconn.rollback()
    myconn.close()

def userLogin():
    print("\nWelcome to User Login.")
    username=input("Please enter USERNAME: ")
    pssword=input("Please enter PASSWORD: ")
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        cur.execute("Select id,name,phone_number,mail_id,user_password,is_active from users;")
        res=cur.fetchall()
        flag1=0
        for i in res:
            uid,uname,pno,mail_id,pwd,isActive=i
            if (mail_id==username or pno==username) and pwd==pssword and isActive=='No':
                print("\nHello",uname,". Your account is deactivated.\nPlease request the Librarian to activate your account.")
                flag1=1
                break
            elif (mail_id==username or pno==username) and pwd==pssword and isActive=='Yes':
                flag1=1
                print("Hello",uname,end='..!\n')
                flag2=1
                while(flag2):
                    inp1=input("1. Visit Your Profile.\n2. Check Libraries in your City.\n3. Check Books Available.\n4. Check Books You've Borrowed.\n5. Update User Profile.\n6. Exit\n\nEnter Your Choice: ")
                    if inp1=='1':
                        userProfile(uid)
                    elif inp1=='2':
                        checkLibrary()
                    elif inp1=='3':
                        booksAvailable()
                    elif inp1=='4':
                        booksBorrowed(uid)
                    elif inp1=='5':
                        userProfileUpdate(uid)
                    elif inp1=='6':
                        print("\nExiting from User Login Page.!!!")
                        flag2=0
                    else:
                        print("\nPlease re-enter the value given in the options only..!")
                break
        if flag1 != 1:
            print("\nPlease enter valid USERNAME and PASSWORD")
    except:
        myconn.rollback()
    myconn.close()

def librarianProfile(librarian_id):
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        cur.execute("Select name,gender,phone_number,original_address,present_address,is_root from librarians where id=(%s)",(librarian_id))
        res=cur.fetchone()
        name,gender,phone_number,original_address,present_address,is_root=res
        print("\nName:-",name,"\nGender:-",gender,"\nPhone Number:-",phone_number,"\nOriginal Address:-",original_address,"\nPresent Address:-",present_address,"\nIs Root:-",is_root)
    except:
        myconn.rollback()
    myconn.close()

def activateExistingLibrarian():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    lname,mail_id,phone_number=input("Enter Name, Mail_ID and Phone Number of the Librarian to be Activated(Comma Separated): ").split(',')
    try:
        root1=input("Would you like to PROVIDE Librarian Root Credentials (Yes/No): ")
        if root1=='No':
            res=cur.execute("update librarians set is_root='No',is_active='Yes' where name=(%s) and mail_id=(%s) and phone_number=(%s) and is_active='No'",(lname,mail_id,phone_number))
            if res==True:
                print("Librarian",lname,"Credential is Activated")
            else:
                print("Librarian Credential are invalid")
        elif root1=='Yes':
            res=cur.execute("update librarians set is_root='Yes',is_active='Yes' where name=(%s) and mail_id=(%s) and phone_number=(%s) and is_active='No'",(lname,mail_id,phone_number))
            if res==True:
                print("Librarian",lname,"Credential is Activated")
            else:
                print("Librarian Credential are invalid")
    except:
        myconn.rollback()
    myconn.close()  
    
def deactivateExistingLibrarian():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    lname,mail_id,phone_number=input("Enter Name, Mail_ID and Phone Number of the Librarian to be Deactivated(Comma Separated): ").split(',')
    try:
        root1=input("Would you like to REMOVE Librarian Root Credentials (Yes/No): ")
        if root1=='No':
            res=cur.execute("update librarians set is_active='No' where name=(%s) and mail_id=(%s) and phone_number=(%s) and is_active='Yes'",(lname,mail_id,phone_number))
            if res==True:
                print("Librarian",lname,"Credential is Deactivated")
            else:
                print("Librarian Credential are invalid")
        elif root1=='Yes':
            res=cur.execute("update librarians set is_root='No',is_active='No' where name=(%s) and mail_id=(%s) and phone_number=(%s) and is_active='Yes'",(lname,mail_id,phone_number))
            if res==True:
                print("Librarian",lname,"Credential is Deactivated")
            else:
                print("Librarian Credential are invalid")
    except:
        myconn.rollback()
    myconn.close()

def activateExistingUser():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    uname,mail_id,phone_number=input("Enter Name, Mail_ID and Phone Number of the User to be Activated(Comma Separated): ").split(',')
    try:
        res=cur.execute("update users set is_active='Yes',books_count_allowed=2 where name=(%s) and mail_id=(%s) and phone_number=(%s) and is_active='No'",(uname,mail_id,phone_number))
        if res==True:
            print("User",uname,"Credential is Activated")
        else:
            print("User Credential are invalid")
    except:
        myconn.rollback()
    myconn.close()

def deactivateExistingUser():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    uname,mail_id,phone_number=input("Enter Name, Mail_ID and Phone Number of the User to be Deactivated(Comma Separated): ").split(',')
    try:
        res=cur.execute("update users set is_active='No',books_count_allowed=0 where name=(%s) and mail_id=(%s) and phone_number=(%s) and is_active='Yes'",(uname,mail_id,phone_number))
        if res==True:
            print("User",uname,"Credential is Deactivated")
        else:
            print("User Credential are invalid")
    except:
        myconn.rollback()
    myconn.close()

def addNewLibrarian(library_id):
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    lname,gender,phone_number,mail_id,librarian_password,original_address,present_address=input("Enter Name,Gender,Phone Number,Mail ID,Librarian Password,Original Address,Present Address of New Librarian to be Added (Hash {#} Separated): ").split('#')
    try:
        cur.execute("Insert into Librarians (library_id,name,gender,phone_number,mail_id,librarian_password,original_address,present_address,is_root,is_active) values ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),'No','No')",(library_id,lname,gender,phone_number,mail_id,librarian_password,original_address,present_address))
        myconn.commit()
        if cur.rowcount>0:
            print("Librarian",lname,"Details are Added")
        else:
            print("Librarian Credentials were unable to add. Please try Again.!!!")
    except:
        myconn.rollback()
    myconn.close()

def addNewUser():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    name,father_name,gender,phone_number,mail_id,user_password,original_address,present_address=input("Enter Name,Father Name,Gender,Phone Number,Mail ID,User Password,Original Address,Present Address of New User to be Added (Hash {#} Separated): ").split('#')
    try:
        cur.execute("Insert into Users (name,father_name,gender,phone_number,mail_id,user_password,original_address,present_address,is_active,books_count_allowed) values ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),'No',0)",(name,father_name,gender,phone_number,mail_id,user_password,original_address,present_address))
        myconn.commit()
        if cur.rowcount>0:
            print("User",name,"Details are Added")
        else:
            print("User Credentials were unable to add. Please try Again.!!!")
    except:
        myconn.rollback()
    myconn.close()

def issueBook(librarian_id,library_id):
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        book_name,user_name=input("\nEnter the Book Name and User Name(Comma Separated): ").split(',')
        cur.execute("Select c.id,c.books_count_allowed,b.id,c.is_active from (Select id from books where name=(%s)) b join (Select id,books_count_allowed,is_active from users where name=(%s)) c on 1=1",(book_name,user_name))
        res=cur.fetchone()
        if len(res)>0:
            if res[3]=='Yes':
                cur.execute("Select id,count_available from books_available where book_id=(%s) and library_id=(%s)",(res[2],library_id))
                res1=cur.fetchone()
                if res1[1]>0:
                    if res[1]>0:
                        cur.execute("Insert into books_borrowed (book_id,user_id,library_id,issued_date,issued_librarian_id,due_date,fine_collected,status) values ((%s),(%s),(%s),(%s),(%s),(%s),0,'Pending')",(res[2],res[0],library_id,datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'),librarian_id,(datetime.datetime.today() + datetime.timedelta(days=15)).strftime('%Y-%m-%d %H:%M:%S')))
                        myconn.commit()
                        if cur.rowcount>0:
                            print("\nBook: ",book_name,"Successfully issued to User: ",user_name)
                            res2=cur.execute("Update users set books_count_allowed=(%s) where id=(%s)",(res[1]-1,res[0]))
                            if res2==True:
                                res3=cur.execute("Update books_available set count_available=(%s) where id=(%s)",(res1[1]-1,res1[0]))
                                if res3==True:
                                    print("\nBook",book_name,"Available Count has been updated to",res1[1]-1)
                                else:
                                    print("\nUnable to Update Availability Count")
                            else:
                                print("\nPresent Book Count Allowed for User: ",user_name,"is 0")
                        else:
                            print("Books Issed Details were unable to add. Please try Again.!!!")
                    else:
                        print("\nBook Count of User: ",user_name,"is 0. Please return any of the books issued and collect new one.")
                else:
                    print("\nBook",book_name,"Not Available in Library.")
            else:
                print("\nUser",user_name,"status is NOT ACTIVE. Please update status to ACTIVE and try Again.")
        else:
            print("\nEither User",user_name,"or Book",book_name,"is unavailable. Please enter proper details.")
    except:
        myconn.rollback()
    myconn.close()

def collectBook(librarian_id,library_id):
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        book_name,user_name=input("\nEnter the Book Name and User Name(Comma Separated): ").split(',')
        cur.execute("Select a.id,a.due_date,c.id,c.books_count_allowed,d.id,d.count_available from (Select id,book_id,user_id,due_date from books_borrowed where library_id=(%s) and status='Pending') a join (Select id from books where name=(%s)) b on a.book_id=b.id join (Select id,books_count_allowed from users where name=(%s)) c on a.user_id=c.id join books_available d on d.book_id=a.book_id",(library_id,book_name,user_name))
        res=cur.fetchall()
        if len(res)>0:
            datediff=(res[0][1] - (datetime.datetime.today())).days
            fine=0
            if datediff<0:
                fine=datediff * -5
                res1=cur.execute("Update books_borrowed set fine_collected=(%s),collected_librarian_id=(%s),collected_date=(%s),status='Collected' where id=(%s)",(fine,librarian_id,datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),res[0][0]))
                if res1==True:
                    print("\nBook Status updated to 'Collected' with Fine Issued=",fine,"for User: ",user_name,"and Book: ",book_name)
                    res2=cur.execute("Update users set books_count_allowed=(%s) where id=(%s)",(res[0][3]+1,res[0][2]))
                    if res2==True:
                        print("\nUser",user_name,"Books Count Allowed increased to",res[0][3]+1)
                        res3=cur.execute("Update books_available set count_available=(%s) where id=(%s)",(res[0][5]+1,res[0][4]))
                        if res3==True:
                            print("\nBook",book_name,"Available Count has been updated to",res[0][5]+1)
                        else:
                            print("\nUnable to Update Availability Count")
                    else:
                        print("\nUnable to update user",user_name,"Books Count Allowed value. Please try again.")
                else:
                    print("\nUnable to update book collected status. Please try again.")
            else:
                res1=cur.execute("Update books_borrowed set collected_librarian_id=(%s),collected_date=(%s),status='Collected' where id=(%s)",(librarian_id,datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),res[0][0]))
                if res1==True:
                    print("\nBook Status updated to 'Collected' with Fine Issued=",fine,"for User: ",user_name,"and Book: ",book_name)
                    res2=cur.execute("Update users set books_count_allowed=(%s) where id=(%s)",(res[0][3]+1,res[0][2]))
                    if res2==True:
                        print("\nUser",user_name,"Books Count Allowed increased to",res[0][3]+1)
                        res3=cur.execute("Update books_available set count_available=(%s) where id=(%s)",(res[0][5]+1,res[0][4]))
                        if res3==True:
                            print("\nBook",book_name,"Available Count has been updated to",res[0][5]+1)
                        else:
                            print("\nUnable to Update Availability Count")
                    else:
                        print("\nUnable to update user",user_name,"Books Count Allowed value. Please try again.")
                else:
                    print("\nUnable to update book collected status. Please try again.")
        else:
            print("\nUser hasn't borrowed the entered book.")
    except:
        myconn.rollback()
    myconn.close()

def addAuthor():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        author_name,address,phone_number=input("\nEnter Name, Address and Phone Number of author to be added (Hash [#] Separated): ").split('#')
        cur.execute("Select id from authors where name=(%s) and address=(%s) and phone_number=(%s)",(author_name,address,phone_number))
        res=cur.fetchall()
        if len(res)>0:
            print("Author Details already Exists.")
        else:
            cur.execute("Insert into authors (name,address,phone_number) values ((%s),(%s),(%s))",(author_name,address,phone_number))
            myconn.commit()
            if cur.rowcount>0:
                print("Author",author_name,"Details are Added")
            else:
                print("Author details were unable to add. Please try Again.!!!")
    except:
        myconn.rollback()
    myconn.close()

def addPublisher():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        publisher_name,address,phone_number=input("\nEnter Name, Address and Phone Number of publisher to be added (Hash [#] Separated): ").split('#')
        cur.execute("Select id from publishers where name=(%s) and address=(%s) and phone_number=(%s)",(publisher_name,address,phone_number))
        res=cur.fetchall()
        if len(res)>0:
            print("Publisher Details already Exists.")
        else:
            cur.execute("Insert into publishers (name,address,phone_number) values ((%s),(%s),(%s))",(publisher_name,address,phone_number))
            myconn.commit()
            if cur.rowcount>0:
                print("Publisher",publisher_name,"Details are Added")
            else:
                print("Publisher details were unable to add. Please try Again.!!!")
    except:
        myconn.rollback()
    myconn.close()

def addLanguage():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        language=input("\nEnter Language Name to be added: ")
        cur.execute("Select id from languages where name=(%s)",(language))
        res=cur.fetchall()
        if len(res)>0:
            print("\nLanguage already Exists.")
        else:
            cur.execute("Insert into languages (name) values ((%s))",(language))
            myconn.commit()
            if cur.rowcount>0:
                print("Language",language,"is Added")
            else:
                print("Language was unable to add. Please try Again.!!!")
    except:
        myconn.rollback()
    myconn.close()

def addNewBook():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        author_name=input("Enter the Author Name: ")
        cur.execute("Select id from authors where name=(%s)",(author_name))
        res=cur.fetchall()
        if len(res)==0:
            print("\nEntered author details doesn't exist. Please add in new author details and continue.")
        else:
            author_id=res[0][0]
            publisher_name=input("Enter the Publisher Name: ")
            cur.execute("Select id from publishers where name=(%s)",(publisher_name))
            res1=cur.fetchall()
            if len(res1)==0:
                print("\nEntered publisher details doesn't exist. Please add in new publisher details and continue.")
            else:
                publisher_id=res1[0][0]
                language=input("Enter Language of Book: ")
                cur.execute("Select id from languages where name=(%s)",(language))
                res2=cur.fetchall()
                if len(res2)==0:
                    print("Entered Language doesn't exist. Please add in new language details.")
                else:
                    language_id=res2[0][0]
                    book_name,price,publication_date,edition,section=input("\nEnter Name, Price, Publication Date, Edition and Section of Book to be added (Hash [#] Separated): ").split('#')
                    cur.execute("Select id from books where name=(%s) and edition=(%s) and section=(%s)",(book_name,edition,section))
                    res3=cur.fetchall()
                    if len(res3)>0:
                        print("\nBook",book_name,"Details Already Exists.")
                    else:
                        cur.execute("Insert into books (name,author_id,publisher_id,price,publication_date,language_id,edition,section) values ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))",(book_name,author_id,publisher_id,price,publication_date,language_id,edition,section))
                        myconn.commit()
                        if cur.rowcount>0:
                            print("Book",language,"details are Added")
                        else:
                            print("Book details was unable to add. Please try Again.!!!")
    except:
        myconn.rollback()
    myconn.close()

def removeBookAvailability():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        book_name,library_address,library_city=input("Enter Book Name and (Library Address, City) whose availability to be reduced (Comma Separated): ").split(',')
        cur.execute("Select a.id,a.count_available from books_available a join (Select id from books where name=(%s)) b on a.book_id=b.id join (Select id from libraries where address=(%s) and city=(%s)) c on a.library_id=c.id",(book_name,library_address,library_city))
        res=cur.fetchone()
        print("\nFor book=",book_name,"in library",library_address,",",library_city,"Count Available is: ",res[1])
        inp=input("\nEnter Final Book Count Availability you wish to change: ")
        res1=cur.execute("update books_available set count_available=(%s) where id=(%s)",(inp,res[0]))
        if res1==True:
            print("\nAvailability Count successfully Updated")
        else:
            print("\nUnable to update Availability Count. Please try again.!!!")
    except:
        myconn.rollback()
    myconn.close()

def addEBook():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        cur.execute("Select name from books a join ebooks b on a.id=b.book_id")
        res=cur.fetchall()
        bookname=input("\nEnter the Book Name whose Extension to be added: ")
        flag=1
        for i in res:
            if bookname==i[0]:
                flag=0
            else:
                continue
        if flag!=0:    
            extension=input("\nEnter the extension: ")
            cur.execute("select id from books where name=(%s)",(bookname))
            res1=cur.fetchone()
            cur.execute("Insert into ebooks (book_id,extension) values((%s),(%s))",(res1[0],extension))
            myconn.commit()
            if cur.rowcount>0:
                print("\nExtension successfully created.")  
            else:
                print("\nExtension was unable to be created. Please try Again.")
        else:
            print("\nExtension already exists for the book you've Entered.")
    except:
        myconn.rollback()
    myconn.close()   

def addNewLibrary():
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        address,city,state,pincode=input("Enter Address, City, State and Pincode of Library to be added (Hash {#} Separated): ").split('#')
        cur.execute("Insert into libraries (address,city,state,pincode) values ((%s),(%s),(%s),(%s))",(address,city,state,pincode))
        myconn.commit()
        if cur.rowcount>0:
            print("\nNew Library Successfully Added.")  
        else:
            print("\nNew Library was unable to be added. Please try Again.")
    except:
        myconn.rollback()
    myconn.close()          

def librarianProfileUpdate(librarian_id):
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        flag=1
        while(flag):
            inp=input("\n1. Update Phone Number.\n2. Update Mail ID.\n3. Update Password.\n4. Update Address.\n5. Exit.\n\nEnter Your Choice: ")
            if inp=='1':
                phone_number=input("Enter Phone Number to be Updated: ")
                res=cur.execute("Update librarians set phone_number=(%s) where id=(%s)",(phone_number,librarian_id))
                if res==True:
                    print("Phone Number Updated Successfully.")
                else:
                    print("Unable to Update Phone Number. Please try again.")
            elif inp=='2':
                mail_id=input("Enter Mail ID to be Updated: ")
                res=cur.execute("Update librarians set mail_id=(%s) where id=(%s)",(mail_id,librarian_id))
                if res==True:
                    print("Mail ID Updated Successfully.")
                else:
                    print("Unable to Update Mail ID. Please try again.")
            elif inp=='3':
                user_password=input("Enter Password to be Updated: ")
                res=cur.execute("Update librarians set user_password=(%s) where id=(%s)",(user_password,librarian_id))
                if res==True:
                    print("Password Updated Successfully.")
                else:
                    print("Unable to Update Password. Please try again.")
            elif inp=='4':
                ch=input("\n1. Update Original Address only.\n2. Update Present Address only.\n3. Update both Original and Present Address.\n\nEnter your Choice: ")
                if ch=='1':
                    original_address=input("Enter Original Address to be Updated: ")
                    res=cur.execute("Update librarians set original_address=(%s) where id=(%s)",(original_address,librarian_id))
                    if res==True:
                        print("Original Address Updated Successfully.")
                    else:
                        print("Unable to Update Original Address. Please try again.")
                elif ch=='2':
                    present_address=input("Enter Present Address to be Updated: ")
                    res=cur.execute("Update librarians set present_address=(%s) where id=(%s)",(present_address,librarian_id))
                    if res==True:
                        print("Present Address Updated Successfully.")
                    else:
                        print("Unable to Update Present Address. Please try again.")
                elif ch=='3':
                    address=input("Enter Address to be Updated: ")
                    res=cur.execute("Update librarians set original_address=(%s) and present_address=(%s) where id=(%s)",(address,address,librarian_id))
                    if res==True:
                        print("Address Updated Successfully.")
                    else:
                        print("Unable to Update Address. Please try again.")
            elif inp=='5':
                print("\nExiting from Librarian Profile Update Page.!!!")
                flag=0
            else:
                print("\nPlease re-enter the value given in the options only..!")
    except:
        myconn.rollback()
    myconn.close()

def profileUpdate():
    inp=input("\n1. Update User Profile.\n2. Update Librarian Profile.\n\nEnter Your Choice: ")
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        if inp=='1':
            name=input("Enter User Name whose Profile To Be Updated: ")
            cur.execute("Select id from users where name=(%s)",(name))
            res=cur.fetchone()
            if len(res)>0:
                userProfileUpdate(res[0])
            else:
                print("No User exists with Name: ",name)
        elif inp=='2':
            name=input("Enter Librarian Name whose Profile To Be Updated: ")
            cur.execute("Select id from librarians where name=(%s)",(name))
            res=cur.fetchone()
            if len(res)>0:
                librarianProfileUpdate(res[0])
            else:
                print("No Librarian exists with Name: ",name)
    except:
        myconn.rollback()
    myconn.close()    

def librarianLogin():
    print("\nWelcome to Librarian Login.")
    username=input("Please enter USERNAME: ")
    pssword=input("Please enter PASSWORD: ")
    myconn=pymysql.connect(host='localhost',user='root',password='',database='library_management_system')
    cur=myconn.cursor()
    try:
        cur.execute("Select id,name,phone_number,mail_id,librarian_password,is_active,is_Root,library_id from librarians;")
        res=cur.fetchall()
        flag1=0
        for i in res:
            lid,lname,pno,mail_id,pwd,isActive,isRoot,library_id=i
            if (mail_id==username or pno==username) and pwd==pssword and isActive=='No':
                print("\nHello",lname,". Your account is deactivated.\nPlease request the Head-Of-Library to activate your account.")
                flag1=1
                break
            elif (mail_id==username or pno==username) and pwd==pssword and isActive=='Yes' and isRoot=='Yes':
                flag1=1
                print("Hello",lname,end='..!\n')
                flag2=1
                while(flag2):
                    inp1=input("1. Visit Your Profile.\n2. Activate Existing Librarian Credentials.\n3. Dectivate Existing Librarian Credentials.\n4. Activate Existing User Credentials.\n5. Dectivate Existing User Credentials.\n6. Add New Librarian.\n7. Add New User.\n8. Add New Author.\n9. Add New Publisher.\n10. Issue Book to User.\n11. Collect Book from User.\n12. Add New Book.\n13. Remove Book due to Damage or Lost.\n14. Add eBook.\n15. Add New Library.\n16. Add New Language.\n17. Update Profile (User or Librarian).\n18. Author Profile Update.\n19. Publisher Profile Update.\n20. Exit\n\nEnter Your Choice: ")
                    if inp1=='1':
                        librarianProfile(lid)
                    elif inp1=='2':
                        activateExistingLibrarian()
                    elif inp1=='3':
                        deactivateExistingLibrarian()
                    elif inp1=='4':
                        activateExistingUser()
                    elif inp1=='5':
                        deactivateExistingUser()
                    elif inp1=='6':
                        addNewLibrarian(library_id)
                    elif inp1=='7':
                        addNewUser()
                    elif inp1=='8':
                        addAuthor()
                    elif inp1=='9':
                        addPublisher()
                    elif inp1=='10':
                        issueBook(lid,library_id)
                    elif inp1=='11':
                        collectBook(lid,library_id)
                    elif inp1=='12':
                        addNewBook()
                    elif inp1=='13':
                        removeBookAvailability()
                    elif inp1=='14':
                        addEBook()
                    elif inp1=='15':
                        addNewLibrary()
                    elif inp1=='16':
                        addLanguage()
                    elif inp1=='17':
                        profileUpdate()
                    elif inp1=='18':
                        authorProfileUpdate()
                    elif inp1=='19':
                        publisherProfileUpdate()
                    elif inp1=='20':
                        print("\nExiting from Librarian Login Page.!!!")
                        flag2=0
                    else:
                        print("\nPlease re-enter the value given in the options only..!")
                break
            elif (mail_id==username or pno==username) and pwd==pssword and isActive=='Yes' and isRoot=='No':
                flag1=1
                print("Hello",lname,end='..!\n')
                flag2=1
                while(flag2):
                    inp1=input("1. Visit Your Profile.\n2. Activate Existing User Credentials.\n3. Deactivate Existing User Credentials.\n4. Add New User.\n5. Add New Author.\n6. Add New Publisher.\n7. Issue Book to User.\n8. Collect Book from User.\n9. Add New Book.\n10. Remove Book due to Damage or Lost.\n11. Add eBook.\n12. Add New Language.\n13. Update Librarian Profile.\n14. Author Profile Update.\n15. Publisher Profile Update.\n16. Exit\n\nEnter Your Choice: ")
                    if inp1=='1':
                        librarianProfile(lid)
                    elif inp1=='2':
                        activateExistingUser()
                    elif inp1=='3':
                        deactivateExistingUser()
                    elif inp1=='4':
                        addNewUser()
                    elif inp1=='5':
                        addAuthor()
                    elif inp1=='6':
                        addPublisher()
                    elif inp1=='7':
                        issueBook(lid,library_id)
                    elif inp1=='8':
                        collectBook(lid,library_id)
                    elif inp1=='9':
                        addNewBook()
                    elif inp1=='10':
                        removeBookAvailability()
                    elif inp1=='11':
                        addEBook()
                    elif inp1=='12':
                        addLanguage()
                    elif inp1=='13':
                        librarianProfileUpdate(lid)
                    elif inp1=='14':
                        authorProfileUpdate()
                    elif inp1=='15':
                        publisherProfileUpdate()
                    elif inp1=='16':
                        print("\nExiting from Librarian Login Page.!!!")
                        flag2=0
                    else:
                        print("\nPlease re-enter the value given in the options only..!")
                break
        if flag1 != 1:
            print("\nPlease enter valid USERNAME and PASSWORD")
    except:
        myconn.rollback()
    myconn.close()

flag=1
while(flag):
    print("\n*------------- Welcome to Library Management System -------------------*")
    inp=input("1. User Login..!\n2. Librarian Login..!\n3. Exit\n\nEnter required choice: ")
    if inp=='1':
        userLogin()
    elif inp=='2':
        librarianLogin()
    elif inp=='3':
        print("\nThanks for visiting the System. Please do come again..!")
        flag=0
    else:
        print("\nPlease re-enter the value given in the options only..!")
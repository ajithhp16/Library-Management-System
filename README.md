# Library-Management-System

This Project is developed using Python programming language and MySQL database.

Library-Management-System Repository has two files.
  1. library_management_system.py
  2. library_management_system.sql
  
Below is the flow provided in Library Management System (library_management_system.py):

1. Welcome page consists of two Login entries, User and Librarian.
2. User or Librarian need to enter Username and Password to login successfully.
    Username can be either be Phone_Number or Mail_ID.
# User Options:
    a. Visit User Profile.
    b. Check Libraries based on either City, State or Pincode.
    c. Check Books Available based on Book_Name, Author or Language.
    d. Check Books borrowed previously returned or currently borrowed.
    e. Update USer Profile i.e., Phone_Number, Mail_ID, Password and Address.

# Librarian Options:
    Librarian can be either Root User or Non-Root User.
    1. Librarian with Root User Credentials ->
        a. Visit Librarian Profile.
        b. Activate Credentials of Existing Librarian Credentials.
        c. Deactivate Credentials of Existing Librarian Credentials.
        d. Activate Credentials of Existing User Credentials.
        e. Deactivate Credentials of Existing User Credentials.
        f. Add New User.
        g. Add New Author.
        h. Add New Publisher.
        i. Issue Book to User.
        j. Collect Book from User.
        k. Add New Book.
        l. Remove Book due to Damage or Lost.
        m. Add eBook extension.
        n. Add New Library.
        o. Add New Language.
        p. Update Profile of either User or Librarian.
        q. Author Profile Update.
        r. Publisher Profile Update.
    2. Librarian without Root User Credentials ->
        a. Visit Librarian Profile.
        d. Activate Credentials of Existing User Credentials.
        e. Deactivate Credentials of Existing User Credentials.
        f. Add New User.
        g. Add New Author.
        h. Add New Publisher.
        i. Issue Book to User.
        j. Collect Book from User.
        k. Add New Book.
        l. Remove Book due to Damage or Lost.
        m. Add eBook extension.
        o. Add New Language.
        p. Update Profile of Librarian.
        q. Author Profile Update.
        r. Publisher Profile Update.
        
Below are the tables created in Library Management System (library_management_system.sql):

1. Authors
2. Books
3. Books_Available
4. Books_Borrowed
5. eBooks
6. Languages
7. Librarians
8. Libraries
9. Publishers
10. Users

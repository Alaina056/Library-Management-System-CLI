#Empty text files are also attached in Google classroom where the respective data is going to store.
#MAKING NECESSARY FUNCTIONS# Python program for implementation of MergeSort
def mergeSort(arr):
        if len(arr) > 1:
                mid = len(arr)//2
                L = arr[:mid]
                R = arr[mid:]
                mergeSort(L)
                mergeSort(R)
                i = j = k = 0
                while i < len(L) and j < len(R):
                        if L[i] < R[j]:
                                arr[k] = L[i]
                                i += 1
                        else:
                                arr[k] = R[j]
                                j += 1
                        k += 1
                while i < len(L):
                        arr[k] = L[i]
                        i += 1
                        k += 1
                while j < len(R):
                        arr[k] = R[j]
                        j += 1
                        k += 1
        return arr

def arr_id():        #MERGE SORT ALGORITHM IMPLEMENTATION
        file = open("Book_data.txt", "r")
        lines = file.readlines()
        list_of_lists = [(line.strip()).split(',') for line in lines]       #2D list
        file.close()
        lst=[]
        for i in list_of_lists:
                lst.append(i[1])
        arr=mergeSort(lst)
        #return arr
        
def save_records(rec,file):
        f=open(file,"a")
        f.write(str(rec))
        f.close()
def register_member():
    records=''
    while True:
        ID=input("Enter ID: ")
        name=input("Enter the Member name:  ")
        address=input("Enter address:  ")
        email=input("What is the your email_address:  ")
        pswd=input("Enter password:  ")
        records+=ID+", "
        records+=name+" , "                                         # storing data into the empty string 
        records+=address+" , "
        records+=email+" , "
        records+=pswd+"\n"                                                 #\n is used to enter other data on next line
        ch=input("Enter 'c' or 'C' to continue or Enter 'e' or 'E' to exit.....    ")
        if ch=='e' or ch=='E':
            save=input("Do you want to save your record?  (yes/no)   ")             
            if save=='yes' or save=="Yes": 
                save_records(records,"Member.txt")                                                   #saving data into file (function is described above)
                print("Data saved successfully!!!!")
            break
        elif ch=="c" or ch=="C":
                continue                                                                                            
        else:
                print("Error!!!!!")
def cancel_membership():
    name=input("Enter Member ID whose membership is to be cancelled: ")
    file = open("Member.txt", "r")
    lines = file.readlines()
    list_of_lists = [(line.strip()).split(',') for line in lines]       #2D list
    file.close()
    lst=[]
    for i in list_of_lists:
        if i[0] !=name:
            lst.append(i)
    new_file=open("Member.txt","w")
    for item in lst:
        new_file.write(item[0]+","+item[1]+","+item[2]+","+item[3]+","+item[4])
    new_file.close()
    print(f"Member ship of ID no. {name} has been cancelled!!!")

def Add_book(bookId,bookName,author,sub,date,status):
    book_details=''
    book_details+=bookId+","
    book_details+=bookName+","
    book_details+=author+","
    book_details+=sub+","
    book_details+=date+","
    book_details+=status+"\n"

    file=open("Book_data.txt","a")
    file.write(str(book_details))
    file.close()

def delete_book(bookid):
    file = open("Book_data.txt", "r")
    lines = file.readlines()
    list_of_lists = [(line.strip()).split(',') for line in lines]       #2D list
    file.close()
    lst=[]
    for i in list_of_lists:
        if i[0] !=bookid:
            lst.append(i)
    new_file=open("Book_data.txt","w")
    for item in lst:
            new_file.write(item[0]+","+item[1]+","+item[2]+","+item[3]+","+item[4]+","+item[5]+"\n")
    new_file.close()

    
def modify_book(bookid,bookName,author,sub,date,status):
    file = open("Book_data.txt", "r")
    lines = file.readlines()
    list_of_lists = [(line.strip()).split(',') for line in lines]       #2D list
    file.close()
    lst=[]
    for i in list_of_lists:
        if i[0] !=bookid:
            lst.append(i)
    new_file=open("Book_data.txt","w")
    for item in lst:
            new_file.write(item[0]+","+item[1]+","+item[2]+","+item[3]+","+item[4]+","+item[5]+"\n")
    new_file.close()
    Add_book(bookid,bookName,author,sub,date,status)
def display_book(lst):
        print(f"BOOK ID: {lst[0]}")
        print(f"BOOK NAME: {lst[1]}")
        print(f"BOOK AUTHOR: {lst[2]}")
        print(f"SUBJECT: {lst[3]}")
        print(f"PUBLICATION DATE: {lst[4]}")
        print(f"STATUS: {lst[5]}")
def display_bookcollection():
        file = open("Book_data.txt", "r")
        lines = file.readlines()
        list_of_lists = [(line.strip()).split(',') for line in lines]       #2D list
        file.close()
        for lst in list_of_lists:
                print(f"BOOK ID: {lst[0]}")
                print(f"BOOK NAME: {lst[1]}")
                print(f"BOOK AUTHOR: {lst[2]}")
                print(f"SUBJECT: {lst[3]}")
                print(f"PUBLICATION DATE: {lst[4]}")
                print(f"STATUS: {lst[5]}")
                print()
        
    
def search():
        field=print("By Which field you want to search: \n1. Book id\n2. Book Name\n3. Author\n4. Subject\n5. Publication date\n") 
        ch=int(input("Enter: "))
        book=input("Write book id/name/author/subject/Publication date: ")
        file = open("Book_data.txt", "r")
        lines = file.readlines()
        list_of_lists = [(line.strip()).split(',') for line in lines]       #2D list
        file.close()
        lst=[]
        for item in list_of_lists:
                if item[0]==book:
                        display_book(item)
                elif item[1]==book:
                        display_book(item)
                elif item[2]==book:
                        display_book(item)
                elif item[3]==book:
                        display_book(item)
                elif item[4]==book:
                        display_book(item)
                else:
                        print("Enter valid information")
def Reserved_book():
        res_bookdetails=''
        bookname=input("Enter book name which you want to reserved: ")
        file = open("Book_data.txt", "r")
        lines = file.readlines()
        list_of_lists = [(line.strip()).split(',') for line in lines]       #2D list
        file.close()
        for item in list_of_lists:
                if item[1]==bookname:
                        if item[5]=="Not Available":
                                print("Book is reserved for the requested member!!!!")
                                item[5]="Reserved"
                                delete_book(item[0])
                                modify_book(item[0],item[1],item[2],item[3],item[4],item[5])
                                res_bookdetails+=item[0]+','
                                res_bookdetails+=item[1]+','
                                res_bookdetails+=item[2]+','
                                res_bookdetails+=item[3]+','
                                res_bookdetails+=item[4]+','
                                res_bookdetails+=item[5]+'\n'
                                save_records(res_bookdetails,"Reserved_book.txt")
                                
                                
                        elif item[5]=="Available":
                                print("The book is already available!!!")
                                chk=input("Do you want to check_out this book? (yes/no): ")
                                if chk=="Yes" or chk=="yes":
                                        checkout()
                        elif item[5]=="Reserved":
                                print("Book is already reserved!!!")
                        else:
                                print("Enter Valid information")
        
def checkout():
        borr_bookdetails=''
        bookname=input("Enter book name which you want to borrow: ")
        file = open("Book_data.txt", "r")
        lines = file.readlines()
        list_of_lists = [(line.strip()).split(',') for line in lines]       #2D list
        file.close()
        for item in list_of_lists:
                if item[1]==bookname:
                        if item[5]=="Available":
                                print("Book is borrowed to the requested member!!!!")
                                item[5]="Not Available"
                                delete_book(item[0])
                                modify_book(item[0],item[1],item[2],item[3],item[4],item[5])
                                issue_date=input("Enter Issue Date: ")
                                due_date=input("Enter Due Date: ")
                                noOfDays=input("Enter number of days the book can be borrowed: ")
                                borr_bookdetails+=item[0]+','
                                borr_bookdetails+=item[1]+','
                                borr_bookdetails+=item[2]+','
                                borr_bookdetails+=item[3]+','
                                borr_bookdetails+=item[4]+','
                                borr_bookdetails+=item[5]+','
                                borr_bookdetails+=issue_date+","
                                borr_bookdetails+=noOfDays+"\n"
                                save_records(borr_bookdetails,"Borrowed_book.txt")
                        elif item[5]=="Not Available":
                                print("The book is currently not available")
                                reserv=input("Do you want to reserve this book? (yes/no): ")
                                if reserv=="Yes" or reserv=="yes":
                                        Reserved_book()
                        elif item[5]=="Reserved":
                                print("Book is already reserved!!!")
                        else:
                                print("Enter Valid information")
def renew_book():
        borr_bookdetails=''
        bookId=input("Enter book ID: ")
        file=open("Borrowed_Book.txt")
        lines=file.readlines()
        list_of_lists = [(line.strip()).split(',') for line in lines]       #2D list
        file.close()
        lst=[]
        for i in list_of_lists:
                if i[0] !=bookId:
                        lst.append(i)
        new_file=open("Borrowed_Book.txt","w")
        for item in lst:
                new_file.write(item[0]+","+item[1]+","+item[2]+","+item[3]+","+item[4]+","+item[5]+","+item[6]+","+item[7]+"\n")
        new_file.close()

        for item in list_of_lists:
                if item[0]==bookId:
                        item[7]=input("Enter number of days for the book is renewed: ")
                        borr_bookdetails+=item[0]+','
                        borr_bookdetails+=item[1]+','
                        borr_bookdetails+=item[2]+','
                        borr_bookdetails+=item[3]+','
                        borr_bookdetails+=item[4]+','
                        borr_bookdetails+=item[5]+','
                        borr_bookdetails+=item[6]+","
                        borr_bookdetails+=item[7]+"\n"
                        save_records(borr_bookdetails,"Borrowed_Book.txt")
                print(f"Book is renewed to further {item[7]} days")
        
def return_book():
        return_bookdetails=''
        bookId=input("Enter book id which you want to returned: ")
        file = open("Book_data.txt", "r")
        lines = file.readlines()
        list_of_lists = [(line.strip()).split(',') for line in lines]       #2D list
        file.close()
        for item in list_of_lists:
                if item[0]==bookId:
                        if item[5]=="Not Available":
                                print("Book is successfully returned to the library!!!!")
                                item[5]="Available"
                                delete_book(item[0])
                                modify_book(item[0],item[1],item[2],item[3],item[4],item[5])
                                return_bookdetails+=item[0]+','
                                return_bookdetails+=item[1]+','
                                return_bookdetails+=item[2]+','
                                return_bookdetails+=item[3]+','
                                return_bookdetails+=item[4]+','
                                return_bookdetails+=item[5]+'\n'
                                save_records(return_bookdetails,"Returned_book.txt")
                                
                                
                        elif item[5]=="Available":
                                print("The book is already returned!!!")
                                chk=input("Do you want to check_out this book? (yes/no): ")
                                if chk=="Yes" or chk=="yes":
                                        checkout()
                        elif item[5]=="Reserved":
                                print("Book is already reserved!!!")
                        else:
                                print("Enter Valid information")
        

#MAIN PROGRAM
        
print("MENU")
print("""
\t 1. Add Book
\t 2. Remove Book
\t 3. Modify or Edit Book
\t 4. search
\t.5. Register Member
\t 6. Cancel Membership
\t 7. Check_Out Book
\t 8. Reserve book
\t 9. Renew book
\t 10. Return book
\t 11. Display all books in sorted order
\t 12. Display whole collection of book
\t 13. Exit""")
ch=int(input("Enter your Choice: "))
while True:
        if ch==1:
                bookId=input("Enter Book ID: ")
                bookName=input("Enter Book Name: ")
                author=input("Enter Author name: ")
                sub=input("Enter Subject: ")
                date=input("Enter Publication date (as date/month/year) :")
                status=input("Enter Status (reserved ,available,not avalable) :")
                Add_book(bookId,bookName,author,sub,date,status)
                x=input("Press y or Y to continue adding books: ")
                if x=="y" or x=="Y":
                        continue
                else:
                        break
        elif ch==2:
                bookid=input("Enter Book ID which is to be deleted: ")
                delete_book(bookid)
                x=input("Press y or Y to continue deleting books: ")
                if x=='y' or x=="Y":
                        continue
                else:
                        break
        elif ch==3:
                bookid=input("Enter book id which is to by modify: ")
                bookName=input("Enter Book Name: ")
                author=input("Enter Author name: ")
                sub=input("Enter Subject: ")
                date=input("Enter Publication date (as date/month/year) :")
                status=input("Enter Status (reserved ,available,not avalable) :")
                modify_book(bookid,bookName,author,sub,date,status)
                x=input("Press y or Y to continue modifying books: ")
                if x=='y' or x=="Y":
                        continue
                else:
                        break
        elif ch==4:
                search()
                x=input("Press y or Y to continue searching books: ")
                if x=='y' or x=="Y":
                        continue
                else:
                        break
        elif ch==5:
                register_member()
                x=input("Press y or Y to continue modifying books: ")
                if x=='y' or x=="Y":
                        continue
                else:
                        break
        elif ch==6:
                cancel_membership()
                x=input("Press y or Y to continue modifying books: ")
                if x=='y' or x=="Y":
                        continue
                else:
                        break
        elif ch==7:
                checkout()
                x=input("Press y or Y to continue: ")
                if x=='y' or x=="Y":
                        continue
                else:
                        break
        elif ch==8:
                Reserved_book()
                x=input("Press y or Y to cotinue: ")
                if x=='y' or x=="Y":
                        continue
                else:
                        break
        elif ch==9:
                renew_book()
                x=input("Press y or Y to cotinue: ")
                if x=='y' or x=="Y":
                        continue
                else:
                        break
        elif ch==10:
                return_book()
                x=input("Press y or Y to cotinue: ")
                if x=='y' or x=="Y":
                        continue
                else:
                        break
        elif ch==11:
                arr_id()
        elif ch==12:
                display_bookcollection()
                break                  
        elif ch==13:
                print("THANK YOU FOR VISITINGH!!!!")
                break
        else:
                print("Enter valid choice: ")
                
                

                    
                
                
                

                



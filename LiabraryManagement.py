import os

class Liabrary:
    def displayBooks(self):
        with open("AvailableBooks.txt") as f:
            data=f.read()
        data=data.split(" ")
        data=set(data)
        print("\nlist of books which ar available in library are as follows : ")
        print("\t",end="")
        print("\n\t".join(data))
    def numOfBooks(self):
        book =input("\n Enter book name : ")
        with open("AvailableBooks.txt") as f:
            data=f.read()
        data=data.split(" ")
        if book in data:
            n=data.count(book)
            print(f"\ntheir are {n} books are avialable in liabrary\n")
        else:
            print("book is not available")
    def borrowBooks(self):
        st=input("\nEnter your name : ")
        with open("StudentsList.txt") as f:
            names=f.read()
        names=names.split(" ")
        with open("AvailableBooks.txt") as f:
            data=f.read()
        data=data.split(" ")
        if st in names:
            with open(f"Students/{st}.txt") as f:
                stdata=f.read()
            stdata=stdata.split(" ")
            if len(stdata)<4:
                book=input("Enter book name : ")
                if book in data:
                    stdata.append(book)
                    stdata=" ".join(stdata)
                    with open(f"Students/{st}.txt","w") as f:
                        f.write(stdata)
                    data.remove(book)
                    data=" ".join(data)
                    with open("AvailableBooks.txt","w") as f:
                        f.write(data)  
                    print("book is successfully issued \n")
                else:
                    print("book is not avialble in the library\n")
            else:
                print("sorry you can`t borrow the book because you already issued the maximum 4 books which are allowed by liabrary authority , so return first and then you will be able to borrow a book\n")
        else:
            book=input("Enter book name : ")
            if book in data:
                names.append(st)
                names=" ".join(names)
                with open("StudentsList.txt","w") as f:
                    f.write(names)
                with open(f"Students/{st}.txt","w") as f:
                    f.write(book)
                data.remove(book)
                data=" ".join(data)
                with open("AvailableBooks.txt","w") as f:
                    f.write(data)
                print("book is successfully issued \n")
            else:
                print("book is not available in library\n")
    def retunbooks(self):
        st=input("\nEnter your name : ")
        with open("StudentsList.txt") as f:
            names=f.read()
        names=names.split(" ")
        if st in names:
            book = input("Enter the name of book which is to be returned : ")   
            with open(f"Students/{st}.txt") as f:
                stdata=f.read()
            stdata=stdata.split(" ")
            if book in stdata:
                if len(stdata)>1:
                    stdata.remove(book)
                    stdata=" ".join(stdata)
                    with open(f"Students/{st}.txt","w") as f:
                        f.write(stdata)
                else:
                    names.remove(st)
                    names=" ".join(names)
                    with open("StudentsList.txt","w") as f:
                        f.write(names)
                    os.remove(f"Students/{st}.txt")
                with open("AvailableBooks.txt") as f:
                        data1=f.read()
                data1=data1.split(" ")
                data1.append(book)
                data1=" ".join(data1)
                with open("AvailableBooks.txt","w") as f:
                    f.write(data1)
                print("book is successfully returned to the library \n")
            else:
                print("sorry this book is not issued by you please return correct book\n")
        else:
            print("sorry you are not issued any book from the library hence you can`t return any book\n")
    def addBooks(self):
        book=input("\nEnter book name to be added : ")
        with open("AvailableBooks.txt") as f:
            data1=f.read()
        with open("Books.txt") as f:
            data=f.read()
        data=data.split(" ")
        data1=data1.split(" ")
        data.append(book)
        data1.append(book)
        data=" ".join(data)
        data1=" ".join(data1)
        with open("AvailableBooks.txt","w") as f:
            f.write(data1)
        with open("Books.txt","w") as f:
            f.write(data)
        print("book is successfully added into the library \n")
    def removeBooks(self):
        book=input("Enter book name : ")
        with open("AvailableBooks.txt") as f:
            data1=f.read()
        with open("Books.txt") as f:
            data=f.read()
        print(data)
        data=data.split(" ")
        data1=data1.split(" ")
        if book in data:
            if book in data1:
                data.remove(book)
                data1.remove(book)
                data=" ".join(data)
                data1=" ".join(data1)
                with open("AvailableBooks.txt","w") as f:
                    f.write(data1)
                with open("Books.txt","w") as f:
                    f.write(data)
                print("book is successfully removed from the library \n")   
            else:
                print("book is in use, someone borrows this book please wait till it being returned\n")
        else:
            print("book is not found in library\n")
    def listOfBooks(self):
        with open("Books.txt") as f:
            data=f.read()
        data=data.split(" ")
        data=set(data)
        print("\n list of books in library is as follows : ")
        print("\t",end="")
        print("\n\t".join(data))
        print("\n")

class Student(Liabrary):
    def displayBookStatus(self):
        name=input("\nEnter your name : ")
        with open("StudentsList.txt") as f:
            names=f.read()
        names=names.split(" ")
        if name in names:
            with open(f"Students/{name}.txt") as f:
                stdata=f.read()
            stdata=stdata.split(" ")
            print("\nlist of your borrowed books are as follows : ")
            for i in range(len(stdata)):
                print(f"\t{i+1}. {stdata[i]}")
            print("\n")    
        else:
            print("you do not have issued any book yet\n")


if __name__=="__main__":
    print("*"*10,"Welcome To Library Management System","*"*10)
    while True:
        print("\nplease choose any one of the following")
        print("1. for Students")
        print("2. for Liabrary management")
        print("3. for exit")
        try:
            c1=int(input("\tEnter your choice : "))
            if c1==1:
                s=Student()
                while True:
                    print("\nplease choose any one of the following")
                    print("1. for see the list of available books in liabrary\n2. To check the numbers of books are avilable for any respective subjects \n3. To issue a Book\n4. To return a book\n5. To see your issued book list\n6. return to main menu\n7. for exit")
                    try:
                        c2=int(input("\tEnter your choice : "))
                        if c2==1:
                            s.displayBooks()
                        elif c2==2:
                            s.numOfBooks()
                        elif c2==3:
                            s.borrowBooks()
                        elif c2==4:
                            s.retunbooks()
                        elif c2==5:
                            s.displayBookStatus()
                        elif c2==6:
                            break
                        elif c2==7:
                            break
                        else:
                            print("invalid choice")
                    except Exception as e:
                        print("please enter correct thing")
            elif c1==2:
                l=Liabrary()
                while True:
                    print("\nplease choose any one of the following")
                    print("1. for see the list of books of liabrary\n2. To add a new book \n3. To remove a book\n4. return to main menu\n5. for exit")
                    try:
                        c2=int(input("\tEnter your choice : "))
                        if c2==1:
                            l.listOfBooks()
                        elif c2==2:
                            l.addBooks()
                        elif c2==3:
                            l.removeBooks()
                        elif c2==4:
                            break
                        elif c2==5:
                            break
                        else:
                            print("invalid choice")
                    except Exception as e:
                        print("Please enter the correct thing")
            elif c1==3:
                break
            else:
                print("invalid choice")
        except Exception as e:
            print("please enter the correct thing")
    print("\n\n"+"*"*10,"       Thanks for Visiting Us       ","*"*10)
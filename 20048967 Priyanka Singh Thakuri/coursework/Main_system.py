# Library Management System

import Read_Book
import Borrow_Book
import Return_Book


dictionary_Book = Read_Book.read_Book()
Book_name = Read_Book.Book_name()

def main_display():
    print()
    print("*******************************************")
    print("*                                         *")
    print("*   Welcome To Library Management System  *")
    print("*                                         *")
    print("*******************************************")
    print()
    name = input("Please register your name: ")
    count = True
    while count==True:
        print()
        print("choose your option: ")
        print("Press 1: view Books Available")
        print("Press 2: Borrow Books")
        print("Press 3: Return Books")
        print("Press 4: Exit the application")
        print()
        repeat = True
        while repeat==True:
            try:
                choice = int(input("Enter the choice: "))
                break
            except:
                print("Enter the correct input!!")
        if choice == 1:
            print("\n\t\t\t\tBooks available right now in stock:\n\n")
            print("==========================================================================================================")
            print("\tBookname\t\t\tAuthor\t\t\t\tPrice\t\tQuantity")
            print("----------------------------------------------------------------------------------------------------------")
            for key,value in dictionary_Book.items():
                print(key +"\t\t\t"+value[0]+"\t\t\t"+value[1]+"\t\t"+value[2])
            print("===========================================================================================================")
            print()
            repeat = False
                
        elif choice == 2:
            List_1 = []
            List_2 = []
            List_3 = []
                
            ans = "yes"
            while ans == "yes":
                BookName = input("Enter the BookName: ")
                if BookName in Book_name:
                    item = dictionary_Book[BookName][2]
                    if int(item)>0:
                        List_1.append(BookName)
                        List_2.append(dictionary_Book[BookName][0])
                        List_3.append(dictionary_Book[BookName][1])
                    else:
                        print("Selected Book is not available")
                else:
                    print("enter the correct BookName")
                ans = input("Do you wanna add another Book:(yes/no):")
            Borrow_Book.borrow(name,List_1,List_2,List_3)
            for i in List_1:
                a = int(dictionary_Book[i][2])
                dictionary_Book[i][2] = str(a-1)
            print(name+ ", Your selected books have been borrowed sucessfully!!")
            repeat = False
                    
        elif choice ==3:
            name = input("Please register your name: ")
            print("***Welcome back!! "+name+"***")
            print("\n")
            List_1 = []
            List_2 = []
            List_3 = []
            day = []
            value = "yes"
            while value == "yes":
                BookName = input("Enter the BookName: ")
                if BookName in Book_name:
                    List_1.append(BookName)
                    List_2.append(dictionary_Book[BookName][0])
                    List_3.append(dictionary_Book[BookName][1])
                    while True:
                        try:
                            days = int(input("Enter the number of days you borrowed the book: "))
                            day.append(days)
                            break
                        except:
                            print("Enter the correct number of days!!!")
                else:
                    print("Enter the correct BookName!!!")
                value = input("Do you wanna return next book:(yes/no):")
            Return_Book.write_return(name,List_1,List_2,List_3,day)
            for i in List_1:
                a = int(dictionary_Book[i][2])
                b = a+1
                dictionary_Book[i][2] = str(b)
            print(name+", The book you borrowed had been returned sucessfully")
            print("Thank you for choosing us, Hope to see you soon")
            repeat = False
        
        elif choice == 4:
             print()
             print("****************************************")
             print("*                                      *")
             print("*     Thanks for choosing us!!         *")
             print("*                                      *")
             print("****************************************")
             print()
             count = False
             repeat = False
        else:
            print("Enter the correct option")
            repeat = True
main_display()


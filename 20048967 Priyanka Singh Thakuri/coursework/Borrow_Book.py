#Creation of bills for borrow process

import datetime
def borrow(name,List_1,List_2,List_3):
    filename = "Borrowed_Book/"+name+".txt"  ##Path for borrow bills
    file = open(filename, "w")
    file.write("\n")
    file.write("*******************************************\n")
    file.write("*                                         *\n")
    file.write("* Welcome To Library Management System    *\n")
    file.write("*                                         *\n")
    file.write("*******************************************\n")
    file.write("\n")
    file.write("\n\t\t\t\t*********Book Borrowed System**********\n\n")
    file.write("Date & Time: "+str(datetime.datetime.now())+"\n")
    file.write("The name of student: "+name+"\n\n")
    file.write("The list of books borrowed by the student is: \n")
    file.write("==========================================================================================================\n")
    file.write("BookName \t\t\t Author \t\t Price\n")
    file.write("==========================================================================================================\n")

    for i in range(len(List_1)):
        file.write(List_1[i] +"\t\t"+ List_2[i] +"\t\t"+ List_3[i])
        file.write("\n")
        file.write("__________________________________________________________________________________________________________\n")
    total = 0
    for i in List_3:
        i = i.replace("$","")
        total = total + float(i)
    file.write("\n")
    file.write("the total price for borrowing a book is: "+"$"+str(total))
    file.write("\n")
    file.write("-------------*-------------*------------*-------------*--------------*------------*------------*------------\n")
    file.close

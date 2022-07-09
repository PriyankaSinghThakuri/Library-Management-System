#Creating of bills for Return process

import datetime
def write_return(name,List_1,List_2,List_3,day):
    filename = "Returned_Book/"+name+".txt"  ##Path for return bills
    file = open(filename, "w")
    file.write("\n")
    file.write("*******************************************\n")
    file.write("*                                         *\n")
    file.write("*   Welcome To Library Management System  *\n")
    file.write("*                                         *\n")
    file.write("*******************************************\n")
    file.write("\n")
    file.write("\n\t\t\t\t*********Book Returned System**********\n\n")
    file.write("Date & Time: "+str(datetime.datetime.now())+"\n")
    file.write("The name of student: "+name+"\n")
    file.write("The list of books borrowed by the user is:\n")
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
    file.write("the total price for borrowing a book is: "+"$"+str(total))
    file.write("\n")
    total_fine = 0
    for i in range(len(day)):
        if day[i] > 10:             #Fine for returning books after 10 days
            fine_day = day[i]-10
            for i in List_3:
                i = i.replace("$","")
                fine = 1.5 * fine_day
            total_fine = fine
    total_price = total + total_fine        #Total price calculation
    file.write("total fine for late returning a book is: "+"$"+str(total_fine))
    file.write("\n")
    file.write("total amount including fine for returning book is: "+"$"+str(total_price))
    file.write("\n")
    file.write("-------------*-------------*------------*-------------*--------------*------------*------------*-----------\n")
    file.close


import datetimep
import listsplit

def borrowBook():
    success=False
    while(True):
        firstName=input("Enter the first name of the borrower: ")
        if firstName.isalpha():
            break
        print("please input alphabet from A-Z")
    while(True):
        lastName=input("Enter the last name of the borrower: ")
        if lastName.isalpha():
            break
        print("please input alphabet from A-Z")
            
    t="Borrow-"+firstName+".txt"
    with open(t,"w+") as f:
        f.write("               Library Management System  \n")
        f.write("                   Borrowed By: "+ firstName+" "+lastName+"\n")
        f.write(" From:   Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
        f.write(" To:     Date: "                "    Time:"               "\n\n")
        f.write("S.N. \t\t Bookname \t      Authorname \n" )
    
    while success==False:
        print("Please select a option below:")
        for i in range(len(listsplit.book_name)):
            print("Enter", i, "to borrow book", listsplit.book_name[i])
    
        try:   
            a=int(input())
            try:
                if(int(listsplit.book_no[a])>0):
                    print("Book is available")
                    with open(t,"a") as f:
                        f.write("1. \t\t"+ lissplit.book_name[a]+"\t\t  "+listsplit.book_author[a]+"\n")

                    listsplit.book_no[a]=int(listsplit.book_no[a])-1
                    with open("booklist.txt","w+") as f:
                        for i in range(5):
                            f.write(listsplit.book_name[i]+","+listsplit.book_author[i]+","+str(listsplit.book_no[i])+","+"$"+listsplit.book_price[i]+"\n")


                    #multiple book borrowing code
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Do you want to borrow more books? However you cannot borrow same book twice. Press y for yes and n for no."))
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Please select an option below:")
                            for i in range(len(listsplit.book_name)):
                                print("Enter", i, "to borrow book", listsplit.book_name[i])
                            a=int(input())
                            if(int(listsplit.book_author[a])>0):
                                print("Book is available")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ listsplit.book_name[a]+"\t\t  "+listsplit.book_author[a]+"\n")

                                listsplit.book_no[a]=int(listsplit.book_no[a])-1
                                with open("booklist.txt","w+") as f:
                                    for i in range(5):
                                        f.write(listsplit.book_name[i]+","+listsplit.book_author[i]+","+str(listsplit.book_no[i])+","+"$"+listsplit.book_price[i]+"\n")
                                        success=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"):
                            print ("Thank you for borrowing books from us. ")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Please choose as instructed")
                        
                else:
                    print("Book is not available")
                    borrowBook()
                    success=False
            except IndexError:
                print("")
                print("Please choose book acording to their number.")
        except ValueError:
            print("")
            print("Please choose as suggested.")

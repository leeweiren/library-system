import listsplit
import datetimep
def returnBook():
    name=input("Enter name of borrower: ")
    a="Borrow-"+name+".txt"
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("$") for a in lines]
    
        with open(a,"r") as f:
            data=f.read()
            print(data)
    except:
        print("The borrower name is incorrect")
        returnBook()

    b="Return-"+name+".txt"
    with open(b,"w+")as f:
        f.write("                Library Management System \n")
        f.write("                   Returned By: "+ name+"\n")
        f.write("    Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
        f.write("S.N.\t\tBookname\t\tCost\n")


    total=0.0
    for i in range(3):
        if listsplit.book_name[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+listsplit.book_name[i]+"\t\t$"+listsplit.book_price[i]+"\n")
                listsplit.book_no[i]=int(listsplit.book_no[i])+1
            total+=float(listsplit.book_price[i])
            
    print("\t\t\t\t\t\t\t"+"$"+str(total))
    print("Is the book return date expired?")
    print("Press Y for Yes and N for No")
    stat=input()
    if(stat.upper()=="Y"and"y"):
        print("By how many days was the book returned late?")
        day=int(input())
        fine=2*day
        with open(b,"a")as f:
            f.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
        total=total+fine
    


    print("Final Total: "+ "$"+str(total))
    with open(b,"a")as f:
        f.write("\t\t\t\t\tTotal: $"+ str(total))
    
        
    with open("booklist.txt","w+") as f:
            for i in range(5):
                f.write(listsplit.book_name[i]+","+listsplit.book_author[i]+","+str(listsplit.book_no[i])+","+"$"+listsplit.book_price[i]+"\n")


import os
import listsplit
import datetimep
import borrow

def main_menu():
    while(True):
        

    
        os.system("cls") #use to clear the screen
        print("\t\t\t We;come To The Lbrary System \n")
        print("\t\t\t 1 - Account Status")
        print("\t\t\t 2 - Catalogue")
        print("\t\t\t 3 - Borrow A Book")
        print("\t\t\t 4 - Return A Book")
        print("\t\t\t 5 - Payment")
        print("\t\t\t 6 - Search")
        print("\t\t\t 0 - Exit \n\n")
        try:
            a = int(input("Please choose a function >> "))
            print()
            if(a==1):
                with open("user.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print()

            elif(a==2):
                with open("booklist","r") as fb:
                    line=fb.read()
                    print(line)
                    print()

            elif(a==3):
                listspilt.listSplit()
                borrow.borrowBook()

            elif(a==4):
                listsplit.listSplit()
                Return.returnBook()

            elif(a==5):
                listsplit.listSplit()
                payment.paymentBook()

            elif(a==6):
                listsplit.listSplit()
                search.searchBook()

            elif(a==0):
                exit_program = input("Press ENTER to exit program")
                exit()

            else:
                print("Please enter a valid choice from 0-6")

        except ValueError:
            print("pls input as suggested>")


                
main_menu()
            
                
                
                

            
            

        



        
    




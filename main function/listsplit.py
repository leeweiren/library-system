def listSplit():
    global bookname
    global authorname
    global quantity
    global cost
    book_id=[]
    book_name=[]
    book_author=[]
    book_no=[]
    book_price[]
    with open("booklist.txt","r") as f:
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    book_ud.append(a.strip("$"))
                elif(ind==1):
                    book_name.append(a)
                elif(ind==2):
                    book_author.append(a)
                elif(ind==3):
                    book_no.append(a)
                elif(ind==4):
                    cost.append(a.strip("$"))
                ind+=1

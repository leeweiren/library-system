from datetime import date
# date object of today's date
def daynonmember():
    dayn=today.day+7
    return dayn

def daymember():
    day=today.day+14
    return day

def dylst():
    if (today.year%4)==0 :
        daylist[1]=29
        if today.month==1:
            d=daylist[0]
        elif today.month==2:
            d=daylist[1]
        elif today.month==3:
            d=daylist[2]
        elif today.month==4:
            d=daylist[3]
        elif today.month==5:
            d=daylist[4]
        elif today.month==6:
            d=daylist[5]
        elif today.month==7:
            d=daylist[6]
        elif today.month==8:
            d=daylist[7]
        elif today.month==9:
            d=daylist[8]
        elif today.month==10:
            d=daylist[9]
        elif today.month==11:
            d=daylist[10]
        elif today.month==12:
            d=daylist[11]

    else:
        
        
        if today.month==1:
            d=daylist[0]
        elif today.month==2:
            d=daylist[1]
        elif today.month==3:
            d=daylist[2]
        elif today.month==4:
            d=daylist[3]
        elif today.month==5:
            d=daylist[4]
        elif today.month==6:
            d=daylist[5]
        elif today.month==7:
            d=daylist[6]
        elif today.month==8:
            d=daylist[7]
        elif today.month==9:
            d=daylist[8]
        elif today.month==10:
            d=daylist[9]
        elif today.month==11:
            d=daylist[10]
        elif today.month==12:
            d=daylist[11]

    return d
    
    
    
today = date.today()
daylist=[31,28,31,30,31,31,30,31,30,31,30,31]
monthlist=[1,2,3,4,5,6,7,8,9,10,11,12]

yn= input("member?(y-yes/n-no)>>")

if yn== "Y" or "y":
    day=daymember()
    dylst()
    if day>d:
        month=today.month+1
        if month>12:
            nd=day-d
            m=monthlist[0]
            y=today.year+1

            print(nd,"/",m,"/",y)
        else :
            nd=day-d
            m=month
            y=today.year

            print(nd,"/",m,"/",y)

    elif day<=d:
        nd=day
        m=today.month
        y=today.year

        print(d,"/",m,"/",y)

elif yn=="N" or "n":
    dayn=daynonmember9()
    d=dylst()
    if dayn>d:
        month=today.month+1
        if month>12:
            nd=dayn-d
            m=monthlist[0]
            y=today.year+1

            print(nd,"/",m,"/",y)
        else :
            nd=dayn-d
            m=month
            y=today.year

            print(nd,"/",m,"/",y)

    elif dayn<d:
        nd=dayn
        m=today.month
        y=today.year

        print(d,"/",m,"/",y)
    
        
            
        
    
    
        
            
            
    
    






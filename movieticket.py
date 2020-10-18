import datetime
time=datetime.datetime.now().hour

def date():

    """
        This function is used to choose which day you want to book tickets.

    """
    print("-----------------------")
    print("Choose the day...!")
    print("-----------------------")
    print("1. TODAY , AFTER",time,": 00")
    print("2. Tomorrow.")
    print("3. Day After Tomorrow.")
    n=int(input("Enter the number from 1,2 and 3:\n"))
    if n not in [1,2,3]:
        print("-----------------------")
        print("Enter Valid Input..!😥")
        print("-----------------------")
        date()
    return n

def theatre():

    """
        This function is used to select which screen u want to watch the movie.

    """
    print("-----------------------")
    print("SELECT A SCREEN...!")
    print("-----------------------")
    for i in range(1,6):
        print(i,"."," SCREEN ",i,sep="")

def movie():

    """
        This function shows the movies currently available.

    """
    print("-----------------------")
    print("SELECT A MOVIE...!")
    print("-----------------------")
    print("1. AVENGERS ENDGAME")
    print("2. THE DARK KNIGHT RISES🖤")
    print("3. SPIDERMAN - FAR FROM HOME🤘")

def select_movieName(t):

    """
        This function is to select the movie to watch.

    """

    if t==1:
        return "AVENGERS ENDGAME"
    elif t==2:
        return "THE DARK KNIGHT RISES🖤"
    else:
        return "SPIDERMAN - FAR FROM HOME🤘"

def showtimings(n):

    """
        This function shows the movie timings.

    """

    l=[]
    print("-----------------------")
    print("SELECT SHOW TIMINGS...!")
    print("-----------------------")
    l.append("1. 11 A.M.")
    l.append("2. 2:00 P.M")
    l.append("3. 5:30 P.M.")
    l.append("4. 9:30 P.M.")
    if n==1:
        if time<11:
            for i in l:
                print(i) 
        elif time<14:
           for i in l[1:]:
                print(i) 
                return 1
        elif time<17:
           for i in l[2:]:
                print(i)  
                return 2
        elif time<21:
           for i in l[3:]:
                print(i)   
                return 3  
        else:
            print("SORRY...! NO SHOW AVAILABLE TODAY CHOOSE OTHER DAY..!") 
    else:      
        for i in l:
            print(i)
        return 1

def select_showtimings(i):

    """
        This is to select the show timings.

    """
    if i==1:
        return "11:00 A.M"
    elif i==2:
        return "2:00 P.M"
    elif i==3:
        return "5:30 P.M."
    else:
        return "9:30 P.M."

def ticket_details(name,t,NO_OF_TICKETS,s,show,m):

    """
        This function to print the ticket details.

    """

    print("YOUR ORDER IS :")
    print("***********")
    print("NAME              :",name)
    print("MOVIE NAME        : ",select_movieName(m))
    print("THEATRE_NAME      :  THEATRE",t)
    print("NUMBER OF TICKETS : ",NO_OF_TICKETS)
    print("ON ",s,select_showtimings(show))
    print("***********")
    

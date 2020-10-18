from greetings import greetings,introduce,voice_msg
from demo import date,theatre,movie,select_movieName,showtimings,select_showtimings,ticket_details

def bot():   
    greetings()
    name=input("\nEnter your name :")
    introduce(name)
    n=date()
    if n==1:
        s="Today "
    elif n==2:
        s="Tomorrow"
    else:
        s="Day After Tomorrow"
    movie()
    m=int(input("ENTER MOVIE OPTION WITH NUMBERS 1,2 & 3 :"))
    if m not in [1,2,3]:
        print("-----------------------")
        print("Enter Valid Input..!😥")
        print("-----------------------")
        movie()
        m=int(input("ENTER MOVIE OPTION WITH NUMBERS 1,2 & 3 :"))
    theatre()
    t=int(input("ENTER THEATRE OPTION :"))
    while t not in range(1,6):
        print("-----------------------")
        print("Enter Valid Input..!😥")
        print("-----------------------")
        theatre()
        t=int(input("ENTER THEATRE OPTION :"))
    q=showtimings(n)
    show=int(input("ENTER SHOW TIMINGS OPTION :"))
    while show not in range(q,5):
        print("-----------------------")
        print("Enter Valid Input..!😥")
        print("-----------------------")
        showtimings(n)
        show=int(input("ENTER SHOW TIMINGS OPTION :"))
    NO_OF_TICKETS = int(input("ENTER NUMBER OF TICKETS.. :"))
    ticket_details(name,t,NO_OF_TICKETS,s,show,m)
    print("DO YOU WANT TO MAKE ANOTHER ORDER :")
    print("1. YES")
    print("2. NO")
    if (input("ENTER YOUR OPINION :")=="1"):
        bot()
    else:
        print("THANK YOU VERY MUCH FOR YOUR ORDER , VISIT AGAIN...!☺")

bot()

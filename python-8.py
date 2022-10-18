import datetime
print("###  Enter The details below in mentioned Formatts ##### ")
try:
    year=int(input("Enter Birth ofyear[YYYY]:"))
    month = int(input("enter Birth of month[MM]:"))
    day = int(input("enter Birth ofday[DD]:"))

    '''hour=int(input("enter hours"))
    min=int(input("enter min"))
    sec=int(input("enter sec"))
    m=int(input("micro sec 000000-999999"))'''

    birth=datetime.date(year,month,day)
    print("Date Of Birth:",birth)

    today=datetime.date.today()
    print("Todays date:",today)
    if birth.month==today.month and today.day==birth.day or today.month>birth.month:
        nextbirthyear=today.year+1

    else:
        nextbirthyear=today.year

    nextbirthday=datetime.date(nextbirthyear,birth.month,birth.day)
    print("Next birthday date:",nextbirthday)

    diff=(nextbirthday-today).days
    d=diff

    print("The days remaining for upcoming Birtday:",diff,'days')
    time=diff*24
    print("The hours:",time,"hours")
    print("The minutes:",time*60,'min')
except ValueError:
    print("Please Enter correct details")

    
   ### OUTPUT ####
  
  ###  Enter The details below in mentioned Formatts ##### 
Enter Birth ofyear[YYYY]:2000
enter Birth of month[MM]:4
enter Birth ofday[DD]:14
Date Of Birth: 2000-04-14
Todays date: 2022-10-18
Next birthday date: 2023-04-14
The days remaining for upcoming Birtday: 178 days
The hours: 4272 hours
The minutes: 256320 min

from text_to_speech import speak
from fpdf import FPDF
import datetime
import fuel_rate as fr   #user difined class or function import 
import random
import smtplib


try :

    title = "SHREE petrol pump"
    speak(" welcome shree petrol pump")
    print("--"*25)
    print(title.center(50))
    print('--'*25)
    a_f = ("avileble fuel")
    print(a_f.center(50))
    print("1) Petrol ")
    print("2) Diesel")
    print('3) CMG')
    print("4) Exit")

    while(True):

        speak("enter valied number like 1 2 3 if you want fuel and you want exit enter 4")
        choice = int(input("enter you fuel type [1/2/3/4]:- "))
    
        if choice == 1 :
            speak("you selected petrol")
            amount = float(input("enter amount :- "))
            fuel_type = "petrol"
            qauntity = amount/fr.petrol()
            print(f"you got {qauntity} liters petrol of RS.{amount} ")
            break

        elif choice == 2 :
            speak("you selected diesel")
            amount = float(input("enter amount :- "))
            fuel_type = "diesel"
            qauntity = amount/fr.diesel()
            print(f"you got {qauntity} liters diesel of RS.{amount} ")
            break

        elif choice == 3 :
            speak("you selected CNG")
            amount = float(input("enter amount :- "))
            fuel_type = "CNG"
            qauntity = amount/fr.cng()
            print(f"you got {qauntity} liters cng of RS.{amount} ") 
            break

        elif choice == 5 :
            print("thank you for visit us i hope see you soon !!!!!!")
            speak("thank you for visit us i hope see you soon ")
            break 

    #live date time
    _date_time = datetime.datetime.now()

    #bill number ganretor
    bill_no = random.randint(999999,9999999)
    
    # make bill pdf
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica',size=15) 
    pdf.text(30,25,txt=f"SHREE Petrol Pump")
    pdf.text(30,30,txt=f"Time and date:- {_date_time}")
    pdf.text(30,35,f"bill no :- {bill_no}")
    pdf.text(30,40,txt=f"you got :- {qauntity} liter")
    pdf.text(30,45,txt=f"amount is :- {amount}")
    pdf.text(30,50,txt="thank you !!!!!")
    pdf.output(f"{bill_no}.pdf")

#sent bill in costamer mail id
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

    server.login("MAILID","PASSWOLRD")
    subject = "SHREE petrol pump bill"
    body = f"{bill_no}.pdf"
    msg = f"subject:{subject}\n\n{body}"
    server.sendmail("SENDER MAILID","RICEVER MAILID",msg)
    print("you bill send on your mail id !!!!!! thank you('~')")


except BaseException as ex:
    print(ex)
    print(" author - shubham mane , contact phone no - 7720007252 or mail id - maneshubham4033@gmail.com")
           
finally:
    print("exception finally")

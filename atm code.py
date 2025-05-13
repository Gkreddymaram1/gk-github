s='''
1.credit
2.debit
3.ministatement
4.exit
'''
name="gopal"
password="1234"
user_name=input("enter your name:")
password=input("enter your possword:")
s='''
1.credit
2.debit
3.ministatement
4.exit
'''
Amount=1000
if name==user_name and  "posswords==possword":
    print(s)
    option=input("enter the option")
    if option==1:
        credit_Amount=float(input("enter the Amount"))
        print("Amount after credit:",Amount+credit_Amount)
    elif option==2:
        debit_amount=float(input("enter the Amount"))
        print("amount after debit:",Amount-debit_amount) 
    elif option==3:
            print("Amount:",Amount)
else:
    print("incorect")
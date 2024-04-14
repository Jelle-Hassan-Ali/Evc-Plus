def User():
    global dic
    User = input("Please Enter Name: ")
    Pass = int(input("Please Enter Pass: "))

    dic = {'Username':User,'Password':Pass}
    print(dic)
def Sear():
    global dic
    Radi = input(f"Please Enter What You Want: ")
    if Radi == 'User':
        print(dic['Username'])
    elif Radi == 'Pass':
        print(dic['Password'])
    else:
        print(f"Dabeylaha Raac Adeer")
        while True:
            print(f'Fadlan dooro Midkood: \n1. Admin: \n2.Radi:')

User()

Sear()









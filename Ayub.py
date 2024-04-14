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
        print("Fadlan Doro: \n1. Admin \n2. Search \n3. Exit")
        doro = int(input(f'Fadlan Doro Midka Aad Rabto: (1-3)'))
        if doro == 1:
            User()
        elif doro == 2:
            Sear()
        elif doro == 3:
            exit()


        break


User()
Sear()









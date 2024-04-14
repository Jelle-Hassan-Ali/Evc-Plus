

Register = []

def add_Reg():
    name = input("Fadlan Gali Magaca: ")
    Tell = int(input("Fadlan Gali Tell-ka: "))
    ID = int(input("Fadlan Gali ID-ga: "))
    Age = int(input("Fadlan Gali Da'da: "))

    Registe = {'name': name, 'Tell': Tell, 'ID': ID, 'Age': Age}
    Register.append(Registe)
    print(f"Reistration Name: {name} Tell:{Tell} with ID: {ID} and Age: {Age} added successfully.")

def remove_Reg():
    name = input("Enter what do you want to remove: ")
    removed = False
    for Registe in Register:
        if Registe['name'] == name:
            Register.remove(Registe)
            print(f"Registration {name} removed successfully. ")
            removed = True
            break
    if not removed:
        print(f"Registration '{name}' not found.")

def view_Reg():
    if Register:
        for Registe in Register:
            print(f"name:{Registe['name']}, Tell:{Registe['Tell']}, ID:{Registe['ID']}, Age:{Registe['Age']} ")
    else:
        print("No Registration found ")

while True:
    print(f"\n -- Registration Form-- \n1. Add Registration \n2. Remove Registration \n3. View Registration \n4. Quit" )
    choise = int(input("Enter Your Choise (1-4): "))

    if choise == 1:
        add_Reg()
    elif choise == 2:
        remove_Reg()
    elif choise == 3:
        view_Reg()
    elif choise == 4:
        break
    else:
        print("invailed choise please correct your choise !!")













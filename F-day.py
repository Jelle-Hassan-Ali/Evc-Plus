"""
ages=[22,33,44,45,55]
for x in ages:
    print(x)
"""
"""
Ser = int(input("Fadlan Gali da'da ad radineyso: "))
ages = [33,55,66,77,88]
for age in ages:

    if Ser in ages:
        if age == Ser:
            print(age)
            break
    else:
        print(f"Kuma Hayo {age} Da'daan")
        break
"""        """
i = 0
while i< 8:
    i += 1
    print(i)
"""
"""
num = 20
while num > 0:
     num -= 1
     print(num)
"""

"""
name = input("Fadlan Gali Magaca ")
number = input("Fadlan Gali Numberka ")
ID = int(input("Fadlan Gali ID-ga "))
age = int(input("Fadlan Gali Da'da "))

def fun():
    List = [{name:'name', number:'number', ID:'ID',age:'age'}]
    List.append(name)
    List.append(number)
    List.append(ID)
    List.append(age)
    print(List)
fun()
"""

#while loop
"""
i = 0
while i <= 4:
    print(i)
  i+=1
"""



"""
num = 0
while num <= 8:
    print(num)
    num += 1
"""
"""
Gel = 0
while Gel <= 9:
    print(Gel)
    Gel += 2


mul = 0
while mul <= 10:
    print(mul)
    mul += 1
"""
"""
ss = 0
while ss < 10:
    print(ss)
    if ss == 5:
        print("Waala helay")
        break
    ss += 1
"""
"""
Maas = 0
while Maas < 16:
    print(Maas)
    Maas += 1
    if Maas == 7:
        print("✔✔✔")
        continue
"""
                              #while loop
"""
num = 0
while num < 8:
    print(num,'num is less then 8')
    num += 1
else:
    print(num, 'is not in list')
"""

#for loop
"""
fruits = ["Banana"]
for  x in fruits:
    print(x)
"""
                                     #School = []

School = []

def add_sub():
    num_subjects = int(input("Please Enter the number of Subjects: "))
    for item in range(num_subjects):
        subject_name = input("Please enter the subject name: ")
        School.append(subject_name)

def view_sub():
    if School:
        for index, subject in enumerate(School, start=1):
            print(f"{index}. {subject}")
    else:
        print("No Subjects Found")

while True:
    print("\n -- Subjects -- \n1. Add Subjects  \n2. View Subjects \n3. Quit")

    choice = int(input("Enter Your Choice (1-3): "))

    if choice == 1:
        add_sub()
    elif choice == 2:
        view_sub()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please enter a valid choice (1-3).")


                                #Simple Calculator usin Class
"""
class Calculator:
    def __init__(self):
       self.ch = int (input('fadlan door \n1.add \n2.sub \n3.mult: '))
       if self.ch == 1:
           self.add()
       elif self.ch == 2:
           self.sub()
       elif self.ch == 3:
           self.mult()
    def add(self):
        self.num1 = float(input('num1: '))
        self.num2 = float(input('num2: '))
        print(self.num1 + self.num2)

    def sub(self):
        self.num1 = float(input('num1: '))
        self.num2 = float(input('num2: '))
        print(self.num1 - self.num2)

    def mult(self):
        self.num1 = float(input("Enter num1: "))
        self.num2 = float(input("Enter num2: "))
        print(self.num1 * self.num2)

Calculator()
"""


"""
numbers = [11,22,33,41,23,55,676,77,221,5,3]
smolest_num = numbers[0]

for number in numbers:
    if number < smolest_num:
        smolest_num = number

print(smolest_num)
"""
"""
cars = ["Ford", "Volvo", "BMW"]
x = cars[1,1]
print(x)
"""
"""
User = input('Fadlan Gali User-ka: ')
Pass = int(input('Fadlan Gali Pass-ka: '))

My_dict = {'Username': User , 'Password': Pass}
print(My_dict)

Sear = input(f'Fadlan Waxa Aad Rabtid: ')
if Sear == 'User':
    print(My_dict['Username'])
elif Sear == 'Pass':
    print(My_dict['Password'])
else:
    print("vailed entery please correc")
"""

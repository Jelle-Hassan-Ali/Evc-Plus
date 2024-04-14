"""
Calculatore = []

def add():

    num1 = int(input('So gali numberka 1aad: '))
    num2 = int(input('So gali numberka 2aad: '))


    print(num1 + num2 )

add()
"""

"""
names = ["Ali","Ahmed","Ayub","Adan","Ari"]
for x in names:
    print(x)
    if x == 'Adan':
        break
"""
"""
def my_kids(*kids):
    print("My midle kids is " + kids[1])
my_kids('Jelle' , 'Hassan', 'Ali')
"""
#Question 8:
#Write a Python program to sort a list of numbers in ascending order using the bubble sort algorithm.
"""
nuber = [3,5,7,9,1,6,2,8]
nuber.sort()
print(nuber)

"""
"""
Question 6:
Write a Python program to find the largest and smallest elements in a given list.

L_numbers = [33,44,55,6,77,8,9,22,13,99, 19]
Largest_num = L_numbers[0]

for number in L_numbers:
    if number > Largest_num:
        Largest_num = number
        
        print(Largest_num)

"""
"""
L_numbers = [33, 44, 55, 6, 77, 8, 9, 22, 13, 99, 19]
Largest_num = L_numbers[0]

for number in L_numbers:
    if number > Largest_num:
        Largest_num = number

print(Largest_num)

"""
"""
x = 1
while x < 100:
    x *= 2
    print(x)

"""
"""
lower = 100
upper =120
print( f" The prime numbers between",lower ,"and" ,upper ,'are: ')
for num in range(lower , upper + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i)==0:
                break
            else:
                print(num)

"""
"""
import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    print("Welcome to the Guess the Number game!")
    print("Try to guess the secret number between 1 and 100.")

    attempts = 0

    while True:
        # Get player's guess
        guess = int(input("Enter your guess: "))

        # Increment the attempts counter
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")

# Run the game
guess_the_number()

"""
"""
def greating(name):
    print("Asc:",name ,"Setahey Halada kawaran sxpw")
greating("Jelle")
"""
"""
def add(x):
    print(x*2)
add(5)
"""
"""
def names(F_name, L_name, Age,Shaqo):
    print(f"Hi My First Name is:", F_name,'And My Last Name is',L_name, 'And Also My Age is ',Age ,'Shaqadeyduna Waa',Shaqo,)
names('Jelle', 'Hassan',21, 'Eng')
"""
"""
def ilmo(*ilmo):
    print("Cunugeyga ugu yar waa: ",ilmo[2])
ilmo("Abdullahi", "Ali","Nasteho ","Nasro")

def kids(child1,child2,child3):
    print("my yuongest child is ",child3)
kids("Jelle", "Hassan","Ali")
"""



class person:
    num1 = int(input('Fadlan so gali 1aad: '))
    num2 = int(input('Fadlan so gali 2aad: '))
    num3 = num1 * num2
p1 = person()
print(p1.num3)
while True:
    print("Waa guuleysatey")
    break
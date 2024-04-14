"""
lis =[11,22,31,2,12,82,29,5]
larg = lis[0]

for num in lis:

    if num > larg:
        larg = num

print(larg)
"""
"""
def M():
    M1 = input(f' Fadlan Gali Mada 1aad: ')
    M2 = input(f' Fadlan Gali Mada 2aad: ')
    M3 = input(f' Fadlan Gali Mada 3aad: ')

    dic ={'Mada 1aad waa': M1, 'Mada 2aad waa': M2, 'Mada 3aad waa': M3}
    print(dic)

    Radi = input(f'Madadee Raadinee: ')
    if Radi == 'M1':
        print(dic['Mada 1aad waa'])
    elif Radi == 'M2':
        print(dic['Mada 2aad waa'])
    elif Radi == 'M3':
        print(dic['Mada 3aad waa'])
M()
"""

def Sub():
    global Dic
    Py = input(f"Fadlan So Gali M 1aad: ")
    Jv = input(f"Fadlan So Gali M 2aad: ")
    Ht = input(f"Fadlan So Gali M 3aad: ")

    Dic = {'M 1aad': Py, 'M 2aad':Jv, 'M 3aad': Ht }
    print(Dic)

def Sear():
    global Dic
    Sear = input(f"Maxaad Radineysaa Wall: ")
    if Sear == 'Py':
        print(Dic['M 1aad'])
    elif Sear == 'Jv':
        print(Dic['M 2aad'])
    elif Sear == 'Ht':
        print(Dic['M 3aad'])


Sub()
Sear()

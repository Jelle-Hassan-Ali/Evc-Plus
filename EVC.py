Pin = 1122
Balance = float(500)
My_number = 616088558
pin = int(input(f" -EVC_PLUS- \n Fadlan Gali Pin-kaaga " ))

if pin == Pin:
    print(f"\n1. Itus Haraagaaga \n2. Kaarka Hadalka \n3. Bixi Biil \n4. Uwareeji -EVC- \n5. Warbixin Kooban \n6. Salaam Bank \n7. Maareynta \n8 Bill Payment")
    ch =int(input(''))
    if ch == 1:
        Lacag = Balance
        print(f"Haraagaagu waa ${Lacag}")
    if ch == 2:
        print("\n1. Kushubo \n2. Ugu shub")
        dooro = int(input(''))
        if dooro == 1:
            Lacag = int(input('Fadlan Gali Lacagta '))
            print(f"Mahubtaa inaad  $ {Lacag} ku shubaneysid \n1. Haa \n2. Maya " )
            dor = int(input(''))
            if dor == 1:
                print(f"Waxaad Kushubatey ${Lacag} {My_number} \n Haraagaaga cusub waa ${Balance-Lacag}")
            else:
                print("Mahadsanid !")
        elif dooro == 2:
            Lacag = int(input('Fadlan Gali Lacagta '))
            Number = int(input('Fadlan Gali Number-ka aad ugu shubeysid '))
            print(f"Mahubtaa inaad ${Lacag} ugu shubtid {Number} \n1. Haa \n2. Maya")
            doro1 = int(input(''))
            if doro1 == 1:
                print(f"Waxaad ${Lacag} Ugu shubtay {Number} \n Haraagaaga cusub waa ${Balance-Lacag} ")
            else:
                print("Mahadsanid!")
    elif ch == 3:
        print(f"Bixi biil \n1. Post Paid \n2. Ku iibso ")
        doro2 = int(input(''))
        if doro2 == 1:
            print("Post Paid \n1. Ogow Biilka \n2. Bixi Biil \n3. Ka Bixi Biil")
            doro3 = int(input(''))
            if doro3 == 1:
                print("an error accurred , please try again")
            elif doro3 == 2:
                Lacag = int (input("Fadlan Gali Lacagta "))
                print(f"Mahubtaa inaa bixisid bill lacagtiisu tahay: ${Lacag} ? \n1. Haa \n2. Maya")
                dr = int(input(''))
                Number = int(input('Fadlan Gali Number-ka aad u direysid bill-ka  '))
                if dr == 1:
                    print(f"Waxaa bill lacagtisu tahay ${Lacag}, U dirtey {Number} \n Xisaabtaadu Waa {Balance-Lacag} ")
                else:
                    print("Thank You ")
            elif doro3 ==3:
                Mobil= int(input("Fadlan Gali Mobilka "))
                Lacag = int(input("Fadlan Gali Lacagta "))
                print(f"Mahubtaa inaa bixisid bill lacagtiisu tahay: ${Lacag} oo lagarabo {My_number} ? \n1. Haa \n2. Maya")
                dr1 = int(input(''))
                if dr1 == 1:
                    print(f"Waxaad Bill lacagtisu tahey ${Lacag} kadirtey {Mobil} \n Bill-kaagu Waa {Balance-Lacag}")
                else:
                    print("Mahasanid!")

        elif doro2 == 2:
            print(f"Ku iibso \n Fadlan Gali Aqoonsiga Ganacsigaaga")

    elif ch == 4:
        Mobil = int(input("Fadlan Gali Mobilka "))
        Lacag = int(input("Fadlan Gali Lacagta "))
        print(f"Mahubtaa inaad ${Lacag} U wareejisid {Mobil} ?\n1. Haa \n2. Maya")
        dr2 = int(input(''))
        if dr2 == 1:
            print(f"[EVC-PLUS]\n ${Lacag} ayaad u wareejisay {Mobil}, \n Haraagaagu waa ${Balance-Lacag}")
        else:
            print("Mahadsanid!")

    elif ch == 5:
        print(f"Warbixin kooban \n1. Last Action \n2. Wareejintii u dambeysay \n3. Iibsashadii u dambeysay \n4. Last 3 Actions \n5 Email Me My Activity ")
        dor3 = int(input(''))
        Number = int = 616800888
        Date = 12/2/2024
        mony = 23
        if dor3 == 1:
            print(f"${mony} ayaad u wareejisay {Number} 12/02/2024 09:56pm")

    elif ch == 6:
        print(f"Salaam Bank \n1. Kawareeji EVC-plus")
        dor4 = int(input(''))
        if dor4 == 1:
            print(f"Fadlan dooro xissabta Bangiga \n1.SALAAM SOMALI BANK \n2. Darasalaam Bank \n3. Bank Beeraha \n4. Salaam Sch")
            dor5 = int(input(''))
            Account = int(input('Fadlan Gali Account-ka '))
            if dor5 == 1:
                print("")










else:
    print(f" Pin-ka aad galisay waa khalad fadlan is hubi ")

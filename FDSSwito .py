print("Welcome to ---SWITO---")
input("Press enter to continue")
x = input("Please enter your name")
def payment():
    print("Available payment gateways\n(A) UPI      (B)CARD      (C)COD")
    iiiiiinput = input("Please choose a method to make the final payment from above options")
    x = "UPI"
    y = "CARD"
    z = "COD"
    if (iiiiiinput == x or y or z):print(x, "thanks for choosing SWITO as your craving's partner !!\nHope you'll love our service !!")
    else:print("Please select a valid payment gateway !")
def toppings():
    print("If you wanna add some toppings or extra cheese please select from below options or else type 'CONTINUE' to go ahead with your previous order")
    print("-Cheese(25)      -Onion(15)      -Capsicum(15)\n-Corn(20)      -Mushroom(50)      -Paneer(40)")
print(x ,"what would you like to have ?\n(A) Indian Cuisine            (B)Italian Cuisine\n(C)Chinese Cuisine           (D)Mexican Cuisine")
iinput = input("Select between above choices available")
a = "Indian Cuisine"
b = "Italian Cuisine"
c = "Chinese Cuisine"
d = "Mexican Cuisine"
if(iinput==a):                                                  ################### INDIAN CUISINE
    print("What would you prefer in Indian Cuisine ?\n(A) Paneer Tikka              (B)Chicken Handi\n(C)Butter Chicken           (D)Veg Kolhapuri")
    iiinput = input("Select between above choices available within Indian Cuisine")
    aa = "Paneer Tikka"
    bb = "Chicken Handi"
    cc = "Butter Chicken"
    dd = "Veg Kolhapuri"
    if (iiinput == aa):                                         # PANEER TIKKA
        print("Please enter the quantity you would like to have ?\n(A) Half Plate(199)           (B)Full Plate(379)\n(C)Muliple Plates")
        iiiinput = input("Please select the quantity you require")
        aaa = "Half Plate"
        bbb = "Full Plate"
        ccc = "Multiple Plates"
        if (iiiinput == aaa):
            print("Why just Half Plate of delicious", iiinput)
            print("Get 4 tandoori rotis free on ordering a full plate of", iiinput)
            print("USE CODE : SWITOROTI\nOr else type (CONTINUE) to go ahead with your Half Plate of", iiinput)
            iiiiinput = input("Please type your desired order")
            aaaa = "SWITOROTI"
            bbbb = "CONTINUE"
            if (iiiiinput == aaaa):
                print("Congrats on getting 4 rotis free !!\nYour total payable bill is ---379---\nWe are sure you'll enjoy our Delicious", iiinput)
                payment()
            elif (iiiiinput == bbbb):
                print("Your total payable bill is ---199---\nWe are sure you'll enjoy our Delicious", iiinput)
                payment()
            else:print("Please select a correct option !!")
        elif (iiiinput == bbb):
            print("You have ordered a full plate of", iiinput)
            print(" Your total payable amount is 379")
            payment()
        elif (iiiinput == ccc):
            x = int(input("Please enter desired quantity"))
            total = x*199
            print(" Your total payable amount is", total)
            payment()
        else:print("Please choose a correct option")
    elif(iiinput == bb):                                          # CHICKEN HANDI
        print("Please enter the quantity you would like to have ?\n(A) Half Plate(400)           (B)Full Plate(750)\n(C)Muliple Plates")
        iiiinput = input("Please select the quantity you require")
        aaa = "Half Plate"
        bbb = "Full Plate"
        ccc = "Multiple Plates"
        if (iiiinput == aaa):
            print("Why just Half Plate of delicious", iiinput)
            print("Get 4 tandoori rotis free on ordering a full plate of", iiinput)
            print("USE CODE : SWITOROTI\nOr else type (CONTINUE) to go ahead with your Half Plate of", iiinput)
            iiiiinput = input("Please type your desired order")
            aaaa = "SWITOROTI"
            bbbb = "CONTINUE"
            if (iiiiinput == aaaa):
                print("Congrats on getting 4 rotis free !!\nYour total payable bill is ---450---\nWe are sure you'll enjoy our Delicious", iiinput)
                payment()
            elif (iiiiinput == bbbb):
                print("Your total payable bill is ---230---\nWe are sure you'll enjoy our Delicious", iiinput)
                payment()
            else:print("Please select a correct option !!")
        elif (iiiinput == bbb):
            print("You have ordered a full plate of", iiinput)
            print(" Your total payable amount is 450")
            payment()
        elif (iiiinput == ccc):
            x = int(input("Please enter desired quantity"))
            total = x*375
            print(" Your total payable amount is", total)
            payment()
        else:print("Please choose a correct option")
    elif (iiinput == cc):                                      # BUTTER CHICKEN
        print("Please enter the quantity you would like to have ?\n(A) Half Plate(380)           (B)Full Plate(700)\n(C)Muliple Plates")
        iiiinput = input("Please select the quantity you require")
        aaa = "Half Plate"
        bbb = "Full Plate"
        ccc = "Multiple Plates"
        if (iiiinput == aaa):
            print("Why just Half Plate of delicious", iiinput)
            print("Get 4 tandoori rotis free on ordering a full plate of", iiinput)
            print("USE CODE : SWITOROTI\nOr else type (CONTINUE) to go ahead with your Half Plate of", iiinput)
            iiiiinput = input("Please type your desired order")
            aaaa = "SWITOROTI"
            bbbb = "CONTINUE"
            if (iiiiinput == aaaa):
                print("Congrats on getting 4 rotis free !!\nYour total payable bill is ---450---\nWe are sure you'll enjoy our Delicious", iiinput)
                payment()
            elif (iiiiinput == bbbb):
                print("Your total payable bill is ---230---\nWe are sure you'll enjoy our Delicious", iiinput)
                payment()
            else:print("Please select a correct option !!")
        elif (iiiinput == bbb):
            print("You have ordered a full plate of", iiinput)
            print(" Your total payable amount is 450")
            payment()
        elif (iiiinput == ccc):
            x = int(input("Please enter desired quantity"))
            total = x * 350
            print(" Your total payable amount is", total)
            payment()
        else:print("Please choose a correct option")
    elif (iiinput == dd):                                      #VEG KOLHAPURI
        print("Please enter the quantity you would like to have ?\n(A) Half Plate(240)           (B)Full Plate(460)\n(C)Muliple Plates")
        iiiinput = input("Please select the quantity you require")
        aaa = "Half Plate"
        bbb = "Full Plate"
        ccc = "Multiple Plates"
        if (iiiinput == aaa):
            print("Why just Half Plate of delicious", iiinput)
            print("Get 4 tandoori rotis free on ordering a full plate of", iiinput)
            print("USE CODE : SWITOROTI\nOr else type (CONTINUE) to go ahead with your Half Plate of", iiinput)
            iiiiinput = input("Please type your desired order")
            aaaa = "SWITOROTI"
            bbbb = "CONTINUE"
            if (iiiiinput == aaaa):
                print("Congrats on getting 4 rotis free !!\nCongrats on getting 4 rotis free\nYour total payable bill is ---450---\nWe are sure you'll enjoy our Delicious", iiinput)
                payment()
            elif (iiiiinput == bbbb):
                print("Your total payable bill is ---230---\nWe are sure you'll enjoy our Delicious", iiinput)
                payment()
            else:print("Please select a correct option !!")
        elif (iiiinput == bbb):
            print("You have ordered a full plate of", iiinput)
            print(" Your total payable amount is 450")
            payment()
        elif (iiiinput == ccc):
            x = int(input("Please enter desired quantity"))
            total = x * 230
            print(" Your total payable amount is", total)
            payment()
        else:print("Please choose a correct option !!")
    else:print("Please choose a correct option !!")
elif(iinput == b):                                 ############### ITALIAN CUISINE
    print("What would you prefer in Italian Cuisine ?\n(A)Italian Pizza              (B)Lasagna\n(C)Spaghetti           (D)Ravioli")
    iiinput = input("Select between above choices available within Italian Cuisine")
    aa = "Italian Pizza"
    bb = "Lasagna"
    cc = "Spaghetti"
    dd = "Ravioli"
    if (iiinput == aa):                                                   # ITALIAN PIZZA
        print("Please enter the quantity you would like to have ?\n(A)Small(249)          (B)Medium(449)\n(C)Large(649)        (D)Multiple Pizzas")
        iiiinput = input("Please select the quantity you require")
        aaa = "Small"
        bbb = "Medium"
        ccc = "Large"
        ddd = "Multiple Pizzas"
        if (iiiinput == aaa):
            print("Why just a small sized", iiinput)
            print("Get free French Fries on ordering a large sized", iiinput)
            print("USE CODE : FFRIES\nOr else type (CONTINUE) to go ahead with your small sized", iiinput)
            iiiiinput = input("Please type your desired order")
            aaaa = "FFRIES"
            bbbb = "CONTINUE"
            if (iiiiinput == aaaa):
                print("Congrats on getting free French Fries !!")
                toppings()
                z = input("Enter your choice")
                if (z == Cheese):
                    print("Your total payable bill is ---674---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Onion):
                    print("Your total payable bill is ---664---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Capsicum):
                    print("Your total payable bill is ---664---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Corn):
                    print("Your total payable bill is ---669---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Mushroom):
                    print("Your total payable bill is ---699---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Paneer):
                    print("Your total payable bill is ---689---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == CONTINUE):
                    print("Your total payable bill is ---649---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                else:
                    print("Please select a correct option !!")
            elif (iiiiinput == bbbb):
                toppings()
                if (z == Cheese):
                    print("Your total payable bill is ---274---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Onion):
                    print("Your total payable bill is ---264---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Capsicum):
                    print("Your total payable bill is ---264---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Corn):
                    print("Your total payable bill is ---269---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Mushroom):
                    print("Your total payable bill is ---299---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Paneer):
                    print("Your total payable bill is ---289---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == CONTINUE):
                    print("Your total payable bill is ---249---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                else:print("Please select a correct option !!")
            else:print("Please select a correct option !!")
        elif (iiiinput == bbb):
            print("Why just a medium sized", iiinput)
            print("Get free Coke on ordering a large sized", iiinput)
            print("USE CODE : FREECOKE\nOr else type (CONTINUE) to go ahead with your medium sized", iiinput)
            iiiiinput = input("Please type your desired order")
            aaaa = "FREECOKE"
            bbbb = "CONTINUE"
            if (iiiiinput == aaaa):
                print("Congrats on getting free Coke !!")
                toppings()
                if (z == Cheese):
                    print("Your total payable bill is ---674---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Onion):
                    print("Your total payable bill is ---664---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Capsicum):
                    print("Your total payable bill is ---664---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Corn):
                    print("Your total payable bill is ---669---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Mushroom):
                    print("Your total payable bill is ---699---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Paneer):
                    print("Your total payable bill is ---689---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == CONTINUE):
                    print("Your total payable bill is ---649---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                else:print("Please select a correct option !!")
            elif (iiiiinput == bbbb):
                toppings()
                if (z == Cheese):
                    print("Your total payable bill is ---474---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Onion):
                    print("Your total payable bill is ---464---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Capsicum):
                    print("Your total payable bill is ---464---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Corn):
                    print("Your total payable bill is ---469---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Mushroom):
                    print("Your total payable bill is ---499---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == Paneer):
                    print("Your total payable bill is ---489---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                elif (z == CONTINUE):
                    print("Your total payable bill is ---449---\nWe are sure you'll enjoy our appetizing", iiinput)
                    payment()
                else:print("Please select a correct option !!")
            else:print("Please select a correct option !!")
        elif (iiiinput == ccc):
            print("You have ordered a large sized", iiinput)
            toppings()
            if (z == Cheese):
                print("Your total payable bill is ---674---\nWe are sure you'll enjoy our appetizing", iiinput)
                payment()
            elif (z == Onion):
                print("Your total payable bill is ---664---\nWe are sure you'll enjoy our appetizing", iiinput)
                payment()
            elif (z == Capsicum):
                print("Your total payable bill is ---664---\nWe are sure you'll enjoy our appetizing", iiinput)
                payment()
            elif (z == Corn):
                print("Your total payable bill is ---669---\nWe are sure you'll enjoy our appetizing", iiinput)
                payment()
            elif (z == Mushroom):
                print("Your total payable bill is ---699---\nWe are sure you'll enjoy our appetizing", iiinput)
                payment()
            elif (z == Paneer):
                print("Your total payable bill is ---689---\nWe are sure you'll enjoy our appetizing", iiinput)
                payment()
            elif (z == CONTINUE):
                print("Your total payable bill is ---649---\nWe are sure you'll enjoy our appetizing", iiinput)
                payment()
            else:print("Please select a correct option !!")
        elif (iiiinput == ddd):
            x = int(input("Please enter desired quantity"))
            total = x*249
            print("If you wanna add some toppings or extra cheese please select from below options or else type 'CONTINUE' to go ahead with your previous order")
            print("-Cheese(25)      -Onion(15)      -Capsicum(15)\n-Corn(20)      -Mushroom(50)      -Paneer(40)")
            z = input("Enter your choice")
            if (z == Cheese):
                p = (x*25)+total
                print("Your total payable bill is", p)
                print("We are sure you'll enjoy our appetizing", iiinput)
                payment()
            elif (z == Onion):
                p = (x * 15) +total
                print("Your total payable bill is", p)
                print("We are sure you'll enjoy our appetizing", iiinput)
                payment()
            elif (z == Capsicum):
                p = (x * 15) + total
                print("Your total payable bill is", p)
                print("We are sure you'll enjoy our appetizing", iiinput)
                payment()
            elif (z == Corn):
                p = (x * 20) + total
                print("Your total payable bill is", p)
                print("We are sure you'll enjoy our appetizing", iiinput)
                payment()
            elif (z == Mushroom):
                p = (x * 50) + total
                print("Your total payable bill is", p)
                print("We are sure you'll enjoy our appetizing", iiinput)
                payment()
            elif (z == Paneer):
                p = (x * 40) + total
                print("Your total payable bill is", p)
                print("We are sure you'll enjoy our appetizing", iiinput)
                payment()
            elif (z == CONTINUE):
                print("Your total payable bill is", total)
                print("We are sure you'll enjoy our appetizing", iiinput)
                payment()
            else:print("Please select a correct option !!")
        else:print("Please choose a correct option")
    elif (iiinput == bb):                                              # LASAGNA
        print("Please enter the quantity you would like to have ?\n(A) Half Plate(299)          (B)Full Plate(549)\n(C)Multiple Plates")
        iiiinput = input("Please select the quantity you require")
        aaa = "Half Plate"
        bbb = "Full Plate"
        ccc = "Multiple Plates"
        if (iiiinput == aaa):
            print("You have ordered a half plate of flavourful", iiinput)
            print(" Your total payable amount is 299")
            payment()
        elif (iiiinput == bbb):
            print("You have ordered a full plate of flavourful", iiinput)
            print(" Your total payable amount is 549")
            payment()
        elif (iiiinput == ccc):
            x = int(input("Please enter desired quantity"))
            total = x*299
            print(" Your total payable amount is", total)
            payment()
        else:print("Please choose a correct option")
    elif (iiinput == cc):                                         #SPAGHETTI
        print("Please enter the quantity you would like to have ?\n(A) Half Plate(199)          (B)Full Plate(389)\n(C)Multiple Plates")
        iiiinput = input("Please select the quantity you require")
        aaa = "Half Plate"
        bbb = "Full Plate"
        ccc = "Multiple Plates"
        if (iiiinput == aaa):
            print("You have ordered a half plate of delicious", iiinput)
            print(" Your total payable amount is 199")
            payment()
        elif (iiiinput == bbb):
            print("You have ordered a full plate of flavourful", iiinput)
            print(" Your total payable amount is 389")
            payment()
        elif (iiiinput == ccc):
            x = int(input("Please enter desired quantity"))
            total = x*199
            print(" Your total payable amount is", total)
            payment()
        else:print("Please choose a correct option")
    elif (iiinput == dd):                                     #RAVIOLI
        print("Please enter the quantity you would like to have ?\n(A) Half Plate(329)          (B)Full Plate(649)\n(C)Multiple Plates")
        iiiinput = input("Please select the quantity you require")
        aaa = "Half Plate"
        bbb = "Full Plate"
        ccc = "Multiple Plates"
        if (iiiinput == aaa):
            print("You have ordered a half plate of delicious", iiinput)
            print(" Your total payable amount is 329")
            payment()
        elif (iiiinput == bbb):
            print("You have ordered a full plate of flavourful", iiinput)
            print(" Your total payable amount is 649")
            payment()
        elif (iiiinput == ccc):
            x = int(input("Please enter desired quantity"))
            total = x*329
            print(" Your total payable amount is", total)
            payment()
        else:print("Please choose a correct option")
    else:print("Please choose a correct option")
elif(iinput == c):                                 ############### CHINESE CUISINE
    print("What would you prefer in Italian Cuisine ?\n(A)Noodles              (B)Manchurian\n(C)Spring Rolls           (D)Tofu")
    iiinput = input("Select between above choices available within Chinese Cuisine")
    aa = "Noodles"
    bb = "Manchurian"
    cc = "Spring Rolls"
    dd = "Tofu"
    if (iiinput == aa):                                   # NOODLES
        print("Please enter the quantity you would like to have ?\n(A) Half Plate(130)           (B)Full Plate(250)\n(C)Muliple Plates")
        iiiinput = input("Please select the quantity you require")
        aaa = "Half Plate"
        bbb = "Full Plate"
        ccc = "Multiple Plates"
        if (iiiinput == aaa):
            print("Why just Half Plate of delicious", iiinput)
            print("Get extra schezwan chutney on ordering a full plate of", iiinput)
            print("USE CODE : SCHEZWAN\nOr else type (CONTINUE) to go ahead with your Half Plate of", iiinput)
            iiiiinput = input("Please type your desired order")
            aaaa = "SCHEZWAN"
            bbbb = "CONTINUE"
            if (iiiiinput == aaaa):
                print("Congrats on getting free extra schezwan chutney !!\nYour total payable bill is ---250---\nWe are sure you'll enjoy our Delicious", iiinput)
                payment()
            elif (iiiiinput == bbbb):
                print("Your total payable bill is ---130---\nWe are sure you'll enjoy our Delicious", iiinput)
                payment()
            else:
                print("Please select a correct option !!")
        elif (iiiinput == bbb):
            print("You have ordered a full plate of", iiinput)
            print(" Your total payable amount is 250")
            payment()
        elif (iiiinput == ccc):
            x = int(input("Please enter desired quantity"))
            total = x * 130
            print(" Your total payable amount is", total)
            payment()
        else:
            print("Please choose a correct option")
    elif (iiinput == bb):                                            # MANCHURIAN
        print("Please enter the quantity you would like to have ?\n(A) Half Plate(140)          (B)Full Plate(270)\n(C)Multiple Plates")
        iiiinput = input("Please select the quantity you require")
        aaa = "Half Plate"
        bbb = "Full Plate"
        ccc = "Multiple Plates"
        if (iiiinput == aaa):
            print("You have ordered a half plate of spicy", iiinput)
            print(" Your total payable amount is 140")
            payment()
        elif (iiiinput == bbb):
            print("You have ordered a full plate of spicy", iiinput)
            print(" Your total payable amount is 270")
            payment()
        elif (iiiinput == ccc):
            x = int(input("Please enter desired quantity"))
            total = x*140
            print(" Your total payable amount is", total)
            payment()
        else:print("Please choose a correct option")
    elif (iiinput == cc):                                         # SPRING ROLL
        print("Please enter the quantity you would like to have ?\n(A) Half Plate(110)          (B)Full Plate(200)\n(C)Multiple Plates")
        iiiinput = input("Please select the quantity you require")
        aaa = "Half Plate"
        bbb = "Full Plate"
        ccc = "Multiple Plates"
        if (iiiinput == aaa):
            print("You have ordered a half plate of mouth-watering", iiinput)
            print(" Your total payable amount is 110")
            payment()
        elif (iiiinput == bbb):
            print("You have ordered a full plate of flavourful", iiinput)
            print(" Your total payable amount is 200")
            payment()
        elif (iiiinput == ccc):
            x = int(input("Please enter desired quantity"))
            total = x*110
            print(" Your total payable amount is", total)
            payment()
        else:print("Please choose a correct option")
    elif (iiinput == dd):                                            # TOFU
        print("Please enter the quantity you would like to have ?\n(A) Half Plate(199)          (B)Full Plate(389)\n(C)Multiple Plates")
        iiiinput = input("Please select the quantity you require")
        aaa = "Half Plate"
        bbb = "Full Plate"
        ccc = "Multiple Plates"
        if (iiiinput == aaa):
            print("You have ordered a half plate of delicious", iiinput)
            print(" Your total payable amount is 199")
            payment()
        elif (iiiinput == bbb):
            print("You have ordered a full plate of flavourful", iiinput)
            print(" Your total payable amount is 389")
            payment()
        elif (iiiinput == ccc):
            x = int(input("Please enter desired quantity"))
            total = x*199
            print(" Your total payable amount is", total)
            payment()
        else:print("Please choose a correct option")
    else:print("Please choose a correct option")
elif(iinput == d):                                 ############### MEXICAN CUISINE
    print("What would you prefer in Italian Cuisine ?\n(A)Burritos              (B)Salsa\n(C)Fajitas           (D)Lomo Saltado")
    iiinput = input("Select between above choices available within Mexican Cuisine")
    aa = "Burritos"
    bb = "Salsa"
    cc = "Fajitas"
    dd = "Lomo Saltado"
    if (iiinput == aa):                                        # BURRITOS
        print("Please enter the quantity you would like to have ?\n(A) Half Plate(259)           (B)Full Plate(499)\n(C)Muliple Plates")
        iiiinput = input("Please select the quantity you require")
        aaa = "Half Plate"
        bbb = "Full Plate"
        ccc = "Multiple Plates"
        if (iiiinput == aaa):
            print("Why just Half Plate of Finger-licking", iiinput)
            print("Get free sauce on ordering a full plate of", iiinput)
            print("USE CODE : SAUCEBUR\nOr else type (CONTINUE) to go ahead with your Half Plate of", iiinput)
            iiiiinput = input("Please type your desired order")
            aaaa = "SAUCEBUR"
            bbbb = "CONTINUE"
            if (iiiiinput == aaaa):
                print("Congrats on getting free sauce !!\nYour total payable bill is ---259---\nWe are sure you'll enjoy our Finger-licking", iiinput)
                payment()
            elif (iiiiinput == bbbb):
                print("Your total payable bill is ---499---\nWe are sure you'll enjoy our Finger-licking", iiinput)
                payment()
            else:
                print("Please select a correct option !!")
        elif (iiiinput == bbb):
            print("You have ordered a full plate of", iiinput)
            print(" Your total payable amount is 499")
            payment()
        elif (iiiinput == ccc):
            x = int(input("Please enter desired quantity"))
            total = x * 259
            print(" Your total payable amount is", total)
            payment()
        else:
            print("Please choose a correct option")
    elif (iiinput == bb):                                             # SALSA
        print("Please enter the quantity you would like to have ?\n(A) Half Plate(179)          (B)Full Plate(349)\n(C)Multiple Plates")
        iiiinput = input("Please select the quantity you require")
        aaa = "Half Plate"
        bbb = "Full Plate"
        ccc = "Multiple Plates"
        if (iiiinput == aaa):
            print("You have ordered a half plate of sizzling", iiinput)
            print(" Your total payable amount is 179")
            payment()
        elif (iiiinput == bbb):
            print("You have ordered a full plate of spicy", iiinput)
            print(" Your total payable amount is 349")
            payment()
        elif (iiiinput == ccc):
            x = int(input("Please enter desired quantity"))
            total = x*179
            print(" Your total payable amount is", total)
            payment()
        else:print("Please choose a correct option")
    elif (iiinput == cc):                                            # SPRING ROLL
        print("Please enter the quantity you would like to have ?\n(A) Half Plate(110)          (B)Full Plate(200)\n(C)Multiple Plates")
        iiiinput = input("Please select the quantity you require")
        aaa = "Half Plate"
        bbb = "Full Plate"
        ccc = "Multiple Plates"
        if (iiiinput == aaa):
            print("You have ordered a half plate of crunchy", iiinput)
            print(" Your total payable amount is 110")
            payment()
        elif (iiiinput == bbb):
            print("You have ordered a full plate of flavourful", iiinput)
            print(" Your total payable amount is 200")
            payment()
        elif (iiiinput == ccc):
            x = int(input("Please enter desired quantity"))
            total = x*110
            print(" Your total payable amount is", total)
            payment()
        else:print("Please choose a correct option")
    elif (iiinput == dd):                                        # TOFU
        print("Please enter the quantity you would like to have ?\n(A) Half Plate(199)          (B)Full Plate(389)\n(C)Multiple Plates")
        iiiinput = input("Please select the quantity you require")
        aaa = "Half Plate"
        bbb = "Full Plate"
        ccc = "Multiple Plates"
        if (iiiinput == aaa):
            print("You have ordered a half plate of delicious", iiinput)
            print(" Your total payable amount is 199")
            payment()
        elif (iiiinput == bbb):
            print("You have ordered a full plate of flavourful", iiinput)
            print(" Your total payable amount is 389")
            payment()
        elif (iiiinput == ccc):
            x = int(input("Please enter desired quantity"))
            total = x*199
            print(" Your total payable amount is", total)
            payment()
        else:print("Please choose a correct option")
    else:print("Please choose a correct option")
else:print("Please choose a correct option !!")
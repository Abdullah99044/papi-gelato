#Functions

def sorryFunction():
    print(".........................")
    print("Sorry dat snap ik niet...")
    print(".........................")

def stap_3_Function(n , y ):
    print("Hier is uw " , y , " met " , n , "bolletje(s)" )

def eindeFunction():
    print("Wilt u nog meer bestellen?")
    while True: 
        answer = input("(Y/N) :")  
        if answer == "Y" :
            print("....................")
            print("Terug naar het begin")
            programFunction()  
        elif answer == "N" :
            print("Bedankt en tot ziens!") 
            return  
        else :
            sorryFunction()      

def smakenFuction(x):
    z = 1
    for i in range(x):
        while True:
            print("Welke smaak wilt u voor bolletje nummer?" , z)
            print("A) Aardbei")
            print("C) Chocolade")
            print("M) Munt")
            print("V) Vanille?")
            k = input("A , C , M , OF V ? : ")
            if k == "A" or "C" or "M" or "V" :
                z += 1
                break
            else:
                print("Sorry dat snap ik niet...")

def bonenFunction(x , y , z , i , n , c):
    r1 = x * 1.10
    r2 = y * 1.25
    r3 = z * 0.75
    r4 = i * 1
    total = r1 + r2 + r3 + i
    if c == "C" and i > 0.3 :
        n = x
    print("----------[Papi Gelato]----------")
    print("Bolletjes  ", x , " x " " € 1,10   =","€",r1)
    print("Horrentjes ", y , " x " " € 1,25   =","€",r2 )
    print("Bakjes     ", z , " x " " € 0,75   =","€",r3)
    print("Topping    ", n , " x " ,"€",i , "   =","€",r4 )
    print("                          ----- +")
    print("Total                    =", "€", total)

def toppingFunction(i , n , A):
    if  A == "A" :
        return 0
    elif A == "B" :
        return 0.5
    elif A == "C" :
        return 0.3 * n 
    elif A == "D" and i == 2:
        return 0.9
    elif A == "D" and i == 1:
        return 0.6
    
def toppingFunction1():
    print("Wat voor topping wilt u: ")
    print(" A) Geen ")
    print(" B) Slagroom" )
    print(" C) Sprinkels ( prijs x aantal bolletjes ")
    print(" D) Caramel Saus ")

def knopF():
    a = input("Druk op een knop om terug te gaan naar het begin")

def programFunction():
    while True:
        print(".........................")
        answer = int(input("Hoeveel bolletjes wilt u? : "))
        print(".........................")
        if answer <= 4 :
            smakenFuction(answer)
            print("Wilt u deze " , answer , " bolletje(s) in")
            print("A) een hoorntje? ")
            print("B) of een bakje?")
            while True:
                answer1 = input("A/B")
                if answer1 == "A":
                    stap_3_Function(answer , "hoorntje") 
                    if answer != 0: 
                        toppingFunction1()
                        answer2 = input(" : ")
                        bonenFunction(answer , 1 , 0 , toppingFunction(1 , answer , answer2), 1 , answer2)
                    eindeFunction()
                    break          
                elif answer1 == "B":
                    stap_3_Function(answer , "bakje")
                    if answer != 0: 
                        toppingFunction1()
                        answer2 = input(" : ")
                        bonenFunction(answer , 0 , 1 , toppingFunction(2, answer , answer2) , 1  , answer2 )
                    eindeFunction()
                    break
                else:
                    sorryFunction()
            break
        elif answer > 4 and answer <= 8:
            print("..........................................................")
            print("Dan krijgt u van mij een bakje met " , answer , "bolletjes")
            smakenFuction(answer)
            if answer != 0: 
                toppingFunction1()
                answer2 = input(" : ")
                bonenFunction(answer , 0 , 1 , toppingFunction(2, answer , answer2) , 1  , answer2 )
            eindeFunction()
            break
        elif answer > 8:
                print("........................................")
                print("Sorry, zulke grote bakken hebben we niet")
                print("........................................")
                knopF()
        else :
            sorryFunction()
            knopF()

#Programma

print("................................................................................")
print("Welkom bij Papi Gelato")
print("................................................................................")
next = input("druk op een knop om door te gaan")
programFunction()







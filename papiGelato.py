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

def bonenFunction(x , y , z):
    r1 = x * 1.10
    r2 = y * 1.25
    r3 = z * 0.75
    total = r1 + r2 + r3
    print("----------[Papi Gelato]----------")
    print("Bolletjes  ", x , " x " " €1,10   =", r1)
    print("Horrentjes ", y , " x " " €1,25   =", r2 )
    print("Bakjes     ", z , " x " " €0,75   =", r3)
    print("                          ----- +")
    print("Total                    =", total)



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
                        bonenFunction(answer , 1 , 0)
                    eindeFunction()
                    break          
                elif answer1 == "B":
                    stap_3_Function(answer , "bakje")
                    if answer != 0: 
                        bonenFunction(answer , 1 , 0)
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
                bonenFunction(answer , 1 , 0)
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







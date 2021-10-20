
#Functions

def sorryFunction():
    print(".........................")
    print("Sorry dat snap ik niet...")
    print(".........................")
def stap_3_Function(n , y):
    print("Hier is uw " , y , " met " , n , "bolletje(s)" )
    print("Wilt u nog meer bestellen?")
    while True: 
        answer = input("(Y/N) :")  
        if answer == "Y" :
            print("....................")
            print("Terug naar het begin")
            programFunction()  
        elif answer == "N" :
            print("Bedankt en tot ziens!") 
            break  
        else :
            sorryFunction()        
def knopF():
    a = input("Druk op een knop om terug te gaan naar het begin")
def programFunction():
    while True:
        print(".........................")
        answer = int(input("Hoeveel bolletjes wilt u? : "))
        print(".........................")
        if answer <= 4 :
            print("Wilt u deze " , answer , " bolletje(s) in")
            print("A) een hoorntje? ")
            print("B) of een bakje?")
            while True:
                answer1 = input("A/B")
                if answer1 == "A":
                    stap_3_Function(answer , "hoorntje")  
                    break          
                elif answer1 == "B":
                    stap_3_Function(answer , "bakje")
                    break
                else:
                    sorryFunction()
            break
        elif answer > 4 and answer <= 8:
            print("..........................................................")
            print("Dan krijgt u van mij een bakje met " , answer , "bolletjes")
            print("..........................................................")
            stap_3_Function(answer , "bolletjes" )
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
print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is")
print("................................................................................")
next = input("druk op een knop om door te gaan")
programFunction()







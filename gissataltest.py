import random
import os
os.system('cls')
a=True
b=True

while b==True:
    os.system('cls')
    print(f"\nDu ska gissa talet, det kan vara vad som hälst från 1 - 100 \n\nDu kan alltid avluta spelet mitt i om du skriver något nummer som inte är mellan 1-100\n\nDu får 7 försök på dig\n")
    number=random.randint(1,100)
    guesses=7
    while guesses>0:
        try:
            guess=int(input("Din gissning!: "))
            if guess==number:
                guesses-=1
                print(f"Du gissa rätt på {7-guesses} försök\n")
                again=input("Vill du spela igen? j/n: ").lower()
                if again=="n" or again=="nej":
                    b=False
                    print("\nHejdå")
                    quit()
                else:
                    break
            elif guess<0 or guess>100:
                print("\nHejdå!")
                quit()
            elif guesses==1:
                print("Du har tyvärr fått slut på försök")
                again=input("Vill du spela igen? j/n: ").lower()
                if again=="n" or again=="nej":
                    b=False
                    print("\nHejdå")
                    quit()
                else:
                    break
            elif guess>number:
                guesses-=1
                print(f"Du gissade för högt \nDu har {guesses} gissningar kvar\n")
            elif guess<number:
                guesses-=1
                print(f"Du gissade för lågt \nDu har {guesses} gissningar kvar\n")
        except ValueError:
            print(f"Snälla använd nummer och inget annat :p \n")
import random
print(f"Du ska gissa talet, det kan vara vad som hälst från 1 - 100 \nDu får 7 försök på dig")
number=random.randint(1,100)
print(number)
a=True
guesses=7
while guesses>0:
    try:
        guess=int(input("Din gissning!: "))
        if guess==number:
            guesses-=1
            print(f"Du gissa rätt på ditt {7-guesses} försök\n")
            break
        elif guesses==1:
            print("Du har tyvärr fått slut på försök")
            break
        elif guess>number:
            guesses-=1
            print(f"Du gissade för högt \nDu har {guesses} gissningar kvar\n")
        elif guess<number:
            guesses-=1
            print(f"Du gissade för lågt \nDu har {guesses} gissningar kvar\n")
    except ValueError:
        print(f"Snälla använd nummer och inget annat :p \n")
    
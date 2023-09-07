import random
print("Du ska gissa talet, det kan vara vad som hälst från 1 - 100   Du får 7 försök på dig")
tal=random.randint(1,100)
print(tal)

totalg=1
igen=True
while igen:
        try:
            gissning=int(input("Gissa talet: "))
        except:
            print("Fel, Du måste ha ett heltal, inga bokstäver eller decimaltal ")

        if totalg==7:
            igen=False
        elif gissning==tal:
            print("Du gissade rätt efter ",totalg," gissningar")
            totalg=totalg+1
            igen2=input("Svara ja om du vill fortsätta och nej om du inte vill: ").lower()
            if igen2=="ja":
                igen=True
            elif igen2=="nej":
                igen=False
            totalg=1
            tal=random.randint(1,100)
            print(tal)
        elif gissning<tal:
            print("Du måste gå högre!")
            totalg=totalg+1
        elif int(gissning>tal):
            print("Du måste gå lägre!")
            totalg=totalg+1

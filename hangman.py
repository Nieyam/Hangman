# print("bitch") 

random = input("Random woord: ")
fouten = 0
gebruikt = []
goed = []

start = True

while start:
    letter = input("Kies een letter: ")

    if letter in gebruikt:
        print("Al gebruikt")
    else:
        gebruikt.append(letter)

        kaas = letter in random 
        if kaas == False:
            fouten = fouten + 1
        else:
            goed.append(letter)

        if fouten > 8:
            print("Game over.. try again")
            break;

        print(goed)
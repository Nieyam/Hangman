# print("bitch") 

random = input("Random woord: ")
fouten = 0
gebruikt = []

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

        if fouten > 8:
            print("Game over.. try again")
            break;
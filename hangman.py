# print("bitch") 

random = input("Random woord: ")
fouten = 0
gebruikt = []
goed = []
for index in random:
    goed += "_"

while True:
    letter = input("Kies een letter: ") #let op spaties

    if letter in gebruikt:
        print("Al gebruikt")
    else:
        gebruikt.append(letter)

        kaas = letter in random 
        if kaas == False:
            fouten = fouten + 1
        else:
            for index in range(len(random)):
                if random[index] == letter:
                    goed[index] = letter

        if fouten > 8:
            print("Game over.. try again")
            break;

        geraden = ''.join(goed)
        if (geraden == random):
            print("Goedzo bitch")
            break;

        print(goed)
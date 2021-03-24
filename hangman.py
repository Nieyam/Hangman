# print("bitch") 

random = input("Random woord: ")
# print(random)
start = True

while start: #maak je een while loop, zo kan je letters blijven raden
    letters = input("Kies een letter: ")
    kaas = letters in random #boolean, komt true/false uit

    print(kaas)

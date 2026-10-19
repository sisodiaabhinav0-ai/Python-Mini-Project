import random
com = random.randint(1,100)
tries = 0


while True:
    tries +=1
    hum =int(input("Guess your number between 1-100:- "))
    if hum==com:
        print(f"Yayy you won the game in { tries} tries!")
        break
    elif hum>com:
        print("Wrong guess go lower!")
    elif hum<com:
        print("Wrong guess go higher!")


#this is just for git
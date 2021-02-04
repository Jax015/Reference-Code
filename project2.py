##class Weapon:
    #def __init__(self, damage, speed):
        #self.damage = damage
        #self.speed = speed

#class Axe(weapon):
    #def __init__(self, damage, speed):
        #super().__init__(10)

#class Bow(weapon):
    #def __init__(self, damage, speed):
        #super().__init__(8)

#class Sword(weapon):
    #def __init__(self, damage, speed):
        #super().__init__(13)

#class







def deathMessage():
    print("You have died!")
def start():
    print("You come across a path split in two. Which way will you go?")
    while True:
        playerinput = input("Right or left? > ").lower()
        if playerinput == "right":
            path1()
            break
        elif playerinput == "left":
            path2()
            break
        else:
            print("Invalid input!")
def path1():
    deathMessage()                 #DEATH MESSAGE
    print("Would you like to retry?")
    while True:
        playerinput = input("Yes or No? > ")
        if playerinput == "Yes".lower():
            start()
        elif playerinput == "No".lower():
            print("Thank you for playing!")
            break
        else:
            print("Invalid Input!")

def path2():
    print("You come across a room with two doors. Which shall you choose?")
    while True:
        playerinput = input("Door (1) or Door (2)? > ")
        if playerinput == "1":
            print("Oh no! a horrible beast appears.")
            deathMessage()                       #DEATH MESSAGE
            print("Would you like to retry?")
            while True:
                playerinput = input("Yes or No? > ").lower()
                if playerinput == "Yes".lower():
                    start()
                elif playerinput == "No".lower():
                    print("Thank you for playing!")
            else:
                print("Invalid Input!")
                break

        elif playerinput == "2":
            print("You have chosen wisely.")
            path3()
            break

def path3():
    print("Ahead of you is a fair maiden. Will you help her?")
    while True:
        playerinput = input("Yes or No > ")
        if playerinput == "Yes".lower():
            print("The kind lady gives you 1000 Gold.")
            path4()
            break
        elif playerinput == "No".lower():
             print("Now you will never know what she had to offer...")
             path4()
             break
        else:
             print("Invalid input!")

def path4():
    print("Stop")


print("Hello! Thank you for choosing to play my game!\n")
print("Hello Adventurer!")
readerName = input("What is your name?")

print("Hello " + readerName)
#Alternatively, print(f"Hello {readerName}")
#https://realpython.com/python-f-strings/

print("Are you ready for your journey?")
while True:
    playerinput = input("Yes or No > ").lower()
    if playerinput == "yes":
        start()
        break
    else:
        print("That's not the attitude!")

input() #Prevent exit

import random
class ganger:
    health = 10
class CorpoSolider:
    health = 25
class playerChoom:
    health = 100

inventory = []
armor = {"head": None, "chest": None, "legs": None, "feet": None, "weapon": None}
implants = {"head": None, "chest": None, "legs": None, "feet": None, "weapon": None}
maxSize = 10
hp = 100
eddies = 400
ganger_health = 10
Arasaka_health = 25
#Working HP system. Only
def main():
    global inventory, armor, hp, ganger_health, Arasaka_health, eddies
    GAME = True
    playerStatus = "alive"

    print(
        "You awaken in your apartment in Night City, leaving it you look outside the atrium of your Megabuilding, your job today is to find \n an engram by tonight,where do you go? What do you start the day with?")

    pChoice = input()

    while GAME:

        if pChoice[0].lower() == "n":
            print("You move down the street towards the north.")
        elif pChoice == "J":
            jobTime = True
            while jobTime == True:
                eddies += 1000
                print("Here's your payment for the day. But I got another thing for you to do, fight this local asshole who is \n disturbing my boys.")
                pChoice = input("If you kill this fool who keeps disturbing my biz, Go kill that fool.Y/N?")
                if pChoice == "Y":
                    print("Alright. Go get that guy.")
                    while ganger_health == 0:
                            Inventory("stack of eddies")
                            print("Thanks for doing this job, heres ya eddies. Gig closed. See you another time choombatta.")
                            break
                    break
                if pChoice == "N":
                        print("Well thats a damn shame...")
                        continue
        elif pChoice == "Chrome":
                chromeShop = True
                while chromeShop == True:
                    pChoice = input("Welcome to the Ripperdoc, What Implants do you want? \n I got Gorilla Arms \n Reinforced Tendons for jumping \n Reinforced Skin \n Sandivestan \n Arasaka Cyberdeck \n If you wanna leave, type L to leave.")
                    if pChoice == "Gorilla Arms":
                        if eddies >= 1000:
                            eddies -= 1000
                            implants["weapon"] = "Gorilla Arms"
                            print("You chrome up with Gorilla Arms!")
                        else:
                            print("Get out broke boy.")
                    elif pChoice == "Reinforced Tendons":
                        if eddies >= 1000:
                            eddies -= 1000
                            implants["feet"] = "Reinforced Tendons"
                            print("You chrome up with Reinforced Tendons! Now you can move faster, and double jump.")
                        else:
                            print("Get out broke boy.")
                    elif pChoice == "Sandivestan":
                        if eddies >= 1000:
                            eddies -= 1000
                            implants["head"] = "Sandivestan"
                            print("You chrome up with Sandivestan, kill some gangers in slow mo!")
                        else:
                            print("Get out broke boy.")
                    elif pChoice == "Cyberdeck":
                        implants["head"] = "Cyberdeck"
                        if eddies >= 1000:
                            eddies -= 1000
                            print("You chrome up with a cyberdeck, enjoy your netrunnin!")
                        else:
                            print("Get out broke boy.")
                    elif pChoice == "Skin":
                        if eddies >= 1000:
                            eddies -= 1000
                            implants["chest"] = "Reinforced Skin"
                            hp += 50
                            print("You chrome up with Reinforced Skin, you can take more damage!")
                        else:
                            print("Get out broke boy.")
                    if pChoice == "L":
                        print("Goodbye, enjoy ya chrome!")
                        chromeShop = False
                        continue
        elif pChoice == "Shop":
                genShop = True
                while genShop == True:
                    pChoice = input("Welcome to my little market. What you want? \n I got pistols \n rifles \n medkits \n clothes \n If you wanna leave, type L to leave.")
                    if pChoice == "pistol":
                        armor["weapon"] = "Lexington Pistol."
                        if eddies >= 500:
                            eddies -= 500
                            print("You get a pistol!")
                        else:
                            print("Why are you here if you got no money man?")
                    elif pChoice == "boots":
                        armor["feet"] = "titanium planted boots"
                        if eddies >= 100:
                            eddies -= 100
                            hp += 5
                            print("You get some boots.")
                        else:
                            print("Why are you here if you got no money man?")
                    elif pChoice == "Noriki Rifle":
                        armor["weapon"] = "Noriki Rifle"
                        if eddies >= 800:
                            eddies -= 800
                            print("You get a Noriki Rifle, enjoy.")
                        else:
                            print("Why are you here if you got no money man?")
                    elif pChoice == "medkit":
                        if eddies >= 100:
                            eddies -= 100
                            inventory= "medkit"
                            hp += 100
                            print("You get a medkit, heal up!")
                        else:
                            print("Why are you here if you got no money man?")
                    elif pChoice == "jacket":
                        if eddies >= 650:
                            eddies -= 650
                            armor["chest"] = "bulletweave jacket."
                            hp += 10
                            print("You get a nice bulletproof jacket, you can take more damage!")
                        else:
                            print("Why are you here if you got no money man?")
                    if pChoice == "L":
                        print("Goodbye, don't come back.")
                        genShop = False
                        continue
        elif pChoice[0].lower() == "e":
            print("You move down the street towards the east.")
        elif pChoice[0].lower() == "w":
            print("You move down the street towards the west.")
        elif pChoice[0].lower() == "h":
            print(hp)
        elif pChoice[0].lower() == "m":
            print(eddies)
        elif pChoice[0].lower() == "s":
            if "the engram" in inventory:
                print("You find the engram and escape with your life back home!")
                GameWin()
            else:
                print("You cannot leave the streets yet, find that engram to pay your fixer.")
        elif pChoice == "QUIT":
            GAME = False
        elif pChoice == "I":
            print("You are holding", inventory)
            print("You are wearing", armor.items())
        elif pChoice == "C":
            print("Your implants are:", implants)
        else:
            print("You need to move on from this street")

        diceRoll = random.random() * 100
        diceaAtRoll = random.random() * 20
        if diceRoll == 6:
            print("A netrunner short circuits your cyberware, thus causing a heart attack and you die.")
            playerStatus = "dead"
            GAME = False
        elif diceRoll <= 10:
            print("You find a dull katana.")
            pChoice = input("Equip katana? Y/N ")
            if pChoice == "Y":
                armor["weapon"] = "dull katana."
            else:
                Inventory("dull katana")
        elif diceRoll <= 15:
            print("You find a bulletweave Jacket.")
            pChoice = input("Equip bulletweave? Y/N ")
            if pChoice == "Y":
                armor["chest"] = "bulletweave jacket."
                hp += 10
            else:
                Inventory("bulletweave jacket")
        elif diceRoll <= 25:
            print("You found a Lexington Pistol")
            pChoice = input("Equip Pistol? Y/N ")
            if pChoice == "Y":
                armor["weapon"] = "Lexington Pistol."
            else:
                Inventory("Lexington Pistol")
            Inventory("'Lexington Pistol': {'attack': 2, 'defense': 1, 'cool': {'style':0, 'clout': 0, 'flex':1}}")
        elif diceRoll <= 30:
            print("You find some eddies! Lucky you!")
            eddies += random.randint(10, 500)
        elif diceRoll <= 35:
            print("You find a pair of titanium planted boots.")
            pChoice = input("Equip You find a pair of titanium planted boots? Y/N ")
            if pChoice == "Y":
                armor["feet"] = "titanium planted boots."
                hp += 5
            else:
                Inventory("titanium planted boots")
        elif diceRoll <= 40:
            print("You found a Ganger, the man comes to you and says 'Looking to die today Choom?'")
            pChoice = input("Fight this ganger? Y/N ")
            if pChoice == "Y":
                print("You start a firefight with the ganger.")
                gangerFirefight = True
                while gangerFirefight == True:
                    pChoice = input("Your options are: Run, or Fight. F for Fight, R for Run")
                    if pChoice == "F":
                        if "Lexington Pistol" or "Gorilla Arms" or "dull katana" in armor or implants or inventory:
                            print("You begin a fight with the Ganger!")
                            while hp > 0 and ganger_health > 0:
                                pChoice = input("Keep fighting!")
                                if pChoice == "F":
                                    if diceaAtRoll <= 15:
                                        ganger_health -= random.randint(5, 10)
                                        ganger_attack = random.choice([True])
                                        if ganger_attack == True:
                                            hp -= random.randint(10, 15)
                        if pChoice == "GHP":
                            print(ganger_health)
                        if Arasaka_health == 0:
                            eddies += random.randint(500, 2500)
                            print("You killed the Ganger!")
                            gangerFirefight = False
                            break
                else:
                    print("The Ganger shoots you in the arm, take 5 damage.")
                    Ganger_attack = random.choice([True])
                    if Ganger_attack == True:
                        hp -= random.randint(5, 10)
                        if hp == 0:
                            GAME = False
            if pChoice == "N":
                print("You run off from the ganger.")
        elif diceRoll <= 65:
            print("You found a Arasaka Patrol, a man comes to you and says 'This is Arasaka Business. Fuck off rat.'")
            pChoice = input("Fight the Agent? Y/N ")
            if pChoice == "Y":
                print("You start a firefight with the Agent.")
                arasakaFirefight = True
                while arasakaFirefight == True:
                            pChoice = input("Your options are: Run, or Fight. F for Fight, R for Run, AHP for opponent Health")
                            if pChoice == "F":
                                Arasaka_health == 20
                                if "Lexington Pistol" or "Gorilla Arms" or "dull katana" in armor or implants or inventory:
                                    print("You begin fighting at the Arasaka Agent!")
                                    while hp>0 and Arasaka_health>0:
                                        pChoice = input("Keep fighting!")
                                        if pChoice == "F":
                                            if diceaAtRoll <= 15:
                                                Arasaka_health -= random.randint(5, 10)
                                                Arasaka_attack = random.choice([True])
                                                if Arasaka_attack == True:
                                                    hp -= random.randint(10, 15)
                                if pChoice == "AHP":
                                        print(Arasaka_health)
                                if Arasaka_health == 0:
                                    eddies += random.randint(500, 2500)
                                    print("You killed the Agent!")
                                    arasakaFirefight = False
                                    break
                            if pChoice == "R":
                                arasakaFirefight = False
                                continue
                else:
                    print("The Arasaka Agent shoots you in the arm.")
                    Arasaka_attack = random.choice([True])
                    if Arasaka_attack == True:
                     hp -= random.randint(10, 15)
                    if hp == 0:
                        GAME = False
            if pChoice == "N":
                print("You run off from the patrol and continue moving.")
        elif diceRoll <= 70:
            print("You found an implant congrats!.")
            Inventory("Sandevistan")
        elif diceRoll <=15:
            print("You found the engram. Get off these streets. Type S to leave")
            Inventory("the engram")

        # print(diceRoll)

        pChoice = input(
            "You see streets to the north, south, east, and west. Where will you go? QUIT to leave the streets.")

    if GAME == False and playerStatus == "alive":
        print("The streets have calmed down, it seems you survived another day in Night City, you head home and get some sleep.\n\nGAME OVER")
    elif GAME == False and playerStatus == "dead":
        print("You are flatlined on the streets of Night City, and your corpse is added to the many collected by the Police \n Eventually ending up in a landfill.")


def GameWin():
    print("You got the engram! Congrats, heres your eddies choom")
    GAME = False


def Inventory(item):
    global inventory, maxSize

    if len(inventory) >= maxSize:
        print("You're inventory is too full. Replace item?")
        pChoice = input("Y/N ")
        if pChoice == "Y":
            i = 0
            while i < len(inventory):
                print("Replace this item?", inventory[i])
                pChoice = input("Y/N ")
                if pChoice == "Y":
                    inventory.insert(i, item)
                    # if you wanted to wear an item from inventory
                    # armor["chest"] = inventory.pop("dirty clothes")

                    # for using consumables
                    # inventory.remove("health potion")

                    # to swap something already in armor
                    # held = armor["weapon"]
                    # armor.update("weapon": "sword")
                    # Inventory(held)

                    # if inventory[i] == None:
                    #   inventory.insert(i, item)
                    break
                else:
                    i = i + 1
    else:
        inventory.append(item)


main()

import useractions
import pyinputplus 

class person:

    def __init__(self, name, health, armor, monney, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.monney = monney

    def showSelf(self):
        print("--------------------------------------")
        print(f"Name : {self.name}")
        print(f"Health : {self.health} PV")
        print(f"Stuff : {self.stuff}")
        print(f"Armor : {self.armor}")
        print(f"Monney : {self.monney} $")
        print("--------------------------------------")

    def attack(self, weapon, target):
        damages = int(weapon.damage - target.armor)
        target.health = target.health - damages
        print(self.name + "a attaqué" + target.name + "avec" + weapon.name + "lui infligeant" + str(damages) + "dégats.")


class monster(person):

    def appear(self):
        print(f"{self.name} à apparus")

class player(person):

    def buyFromMarket(self, itemToBuy):
        if self.monney < itemToBuy.price:
            print("Fonds insuffisant")
            return False
        else :
            self.monney = self.monney - itemToBuy.price
            print(f"{itemToBuy.name} acheté ! ( - {itemToBuy.price} )")
            return True


class item :
    def __inti__(self, name, price):
        self.name = name 
        self.price = price


class weapon(item):

    def __init__(self, name, damage, price):
        self.name = name 
        self.damage = damage
        self.price = price

    def showWeapon(self):
        print("--------------------------------------")
        print(f"Name : {self.name}")
        print(f"Damage : {self.damage}")
        print(f"Price : {self.Price} $")        
        print("--------------------------------------")

class armor(item):
    
    def __init__(self, name, armor, price):
        self.name = name 
        self.armor = armor
        self.price = price

    def showArmor(self):
        print("--------------------------------------")
        print(f"Name : {self.name}")
        print(f"Armor : {self.armor}")
        print(f"Price : {self.Price} $")        
        print("--------------------------------------")

class market:

    def __init__(self, weaponList, armorList):
        self.weaponList = weaponList
        self.armorList = armorList

    def showMarket(self, actualPlayer):

        weaponId = 0 
        armorId = 0
        print("<<--------------- MARKET --------------->>")
        print("WEAPONS :")
        for weapon in self.weaponList:
            print(f"[{weaponId}] | {weapon.name} | {weapon.damage} Damages | {weapon.price} $")
            print("_________________________________________________________")
            weaponId += 1
        print("ARMORS :")
        for armor in self.armorList:
            print(f"[{armorId}] | {armor.name} | {armor.armor} Armor | {armor.price} $")
            print("_________________________________________________________")
            armorId += 1
        self.sell(actualPlayer, armorId, weaponId)
        

    def sell(self, player, maxArmor, maxWeapon):

        weaponOrArmor = pyinputplus.inputMenu(["Weapons", "Armors"], numbered=True)

        if weaponOrArmor == "Weapons":
            
            print(self.weaponList)
            item = pyinputplus.inputMenu(list, numbered=True)

            player.buyFromMarket(item)

        else:
            item = input("Choose the id of the weapon you want to buy : ")
            while (int(item) >= maxWeapon) :
                print("Please enter a valid number")
                item = int(input("Choose the id of the weapon you want to buy : "))
            player.buyFromMarket(self.weaponList[int(item)])
     
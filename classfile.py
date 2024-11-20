import useractions


class person:

    def __init__(self, name, health, armor, monney):
        self.name = name
        self.health = health
        self.stuff = []
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
    
    def buyFromMarket(self, itemToBuy):
        pass

    def changeName():
        pass

class weapon:

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

class armor:
    
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

    def showMarket(self):

        weaponId = 0 
        armorId = 0
        print("<<--------------- MARKET --------------->>")
        for weapon in self.weaponList:
            print(f"[{MarketId}] | {weapon.name} | {weapon.damage} Damages | {weapon.price} $")
            print("_________________________________________________________")
            weaponId += 1
        for armor in self.armorList:
            print(f"[{MarketId}] | {armor.name} | {armor.armor} Armor | {armor.price} $")
            print("_________________________________________________________")
            armorId += 1

    def sell():
        pass


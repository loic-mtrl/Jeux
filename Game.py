import useractions
import classfile
import pyinputplus 

#class game:
   # def __init__(self, name="game"):
  #      self.name=name

  #  def play(self):

# WEAPONS
sword = classfile.weapon("Sword", 1004, 400)
sword1 = classfile.weapon("Sword1", 1040, 130)
sword2 = classfile.weapon("Sword2", 1200, 120)
sword3 = classfile.weapon("Sword3", 1400, 100)
sword4 = classfile.weapon("Sword4", 100, 10)
hands = classfile.weapon("hands", 10, 0)

weaponList = [sword, sword1, sword2, sword3, sword4]

# ARMOR
armor = classfile.armor("armor", 50, 280)
armor1 = classfile.armor("armor1", 70, 120)

armorList = [armor, armor1]

market = classfile.market(weaponList, armorList)

# PLAYERS
loic = classfile.player("loic", 500, 10, 100000000000, hands)
ery = classfile.monster("ery", 1000, 10, 100000000000, sword)


market.showMarket(loic)
        




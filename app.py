class Person:
    def __init__(self, name, health, stuff, armor):
        self.name = name
        self.health = health
        self.stuff = stuff
        self.armor = armor
    def attack(self, weapon, target):
        damages = weapon.damages - calculateArmor(target)
        target.health = target.health - damages
        return (self.name + "a attaqué" + target.name + "avec" + weapon.name + "lui infligeant" + damages + "dégats.")

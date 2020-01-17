import random
# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        self.kills = 0

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    #attack se hereda automaticamente

    def __repr__(self):
        s = "["+self.name+"] "+"HP: "+str(self.health)+" AT: "+str(self.strength)
        if self.kills > 0:
            s += " Kills: "+str(self.kills)
        return s

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if(self.health > 0):
            return self.name+" has received "+str(damage)+" points of damage"
        else:
            return self.name+" has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    #attack se hereda automaticamente
    def __repr__(self):
        s = "[a saxon] "+"HP: "+str(self.health)+" AT: "+str(self.strength)
        if self.kills > 0:
            s += " Kills: "+str(self.kills)
        return s

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if(self.health > 0):
            return "A Saxon has received "+str(damage)+" points of damage"
        else:
            return "A Saxon has died in combat"

# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def __repr__(self):
        s = "\n-----Standing battle members:-----\n"
        for i in self.vikingArmy:
            s += str(i) + '\n'
        print('\n')
        for j in self.saxonArmy:
            s += str(j) + '\n'
        #s= str(len(self.vikingArmy))+" vikings and "+str(len(self.saxonArmy))+" saxons"
        return s

    def addViking(self,viking):
        self.vikingArmy.append(viking)

    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        viki = random.randint(0,len(self.vikingArmy)-1)
        saxo = random.randint(0,len(self.saxonArmy)-1)
        resultado = self.saxonArmy[saxo].receiveDamage(self.vikingArmy[viki].attack())
        if(resultado[-1] == "t"):
            self.saxonArmy.remove(self.saxonArmy[saxo])
            self.vikingArmy[viki].kills += 1
        return resultado

    def saxonAttack(self):
        viki = random.randint(0,len(self.vikingArmy)-1)
        saxo = random.randint(0,len(self.saxonArmy)-1)
        resultado = self.vikingArmy[viki].receiveDamage(self.saxonArmy[saxo].attack())
        if(resultado[-1] == "t"):
            self.vikingArmy.remove(self.vikingArmy[viki])
            self.saxonArmy[saxo].kills += 1
        return resultado

    def showStatus(self):
        if(len(self.saxonArmy) == 0):
            return "Vikings have won the war of the century!"
        elif(len(self.vikingArmy) == 0):
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    
    def heroesOfWar(self):
        if(len(self.saxonArmy) != 0):
            print("This battle will be long remembered...")
        elif(len(self.vikingArmy) != 0):
            remain = self.vikingArmy[0]
            for i in self.vikingArmy:
                if remain.kills < i.kills:
                    remain = i
            print("This battle will always be remembered as THE BATTLE OF "+str.upper(remain.name)+"\n")
        else:
            print("---")
        

import random
player = {
 "name": "",
 "health": 100,
 "damage": 12,
 "armor": 1.5,
 "CritChanse": 20,
 "ShieldChanse": 20

}
enemy = {
 "name": "",
 "health": 100,
 "damage": 12,
 "armor": 1.2,
 "CritChanse": 20,
 "ShieldChanse": 20

}
def selectName(person):
    person["name"] = input("input player1 name ")

selectName(player)
selectName(enemy)
def Attack(attacker, defencer):
 if criticalHit(attacker) == True :
     boom = damageReduction(attacker, defencer)*2
 elif Shield(defencer) == True:
     boom = damageReduction(attacker, defencer)*0
 else:
     boom = damageReduction(attacker, defencer)
     
 defencer["health"] = defencer["health"] - boom
 print(attacker["name"]," hit", defencer["name"], " and  done ", boom, " damage" )
 print(defencer["health"], "remain health ", defencer["name"])
	
def damageReduction(attacker, defencer):
    hit = attacker["damage"] / defencer["armor"]
    return hit

def criticalHit(attacker):
    critical = random.random()*100
    if critical <= attacker["CritChanse"]:
        print ("Critical Hit!")
        return True
    else: return False
    
def Shield(defencer):
    chanse = random.random()*100
    if chanse <= defencer["ShieldChanse"]:
        print ("Shield Succesfull")
        return True
    else: return False

def usePotion(person):
    if person["potion"] > 0:
        person["health"] = person["health"] +30
    else: print("You have not a Potion")

def fight(attacker, defencer):
            while attacker["health"]>0 and defencer["health"] > 0:
                if attacker["health"]>0:
                    Attack(attacker, defencer)
                if defencer["health"]>0:
                    Attack(defencer, attacker)
                if AliveTest(attacker) == False:
                    print(defencer["name"], " win the battle")
                    break
                elif AliveTest(defencer) == False:
                    print(attacker["name"], " win the battle")
                    break
def AliveTest(person):
    if person["health"]<=0:
        print(person["name"]," is dead :(")
        person["status"]="dead"
        return False
    else: return True

fight(player,enemy)
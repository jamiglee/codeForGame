def getPosition(x, y):
    return {"x":x, "y":y}

def summonFriend(friendType):
    while self.costOf(friendType) < self.gold:
        self.summon(friendType)

def commandSoldier(friend):
    if friend.pos.x < 60:
        self.command(friend, "move", getPosition(friend.pos.x + 10, friend.pos.y))
    else if friend.pos.x < 80 and friend.pos.x >= 60:
        self.command(friend, "move", getPosition(friend.pos.x + 10, friend.pos.y + (36 - friend.pos.y)))
    else if friend.pos.x >= 100 and friend.pos.x < 250:
        attackEnemy(friend, findNearestEnemy(friend))

def commandArcher(friend):
    if self.now() > 2:
        if friend.pos.x < 90:
            self.command(friend, "move", getPosition(friend.pos.x + 5, 36))
            enemies = self.findEnemies()
            enemy = friend.findNearest(enemies)
            if enemy and enemy.type != "catapult":
                attackEnemy(friend, enemy)
        else if friend.pos.x < 100 and friend.pos.x >= 90:
            self.command(friend, "defend", getPosition(100, 36))

            attackEnemy(friend, findNearestEnemy(friend))

def findNearestEnemy(friend):
    enemies = self.findEnemies()
    if len(enemies) > 0:
        enemy = self.findNearest(enemies)
        if self.pos < 290 and enemy and enemy.pos < 290:
            return enemy
    else:
        return None

def commandPaladin(friend):
    if friend.health < (friend.maxHealth * 3 / 4) and friend.canCast("heal"):
        self.command(friend, "cast", "heal", friend)

    # friends = self.findFriends()
    # for i in friends:
    #     if i.maxHealth > 100 and i.health < i.maxHealth / 2 and friend.distanceTo(i) < 15:
    #         self.command(friend, "cast", "heal", i)
    #         break

    if friend.pos.x < 80:
        self.command(friend, "move", getPosition(friend.pos.x + 10, friend.pos.y))
    else:
        if friend.pos.x > 140:
            attackEnemy(friend, findNearestEnemy(friend))

def attackCatapult():
    friends = self.findFriends()
    soldiers = self.findByType("soldier", friends)
    soldierAttackCatapults = []
    catapults = self.findByType("catapult")
    catapultNumber = len(catapults)
    for catapult in catapults:
        nearestSoldier = self.findNearest(soldiers)
        distanceToCatapult = 9999
        for i in soldiers:
            if i.distanceTo(catapult) < distanceToCatapult and i not in soldierAttackCatapults:
                nearestSoldier = i
                distanceToCatapult = i.distanceTo(catapult)
        soldierAttackCatapults.append(nearestSoldier)
        if nearestSoldier:
            self.command(nearestSoldier, "move", catapult.pos)
    return soldierAttackCatapults

def attackEnemy(friend, enemy):
    if enemy:
        # print ("attack enemy, " + "friend:" + friend + "enemy:" + enemy)
        self.command(friend, "attack", enemy)

def commandFriends(soldierExcept):
    friends = self.findFriends()
    for friend in friends:
        if friend not in soldierExcept:
            if friend.type == "soldier":
                commandSoldier(friend)
            elif friend.type == "archer":
                commandArcher(friend)
            elif friend.type == "paladin":
                commandPaladin(friend)

def commandHeroAttack():
    if self.pos.x < 80:
        self.move(getPosition(self.pos.x + 15, 36))
    else if self.pos.x > 80 and self.pos.x < 250:
        enemies = self.findEnemies()
        enemy = self.findNearest(enemies)
        if enemy and enemy.type != "catapult" and enemy.pos.x < 250:
            self.attack(enemy)
        else:
            self.move(getPosition(self.pos.x + 1, self.pos.y))
    else if self.pos.x > 250:
        enemies = self.findEnemies()
        enemy = self.findNearest(enemies)
        warlocks = self.findByType("warlock")
        warlock = self.findNearest(warlocks)
        if warlock:
            self.attack(warlock)
        else:
            if enemy:
                self.attack(enemy)

def friendBack():
    summonFriend("archer")
    friends = self.findFriends()
    for i in friends:
        if i.type == "archer":
            self.command(i, "defend", getPosition(1, 37))

def healFriends(soldierExcept):
    friends = self.findFriends()
    paladins = self.findByType("paladin", friends)
    if len(soldierExcept) > 1 and len(paladins) > 1:
        self.command(paladins[0], "cast", "heal", soldierExcept[0])
        self.command(paladins[1], "cast", "heal", soldierExcept[1])

def readyForSecondLevel():
    # for i in range(6):
    summonFriend("archer")
    archers = self.findByType("archer")
    for archer in archers:
        self.command(archer, "defend", getPosition(87, 37))

    unhealthFriends=[]
    friends = self.findFriends()
    for i in friends:
        if i.type == "soldier":
            unhealthFriends.append(i)

    while(len(unhealthFriends) > 0):
        self.say("before " + len(unhealthFriends))
        for i in unhealthFriends:
            if i.health < i.maxHealth and i.maxHealth > 80 and i.health > 0:
                healFriend(i)
            else:
                # self.say("remove " + i)
                unhealthFriends.remove(i)

def healFriend(friend):
    friends = self.findFriends()
    paladins = self.findByType("paladin", friends)
    for i in paladins:
        if friend.health == friend.maxHealth:
            return
        else if i.canCast("heal"):
            self.command(i, "cast", "heal", friend)

def posLessThen90():
    while self.pos.x < 90:
        soldierExcept = attackCatapult()
        healFriends(soldierExcept)
        commandFriends(soldierExcept)
        commandHeroAttack()

#second level function
def secondLevel():
    towers = self.findByType("tower")
    target = getPosition(127, 33)
    while(self.pos.x < 110 or len(towers) != 0):
        towers = []
        for i in self.findByType("tower"):
            towers.append(i)
        if self.distanceTo(target) > 4 and len(towers) == 2:
            self.move(target)
            if self.pos.x > 105:
                attackTower()
        else:
            pos2 = getPosition(130, 29)
            if len(towers) < 2:
                if self.distanceTo(pos2) > 2:
                    self.moveXY(pos2.x, pos2.y)
                self.shield()
                attackTower()
            else:
                self.shield()
                attackTower()

def attackTower():
    friends = self.findByType("archer")
    towers = self.findByType("tower")
    enemy = self.findNearest(towers)
    for i in friends:
        attackEnemy(i, enemy)

def healHero():
    paladins = self.findByType("paladin", self.findFriends())
    while(self.health < self.maxHealth):
        for i in paladins:
            self.command(i, "cast", "heal", self)

def callFriendsToThirdTarget():
    targetPos = [getPosition(250, 56), getPosition(250, 20)]
    part = 0
    for i in self.findFriends():
        self.command(i, "move", targetPos[part%2])
        part += 1

def thirdLevelReady():
    while self.pos.x < 240:
        commandHeroAttack()
        soldiers = []
        commandFriends(soldiers)

def defendOnPosition(position):
    for i in self.findFriends():
        if i.type == "archer":
            self.command(i, "defend", getPosition(position.x - 10, position.y))
        else:
            self.command(i, "defend", position)
    pass

def heroMoveToFlag():
    loop:
        flag = self.findFlag()
        if flag:
            if flag.color == "green":
                self.move(flag.pos)
                self.pickUpFlag(flag)
                self.shield()
            else if flag.color == "black":
                pos = flag.pos
                defendOnPosition(pos)
                self.move(flag.pos)
                self.pickUpFlag(flag)
                summonFriend("archer")
                self.shield()
            else:
                print("attack warlock")
                killWitch()
                self.move(flag.pos)
                self.pickUpFlag(flag)
                self.shield()
        # else:
        #     enemy = findNearestEnemy()
        #     if enemy:
        #         self.attack(enemy)
        #     else:
        #         self.move(getPosition(self.pos.x + 1, self.pos.y))

def killWitch():
    witches = self.findByType("warlock")
    lens = len(witches)
    if lens > 0:
        part = 0
        for i in self.findFriends():
            self.command(i, "attack", witches[part % lens])
        self.attack(witches[0])

def defendHero(pos):
    friends = self.findFriends()
    warlocks = self.findByType("warlock")
    warlock = self.findNearest(warlocks)
    enemy = self.findNearest(self.findEnemies())
    for i in friends:
        if warlock:
            self.command(i, "attack", warlock)
        else:
            nearestEnemy = findNearestEnemy(i)
            if nearestEnemy:
                self.command(i, "attack", nearestEnemy)
            else:
                if enemy:
                    self.command(i, "attack", enemy)
                else:
                    self.command(i, "defend", self.pos)

def wait():
    while self.health < self.maxHealth * 0.98:
        self.move(self.pos)
        summonFriend("archer")

    self.moveXY(256, 34)

def finalAttack():

    while True:
        flag = self.findFlag()
        if flag:
            self.move(flag.pos)
            self.pickUpFlag(flag)
            defendHero(self.pos)

        summonFriend("archer")
        commandHeroAttack()
        defendHero(self.pos)

friendBack()
posLessThen90()
readyForSecondLevel()
summonFriend("archer")
self.moveXY(130, 37)
secondLevel()
self.moveXY(155, 34)
callFriendsToThirdTarget()
print("ready for thirdLevelReady")
thirdLevelReady()
# heroMoveToFlag()
# defendOnPosition(getPosition(250, 33))
wait()
finalAttack()
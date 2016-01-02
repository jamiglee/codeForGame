# Defend your towers in this replayable challenge level!
# Step on an X if you have 20 gold to build a soldier.
# http://cn.codecombat.com/play/level/sarven-siege
#

def getPosition(x, y):
    return {"x":x, "y":y}

def movePosition(pos):
    if self.isReady("jump"):
      self.jumpTo(pos)
    else:
      self.move(pos)

def moveToPosition(pos):
    while self.distanceTo(pos) > 0:
        if self.isReady("jump"):
          self.jumpTo(pos)
        else:
          self.move(pos)

def summonFriend(friendType):
    if self.costOf(friendType) < self.gold:
        self.summon(friendType)
        index += 1

def soldierFindCoin():
    soldiers = self.findFriends()
    coins = self.find
    for i in soldiers:
        if i.type == "soldier":
            coins = self.findItems()
            coin = i.findNearest(coins)
            self.command(i, "move", coin.pos)

def commandSoldierAttack():
    enemies = self.findEnemies()
    friends = self.findFriends()
    for i in friends:
        if i.type != "arrow-tower":
            enemy = i.findNearest(enemies)
            self.command(i, "defend", defendPos)
            # if enemy:
            #     self.command(i, "attack", enemy)
            # else:
            #     self.command(i, "defend", defendPos)

towerPos = [getPosition(78, 51), getPosition(78, 78), getPosition(78, 22)]
defendPos = getPosition(69, 51)

loop:
    coins = self.findItems()
    coin = self.findNearest(coins)
    distance = 9999
    for i in coins:
        if i.value >= 2 and self.distanceTo(i) < distance:
            distance = self.distanceTo(i)
            coin = i

    movePosition(coin.pos)
    summonFriend("archer")
    commandSoldierAttack()

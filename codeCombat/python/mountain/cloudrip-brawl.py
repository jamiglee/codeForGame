# Stay alive for one minute.
# If you win, the next time you play will be more difficult and more rewarding!
# If you lose, you must wait a day before submitting again.
# http://cn.codecombat.com/play/level/cloudrip-brawl

def getPosition(x, y):
    return {"x":x, "y":y}

def summonFriend(friendType):
    if self.costOf(friendType) < self.gold:
        self.summon(friendType)

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

def pickCoins():
    coins = self.findItems()
    coin = self.findNearest(coins)
    distance = 9999
    for i in coins:
        if i.value >= 2 and self.distanceTo(i) < distance:
            distance = self.distanceTo(i)
            coin = i

    movePosition(coin.pos)

# def heroAttack():
#     enemies = self.findEnemies()
#     enemy = self.findNearest(enemies)
#     if enemy:
#         if self.distanceTo(enemy) > 7 and self.isReady("jump"):
#             self.jumpTo(enemy.pos)
#         else:
#             if self.isReady("bash"):
#                 self.bash(enemy)
#             else:
#                 self.attack(enemy)

#     else:
#         self.move(getPosition(60, 50))

def defendHero(pos):
    friends = self.findFriends()
    for i in friends:
        self.command(i, "defend", pos)
loop:
    summonFriend("archer")
    pickCoins()
    # heroAttack()
    defendHero(self.pos)


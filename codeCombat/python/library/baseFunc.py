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
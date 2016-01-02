def getPosition(x, y):
    return {"x":x, "y":y}

def summonFriend(friendType):
    if self.costOf(friendType) < self.gold:
        self.summon(friendType)

def moveToPosition(pos):
    while self.distanceTo(pos) > 0:
        if self.isReady("jump"):
          self.jumpTo(pos)
        else:
          self.move(pos)
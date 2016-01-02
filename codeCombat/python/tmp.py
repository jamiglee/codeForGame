# 生存一分钟。
# 如果你赢了，这关卡将会变得更难（以及更好的奖励）。
# 如果你输了，你必须等待24小时后才能再次挑战。
# 记得，每一次提交都会获得不同的地图。
# http://cn.codecombat.com/play/level/backwoods-brawl

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

def heroAttack():
    enemies = self.findEnemies()
    enemy = self.findNearest(enemies)
    if enemy:
        if self.distanceTo(enemy) > 7 and self.isReady("jump"):
            self.jumpTo(enemy.pos)
        else:
            if self.isReady("bash"):
                self.bash(enemy)
            else:
                self.attack(enemy)

    else:
        self.move(getPosition(60, 50))

def defendHero(pos):
    friends = self.findFriends()
    for i in friends:
        self.command(i, "defend", pos)
loop:
    summonFriend("griffin-rider")
    heroAttack()
    defendHero(self.pos)

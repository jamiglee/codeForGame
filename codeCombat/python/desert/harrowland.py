# 使用你最聪明的编程技术来胜过你的对手！
# 你需要更好的策略和好的装备来赢得这关。
# http://cn.codecombat.com/play/level/harrowland

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

def attack(friend, enemy):
    if enemy:
        self.command(friend, "attack", enemy)

def archerAttack(friend, enemy):
    if enemy:
        self.command(friend, "attack", enemy)
    pass

def soldierAttack(friend, enemy):
    if enemy:
        self.command(friend, "attack", enemy)

loop:
    summonFriend("archer")
    enemies = self.findEnemies()
    enemyArchers = self.findByType("archer", enemies)
    enemySoldiers = self.findByType("soldier", enemies)
    friends = self.findFriends()

    for i in friends:
        enemy = i.findNearest(enemies)
        if i.type == "archer":
            nearestArcher = i.findNearest(enemyArchers)
            if nearestArcher:
                attack(i, nearestArcher)
            else:
                if enemy and enemy.type != "sand-yak":
                    attack(i, enemy)
        else:
            if enemy and enemy.type != "sand-yak":
                attack(i, enemy)

    nearestEnemy = self.findNearest(enemies)
    if nearestEnemy:
        if self.health < self.maxHealth - 800:
            self.shield()
        elif self.isReady("bash"):
            if self.distanceTo(nearestEnemy) > 7:
                self.jumpTo(nearestEnemy.pos)
                self.bash(nearestEnemy)
            else:
                self.bash(nearestEnemy)
        else:
            if self.distanceTo(nearestEnemy) > 7:
                self.jumpTo(nearestEnemy.pos)
            self.attack(nearestEnemy)
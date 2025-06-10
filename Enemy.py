import random as random


class Enemy:
    enemies = []
    def __init__(self, name:str, health_points:int, attack_points:int, mercy_chance:float, attack_chance:float):
        self.name = name
        self.health_points = health_points
        self.attack_points = attack_points
        self.mercy_chance = mercy_chance
        self.attack_chance = attack_chance
        self.enemy_tmp_health = health_points
        Enemy.enemies.append(str(self))

    def attack_player(self, player):
        chance = random.random()
        print(f"attach_player chance: {chance}")
        if(chance < self.attack_chance):
             player.health_points -= self.attack_points

    def mercy_success(self,player)->bool:
        spared = False
        chance = random.random()
        chance += player.mercy_chance
        print(f"mercy chance: {chance}")
        if(chance > self.mercy_chance):
            self.enemy_tmp_health = 0
            spared = True
        print(spared)
        return spared
    def enemy_reset(self):
        self.enemy_tmp_health = self.health_points

class Player:
    # information about player
    def __init__(self, atack_points: int, mercy_chance: int, max_health_points: int):
        self.attack_points = atack_points
        self.mercy_chance = mercy_chance
        self.max_health_points = max_health_points
        self.health_points = max_health_points
        self.inventory = {"egg": 0, "leaf": 5, "feather": 0}

    # we use it when player attacks enemy (obviously)
    def attack_enemy(self, enemy):
        enemy.enemy_tmp_health -= self.attack_points
    # here we reset player values when player dies
    def reset(self):
        self.max_health_points = 50
        self.health_points = self.max_health_points
        self.attack_points = 10
        self.mercy_chance = 0
        self.inventory = {"egg": 0, "leaf": 5, "feather": 0}
    # jest 2 w nocy a ja piszę dokumentacje
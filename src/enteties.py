# here we create player and enemies with correct values

from src.Enemy import Enemy
from Player import Player

player = Player(10,0,50)

spider = Enemy("spider", 100, 5, 0.9, 0.5)

water_blob = Enemy("water blob", 200, 10, 0.66, 0.66)

bimbo_bear = Enemy("bimbo bear", 300, 15, 0.75, 0.75)

talking_dog = Enemy("talking dog", 400, 20, 0.8, 0.8)

fish_boss = Enemy("fish boss", 500, 25, 0.84, 0.84)


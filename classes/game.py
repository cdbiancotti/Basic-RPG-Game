import random


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, item, lives):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = magic
        self.item = item
        self.lives = lives
        self.action = ['Attack', 'Magic', "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def heal(self, cost):
        self.hp += cost
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        if self.mp >= cost:
            self.mp -= cost
        else:
            print("You need more mana")

    def choose_action(self):
        i = 1
        print(Bcolors.OKBLUE + "    ACTIONS:" + Bcolors.ENDC)
        for item in self.action:
            print("         ", str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(Bcolors.OKBLUE + "    SPELLS:" + Bcolors.ENDC)
        for spell in self.magic:
            print("         ", str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print(Bcolors.OKBLUE + "    ITEMS:" + Bcolors.ENDC)
        for item in self.item:
            print("         ", str(i) + ".", item["item"].name + ":", item["item"].description, "(x"
                  + str(item["quantity"]) + ")")
            i += 1

    def choose_enemy(self, enemies):
        i = 1
        print(Bcolors.OKBLUE + "    ENEMIES:" + Bcolors.ENDC)
        for enemy in enemies:
            print("         ", str(i) + ".", enemy.name, str(enemy.hp) + "/" + str(enemy.maxhp))
            i += 1
        choice = int(input("    Choose enemy: ")) - 1
        if enemies[choice].hp == 0:
            print("That enemy is dead! Choose anohter enemy!")
            return self.choose_enemy(enemies)
        return choice

    def get_enemy_stats(self):

        enemy_bar = ""
        enemy_points = (self.hp / self.maxhp) * 100 / 2

        while enemy_points > 0:
            enemy_bar += "/"
            enemy_points -= 1

        while len(enemy_bar) < 50:
            enemy_bar += " "

        enemy_hp = str(self.hp) + "/" + str(self.maxhp)
        enemy_space = len(str(self.maxhp)) - len(str(self.hp))
        if enemy_space > 0:
            enemy_hp = (" " * enemy_space) + enemy_hp

        print("                         __________________________________________________")
        print(Bcolors.BOLD + self.name + ":       " + enemy_hp + " |"
              + Bcolors.FAIL + enemy_bar
              + Bcolors.ENDC + "|")

    def get_stats(self):

        hp_bar = ""
        hp_points = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_points = (self.mp / self.maxmp) * 100 / 10

        while hp_points > 0:
            hp_bar += "/"
            hp_points -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_points > 0:
            mp_bar += "/"
            mp_points -= 12

        while len(mp_bar) < 10:
            mp_bar += " "

        str_hp = str(self.hp) + "/" + str(self.maxhp)
        spaceh = len(str(self.maxhp)) - len(str(self.hp))
        if spaceh > 0:
            str_hp = (" " * spaceh) + str_hp

        str_mp = str(self.mp) + "/" + str(self.maxmp)
        spacem = len(str(self.maxmp)) - len(str(self.mp))
        if spacem > 0:
            str_mp = (" " * spacem) + str_mp

        print("                           _________________________            __________")
        print(Bcolors.BOLD + self.name + ":          " + str_hp + " |"
              + Bcolors.OKGREEN + hp_bar
              + Bcolors.ENDC + Bcolors.BOLD + "|  " + str_mp + " |" + Bcolors.OKBLUE
              + mp_bar + Bcolors.ENDC + "|")

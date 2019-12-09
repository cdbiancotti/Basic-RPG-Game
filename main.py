from classes.game import Bcolors, Person
from classes.magic import Spell
from classes.inventory import Item
import random

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 15, 150, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 13, 130, "black")

# Create White Magic
cure = Spell("Cure", 10, 100, "white")
cura = Spell("Cura", 15, 200, "white")

player_spells = [fire, thunder, blizzard, meteor, cure, cura]

# Create some item
potion = Item("Potion", "potion", "Heals for 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals for 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals for 250 HP", 250)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("Mega Elixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_item = [{"item": potion, "quantity": 5},
               {"item": hipotion, "quantity": 5},
               {"item": superpotion, "quantity": 5},
               {"item": elixer, "quantity": 5},
               {"item": hielixer, "quantity": 5},
               {"item": grenade, "quantity": 5}]

# Instantiate People
player1 = Person("Valos", 3450, 570, 315, 34, player_spells, player_item, True)
player2 = Person("Nick ", 2835, 980, 160, 34, player_spells, player_item, True)
player3 = Person("Robot", 5100, 345, 380, 34, player_spells, player_item, True)
enemy1 = Person("Goblin", 2100, 65, 45, 25, [], [], True)
enemy2 = Person("   Imp", 1200, 65, 45, 25, [], [], True)
enemy3 = Person("Magi", 24000, 630, 480, 25, [], [], True)

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

# The run start
running = True

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)

while running:
    # Life Bars
    print("\n")
    print(Bcolors.BOLD + "NAME:                    HP:                                MP:" + Bcolors.ENDC)
    for player in players:
        player.get_stats()
    print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()
    print("\n\n")

    print("=====================================================\n")

    players_defeated = 0
    enemies_defeated = 0   # FOR A KILLED ENEMY, IN THE CLIP, THE TEACHER USE METHOD "DEL" TO DELETE THE ENEMY DEFEATED

    # Try to use DEL to enemies defeated and comment that lines of codes

    # Check if player won
    if enemies_defeated == 3:
        print(Bcolors.OKGREEN + "\n" + "==========================" + "\n" + "YOUR HERO'S DEFEAT THE ENEMY'S!"
              + "\n" + "==========================" + Bcolors.ENDC)
        running = False

    for player in players:
        if player.hp == 0:
            players_defeated += 1
            continue

        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) - 1

        if index == 0:
            # Attack to an enemy
            enemy_target = player.choose_enemy(enemies)
            dmg = player.generate_damage()
            enemies[enemy_target].take_damage(dmg)
            print("\nYou attacked for", dmg, "points of damage. Enemy HP:", enemies[enemy_target].get_hp())
        elif index == 1:
            # Spell to an enemy
            enemy_target = player.choose_enemy(enemies)
            player.choose_magic()
            magic_choice = int(input("  Choose a spell: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            spell_dmg = spell.generate_spell_damage()

            current_mp = player.get_mp()

            if current_mp < spell.cost:
                print(Bcolors.FAIL + "\nNot enough MP.\n" + Bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(spell_dmg)
                print(Bcolors.OKBLUE + "\n" + spell.name + " heals for", str(spell_dmg), "HP." + Bcolors.ENDC)
            elif spell.type == "black":
                enemies[enemy_target].take_damage(spell_dmg)
                print(Bcolors.OKBLUE + "\n" + spell.name + " deals", str(spell_dmg), "points of damage to the enemy."
                      + Bcolors.ENDC)
        elif index == 2:
            # Items to choose
            print("\/\/\/\/\/\/\/")
            player.choose_item()
            item_choise = int(input("   Choose item: ")) - 1

            if item_choise == -1:
                continue

            item = player.item[item_choise]["item"]

            if player.item[item_choise]["quantity"] == 0:
                print("You don´t have any", item.name, "in your inventory")
                continue

            player.item[item_choise]["quantity"] -= 1
            if item.type == "potion":
                player.heal(item.prop)
                print("\n" + Bcolors.OKGREEN + item.name, "heals for", str(item.prop), "HP" + Bcolors.ENDC)
            elif item.type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print("\n" + Bcolors.OKGREEN + item.name, "fully restored the HP/MP" + Bcolors.ENDC)
            elif item.type == "attack":
                enemy_target = player.choose_enemy(enemies)
                enemies[enemy_target].take_damage(item.prop)
                print(Bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to the enemy."
                      + Bcolors.ENDC)

    # Check if enemy won
    if players_defeated == 3:
        print(Bcolors.FAIL + "\n" + "==========================" + "\n" + "Your enemy defeat your hero's!"
              + "\n" + "==========================" + Bcolors.ENDC)
        running = False

    # Enemy attack phase
    # Add to this lines of code some magic and items to the enemy
    for enemy in enemies:
        if enemy.hp > 0:
            target = random.randrange(0, 3)
            enemy_dmg = enemy.generate_damage()
            points = 0
            for player in players:
                if player.hp == 0:
                    points += 1
            if points == 3:
                continue
            while players[target].hp == 0:
                target = random.randrange(0, 3)
            players[target].take_damage(enemy_dmg)
            print("The enemy attacked for", enemy_dmg, "points of damage. Player HP:", players[target].get_hp())
        elif enemy.lives:
            enemy.lives = False
            enemies_defeated += 1



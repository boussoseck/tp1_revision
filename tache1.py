import random

pts_vie_user = 50
pts_vie_ennemi = 50
potion = 3
# attaque_user = pts_vie_ennemi - random.randint(5, 10)
# attaque_ennemi = pts_vie_user - random.randint(5, 15)

print("*** JEU DE ROLE ***")
while pts_vie_user > 0 and pts_vie_ennemi > 0:
  option = input("Tapez (1) pour attaquer ou tapez (2) pour utiliser une potion: ")
  if not option.isdigit():
    print("Veuillez choisir une option valide")
    continue
  option = int(option)
  if option == 1:
    user_attack = random.randint(5, 10)
    pts_vie_ennemi -= user_attack
    print(f"Vous avez inflige {user_attack} points de degats a l'ennemi")
  elif option == 2 and potion > 0:
    pts_vie_potion = random.randint(15, 50)
    pts_vie_user += pts_vie_potion
    potion -= 1
    print(f"Vous avez recupere {pts_vie_potion} points de vie et vous avez {potion} restantes")
  else:
    print("Vous n'avez plus de potions")
    continue
  if pts_vie_ennemi <= 0:
    print("Vous avez gagne")
    break

  ennemi_attack = random.randint(5, 15)
  pts_vie_user -= ennemi_attack
  print(f"L'attaque de l'ennemi vous a coute {ennemi_attack} ponits de vie")

  if pts_vie_user <= 0:
    print("Vous avez perdu")
    break

  print(f"Il vous reste {pts_vie_user} points de vie. Votre ennemi a {pts_vie_ennemi} points de vie")
  print("-" * 50)
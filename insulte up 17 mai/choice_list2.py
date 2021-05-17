from Player import Player_one, Player_two
import pygame
import random
import os 
from score import hpcalcul, score
# un dictionnaire pour associer un score avec un des morceaux de phrases, le score est calculé en additionnant les scores
nom = {"ta mère" : 3,
       "ta tante" : 2,
       "tu" : 1 ,
       "la voiture de ton cousin" : 2,
       "Satan" : 3,
       "un hamster" : 3,
       "la culotte de Staline" : 2,
       "ta femme" : 3}

verbe = {"ressemble à " : 2,
         "à l'odeur de" : 2,
         "est" : 1,
         "voulais être" : 2 ,
         "aime secretement" : 3}

multiplicateur = {"et" : 1}

finisseur = {"je parie!" : 2,
             "sans mentir!" : 2}

# tirage au sort des propositions
def list_randomizer(d):
    C = random.choice(list(d.items()))
    return C

def list_init():
    randList = random.choice([nom,verbe,multiplicateur,finisseur])
    x = list_randomizer(randList)
    return x

list_prop = {}
while len(list_prop) < 9:
    list_prop.update({list_init()})

### Debut d'une manche

def start_game():
    os.system('cls')
    print("Bonjour bienvenue dans le jeu d'insulte")
    print('Pour commencer tape 1')
    choice = input("<")
    listofkeys = list_prop.keys()
    listofkeys = list(listofkeys)
    if choice == ("1") :
        main_gameloop()
    else :
        quit

#### tant que la liste des proposition n'est pas vide
def game(): 
    print('Début de la manche')
   
    listofkeys = list_prop.keys()
    listofkeys = list(listofkeys)
    currentplayer = 1
    while len (listofkeys) > 0 :
            print(*listofkeys, sep=" | ")
            if currentplayer == 1 :
                print('Joueur 1 a toi de jouer')
                print('Choisis un mot')
                choice = input("<")
                if choice == ('0'):
                    Player_one.list.append(listofkeys[0])
                    del listofkeys[0]
                    print("Phrase du Joueur 1 :[",*Player_one.list,"]")
                    print("C'est au joueur numéro 2 de choisir un mot")
                    currentplayer = 2
                    print("Choisis ce que tu prend")
                elif choice == ('1'):
                        Player_one.list.append(listofkeys[1])
                        del listofkeys[1]
                        print(Player_one.list)
                        print("C'est au joueur numéro 2 de choisir un mot")
                        currentplayer = 2
                        print("Choisis ce que tu prend")
                    
                elif choice == ('2'):
                    Player_one.list.append(listofkeys[2])
                    del listofkeys[2]
                    print(Player_one.list)
                    print("C'est au joueur numéro 2 de choisir un mot")
                    currentplayer = 2
                    print("Choisis ce que tu prend")
                
                elif choice == ('3'):
                    Player_one.list.append(listofkeys[3])
                    del listofkeys[3]
                    print(Player_one.list)
                    print("C'est au joueur numéro 2 de choisir un mot")
                    currentplayer = 2
                    print("Choisis ce que tu prend")
                
                elif choice == ('4'):
                    Player_one.list.append(listofkeys[4])
                    del listofkeys[4]
                    print(Player_one.list)
                    print("C'est au joueur numéro 2 de choisir un mot")
                    currentplayer = 2
                    print("Choisis ce que tu prend")

                elif choice == ('5'):
                        Player_one.list.append(listofkeys[5])
                        del listofkeys[5]
                        print(Player_one.list)
                        print("C'est au joueur numéro 2 de choisir un mot")
                        currentplayer = 2
                        print("Choisis ce que tu prend")
                    
                elif choice ==('6'):
                        Player_one.list.append(listofkeys[6])
                        del listofkeys[6]
                        print(Player_one.list)
                        print("C'est au joueur numéro 2 de choisir un mot")
                        currentplayer = 2
                        print("Choisis ce que tu prend")
                    
                elif choice == ('7'):
                        Player_one.list.append(listofkeys[7])
                        del listofkeys[7]
                        print(Player_one.list)
                        print("C'est au joueur numéro 2 de choisir un mot")
                        currentplayer = 2
                        print("Choisis ce que tu prend")
                    
                elif choice == ('8'):
                        Player_one.list.append(listofkeys[8])
                        del listofkeys[8]
                        print(Player_one.list)
                        print("C'est au joueur numéro 2 de choisir un mot")
                        currentplayer = 2
                        print("Choisis ce que tu prend")          
            else :
                choice = input("<")
                if choice == ('0'):
                    Player_two.list.append(listofkeys[0])
                    del listofkeys[0]
                    print(Player_two.list)
                    print("C'est au joueur numéro 1 de choisir un mot")
                    currentplayer = 1
                    print("Choisis ce que tu prend")
                
                elif choice == ('1'):
                    Player_two.list.append(listofkeys[1])
                    del listofkeys[1]
                    print(Player_two.list)
                    print("C'est au joueur numéro 1 de choisir un mot")
                    currentplayer = 1
                    print("Choisis ce que tu prend")
                
                elif choice == ('2'):
                    Player_two.list.append(listofkeys[2])
                    del listofkeys[2]
                    print(Player_two.list)
                    print("C'est au joueur numéro 1 de choisir un mot")
                    currentplayer = 1
                    print("Choisis ce que tu prend")
                
                elif choice == ('3'):
                    Player_two.list.append(listofkeys[3])
                    del listofkeys[3]
                    print(Player_two.list)
                    print("C'est au joueur numéro 1 de choisir un mot")
                    currentplayer = 1
                    print("Choisis ce que tu prend")
                
                elif choice == ('4'):
                    Player_two.list.append(listofkeys[4])
                    del listofkeys[4]
                    print(Player_two.list)
                    print("C'est au joueur numéro 1 de choisir un mot")
                    currentplayer = 1
                    print("Choisis ce que tu prend")

                elif choice == ('5'):
                    Player_two.list.append(listofkeys[5])
                    del listofkeys[5]
                    print(Player_two.list)
                    print("C'est au joueur numéro 1 de choisir un mot")
                    currentplayer = 1
                    print("Choisis ce que tu prend")
                
                elif choice ==('6'):
                    Player_two.list.append(listofkeys[6])
                    del listofkeys[6]
                    print(Player_two.list)
                    print("C'est au joueur numéro 1 de choisir un mot")
                    currentplayer = 1
                    print("Choisis ce que tu prend")
                
                elif choice == ('7'):
                    Player_two.list.append(listofkeys[7])
                    del listofkeys[7]
                    print(Player_two.list)
                    print("C'est au joueur numéro 1 de choisir un mot")
                    currentplayer = 1
                    print("Choisis ce que tu prend")
                
                elif choice == ('8'):
                    Player_two.list.append(listofkeys[8])
                    del listofkeys[8]
                    print(Player_two.list)
                    print("C'est au joueur numéro 1 de choisir un mot")
                    currentplayer = 1
        
                    print("Choisis ce que tu prend")
            if not listofkeys :
                print("Vous avez fini de choisir tous les 2")
                print(" on va donc savoir qui va perdre")
                
                print('La phrase du joueur 1')
                print(Player_one.list)
                

                print('Et voici donc la phrases du joueur 2')
                print(Player_two.list)
                

                score()
                print('les scores sont de :')
                print(Player_one.score)
                print(Player_two.score)
                hpcalcul()
                
                Player_one.score = 0
                
                Player_two.score = 0
                
                list_prop.clear
        
####ecran de victoire

def wongame():
    print("bravo a toi, tu as battu ton pote\n")
    print("je pensais pas que tu pourrais le faire bravo")

####main game loop qui va relancé a chaque fin de manche

def main_gameloop():
    while Player_one.health > 0 :
        game()
    else:
        wongame()



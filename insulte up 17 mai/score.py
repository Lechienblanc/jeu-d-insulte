

from Player import Player_one, Player_two
import pygame
import random
import os 
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

list1 = Player_one.list

def score():
    if 'ta mère' in Player_one.list:
        Player_one.score = Player_one.score + 3
        

    elif 'Satan' in Player_one.list:
        Player_one.score = Player_one.score + 3
        
    elif "un hamster" in Player_one.list:
        Player_one.score = Player_one.score + 3
        

    elif "ta femme" in Player_one.list:
        Player_one.score = Player_one.score + 3
        

    
    elif "la culotte de Staline" in Player_one.list:
        Player_one.score = Player_one.score + 2
        
    elif "la voiture de ton cousin" in Player_one.list:
        Player_one.score = Player_one.score + 2
       

    elif "ta tante" in Player_one.list:
        Player_one.score = Player_one.score + 2
        
    
    elif "tu" in Player_one.list:
        Player_one.score = Player_one.score + 1
        
    
    ####player 1 check si il y a un verbe

    if "ressemble à " in Player_one.list:
        Player_one.score = Player_one.score + 2
        

    elif "à l'odeur de" in Player_one.list:
        Player_one.score = Player_one.score + 2
        
    elif "est" in Player_one.list:
        Player_one.score = Player_one.score + 1
        

    elif "voulais être" in Player_one.list:
        Player_one.score = Player_one.score + 2
        

    
    elif "aime secretement" in Player_one.list:
        Player_one.score = Player_one.score + 3
        
    ##### Player 1 check si y'a un finisseur ######

    if "je parie!" in Player_one.list:
        Player_one.score = Player_one.score + 2
        

    elif "sans mentir!" in Player_one.list:
        Player_one.score = Player_one.score + 2
        
   
    #### Player 2 check si sa liste contient des noms#####

    if 'ta mère' in Player_two.list:
        Player_two.score = Player_two.score + 3
        
    elif 'Satan' in Player_two.list:
        Player_two.score = Player_two.score + 3
        
    elif "un hamster" in Player_two.list:
        Player_one.score = Player_two.score + 3
        

    elif "ta femme" in Player_two.list:
        Player_two.score = Player_two.score + 3
        

    
    elif "la culotte de Staline" in Player_two.list:
        Player_two.score = Player_two.score + 2
        
    elif "la voiture de ton cousin" in Player_one.list:
        Player_two.score = Player_two.score + 2
        

    elif "ta tante" in Player_two.list:
        Player_two.score = Player_two.score + 2
        
    
    elif "tu" in Player_two.list:
        Player_two.score = Player_two.score + 1

###### player 2 check si il y a un verbe
    if "ressemble à " in Player_two.list:
        Player_two.score = Player_two.score + 2
        

    elif "à l'odeur de" in Player_two.list:
        Player_two.score = Player_two.score + 2
        
    elif "est" in Player_two.list:
        Player_two.score = Player_two.score + 1
        

    elif "voulais être" in Player_two.list:
        Player_one.score = Player_one.score + 2
        

    
    elif "aime secretement" in Player_two.list:
        Player_two.score = Player_two.score + 3


###### Player 2 check si y'a un finisseur

    if "je parie!" in Player_two.list:
        Player_two.score = Player_two.score + 2
        

    elif "sans mentir!" in Player_two.list:
        Player_two.score = Player_one.score + 2



def hpcalcul():
    if Player_one.score > Player_two.score :
        Player_two.health = Player_two.health - 10
        print('Les Hp du joueurs 1 sont de :')
        print(Player_one.health)
        print("Les hp du joueurs 2 sont de :")
        print(Player_two.health)
    elif Player_one.score < Player_two.score:       
        Player_one.health = Player_one.health - 10
        print('Les Hp du joueurs 1 sont de :')
        print(Player_one.health)
        print("Les hp du joueurs 2 sont de :")
        print(Player_two.health)
    else:
        Player_two.health = Player_two.health - 10
        Player_one.health = Player_one.health - 10
        print(Player_one.health)
        print(Player_two.health)



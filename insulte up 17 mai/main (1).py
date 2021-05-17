import cmd
from Player import andregiant, femur
from Player import Player_one, Player_two
from choice_list2 import start_game
import textwrap
import sys
import os 
import time 
import random 
import pickle
import math


# import choice_list

def menu():
    option = input(">")
    if option.lower() == ("1"):
        screen_selection()


def menu_screen():
    print('****************')
    print(' Projet Insulte ')
    print('****************')
    print('     Start      ')
    print('     Help       ')
    print('     Quit       ')
    print('****************')
    menu()

def screen_selection():
    os.system('cls')
    print( "Andre The Giant" )
    print(" Health:", andregiant.health," + ")
    print(" Tap 1 to choose Andre the Giant Max")
    print('************************************')
    print( "Femur")
    print(" Health:", femur.health," + ")
    print( "Tap 2 to choose the broke famous")
    print('************************************')
    character_selection()

def character_selection():
    choice = input(">")
    if choice == ("1"):
        Player_one.health = andregiant.health
        print("player1:",Player_one.health,"HP")
        character_selection2()
    elif choice == ("2"): 
        Player_one.health = femur.health
        print("player1:",Player_one.health,"HP")
        character_selection2()
    else:
        print(" player invalid ")
        character_selection()

def character_selection2():
    choice = input(">")
    if choice == ("1"):
        Player_two.health = andregiant.health
        print("player2:",Player_two.health,"HP")
        
    elif choice == ("2"): 
        Player_two.health = femur.health
        print("player2:",Player_two.health,"HP")
        start_game()
    else:
        print(" player invalid ")
        character_selection()

def show():
    print("player1",Player_one.health)
    
    # print(" Health:", player2.health," + ")
    

menu_screen()


    
# pygame.init()


# screen = pygame.display.set_mode((1080, 720))
# pygame.display.set_caption("Insult Game")


# running = True

# while running:

#     pygame.display.flip()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#             pygame.quit()
#             print("Quitting game") 
""" Here we call the commands functions from the Commands class, and present them to the user as a multiple choice questionart """
from __future__ import unicode_literals
import sys
from commands import Commands
from player import player
import questionary
from virt import find, mata, suspend, resume, get_vk, is_combination_pressed, on_press, on_release

resposta = questionary.select("What do you want do to? ", choices=["Start the Player", "Stop the Player", "Suspend the Player", "Resume the Player", "Exit"]).ask()

if resposta == "Start the Player":
    player()
if resposta == "Stop the Player":
    com = Commands()  # It is always needed to instantiate the class. Only then can you access the methods
    com.mata()
if resposta == "Suspend the Player":
    com = Commands()
    com.suspend()
if resposta == "Resume the Player":
    com = Commands()
    com.resume()
if resposta == "Exit":
    sys.exit()

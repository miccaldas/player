""" Here we call the commands functions from the Commands class, and present them to the user as a multiple choice questionart """
from __future__ import unicode_literals
import sys
from player import player
import questionary
from commands import find, mata, suspend, resume, get_vk, is_combination_pressed, on_press, on_release

resposta = questionary.select("What do you want do to? ", choices=["Start the Player", "Stop the Player", "Suspend the Player", "Resume the Player", "Exit"]).ask()

if resposta == "Start the Player":
    player()
if resposta == "Stop the Player":
    mata()
if resposta == "Suspend the Player":
    suspend()
if resposta == "Resume the Player":
    resume()
if resposta == "Exit":
    sys.exit()

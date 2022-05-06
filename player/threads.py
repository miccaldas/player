"""Module Docstring"""
import os
from threading import Thread
from time import sleep

import click
import isort
import psutil
import snoop
from pydub import AudioSegment
from pydub.playback import play
from pynput.keyboard import Key, KeyCode, Listener
from snoop import pp
from tqdm import tqdm


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def player():
    """The program should present the content of the 'music' folder, create a prompt for the user to choose from, and reproduce the files
    with a timer."""
    # https://stackoverflow.com/questions/5817209/browse-files-and-subfolders-in-python
    for i in os.scandir("/home/mic/python/yt_player/yt_player/music"):
        if i.is_file():
            print(i.path)
        elif i.is_dir():
            print(i.path)
    print(
        r"""
      ___           ___           ___                       ___                    ___                       ___                       ___           ___
     /\  \         /\  \         /\__\                     /\__\                  /\  \                     /\  \                     /\__\         /\  \
    |::\  \        \:\  \       /:/ _/_       ___         /:/  /                 /::\  \                   /::\  \         ___       /:/ _/_       /::\  \
    |:|:\  \        \:\  \     /:/ /\  \     /\__\       /:/  /                 /:/\:\__\                 /:/\:\  \       /|  |     /:/ /\__\     /:/\:\__\
  __|:|\:\  \   ___  \:\  \   /:/ /::\  \   /:/__/      /:/  /  ___            /:/ /:/  /  ___     ___   /:/ /::\  \     |:|  |    /:/ /:/ _/_   /:/ /:/  /
 /::::|_\:\__\ /\  \  \:\__\ /:/_/:/\:\__\ /::\  \     /:/__/  /\__\          /:/_/:/  /  /\  \   /\__\ /:/_/:/\:\__\    |:|  |   /:/_/:/ /\__\ /:/_/:/__/___
 \:\~~\  \/__/ \:\  \ /:/  / \:\/:/ /:/  / \/\:\  \__  \:\  \ /:/  /          \:\/:/  /   \:\  \ /:/  / \:\/:/  \/__/  __|:|__|   \:\/:/ /:/  / \:\/:::::/  /
  \:\  \        \:\  /:/  /   \::/ /:/  /   ~~\:\/\__\  \:\  /:/  /            \::/__/     \:\  /:/  /   \::/__/      /::::\  \    \::/_/:/  /   \::/~~/~~~~
   \:\  \        \:\/:/  /     \/_/:/  /       \::/  /   \:\/:/  /              \:\  \      \:\/:/  /     \:\  \      ~~~~\:\  \    \:\/:/  /     \:\~~\
    \:\__\        \::/  /        /:/  /        /:/  /     \::/  /                \:\__\      \::/  /       \:\__\          \:\__\    \::/  /       \:\__\
     \/__/         \/__/         \/__/         \/__/       \/__/                  \/__/       \/__/         \/__/           \/__/     \/__/         \/__/
"""
    )
    print("\n")
    escolha = str(input(click.style(" » What do you want to hear? :~ ", fg="green", bold=True)))
    pp(escolha)

    print("\n")
    album = []
    for i in os.scandir(escolha):
        if i.is_file():
            album.append(i.path)
    for song in album:
        musicas = os.path.basename(os.path.normpath(song))
        print(click.style(musicas, fg="bright_white", bold=True))
        sound = AudioSegment.from_file(song)
        t = Thread(target=play, args=(sound,))
        t.start()
        dur = sound.duration_seconds
        for sec in tqdm(range(int(dur)), bar_format="{desc}: {percentage:.0f}%|{bar} | {elapsed}<{remaining}"):
            sleep(1)
        tq = Thread(target=tqdm)
        tq.start()
        print("\n")


@snoop
def find():
    """Find the process pid with psutil"""
    player()
    lspid = []  # Create a list to house the processes output
    name = "python"  # The player name process is always python
    for p in psutil.process_iter(["name"]):  # For item in list of iterable processes names,
        if p.info["name"] == name:  # If process name is the same as python,
            lspid.append(p)  # Append to list
    player_pid = lspid[0].pid  # The player pid seems to be always the first on the list of processes.
    # As the list items are psutil.Process objects, you can add to it the pid method to return only the pid
    p = psutil.Process(int(player_pid))  # Creates a psutil.Process with just the pid
    return p


def mata():
    mata = find()
    mata.kill()  # https://psutil.readthedocs.io/en/latest/


def suspend():
    sus = find()
    sus.suspend()


def resume():
    res = find()
    res.resume()


function_keys = {
    frozenset([Key.alt, KeyCode(vk=107)]): mata,
    frozenset([Key.alt, KeyCode(vk=115)]): suspend,
    frozenset([Key.alt, KeyCode(vk=114)]): resume,
}


pressed_vks = set()


def get_vk(key):
    """
    Get the virtual key code from a key.
    These are used so case/shift modifications are ignored.
    """
    return key.vk if hasattr(key, "vk") else key.value.vk


def is_combination_pressed(combination):
    """Check if a combination is satisfied using the keys pressed in pressed_vks"""
    return all([get_vk(key) in pressed_vks for key in combination])


def on_press(key):
    """When a key is pressed"""
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.add(vk)  # Add it to the set of currently pressed keys
    for combination in function_keys:  # Loop through each combination
        if is_combination_pressed(combination):  # Check if all keys in the combination are pressed
            function_keys[combination]()  # If so, execute the function


def on_release(key):
    """When a key is released"""
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys


if __name__ == "__main__":
    player()


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

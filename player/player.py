""" Module to choose and reproduce music kept in the computer """
import os
from time import sleep
import threading
from pydub import AudioSegment
from pydub.playback import play
from tqdm import tqdm
import click


def player():
    """The program should present the content of the 'music' folder, create a prompt for the user to choose from, and reproduce the files
    with a timer."""
    # https://stackoverflow.com/questions/5817209/browse-files-and-subfolders-in-python
    for i in os.scandir("/home/mic/music"):
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
    print("\n")
    album = []
    for i in os.scandir(escolha):
        if i.is_file():
            album.append(i.path)
    for song in album:
        musicas = os.path.basename(os.path.normpath(song))
        print(click.style(musicas, fg="bright_white", bold=True))
        sound = AudioSegment.from_file(song)
        threading.get_ident()
        t = threading.Thread(target=play, args=(sound,))
        t.start()
        dur = sound.duration_seconds
        for sec in tqdm(range(int(dur)), bar_format="{desc}: {percentage:.0f}%|{bar} | {elapsed}<{remaining}"):
            sleep(1)
        print("\n")


if __name__ == "__main__":
    player()

"""
Module that initiates all the others.
"""
import os
import pickle

import snoop
from blessed import Terminal
from snoop import pp

from choose import choose
from play import player


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(out="logs", overwrite=True, watch_extras=[type_watch])


@snoop
def main():
    """"""
    music = "/home/mic/python/yt_player/yt_player/music"

    choose(music)
    bins = os.listdir(os.getcwd())

    if "choice.bin" in bins:
        with open("choice.bin", "rb") as f:
            artist = pickle.load(f)
        album = choose(f"{music}/{artist[0]}")
        with open("choice.bin", "rb") as g:
            album = pickle.load(g)
            player(f"{music}/{artist[0]}/{album[0]}")


if __name__ == "__main__":
    main()

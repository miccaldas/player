"""
Module that initiates all the others.
"""
import os
import pickle
import sys
import threading
from time import sleep

import ffmpeg
import snoop
from playsound import playsound
from rich.console import Console
from snoop import pp
from tqdm import tqdm

from choose import choose

sys.tracebacklimit = 0


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(out="logs", overwrite=True, watch_extras=[type_watch])


@snoop
def choice_collector():
    """
    The 'choose' module, collects the user chosen artist and album and creates
    a path from them. Creates pickle files from this. Runs before the other
    'threadable' modules start.
    """
    music = "/home/mic/python/yt_player/yt_player/music"

    # Mostly the 'choose' module, shows the contents of folders
    # and lets the user choose one of its members and keeps it
    # in a pickle file. The  first level is the folder that
    # houses all the musicians. User chooses one.
    choose(music)
    bins = os.listdir(os.getcwd())
    # 'choice.bin' is the output of 'choose'. If the file's there
    # we can proceed.
    if "choice.bin" in bins:
        with open("choice.bin", "rb") as f:
            artst = pickle.load(f)
        # Here we show the content of the chosen musician. The user
        # chooses an album to listen. We add it to the artist info
        # that we gathered before, to get the full path to the chosen
        # album. We pickle it.
        choose(f"{music}/{artst[0]}")
        with open("choice.bin", "rb") as g:
            album = pickle.load(g)
            song = f"{music}/{artst[0]}/{album[0]}"

    with open("song.bin", "wb") as f:
        pickle.dump(song, f)


if __name__ == "__main__":
    choice_collector()


@snoop
def player():
    """
    'Playsound' is the simplest player I
    know. It has only one argument, 'block'
    which is boolean that determines if the
    Playsound's execution is blocking or not.
    When I tried it as not blocking it
    wouldn't work.
    """
    with open("song.bin", "rb") as f:
        song = pickle.load(f)
    playsound(song)


@snoop
def duration():
    """
    We use 'ffmpeg' to get metadata about the
    duration of musics. If there's nothing in
    'duration', we'll assume the song is about
    three minutes long. This information is
    used by Tqdm.
    """
    with open("song.bin", "rb") as g:
        length = pickle.load(g)

    # The metadata is kept in a list called 'streams', that
    # houses a dictionary with the information. To search it
    # know that there is only the dictionary below the list,
    # so it's just a case of ['stream'][0][<metada_you_want>]
    duration = ffmpeg.probe(length)["streams"][0]["duration"]
    if duration:
        return duration
    else:
        duration = 224
        return duration


@snoop
def ticker():
    """
    The program should present the content of the 'music' folder,
    create a prompt for the user to choose from, and reproduce the files
    with a timer.

    'F6' - Lowers the volume,
    'F7' - Raises it,
    'F8' - Mutes it.
    'Ctrl-Alt-p' - Stops the player.
    """
    dur = duration()
    drt = float(dur)
    drtn = int(drt)

    console = Console()
    console.print(
        """[bold #E9B384]
  ############################
  ##    MUSIC PLAYER        ##
  ############################
  ##     Louder - 'F7'      ##
  ##     Lower  - 'F6'      ##
  ##     Mute   - 'F8'      ##
  ##  Stop   - 'Ctrl-Alt-p' ##
  ############################
  [/]
            """
    )
    for i in tqdm(
        range(drtn),
        position=0,
        ncols=70,
        colour="yellow",
        bar_format="{percentage:3.0f}%|{bar}| {remaining}]",
    ):
        sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=ticker)
    t2 = threading.Thread(target=player)
    t1.start()
    t2.start()

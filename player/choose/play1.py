""" Module to choose and reproduce music kept in the computer """
import threading
from time import sleep

import snoop
from blessed import Terminal
from progressbar import progressbar
from pydub import AudioSegment
from pydub.playback import play


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(out="logs", overwrite=True, watch_extras=[type_watch])


@snoop
def player(song):
    """
    The program should present the content of the 'music' folder,
    create a prompt for the user to choose from, and reproduce the files
    with a timer.

    'F6' - Lowers the volume,
    'F7' - Raises it,
    'F8' - Mutes it.
    """
    sound = AudioSegment.from_file(song)


if __name__ == "__main__":
    player()

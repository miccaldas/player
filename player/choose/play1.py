""" Module to choose and reproduce music kept in the computer """
import threading
from time import sleep

import snoop
from alive_progress import alive_it
from blessed import Terminal
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
    term = Terminal()
    wdth = int(term.width / 4)
    ht = int(term.height / 2)
    title = """



    ###########################
    ##     MUSIC PLAYER      ##
    ###########################
    """

    with term.fullscreen(), term.cbreak():
        print(term.move + term.black_on_peachpuff + term.bold + term.clear, end="")
        sound = AudioSegment.from_file(song)
        t = threading.Thread(target=play, args=(sound,))
        print(title)
        t.start()
        dur = int(sound.duration_seconds)

        for i in alive_it(range(dur)):
            print(i)


if __name__ == "__main__":
    player()

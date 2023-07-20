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
        # threading.get_ident()
        t = threading.Thread(target=play, args=(sound,))
        print(term.nove_xy(wdth, ht) + title)
        t.start()
        dur = sound.duration_seconds

        # Use underscore for when you want a for loop, but don't care about the index.
        # Suggested by Sourcery.

        # print(term.move_xy(wdth, (ht + 6)
        for i in progressbar(range(int(dur))):
            sleep(1)
    print("\n")


if __name__ == "__main__":
    player()

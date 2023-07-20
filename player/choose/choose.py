"""
Module to show the contents of the music folder, and collect user's choice.
"""
import os
import pickle

import snoop

# import subprocess
from blessed import Terminal
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(out="logs", overwrite=True, watch_extras=[type_watch])


@snoop
def choose(content):
    """
    Presents the content of a folder. Returns an entry id.
    """
    content_list = os.listdir(content)
    # Integer with the length of the longest album name.
    longest = len(max(content_list))
    choicelst = []

    if content.endswith("music"):
        title = "CHOOSE AN ARTIST"
    else:
        title = "CHOOSE AN ALBUM"

    heights = []

    term = Terminal()
    # To center the album entries, we divide the screen width/height by two, and
    # from that number, subtract the value of 'longest' entry, for width, ang entries
    # length, for height.
    # wdth = int((term.width - longest) / 2)
    wdth = int(term.width / 4)
    # The initial height is found by first finding the number of lines of the text will
    # use. That means, the length of the list of albums, two lines for the title and its
    # separator and two lines for the exit message and its separator. We subtract this
    # from the height of the screen, if we didn't, the text would like it started too
    # low in the screen. Finally we divide the result by two.
    ht = int((term.height - (len(content_list) + 4)) / 2)
    # Calculates the title's width, it uses the block of text initial width, looks for
    # the longest line there, divides it by two and adds the halved number to the
    # initial width.
    twdth = wdth + int(longest / 2)
    # In order to define the height of each entry, we use 'enumerate' to create a
    # new list. The first element is an integer version of id, so we can use it defining
    # entry height and choosing what to play. The string version of the id serves as an
    # identifer for the user.
    albums = [[f, str(f) + " - " + "".join(i)] for f, i in enumerate(content_list)]

    # 'fullscreen' permits to restore the terminal screen to exactly how it was before
    # entering the 'player' app. Without it, the content of the app, although not
    # usable, would still be visible after exit. 'cbreak' registers individual keyboard
    # clicks. While inside this context manager, it'll log all keypresses.
    with term.fullscreen(), term.cbreak():
        # Clears, prepares, defines background/foreground colors, for the screen.
        print(term.move + term.black_on_peachpuff + term.bold + term.clear, end="")
        # The title height is the text block initial height minus one for the title and
        # one more for the seprator
        print(term.move_xy(twdth, (ht - 2)) + title)
        # To ensure that the album entries stack one after the other verticallly, we use
        # the 'idx' value, that starts at 0, and add it to the initial height of the
        # entries. We register these heights in a list called "heights".
        for album in albums:
            hght = ht + album[0]
            heights.append(hght)
            print(term.move_xy(wdth, hght) + "\n".join(term.wrap(album[1])))
        # To define the height of the exit information line, as below the the text block
        # plus a sperator line and the line proper; we get the last value in the
        # 'heights' list, corresponding to the height of the last entry, and add two.
        exitht = heights[-1] + 2
        print(term.move_xy(wdth, exitht) + "Press 'e' to exit after choosing. Press 'q' to exit this screen.")

        # Here to assure we can access 'inpt' value outside the loop.
        inpt = ""
        # While there's no exit call...
        while inpt.lower() != "q":
            # the variable will collect clicked keyboard keys names.
            inpt = term.inkey()
            # If we used the 'q' key to exit this loop, besides the key intended to press
            # it would add 'q' from the exit command. To avoid this, we create a loop
            # that runs while no one presses 'e', creating a exit command to the loop
            # alone but, as there is no more code ahed except a 'return' statement, it
            # in effect closes the program.
            if inpt != "e":
                # We collect keypresses in a list...
                choicelst.append(str(inpt))
                # if there's more than one, we add append it to the previous one. This
                # way we're able to collect two digit numbers.
                chcstr = "".join(choicelst)
                # To compare input result with the idx from the enumerated list.
                # chc = int(chcstr)
                if chcstr:
                    choice = [i for f, i in enumerate(content_list) if f == int(chcstr)]
                with open("choice.bin", "wb") as f:
                    pickle.dump(choice, f)
            else:
                break

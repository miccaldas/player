""" Module that aggregates all commands. find() gives the pid and the other functions use psutil to do various manipulations """
import isort
import psutil

# import snoop
from pynput.keyboard import Key, KeyCode, Listener


# @snoop
def find():
    """Find the process pid with psutil"""
    name = "python"  # The player name process is always python
    lspid = [p for p in psutil.process_iter(["name"]) if p.info["name"] == name]
    player_pid = lspid[0].pid  # The player pid seems to be always the first on the list of processes.
    return psutil.Process(int(player_pid))


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
    return all(get_vk(key) in pressed_vks for key in combination)


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


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

""" Module that aggregates all commands. find() gives the pid and the other functions use psutil to do various manipulations """
import psutil


class Commands:

    def find(self):
        """Find the process pid with psutil"""
        lspid = []                                  # Create a list to house the processes output
        name = 'python'                             # The player name process is always python
        for p in psutil.process_iter(['name']):     # For item in list of iterable processes names,
            if p.info['name'] == name:              # If process name is the same as python,
                lspid.append(p)                     # Append to list
        player_pid = lspid[0].pid                   # The player pid seems to be always the first on the list of processes.
        # As the list items are psutil.Process objects, you can add to it the pid method to return only the pid
        p = psutil.Process(int(player_pid))         # Creates a psutil.Process with just the pid
        return p

    def mata(self):
        find = self.find()
        find.kill()                                 # https://psutil.readthedocs.io/en/latest/

    def suspend(self):
        find = self.find()
        find.suspend()

    def resume(self):
        find = self.find()
        find.resume()

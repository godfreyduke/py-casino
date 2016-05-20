"""
Terminal controls. If you want to change stuff in the view, this is the place.
"""
import os


class Terminal:
    def __init__(self):
        pass

    @staticmethod
    def clear_screen():
        """This function will clear the screen of any text.

        :return: None
        """
        print("\n" * 10)
        # TODO: This is totally a hack, simple clear for now.
        # os.system('clear')
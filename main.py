# This is a sample Python script.
import subprocess

import cliwrapper


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    dpkg = cli_wrapper.clCliWrapperDpkg()
    dpkg.list()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

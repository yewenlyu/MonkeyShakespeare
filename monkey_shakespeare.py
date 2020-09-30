import random
import string
import math
import re
import os
import io


class MonkeyShakespeare:
    """
    Private Fields:
    _fname(str):    Validated file name
    _fsize(float):  File size in decimal
    _funit(str):    Unit for _fize, can take 'kb'|'mb'|'gb'

    Public Methods:
    run():          Create a file of specified name and size with random characters
    """
    def __init__(self):
        print("\n---- Random File Generator ----")
        self._fname = self._file_name_guard()
        self._fsize, self._funit = self._file_size_guard()

    def _file_name_guard(self):
        """ Valid file name should not contain any of '<>:"/\\|?*' """
        fname = input("\nPlease name your file:\n")
        pattern = re.compile("^[\w\-. ]+$")
        while (not pattern.fullmatch(fname)):
            fname = input(f"\n\"{fname}\" is not valid file name, please enter another file name:\n")
        while (os.path.isfile(f"./{fname}")):
            fname = input(f"\n\"{fname}\" already exists in this directory, please enter another file name:\n")
        return fname

    def _file_size_guard(self):
        """ Accept possitive integer or floating number with unit 'kb', 'mb' or 'gb' """
        fsize_unit = input("\nPlease enter file size (e.g. \"30mb\" or \"150.25kb\"):\n" +
            "(WARNING: Choosing file larger than 2GB might cause stack overflow)\n")
        pattern = re.compile("(\d+\.?\d*)(kb|mb|gb)")

        while (not pattern.fullmatch(fsize_unit.lower())):
            fsize_unit = input(f"\n\"{fsize_unit}\" is not a file size, please try again (e.g. \"30mb\" or \"150.25kb\"):\n")

        fsize_unit_tuple = pattern.fullmatch(fsize_unit.lower()).groups()
        return fsize_unit_tuple[0], fsize_unit_tuple[1]

    def _byte(self, value, unit=None):
        """ Convert string value in byte to number in specified unit """
        if unit is None:
            unit = self._funit
        return int(float(value) * 1024 * (1024 ** ['kb', 'mb', 'gb'].index(unit.lower())))

    def _monkey_shakespeare_write(self):
        """ Generate file in specified size, filled with random characters """
        doc = ''.join([random.choice(string.ascii_lowercase) for i in range(self._byte(self._fsize))])

        with open(self._fname, 'w') as f:
            f.write(doc)
        pass

    def run(self):
        print(f"\nGenerating \"{self._fname}\" with size: {self._fsize}{self._funit.upper()}, please wait...")
        self._monkey_shakespeare_write()
        print("File generated at: " +
            os.path.join(os.path.dirname(os.path.realpath(__file__)), self._fname))


def main():
    respond = ""
    while (respond.lower() != 'q'): 
        MonkeyShakespeare().run()
        respond = input("\nPress ENTER to continue, press 'q' to exit.\n")


if __name__ == "__main__":
    main()

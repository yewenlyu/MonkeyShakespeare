import random
import string
import math
import re
import os


class MonkeyShakespeare:

    def __init__(self):
        print("\n---- Random File Generator ----")
        self._fname = self._file_name_guard()
        self._funit = self._size_unit_guard()
        self._fsize = self._file_size_guard()

    def _file_name_guard(self):
        """ Valid file name should not contain any of '<>:"/\\|?*' """
        fname = input("\nPlease name your file:\n")
        pattern = re.compile("^[\w\-. ]+$")
        while (not pattern.fullmatch(fname)):
            fname = input(f"\n\"{fname}\" is not valid file name, please enter another file name:\n")
        while (os.path.isfile(f"./{fname}")):
            fname = input(f"\n\"{fname}\" already exists in this directory, please enter another file name:\n")
        return fname

    def _size_unit_guard(self):
        """ Accept 'kb', 'mb' or 'gb', not-case-sensitive """
        funit = input("\nPlease enter a file size unit (kb/mb/gb):\n")
        while (funit.lower() not in ['kb', 'mb', 'gb']):
            funit = input(
                f"\n\"{funit.lower()}\" is not a valid unit, please choose amongst kb/mb/gb:\n")
        return funit

    def _file_size_guard(self):
        """ Accept possitive integer or floating number, warning occurs when exceeds 2GB """
        fsize = input("\nPlease enter file size:\n" +
            "(WARNING: Choosing file larger than 2GB might cause stack overflow)\n")
        while (not self._is_float(fsize) or self._byte(fsize) <= 0 or self._byte(fsize) > self._byte(3, 'gb')):

            # Handle invalid file size
            while (not self._is_float(fsize) or self._byte(fsize) <= 0):
                fsize = input(f"\n\"{fsize}\" is not a valid file size, please enter a positive integer or float:\n")

            # Handle large file size: prompt user to re-enter funit & fsize
            if (self._byte(fsize) > self._byte(2, 'gb')):
                response = input(f"{fsize}{self._funit.upper()} is a large file size that might cause stack overflow, " +
                    "do you still wish to continue? (Y/N)\n")
                if (response[0].lower() == 'y'):
                    break
                elif (response[0].lower() == 'n'):
                    self._funit = self._size_unit_guard()
                    fsize = input("Please enter file size as a number:\n")

        return fsize

    @staticmethod
    def _is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def _byte(self, value, unit=None):
        """ Convert string value in byte to number in specified unit """
        if unit is None:
            unit = self._funit
        return int(float(value) * 1024 * (1024 ** ['kb', 'mb', 'gb'].index(unit.lower())))

    def _monkey_shakespeare_write(self):
        """ Generate file in specified size, filled with random characters 
        Key Word Args:
        fname: User specified file name
        fsize: File size in byte
        """
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
    MonkeyShakespeare().run()
    input("\nPress ENTER to exit.")


if __name__ == "__main__":
    main()

import sys

from .Hello import *
from .Hi import *


class Say:
    def __init__(self) -> None:
        self.hello = Hello()
        self.hi = Hi()

    def print_say(self):
        self.hello.print_hello()
        self.hi.print_hi()
        print("---------------------------------")
        print(__name__)
        print(__package__)
        print(__file__)

        print("---------------------------------")
        sys.exit()

# a === b
# a >> b

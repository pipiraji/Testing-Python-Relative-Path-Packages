import sys
from os import path

if __name__ == "__main__":
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    from FirstPackage.Say import *

    Say().print_say()

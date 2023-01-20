import os
from typing import List


class CreateDirs:
    def __init__(self,
                 dirs2make: List):
        self.__create_required_dirs(dirs2make=dirs2make)

    @staticmethod
    def __create_required_dirs(dirs2make: List):
        [os.mkdir(dirpath) for dirpath in dirs2make]

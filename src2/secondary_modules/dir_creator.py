import os
from src.secondary_modules.time_id_creator import TimeID


class DirsCreator:
    def __init__(self,
                 config):
        self.__create_required_dirs(config=config)

    @staticmethod
    def __create_required_dirs(config):
        print(config.modelname)
        print(TimeID().timeid)
        dir_config = config.dirs2make
        [
            os.makedirs(
                os.path.join(
                    *dir_config.__dict__[key], config.modelname.modelname + TimeID().timeid
                ), exist_ok=True
            )
            for key in dir_config.__dict__
        ]

import os
from src.config.load_conifg import Config


class DirsCreator:
    def __init__(self,
                 config: Config,
                 time_id: str):
        self.__create_required_dirs(
            config=config,
            time_id=time_id
        )

    @staticmethod
    def __create_required_dirs(config: Config, time_id: str):
        dir_config = config.dirs2make
        [
            os.makedirs(
                os.path.join(
                    *dir_config.__dict__[key], config.modelname.modelname + time_id
                ), exist_ok=True
            )
            for key in dir_config.__dict__
        ]

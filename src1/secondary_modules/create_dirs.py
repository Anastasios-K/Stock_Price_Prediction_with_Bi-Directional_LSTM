import os


class CreateDirs:
    def __init__(self,
                 config):
        self.__create_required_dirs(config=config)

    @staticmethod
    def __create_required_dirs(config):
        dir_config = config.dirs2make
        [
            os.makedirs(
                os.path.join(
                    *dir_config.__dict__[key]
                ), exist_ok=True
            )
            for key in dir_config.__dict__
        ]

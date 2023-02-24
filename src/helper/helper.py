import yaml
import os
from datetime import datetime


class Helper:
    """ Class with all helper fuctions. """

    @staticmethod
    def create_str_time_id() -> str:
        """
        Create a unique timestamp (date & time) and returns it as a string.
        All the special characters are removed. Date and Time is split by underscore.
        """
        timestamp = str(datetime.now()).split(".")[0]
        date = timestamp.split(" ")[0]
        time = timestamp.split(" ")[1]
        date = date.replace("-", "")
        time = time.replace(":", "")
        timeid = date + "_" + time
        return timeid

    @staticmethod
    def read_yaml_file(path: str):
        """ Read a yaml file and return its content. """
        with open(path) as file:
            content = yaml.load(file, Loader=yaml.FullLoader)
            file.close()
        return content

    @staticmethod
    def create_required_dirs(config, unique_id: str = None):
        """
        Create all the directories that are set in the configuration yaml file.
        Optionally, It can integrate a unique id (usually a timestamp) into the directory names.
        """
        dir_config = config.dirs2make
        [
            os.makedirs(
                os.path.join(
                    *dir_config.__dict__[key], config.modelname.modelname + unique_id
                ), exist_ok=True
            )
            for key in dir_config.__dict__
        ]

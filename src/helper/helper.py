import yaml
from datetime import datetime


class Helper:

    def __init__(self):
        self.info_storage = dict()
        if len(self.info_storage) == 0:
            self.__init_time_id()

    def __init_time_id(self):
        timestamp = str(datetime.now()).split(".")[0]
        date = timestamp.split(" ")[0]
        time = timestamp.split(" ")[1]
        date = date.replace("-", "")
        time = time.replace(":", "")
        timeid = date + "_" + time
        self.update_info_tracker(
            dict(timeid=timeid)
        )

    def update_info_tracker(self, info: dict) -> None:
        self.info_storage.update(info)

    @staticmethod
    def read_yaml_file(path: str):
        with open(path) as file:
            content = yaml.load(file, Loader=yaml.FullLoader)
            file.close()
        return content

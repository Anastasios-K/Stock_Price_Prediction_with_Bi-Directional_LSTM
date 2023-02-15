import yaml


class YamlReader:
    def __init__(self,
                 path):

        self.content = self.__read_yaml_file(path=path)

    @staticmethod
    def __read_yaml_file(path: str):
        with open(path) as file:
            content = yaml.load(file, Loader=yaml.FullLoader)
            file.close()
        return content

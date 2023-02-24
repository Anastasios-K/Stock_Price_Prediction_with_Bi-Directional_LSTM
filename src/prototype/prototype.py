import pandas as pd
from src.config.load_conifg import Configurator
from src.helper.helper import Helper


class Prototype:

    __config_obj = None
    __info_tracker_obj = None
    __data_parser = None
    # __data_explorator = None
    # __data_technical_analyser = None
    # __data_preparator = None
    # __model_trainer = None
    # __model_tester = None
    # __model_traker = None

    def __init__(self):
        for i in range(3):
            print(i)

        print(self.config_obj)
        print(self.info_tracker_obj)
        # self.data: pd.DataFrame
        # self.config: Configurator = self.config_obj
        # self.info_tracker: Helper = self.info_tracker_obj

    @property
    def config_obj(self):
        return self.__config_obj

    @config_obj.setter
    def config_obj(self, obj):
        self.__config_obj = obj

    @property
    def info_tracker_obj(self):
        return self.__info_tracker_obj

    @info_tracker_obj.setter
    def info_tracker_obj(self, obj):
        self.__info_tracker_obj = obj

    @property
    def data_parser(self):
        return self.__data_parser

    @data_parser.setter
    def data_parser(self, obj):
        self.__data_parser = obj


CONFIG_PATH = "src\\config\\config.yaml"

config_obj = Configurator(CONFIG_PATH)

run = Prototype

run.config_obj = config_obj
#
xxx = run()

xxx.info_tracker_obj = Helper()


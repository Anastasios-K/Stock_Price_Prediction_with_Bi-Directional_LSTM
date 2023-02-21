import pandas as pd
from src.config.load_conifg import Configurator


class LabelsCreator:

    def __init__(self, data: pd.DataFrame, config: Configurator):

        self.data = data
        self.config = config

        self.__diff_col = "Diff"
        self.__calc_price_difference()
        self.__create_labels()

    def __calc_price_difference(self) -> None:
        shifted_col = "Shifted_Close"
        self.data[shifted_col] = self.data[self.config.dfstructure.close].shift(1)
        self.data[self.__diff_col] = (self.data[self.config.dfstructure.close] / self.data[shifted_col]) - 1

    def __create_labels(self) -> None:
        tollerance = self.config.labeltolerance.tolerance
        self.data.loc[self.data[self.__diff_col] > tollerance, self.config.dfstructure.labels] = 1

        self.data.loc[self.data[self.__diff_col] < -tollerance, self.config.dfstructure.labels] = -1
        self.data.loc[
            (self.data[self.__diff_col] < tollerance) &
            (self.data[self.__diff_col] > -tollerance),
            self.config.dfstructure.labels
        ] = 0


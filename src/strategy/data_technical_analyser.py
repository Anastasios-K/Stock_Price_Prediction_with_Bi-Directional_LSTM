from src.config.load_conifg import Configurator
from src.interface.interfaces import TechAnalyser
from src.data_TA_features.simple_moving_avg import simple_movinge_avg
from src.data_TA_features.exponential_moving_avg import exponential_moving_avg
from src.data_TA_features.moving_avg_convergence_divergence import moving_avg_convergence_divergence
from src.data_TA_features.money_flow_index import MFI
import pandas as pd


class DataTechnicalAnalyser(TechAnalyser):
    """ Provides all methods related to the Technical Analysis features. """

    __data: pd.DataFrame
    __config: Configurator

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, value):
        self.__config = value

    def add_sma(self):
        """ Add simple moving average. """
        self.data["SMA"] = simple_movinge_avg(
            data=self.data,
            config=self.config
        )

    def add_ema(self):
        """ Add exponential moving average. """
        self.data["EMA"] = exponential_moving_avg(
            data=self.data,
            config=self.config,
            rolling_window=self.config.techanal.emawindow
        )

    def add_macd(self):
        """ Add moving average convergence divergence. """
        self.data["MACD"] = moving_avg_convergence_divergence(
            data=self.data,
            config=self.config
        )

    def add_mfi(self):
        """ Add money flow index. """
        self.data["MFI"] = MFI(
            data=self.data,
            config=self.config
        ).calc_money_flow_index()

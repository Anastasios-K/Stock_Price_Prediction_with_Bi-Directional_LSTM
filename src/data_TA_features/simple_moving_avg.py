import pandas as pd
from src.config.load_conifg import Config


class SMA:
    """ Simple Moving Average """

    def __init__(self,
                 data: pd.DataFrame,
                 config: Config):

        self.sma = self.__simple_movinge_avg(
            data=data,
            config=config,
        )

    @staticmethod
    def __simple_movinge_avg(data: pd.DataFrame,
                             config: Config) -> pd.DataFrame:
        rolling_window = config.techanal.smawindow
        sma = data[config.dfstructure.close].rolling(rolling_window).mean()
        return sma

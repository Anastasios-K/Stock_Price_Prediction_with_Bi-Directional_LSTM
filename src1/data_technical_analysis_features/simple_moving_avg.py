import pandas as pd


class SMA:
    """ Simple Moving Average """

    def __init__(self,
                 data: pd.DataFrame,
                 config,
                 ):

        self.sma = self.__simple_movinge_avg(
            data=data,
            config=config,
        )

    @staticmethod
    def __simple_movinge_avg(data,
                             config,
                             ):
        rolling_window = config.techanal.smawindow
        sma = data[config.dfstructure.close].rolling(rolling_window).mean()
        return sma

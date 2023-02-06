import pandas as pd


class SMA:
    """ Simple Moving Average """

    def __init__(self,
                 dataframe: pd.DataFrame,
                 config,
                 ):

        self.sma = self.__simple_movinge_avg(
            df=dataframe,
            config=config,
        )

    @staticmethod
    def __simple_movinge_avg(df,
                             config,
                             ):
        rolling_window = config.techanal.smawindow
        sma = df[config.dfstructure.close].rolling(rolling_window).mean()
        return sma

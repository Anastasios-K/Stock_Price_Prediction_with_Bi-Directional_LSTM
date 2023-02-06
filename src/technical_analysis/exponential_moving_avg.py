import numpy as np
import pandas as pd


class EMA:
    """ Exponential Moving Average """

    def __init__(self,
                 dataframe: pd.DataFrame,
                 config,
                 rolling_window
                 ):

        self.ema = self.__exponential_moving_avg(
            df=dataframe,
            config=config,
            rolling_window=rolling_window
        )

    @staticmethod
    def __exponential_moving_avg(df,
                                 config,
                                 rolling_window
                                 ):
        temp_df = df.copy()
        temp_df.loc[:rolling_window, config.dfstructure.close] = np.nan
        temp_df["ema"] = temp_df[config.dfstructure.close].ewm(
            span=rolling_window,
            adjust=False
        ).mean()
        ema = temp_df["ema"]
        return ema

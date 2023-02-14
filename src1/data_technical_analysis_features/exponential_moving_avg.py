import numpy as np
import pandas as pd


class EMA:
    """ Exponential Moving Average """

    def __init__(self,
                 data: pd.DataFrame,
                 config,
                 rolling_window
                 ):

        self.ema = self.__exponential_moving_avg(
            data=data,
            config=config,
            rolling_window=rolling_window
        )

    @staticmethod
    def __exponential_moving_avg(data,
                                 config,
                                 rolling_window
                                 ):
        temp_df = data.copy()
        temp_df.loc[:rolling_window, config.dfstructure.close] = np.nan
        temp_df["ema"] = temp_df[config.dfstructure.close].ewm(
            span=rolling_window,
            adjust=False
        ).mean()
        ema = temp_df["ema"]
        return ema

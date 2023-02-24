import numpy as np
import pandas as pd
from src.config.load_conifg import Configurator


def exponential_moving_average(data: pd.DataFrame, config: Configurator, rolling_window: int):
    """ Exponential Moving Average """
    timestamp_index = data.index[rolling_window]

    temp_df = data.copy()
    temp_df.loc[:timestamp_index, config.dfstructure.close] = np.nan
    temp_df["ema"] = temp_df[config.dfstructure.close].ewm(
        span=rolling_window,
        adjust=False
    ).mean()
    ema = temp_df["ema"]
    return ema


import pandas as pd
from src.config.load_conifg import Configurator


def simple_movinge_avg(data: pd.DataFrame, config: Configurator) -> pd.DataFrame:
    """ Simple Moving Average """
    rolling_window = config.techanal.smawindow
    sma = data[config.dfstructure.close].rolling(rolling_window).mean()
    return sma


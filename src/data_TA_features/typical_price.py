import pandas as pd
from src.config.load_conifg import Configurator


def typical_price(data: pd.DataFrame, config: Configurator):
    """ Typical Price (tp) """
    tp = (
            data[config.dfstructure.close] +
            data[config.dfstructure.high] +
            data[config.dfstructure.low]
    ) / 3

    return tp

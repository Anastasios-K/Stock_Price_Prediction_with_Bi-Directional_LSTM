from src.data_TA_features.moving_avg_convergence_divergence import MACD
from src.config.load_conifg import Configurator
import pandas as pd


def signal(data: pd.DataFrame, config: Configurator) -> pd.DataFrame:
    """ Price Signal """
    macd = MACD(
        data=data,
        config=config
    ).macd

    signal = pd.DataFrame(macd.ewm(
        span=config.techanal.signalwindow,
        adjust=False
    ).mean())
    return signal

from src.data_TA_features.moving_avg_convergence_divergence import moving_avg_convergence_divergence
from src.config.load_conifg import Configurator
import pandas as pd


def signal(data: pd.DataFrame, config: Configurator) -> pd.DataFrame:
    """ Price Signal """
    macd = moving_avg_convergence_divergence(
        data=data,
        config=config
    ).macd

    signal = pd.DataFrame(macd.ewm(
        span=config.techanal.signalwindow,
        adjust=False
    ).mean())
    return signal

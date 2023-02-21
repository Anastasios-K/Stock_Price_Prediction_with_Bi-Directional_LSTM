import pandas as pd
from src.data_TA_features.exponential_moving_avg import exponential_moving_avg
from src.config.load_conifg import Configurator


def moving_avg_convergence_divergence(data: pd.DataFrame, config: Configurator) -> pd.DataFrame:
    """ Moving Average Convergence Divergence """
    ema_short = exponential_moving_avg(
        data=data,
        config=config,
        rolling_window=config.techanal.macdshortwindow
    )

    ema_long = exponential_moving_avg(
        data=data,
        config=config,
        rolling_window=config.techanal.macdlongwindow
    )

    macd = ema_short - ema_long
    return macd


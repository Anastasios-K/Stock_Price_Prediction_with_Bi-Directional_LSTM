import pandas as pd
from src.data_technical_analysis_features.exponential_moving_avg import EMA


class MACD:
    """ Moving Average Convergence Divergence """

    def __init__(self,
                 data: pd.DataFrame,
                 config
                 ):

        self.macd = self.__moving_avg_convergence_divergence(
            data=data,
            config=config
        )

    @staticmethod
    def __moving_avg_convergence_divergence(data,
                                            config,
                                            ):
        ema_short = EMA(
            data=data,
            config=config,
            rolling_window=config.techanal.macdshortwindow
        ).ema

        ema_long = EMA(
            data=data,
            config=config,
            rolling_window=config.techanal.macdlongwindow
        ).ema

        macd = ema_short - ema_long
        return macd

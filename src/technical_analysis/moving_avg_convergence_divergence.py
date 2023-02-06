import pandas as pd
from src.technical_analysis.exponential_moving_avg import EMA


class MACD:
    """ Moving Average Convergence Divergence """

    def __init__(self,
                 dataframe: pd.DataFrame,
                 config
                 ):

        self.macd = self.__moving_avg_convergence_divergence(
            df=dataframe,
            config=config
        )

    @staticmethod
    def __moving_avg_convergence_divergence(df,
                                            config,
                                            ):
        ema_short = EMA(
            dataframe=df,
            config=config,
            rolling_window=config.techanal.macdshortwindow
        ).ema

        ema_long = EMA(
            dataframe=df,
            config=config,
            rolling_window=config.techanal.macdlongwindow
        ).ema

        macd = ema_short - ema_long
        return macd

from src.technical_analysis.exponential_moving_avg import EMA


class MACD:
    """ Moving Average Convergence Divergence """

    def __init__(self,
                 close_price,
                 rolling_window_short=12,
                 rolling_window_long=26
                 ):

        self.macd = self.__moving_avg_convergence_divergence(
            close_price=close_price,
            rolling_window_short=rolling_window_short,
            rolling_window_long=rolling_window_long
        )

    @staticmethod
    def __moving_avg_convergence_divergence(close_price,
                                            rolling_window_short,
                                            rolling_window_long
                                            ):
        ema_short = EMA(
            close_price=close_price,
            rolling_window=rolling_window_short
        ).ema
        ema_long = EMA(
            close_price=close_price,
            rolling_window=rolling_window_long
        ).ema
        macd = ema_short - ema_long
        return macd

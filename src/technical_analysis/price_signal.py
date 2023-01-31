from src.technical_analysis.moving_avg_convergence_divergence import MACD
import pandas as pd


class PS:
    """ Price Signal """

    def __init__(self,
                 close_price,
                 signal_window=9
                 ):

        self.sma = self.__signal(
            close_price=close_price,
            signal_window=signal_window
        )

    @staticmethod
    def __signal(close_price,
                 signal_window: int = 9):
        macd = MACD(
            close_price=close_price
        ).macd

        signal = pd.DataFrame(macd.ewm(span=signal_window, adjust=False).mean())
        return signal
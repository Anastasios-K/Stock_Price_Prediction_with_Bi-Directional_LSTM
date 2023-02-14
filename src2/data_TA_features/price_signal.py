from src.data_TA_features.moving_avg_convergence_divergence import MACD
from src.config.load_conifg import Config
import pandas as pd


class PS:
    """ Price Signal """

    def __init__(self,
                 data: pd.DataFrame,
                 config: Config):

        self.sma = self.__signal(
            data=data,
            config=config
        )

    @staticmethod
    def __signal(data: pd.DataFrame,
                 config: Config) -> pd.DataFrame:
        macd = MACD(
            data=data,
            config=config
        ).macd

        signal = pd.DataFrame(macd.ewm(
            span=config.techanal.signalwindow,
            adjust=False
        ).mean())
        return signal

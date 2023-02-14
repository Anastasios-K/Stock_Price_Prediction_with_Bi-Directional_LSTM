from src.data_technical_analysis_features.moving_avg_convergence_divergence import MACD
import pandas as pd


class PS:
    """ Price Signal """

    def __init__(self,
                 data,
                 config
                 ):

        self.sma = self.__signal(
            data=data,
            config=config
        )

    @staticmethod
    def __signal(data,
                 config,
                 ):
        macd = MACD(
            data=data,
            config=config
        ).macd

        signal = pd.DataFrame(macd.ewm(
            span=config.techanal.signalwindow,
            adjust=False
        ).mean())
        return signal

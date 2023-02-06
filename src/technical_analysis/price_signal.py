from src.technical_analysis.moving_avg_convergence_divergence import MACD
import pandas as pd


class PS:
    """ Price Signal """

    def __init__(self,
                 dataframe,
                 config
                 ):

        self.sma = self.__signal(
            df=dataframe,
            config=config
        )

    @staticmethod
    def __signal(df,
                 config,
                 ):
        macd = MACD(
            dataframe=df,
            config=config
        ).macd

        signal = pd.DataFrame(macd.ewm(
            span=config.techanal.signalwindow,
            adjust=False
        ).mean())
        return signal

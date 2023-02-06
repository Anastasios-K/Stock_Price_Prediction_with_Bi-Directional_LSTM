import pandas as pd
from src.technical_analysis.simple_moving_avg import SMA
from src.technical_analysis.exponential_moving_avg import EMA
from src.technical_analysis.moving_avg_convergence_divergence import MACD
from src.technical_analysis.money_flow_index import MFI


class TechnicalAnalysis:

    def __init__(self,
                 cooked_data: pd.DataFrame,
                 config
                 ):
        self.dataframe = cooked_data
        self.config = config

    def add_sma(self):
        sma = SMA(
            dataframe=self.dataframe,
            config=self.config
        ).sma
        self.dataframe["SMA"] = sma

    def add_ema(self):
        ema = EMA(
            dataframe=self.dataframe,
            config=self.config,
            rolling_window=self.config.techanal.emawindow
        ).ema
        self.dataframe["EMA"] = ema

    def add_macd(self):
        macd = MACD(
            dataframe=self.dataframe,
            config=self.config
        ).macd
        self.dataframe["MACD"] = macd

    def add_mfi(self):
        mfi = MFI(
            dataframe=self.dataframe,
            config=self.config
        ).mfi
        self.dataframe["MFI"] = mfi

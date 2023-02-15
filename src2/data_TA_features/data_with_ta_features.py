from src.data_engineering.engineering_management import DataReady4Analysis
from src.data_TA_features.simple_moving_avg import SMA
from src.data_TA_features.exponential_moving_avg import EMA
from src.data_TA_features.moving_avg_convergence_divergence import MACD
from src.data_TA_features.money_flow_index import MFI


class TaFeaturesAddition:
    """ Add Technical Analysis features into the given data. """
    def __init__(self,
                 obj: DataReady4Analysis,
                 sma=False,
                 ema=False,
                 macd=True,
                 mfi=True):
        if isinstance(obj, DataReady4Analysis):
            pass
        else:
            raise ValueError("Requires DataReady4Analysis object")

        self.data_with_TA_features = obj.data_ready4analysis.copy()
        self.config = obj.config

        if sma:
            self.data_with_TA_features["SMA"] = SMA(
                data=self.data_with_TA_features,
                config=self.config
            ).sma

        if ema:
            self.data_with_TA_features["EMA"] = EMA(
                data=self.data_with_TA_features,
                config=self.config,
                rolling_window=self.config.techanal.emawindow
            ).ema

        if macd:
            self.data_with_TA_features["MACD"] = MACD(
                data=self.data_with_TA_features,
                config=self.config
            ).macd

        if mfi:
            self.data_with_TA_features["MFI"] = MFI(
                data=self.data_with_TA_features,
                config=self.config
            ).mfi

import pandas as pd
from src.config.load_conifg import Config
from src.data_TA_features.simple_moving_avg import SMA
from src.data_TA_features.exponential_moving_avg import EMA
from src.data_TA_features.moving_avg_convergence_divergence import MACD
from src.data_TA_features.money_flow_index import MFI


class TaFeaturesAddition:
    """ Add Technical Analysis features into the given data. """
    def __init__(self,
                 data: pd.DataFrame,
                 config: Config,
                 sma=False,
                 ema=False,
                 macd=True,
                 mfi=True):

        self._data_with_TA_features = data
        self._config = config

        if sma:
            self._data_with_TA_features["SMA"] = SMA(
                data=self._data_with_TA_features,
                config=self._config
            ).sma

        if ema:
            self._data_with_TA_features["EMA"] = EMA(
                data=self._data_with_TA_features,
                config=self._config,
                rolling_window=self._config.techanal.emawindow
            ).ema

        if macd:
            self._data_with_TA_features["MACD"] = MACD(
                data=self._data_with_TA_features,
                config=self._config
            ).macd

        if mfi:
            self._data_with_TA_features["MFI"] = MFI(
                data=self._data_with_TA_features,
                config=self._config
            ).mfi

    @property
    def data_with_ta_features(self):
        return self._data_with_TA_features

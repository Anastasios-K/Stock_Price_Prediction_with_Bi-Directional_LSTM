from src.data_engineering.data_ready4analysis import DataReady4Analysis
from src.data_technical_analysis_features.simple_moving_avg import SMA
from src.data_technical_analysis_features.exponential_moving_avg import EMA
from src.data_technical_analysis_features.moving_avg_convergence_divergence import MACD
from src.data_technical_analysis_features.money_flow_index import MFI


class TaFeaturesAddition:
    def __init__(self,
                 data_ready4analysis: DataReady4Analysis,
                 sma=False,
                 ema=False,
                 macd=True,
                 mfi=True
                 ):
        if isinstance(data_ready4analysis, DataReady4Analysis):
            pass
        else:
            raise ValueError("Expects DataReady4Analysis object")

        self.__data = data_ready4analysis.data_ready4analysis
        self.__config = data_ready4analysis.config

        if sma:
            self.__data["SMA"] = SMA(
                data=self.__data,
                config=self.__config
            ).sma

        if ema:
            self.__data["EMA"] = EMA(
                data=self.__data,
                config=self.__config,
                rolling_window=self.__config.techanal.emawindow
            ).ema

        if macd:
            self.__data["MACD"] = MACD(
                data=self.__data,
                config=self.__config
            ).macd

        if mfi:
            self.__data["MFI"] = MFI(
                data=self.__data,
                config=self.__config
            ).mfi
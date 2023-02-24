from src.interface.interfaces import TechnicalAnalyser
from src.prototype.data_parser import DataParser
from src.prototype.data_explorator import DataExplorator
from src.data_TA_features.simple_moving_avg import simple_movinge_avg
from src.data_TA_features.exponential_moving_avg import exponential_moving_avg
from src.data_TA_features.moving_avg_convergence_divergence import moving_avg_convergence_divergence
from src.data_TA_features.money_flow_index import MFI
from typing import Union


class DataTechnicalAnalyser(TechnicalAnalyser):

    def __init__(self, data_obj: Union[DataParser, DataExplorator]):
        if not isinstance(data_obj, DataParser) or not isinstance(data_obj, DataExplorator):
            TypeError("DataTechnicalAnalyser requires DataParser object or DataExplorator object")
        else:
            self.config = data_obj.config
            self.helper = data_obj.helper
            self.data = data_obj.data

    def add_sma(self):
        self.data["SMA"] = simple_movinge_avg(
            data=self.data,
            config=self.config
        )

    def add_ema(self):
        self.data["EMA"] = exponential_moving_avg(
            data=self.data,
            config=self.config,
            rolling_window=self.config.techanal.emawindow
        )

    def add_macd(self):
        self.data["MACD"] = moving_avg_convergence_divergence(
            data=self.data,
            config=self.config
        )

    def add_mfi(self):
        self.data["MFI"] = MFI(
            data=self.data,
            config=self.config
        ).calc_money_flow_index()

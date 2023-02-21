import pandas as pd
from src.secondary_modules.dir_creator import DirsCreator
from src.data_engineering.fix_data_format import fix_data_format
from src.data_engineering.data_visualisation import DataOverview
from src.config.load_conifg import Config
from src.data_engineering.handle_nan_values import count_nan_values, replace_nan_values
from src.data_engineering.handle_duplicates import count_duplicates, remove_duplicates
from src.data_exploration.plot_distribution import DistributionPlot
from src.data_exploration.eda_pd_profiling import ProfilingEDA
from src.data_exploration.plot_correlation import CorrPlot
from src.data_exploration.plot_autocorrelation import AutocorrPlot
from src.data_TA_features.data_with_ta_features import TaFeaturesAddition
from src.secondary_modules.info_tracker import InfoTracker
from src.secondary_modules.time_id_creator import TimeID
from typing import Union
from dataclasses import dataclass


class FixedDTypeData:
    print("ok")

    def __init__(self):
        self._data = pd.read_csv("data/TSCO.csv")
        self._info = InfoTracker()
        self.update_info(key="time_id", value=123)

    @property
    def data(self):
        return self._data

    # @property
    # def config(self):
    #     return self._config

    @property
    def info(self):
        return self._info

    def update_info(self, key, value):
        self._info.__dict__[key] = value


class NoNanData(FixedDTypeData):
    print("ok2")

    def __init__(self):
        super(NoNanData, self).__init__()
        self.update_info(key="nan_amount", value="tas")
        FixedDTypeData.data["Close"] = 100


    # def update_info(self, key, value):
    #     self._info.__dict__[key] = value
#
# class NoDuplData(FixedDTypeData):
#     print("ok3")
#
#     def __init__(self):
#         self.update_info(key="duplicates_amount", value="kws")
#         self._data["Open"] = 200


# class Ready4AnalysisData(NoDuplData, NoNanData):
#     print("ok4")
#
#     def __init__(self):
        # self.update_info(key="duplicates_amount", value="kws")


CONFIG_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\src\\config\\config.yaml"
config = Config(config_path=CONFIG_PATH)

a = FixedDTypeData()
b = NoNanData()
# c = NoDuplData()
# d = Ready4AnalysisData()





# class FixedDTypeData:
#
#     def __init__(self, obj):
#         if isinstance(obj, FixedDTypeData):
#             self._config = obj._config
#             self._data = obj._data
#             self._info_tracker = obj._info_tracker
#
#         if isinstance(obj, Config):
#             time_id = TimeID().timeid
#             self._config = obj
#             self._data = fix_data_format(
#                 raw_data=pd.read_csv(obj.paths.datapath),
#                 config=obj
#             )
#             self._info_tracker = dict()
#             self._info_tracker.update(dict(time_id=time_id))
#             self._info_tracker.update(dict(stockname=obj.stockname.stockname))
#             # self._info_tracker.time_id = time_id
#             # self._info_tracker.stock_name = obj.stockname.stockname
#
#             DirsCreator(
#                 config=obj,
#                 time_id=time_id
#             )
#         else:
#             raise TypeError
#
#     @property
#     def data(self):
#         return self._data
#
#     @property
#     def info_tracker(self):
#         return self._info_tracker
#
#     @property
#     def config(self):
#         return self._config
#
#     @data.setter
#     def data(self, value):
#         self._data = value
#
#     def add_into_info_tracker(self, key, value):
#         self._info_tracker.update({
#             f"{key}": value
#         })
#
#     def plot_data_various_resolutions(self, title) -> None:
#         DataOverview(data=self._data, config=self._config, title=title)
#
#
# class NoNanData(FixedDTypeData):
#
#     def __init__(self, obj):
#         super().__init__(obj)
#
#         if isinstance(obj, NoNanData):
#             pass
#         elif isinstance(obj, FixedDTypeData):
#             nan_amount = count_nan_values(data=obj._data)
#             FixedDTypeData._config = obj._config
#             obj._data["Close"] = 100
#             self._data = obj._data
#             self.add_into_info_tracker(key="nan_amount", value=554342)
            # FixedDTypeData._data = replace_nan_values(
            #     data=obj._data,
            #     config=obj._config
            # )
            # FixedDTypeData.add_into_info_tracker(self, key="nan_amount", value=nan_amount)



#
# class NoDuplData(FixedDTypeData):
#
#     def __init__(self, obj):
#         super().__init__(obj=obj)
#         if isinstance(obj, NoDuplData):
#             FixedDTypeData._config = obj._config
#             FixedDTypeData._data = obj._data
#             FixedDTypeData._info_tracker = obj._info_tracker
#
#         elif isinstance(obj, FixedDTypeData):
#             dupl_amount = count_duplicates(
#                 data=obj._data,
#                 config=obj._config
#             )
#             FixedDTypeData._test = 3
#             FixedDTypeData._config = obj._config
#             FixedDTypeData._data = remove_duplicates(
#                 data=obj._data,
#                 config=obj._config
#             )
#             FixedDTypeData._info_tracker.duplicates_amount = dupl_amount
#
#
# class Ready4AnalysisData(NoDuplData, NoNanData):
#
#     def __init__(self, obj):
#         super().__init__(obj=obj)
#         if isinstance(obj, Ready4AnalysisData):
#             FixedDTypeData._config = obj._config
#             FixedDTypeData._data = obj._data
#             FixedDTypeData._info_tracker = obj._info_tracker
#
#         elif isinstance(obj, NoNanData) or isinstance(obj, FixedDTypeData):
#             print("edw")
#             dupl_amount = count_duplicates(
#                 data=obj._data,
#                 config=obj._config
#             )
#             FixedDTypeData._config = obj._config
#             FixedDTypeData._data = remove_duplicates(
#                 data=obj._data,
#                 config=obj._config
#             )
#             FixedDTypeData._info_tracker["dsghnfn"] = dupl_amount
#
#         elif isinstance(obj, NoDuplData) or isinstance(obj, FixedDTypeData):
#             print("ekei")
#             nan_amount = count_nan_values(data=obj._data)
#             FixedDTypeData._config = obj._config
#             FixedDTypeData._data = replace_nan_values(
#                 data=obj._data,
#                 config=obj._config
#             )
#             FixedDTypeData._info_tracker["dsgdsbsb"] = nan_amount

        # elif isinstance(obj, FixedDTypeData):
        #     count_nan_values(
        #         data=obj._data,
        #     )
        #     FixedDTypeData._config = obj._config
        #     no_nans_data = replace_nan_values(
        #         data=obj._data,
        #         config=obj._config
        #     )
        #     count_duplicates(
        #         data=obj._data,
        #         config=obj._config
        #     )
        #     FixedDTypeData._data = remove_duplicates(
        #         data=no_nans_data,
        #         config=obj._config
        #     )
        #     FixedDTypeData._test = 4

    def create_eda_report(self, report_name: str = "EDA_Report"):
        ProfilingEDA(
            dataframe=self._data,
            config=self._config,
            report_name=report_name
        )

    def plot_distribution(self, file_name: str = "Data_Distribution"):
        DistributionPlot(
            dataframe=self._data,
            config=self._config,
            file_name=file_name
        )

    def plot_correlation(self, fig_titile: str = "Correlation_Analysis"):
        CorrPlot(
            dataframe=self._data,
            config=self._config,
            fig_title=fig_titile
        )

    def plot_autocorrelation(self):
        AutocorrPlot(
            dataframe=self._data,
            config=self._config
        )

    def add_ta_features(self):
        self._data = TaFeaturesAddition(
            data=self._data,
            config=self._config
        ).data_with_ta_features





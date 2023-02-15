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


class FixedDTypeData:

    def __init__(self, config: Config):
        self._info_tracker = InfoTracker(
            stock_name=config.stockname.stockname,
            time_id=TimeID().timeid
        )
        DirsCreator(
            config=config,
            time_id=self._info_tracker.time_id
        )

        self._config = config
        self._data = fix_data_format(
            raw_data=pd.read_csv(config.paths.datapath),
            config=config
        )

    @property
    def data(self):
        return self._data

    @property
    def config(self):
        return self._config

    @staticmethod
    def plot_data_various_resolutions(data, config, title) -> None:
        DataOverview(data=data, config=config, title=title)


class NoNanData(FixedDTypeData):

    def __init__(self, obj, config: Config):
        FixedDTypeData.__init__(self, config=config)
        if isinstance(obj, NoNanData):
            pass
        elif isinstance(obj, FixedDTypeData):
            count_nan_values(
                data=obj._data,
                config=config
            )
            FixedDTypeData._config = config
            FixedDTypeData._data = replace_nan_values(
                data=obj._data,
                config=config
            )


class NoDuplData(FixedDTypeData):

    def __init__(self, obj, config: Config):
        FixedDTypeData.__init__(self, config=config)
        if isinstance(obj, NoDuplData):
            pass
        elif isinstance(obj, FixedDTypeData):
            count_duplicates(
                data=obj._data,
                config=config
            )
            FixedDTypeData._config = config
            FixedDTypeData._data = remove_duplicates(
                data=obj._data,
                config=config
            )


class Ready4AnalysisData(NoDuplData, NoNanData):

    def __init__(self, obj, config: Config):
        NoDuplData.__init__(self, obj, config)
        NoNanData.__init__(self, obj, config)
        if isinstance(obj, Ready4AnalysisData):
            pass
        elif isinstance(obj, NoNanData):
            count_duplicates(
                data=obj._data,
                config=config
            )
            FixedDTypeData._config = config
            FixedDTypeData._data = remove_duplicates(
                data=obj._data,
                config=config
            )
        elif isinstance(obj, NoDuplData):
            count_nan_values(
                data=obj._data,
                config=config
            )
            FixedDTypeData._config = config
            FixedDTypeData._data = replace_nan_values(
                data=obj._data,
                config=config
            )
        elif isinstance(obj, FixedDTypeData):
            count_nan_values(
                data=obj._data,
                config=config
            )
            FixedDTypeData._config = config
            no_nans_data = replace_nan_values(
                data=obj._data,
                config=config
            )
            count_duplicates(
                data=obj._data,
                config=config
            )
            FixedDTypeData._data = remove_duplicates(
                data=no_nans_data,
                config=config
            )

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





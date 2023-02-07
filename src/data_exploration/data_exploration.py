from src.data_exploration.eda_pd_profiling import ProfilingEDA
from src.data_exploration.plot_correlation import CorrPlot
from src.data_exploration.plot_distribution import DistributionPlot
from src.data_exploration.plot_autocorrelation import AutocorrPlot
from src.abstract.DataReady4AnalysisAbstract import DataReady4AnalysisAbstract


class DataExploration:

    def __init__(self,
                 data_ready4analysis: DataReady4AnalysisAbstract
                 ):
        self.__data = data_ready4analysis.data
        self.__config = data_ready4analysis.config

        if (
                self.__config.dataengin.no_nans and
                self.__config.dataengin.no_dupl
        ) in data_ready4analysis._status:
            pass
        else:
            raise Exception("You have to run both handle_nan_values and handle_duplicates processes")

    def pd_profiling_eda(self,
                         report_name
                         ):
        ProfilingEDA(
            dataframe=self.__data,
            config=self.__config,
            report_name=report_name
        )

    def plot_data_distribution(self):
        DistributionPlot(
            dataframe=self.__data,
            config=self.__config
        )

    def plot_correlation(self,
                         fig_title,
                         corr_method="pearson"
                         ):
        CorrPlot(
            dataframe=self.__data,
            config=self.__config,
            fig_title=fig_title,
            corr_method=corr_method
        )

    def plot_autocorrelations(self):
        AutocorrPlot(
            dataframe=self.__data,
            config=self.__config
        )

from src.data_exploration.eda_pd_profiling import ProfilingEDA
from src.data_exploration.plot_correlation import CorrPlot
from src.data_exploration.plot_distribution import DistributionPlot
from src.data_exploration.plot_autocorrelation import AutocorrPlot
from src.data_engineering.data_ready4analysis import DataReady4Analysis


class DataExploration:

    def __init__(self, data_ready4analysis: DataReady4Analysis):
        if isinstance(data_ready4analysis, DataReady4Analysis):
            pass
        else:
            raise ValueError("Expects DataReady4Analysis object")

        self.__data = data_ready4analysis.data_ready4analysis
        self.__config = data_ready4analysis.config

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

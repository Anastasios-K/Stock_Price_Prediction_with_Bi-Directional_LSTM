import pandas as pd
from src.data_exploration.eda_pd_profiling import ProfilingEDA
from src.data_exploration.plot_correlation import PlotCorrel
from src.data_exploration.plot_distribution import PlotDistributions
from src.data_exploration.plot_autocorrelation import PlotAutocorr


class DataExploration:

    def __init__(self,
                 cooked_data: pd.DataFrame,
                 config):
        self.__dataframe = cooked_data
        self.__config = config

    def pd_profiling_eda(self,
                         report_name
                         ):
        ProfilingEDA(
            dataframe=self.__dataframe,
            config=self.__config,
            report_name=report_name
        )

    def plot_data_distribution(self):
        PlotDistributions(
            dataframe=self.__dataframe,
            config=self.__config
        )

    def plot_correlation(self,
                         fig_title,
                         corr_method="pearson"
                         ):
        PlotCorrel(
            dataframe=self.__dataframe,
            config=self.__config,
            fig_title=fig_title,
            corr_method=corr_method
        )

    def plot_autocorrelations(self):
        PlotAutocorr(
            dataframe=self.__dataframe,
            config=self.__config
        )

from src.data_exploration.eda_pd_profiling import ProfilingEDA
from src.data_exploration.calc_correlation import CalcCorrel
from src.data_exploration.correlation_with_delays import CorrShiftedFeature
from src.data_exploration.plot_distribution import PlotDistributions


class DataExploration:

    def __init__(self,
                 dataframe,
                 config):
        self.__dataframe = dataframe
        self.__config = config

    def pd_profiling_eda(self,
                         report_name
                         ):
        ProfilingEDA(dataframe=self.__dataframe,
                     config=self.__config,
                     report_name=report_name)

    def calc_data_distribution(self):
        PlotDistributions(dataframe=self.__dataframe,
                          config=self.__config)

    def calc_correlation(self,
                         fig_title,
                         corr_method="pearson"
                         ):
        CalcCorrel(dataframe=self.__dataframe,
                   config=self.__config,
                   fig_title=fig_title,
                   corr_method=corr_method)

    def calc_multi_shifted_correlations(self,
                                        corr_method="pearson"
                                        ):
        CorrShiftedFeature(dataframe=self.__dataframe,
                           config=self.__config,
                           corr_method=corr_method)

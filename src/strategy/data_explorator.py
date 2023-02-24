import pandas as pd
from src.config.load_conifg import Configurator
from src.interface.interfaces import Explorator
from src.data_exploration.eda_pd_profiling import create_eda_report
from src.data_exploration.plot_distribution import create_distr_subplots
from src.data_exploration.plot_correlation import CorrPlot
from src.data_exploration.plot_autocorrelation import AutocorrPlot


class DataExplorator(Explorator):
    """ Provides all methods related to data exploration analysis. """

    __data: pd.DataFrame
    __config: Configurator

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, value):
        self.__config = value

    def cerate_eda_report(self, report_name: str):
        """ Create Explanatory Data Analysis Report, using pandas profiling. """
        create_eda_report(
            data=self.__data,
            config=self.__config,
            report_name=report_name
        )

    def plot_distribution(self, fig_title):
        """ Plot distribution for each data feature. """
        create_distr_subplots(
            data=self.__data,
            config=self.__config,
            file_name=fig_title
        )

    def plot_correlation(self, fig_title):
        """ Plot correlation heatmap. """
        CorrPlot(
            data=self.__data,
            config=self.__config,
            fig_title=fig_title
        )

    def plot_autocorrelation(self):
        """ Plot Autocorrelation. """
        AutocorrPlot(
            data=self.__data,
            config=self.__config
        )

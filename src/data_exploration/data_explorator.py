import pandas as pd
from src.config.load_conifg import Configurator
from src.interface.interface import Explorator
from src.data_exploration.plot_multi_resolutions import MultiResolution
from src.data_exploration.eda_pd_profiling import create_eda_report
from src.data_exploration.plot_distribution import create_distr_subplots
from src.data_exploration.plot_correlation import CorrPlot
from src.data_exploration.plot_autocorrelation import AutocorrPlot


class DataExplorator(Explorator):
    """ Provides all methods related to data exploration analysis. """

    def __init__(
            self,
            data: pd.DataFrame,
            config: Configurator,
            unique_id: str
    ):
        self.__data = data
        self.__config = config
        self.__unique_id = unique_id

    def plot_multi_resolution(self, title: str) -> None:
        """ Create and save a plot of different resolutions of the given data. """
        MultiResolution(
            data=self.__data,
            config=self.__config,
            unique_id=self.__unique_id,
            title=title
        )

    def cerate_eda_report(self, report_name: str) -> None:
        """ Create Explanatory Data Analysis Report, using pandas profiling. """
        create_eda_report(
            data=self.__data,
            config=self.__config,
            unique_id=self.__unique_id,
            report_name=report_name
        )

    def plot_distribution(self, fig_title: str) -> None:
        """ Plot distribution for each data feature. """
        create_distr_subplots(
            data=self.__data,
            config=self.__config,
            unique_id=self.__unique_id,
            file_name=fig_title
        )

    def plot_correlation(self, fig_title: str) -> None:
        """ Plot correlation heatmap. """
        CorrPlot(
            data=self.__data,
            config=self.__config,
            unique_id=self.__unique_id,
            fig_title=fig_title
        )

    def plot_autocorrelation(self) -> None:
        """ Plot Autocorrelation. """
        AutocorrPlot(
            data=self.__data,
            config=self.__config,
            unique_id=self.__unique_id
        )

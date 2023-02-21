from src.interface.interfaces import Explorator
from src.prototype.data_parser import DataParser
from src.data_exploration.eda_pd_profiling import create_eda_report
from src.data_exploration.plot_distribution import create_distr_subplots
from src.data_exploration.plot_correlation import CorrPlot
from src.data_exploration.plot_autocorrelation import AutocorrPlot


class DataExplorator(Explorator):

    def __init__(self, data_parser: DataParser):
        if not isinstance(data_parser, DataParser):
            TypeError("DataExplorator requires DataParser object")
        else:
            self.config = data_parser.config
            self.helper = data_parser.helper
            self.data = data_parser.data

    def cerate_eda_report(self, report_name: str):
        create_eda_report(
            data=self.data,
            config=self.config,
            report_name=report_name
        )

    def plot_distribution(self, fig_title):
        create_distr_subplots(
            data=self.data,
            config=self.config,
            file_name=fig_title
        )

    def plot_correlation(self, fig_title):
        CorrPlot(
            data=self.data,
            config=self.config,
            fig_title=fig_title
        )

    def plot_autocorrelation(self):
        AutocorrPlot(
            data=self.data,
            config=self.config
        )

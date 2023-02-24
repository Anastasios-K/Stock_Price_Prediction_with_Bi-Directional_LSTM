from abc import ABC, abstractmethod


class Explorator(ABC):

    @abstractmethod
    def plot_multi_resolution(self, title):
        pass

    @abstractmethod
    def cerate_eda_report(self, report_name):
        pass

    @abstractmethod
    def plot_distribution(self, file_name):
        pass

    @abstractmethod
    def plot_correlation(self, fig_title):
        pass

    @abstractmethod
    def plot_autocorrelation(self):
        pass

#
# class TechAnalyser(ABC):
#
#     @staticmethod
#     @abstractmethod
#     def calc_sma(data, config):
#         pass
#
#     @staticmethod
#     @abstractmethod
#     def add_ema(data, config):
#         pass
#
#     @staticmethod
#     @abstractmethod
#     def add_macd(data, config):
#         pass
#
#     @staticmethod
#     @abstractmethod
#     def add_mfi(data, config):
#         pass


class Creator(ABC):

    @abstractmethod
    def _calc_price_difference(self, data, config):
        pass

    @abstractmethod
    def create_labels(self, data, config):
        pass

    @abstractmethod
    def create_label_weights(self, labels):
        pass


class Builder(ABC):

    @abstractmethod
    def _reshape_data(self):
        pass

    @abstractmethod
    def _build_model(self, hp):
        pass

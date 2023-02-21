from abc import ABC, abstractmethod


class Explorator(ABC):

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


class TechAnalyser(ABC):

    @abstractmethod
    def add_sma(self):
        pass

    @abstractmethod
    def add_ema(self):
        pass

    @abstractmethod
    def add_macd(self):
        pass

    @abstractmethod
    def add_mfi(self):
        pass


class Creator(ABC):

    @abstractmethod
    def _calc_price_difference(self):
        pass

    @abstractmethod
    def create_labels(self):
        pass

    @abstractmethod
    def create_label_weights(self, labels):
        pass


class Learner(ABC):

    @abstractmethod
    def scale_data(self):
        pass

    @abstractmethod
    def build_model(self):
        pass

    @abstractmethod
    def train_model(self):
        pass

    @abstractmethod
    def test_model(self):
        pass

    @abstractmethod
    def track_model(self):
        pass



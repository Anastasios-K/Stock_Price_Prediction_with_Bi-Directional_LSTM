from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def _read_data(self):
        pass

    @abstractmethod
    def _fix_data_format(self):
        pass

    @abstractmethod
    def _handle_nan_values(self):
        pass

    @abstractmethod
    def _handle_duplicates(self):
        pass


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


class TechnicalAnalyser(ABC):

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


class Preparator(ABC):

    @abstractmethod
    def create_labels(self):
        pass

    @abstractmethod
    def drop_nans(self):
        pass

    @abstractmethod
    def drop_unused_features(self):
        pass

    @abstractmethod
    def split_train_test(self):
        pass

    @abstractmethod
    def scale_data(self):
        pass


class Builder(ABC):

    @abstractmethod
    def reshape_data(self):
        pass

    @abstractmethod
    def build_model(self):
        pass

    @abstractmethod
    def init_tuner(self):
        pass


class Trainer(ABC):

    @abstractmethod
    def train_model(self):
        pass


class Tester(ABC):

    @abstractmethod
    def collect_best_models(self):
        pass

    @abstractmethod
    def predict_with_best_model(self):
        pass

    @abstractmethod
    def calc_performance_metrics(self):
        pass


class Tracker(ABC):

    @abstractmethod
    def track_project_params(self):
        pass

    @abstractmethod
    def track_hyper_params(self):
        pass

    @abstractmethod
    def performance_metrics(self):
        pass

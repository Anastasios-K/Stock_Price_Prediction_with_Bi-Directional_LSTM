from abc import ABC, abstractmethod


class DataReady4AnalysisAbstract(ABC):

    _status = None

    @abstractmethod
    def __init__(self, data, config):
        self.data = data
        self.config = config
        pass

    @abstractmethod
    def handle_nan_values(self):
        pass

    @abstractmethod
    def handle_duplicates(self):
        pass

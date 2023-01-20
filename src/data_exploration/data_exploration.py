from src.data_exploration.EDA_pd_profiling import ProfilingEDA


class DataExploration:

    def __init__(self, data):
        self.data_exploration = ProfilingEDA(dataframe=data)
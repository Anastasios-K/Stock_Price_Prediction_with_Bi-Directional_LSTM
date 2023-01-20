from src.data_engineering.s1_collect_data import GetData


class DataEngineering:

    def __init__(self, config):
        self.data_engineering = GetData(config=config)\
            .handle_nan_values()\
            .handle_duplicates()\
            .fix_data_types()\
            .plot_data()
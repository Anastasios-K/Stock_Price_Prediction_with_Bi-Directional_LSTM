from src.data_engineering.handle_nan_values import HandleNanValues
from src.data_engineering.handle_duplicates import HandleDuplicates
from src.data_engineering.validate_data_types import HandleDataTypes
from src.data_engineering.plot_data import PlotData
from src.data_engineering.set_timestamp_as_index import SetIndex


class DataEngineering:

    def __init__(self,
                 dataframe,
                 config):
        self.dataframe = dataframe
        self.config = config

    def handle_nan_values(self):
        obj = HandleNanValues(
            dataframe=self.dataframe,
            config=self.config
        )
        self.dataframe = obj.df

    def handle_duplicates(self):
        obj = HandleDuplicates(
            dataframe=self.dataframe,
            config=self.config
        )
        self.dataframe = obj.df

    def handle_data_types(self):
        obj = HandleDataTypes(
            dataframe=self.dataframe,
            config=self.config
        )
        self.dataframe = obj.df

    def plot_data(self,
                  specific_file_name: str = ""
                  ):
        obj = PlotData(
            dataframe=self.dataframe,
            config=self.config,
            specific_file_name=specific_file_name
        )
        self.dataframe = obj.df

    def set_time_as_index(self):
        obj = SetIndex(
            dataframe=self.dataframe,
            config=self.config
        )
        self.dataframe = obj.df

from src.data_engineering.handle_nan_values import HandleNanValues
from src.data_engineering.handle_duplicates import HandleDuplicates
from src.data_engineering.handle_data_types import HandleDataTypes
from src.data_engineering.plot_diff_data_resolutions import DataResolution


class DataEngineering:
    """
    Gather all data engineering methods.
    """

    def __init__(self,
                 dataframe,
                 config):
        self.dataframe = dataframe
        self.config = config

    def handle_data_types(self):
        obj = HandleDataTypes(
            dataframe=self.dataframe,
            config=self.config
        )
        self.dataframe = obj.df

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

    def plot_diff_df_resolutions(self, fig_title):
        obj = DataResolution(
            dataframe=self.dataframe,
            config=self.config,
            fig_title=fig_title
        )
        self.dataframe = obj.df

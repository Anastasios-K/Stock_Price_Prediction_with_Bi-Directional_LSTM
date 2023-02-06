from src.data_engineering.handle_nan_values import HandleNanValues
from src.data_engineering.handle_duplicates import HandleDuplicates
from src.data_engineering.handle_data_types import HandleDataTypes
from src.data_engineering.plot_diff_data_resolutions import DataResolution
from src.data_exploration.data_exploration import DataExploration
from src.technical_analysis.technical_analysis import TechnicalAnalysis


class DataEngineering:
    """
    Gather all data engineering methods.
    """

    def __init__(self,
                 row_data,
                 config
                 ):
        self.dataframe = row_data
        self.config = config

    def handle_data_types(self):
        obj = HandleDataTypes(
            row_data=self.dataframe,
            config=self.config
        )
        self.dataframe = obj.cooked_data

    def handle_nan_values(self):
        obj = HandleNanValues(
            row_data=self.dataframe,
            config=self.config
        )
        self.dataframe = obj.cooked_data

    def handle_duplicates(self):
        obj = HandleDuplicates(
            row_data=self.dataframe,
            config=self.config
        )
        self.dataframe = obj.cooked_data

    def plot_diff_df_resolutions(self, fig_title):
        obj = DataResolution(
            row_data=self.dataframe,
            config=self.config,
            fig_title=fig_title
        )
        self.dataframe = obj.cooked_data

    def data_exploration(self):
        return DataExploration(cooked_data=self.dataframe,
                               config=self.config)

    def technical_analysis(self):
        return TechnicalAnalysis(cooked_data=self.dataframe,
                                 config=self.config)

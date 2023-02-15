from src.data_engineering.handle_duplicates import DataWithoutDuplicates
from src.data_engineering.handle_nan_values import DataWithoutNans


class DataReady4Analysis(DataWithoutNans, DataWithoutDuplicates):
    """ Derived class. Provides the data ready for analysis, without NaNs and duplicates"""

    def __init__(self, data_getter_fixer_obj):

        super().__init__(data_getter_fixer=data_getter_fixer_obj)
        self.data_ready4analysis = self.remove_duplicates(data=self.data_without_nans)
        self.plot_all_resolutions(data=self.data_ready4analysis, title="Data_Ready_for_Analysis")
        del self.data_without_dupls
        del self.data_without_nans

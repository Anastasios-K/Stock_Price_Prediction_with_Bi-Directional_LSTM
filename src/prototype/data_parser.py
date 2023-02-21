import pandas as pd
from src.interface.interfaces import Parser
from src.config.load_conifg import Configurator
from src.data_engineering.fix_data_format import fix_data_format
from src.data_engineering.handle_nan_values import count_nan_values, replace_nan_values
from src.data_engineering.handle_duplicates import count_duplicates, remove_duplicates
from src.data_engineering.data_visualisation import DataOverview
from src.helper.helper import Helper


class DataParser(Parser):
    """
    Protected Methods:
    Read data.
    Fix data types.
    Count NaN values and duplicates.
    Store amount of NaN values and duplicates into the Helper.info_tracker object.
    Handle NaN values and duplicates.

    Public Method:
    Plot various data frequencies.
    """

    def __init__(self, config: Configurator, helper: Helper):
        if not isinstance(config, Configurator) or not isinstance(helper, Helper):
            TypeError("DataParser requires Configurator object and Helper object")
        else:
            self.config = config
            self.helper = helper
            self.data = self._read_data()
            self._fix_data_format()
            self._handle_nan_values()
            self._handle_duplicates()

    def _read_data(self) -> pd.DataFrame:
        """ Read data. """
        return pd.read_csv(self.config.paths.datapath)

    def _fix_data_format(self):
        """ Fix data format. """
        self.data = fix_data_format(
            raw_data=self.data,
            config=self.config
        )

    def _handle_nan_values(self):
        """ Handle NaN values. """
        self.helper.update_info_tracker(info={
            "nan_values": count_nan_values(data=self.data)
        })
        self.data = replace_nan_values(
            data=self.data,
            config=self.config
        )

    def _handle_duplicates(self):
        """ Handle Duplicates. """
        self.helper.update_info_tracker(info={
            "duplicates": count_duplicates(
                data=self.data,
                config=self.config
            )
        })
        self.data = remove_duplicates(
            data=self.data,
            config=self.config
        )

    def plot_various_frequencies(self):
        """ Plot various frequencies of the givven data. """
        DataOverview(
            data=self.data,
            config=self.config
        )


# conf_path = "src\\config\\config.yaml"
# config = Configurator(conf_path)
# helpp = Helper()
# xxx = DataParser(config=config, helper=helpp)

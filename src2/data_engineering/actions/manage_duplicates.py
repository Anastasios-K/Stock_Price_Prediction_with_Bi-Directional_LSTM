import pandas as pd
from src.config.load_conifg import Config
from src.secondary_modules.report_saving import ReportSaving
from src.secondary_modules.time_id_creator import TimeID


class DuplicateRemoval:
    """ Intermediate class.  Counts and Removes duplicates based on the "Date" feature. """

    def __init__(self,
                 data: pd.DataFrame,
                 config: Config):
        self.config = config
        self.__count_duplicates(data=data)
        self.no_dupl_data = self.__remove_duplicates(data=data)

    def __set_date_index(self, data: pd.DataFrame) -> pd.DataFrame:
        """ Set Date feature as """
        config = self.config
        data[config.dfstructure.date] = data.index
        return data

    def __count_duplicates(self, data: pd.DataFrame) -> None:
        config = self.config
        data = self.__set_date_index(data=data)
        path2save = (
                config.dirs2make.reports +
                config.modelname.modelname
        )
        dupli_amount = data[config.dfstructure.date].duplicated(False).sum()

        ReportSaving(
            path2save=path2save,
            data=list(str(dupli_amount)),
            title="Duplicates"
        )

    def __remove_duplicates(self, data: pd.DataFrame) -> pd.DataFrame:
        config = self.config
        data = self.__set_date_index(data=data)
        data.drop_duplicates(
            subset="Date",
            keep="first",
            inplace=True
        )
        data.drop(
            columns=[config.dfstructure.date],
            inplace=True
        )
        return data

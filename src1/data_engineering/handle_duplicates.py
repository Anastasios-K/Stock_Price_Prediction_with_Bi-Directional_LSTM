import pandas as pd
from src.secondary_modules.report_saving import ReportSaving


class DataWithoutDuplicates:
    """ Intermediate class.  Counts and Removes duplicates based on the "Date" feature. """

    def __init__(self, data_getter_fixer):

        data = data_getter_fixer.fixed_format_data
        self.config = data_getter_fixer.config
        super().__init__(data_getter_fixer=data_getter_fixer)

        self.__count_duplicates(data=data)
        self.data_without_dupls = self.remove_duplicates(data=data)

    def __set_date_index(self, data):
        data[self.config.dfstructure.date] = data.index
        return data

    def __count_duplicates(self, data: pd.DataFrame):
        data = self.__set_date_index(data=data)
        config = self.config
        path2save = config.dirs2make.reports
        dupli_amount = data[config.dfstructure.date].duplicated(False).sum()

        ReportSaving(
            path2save=path2save,
            data=list(str(dupli_amount)),
            title="Duplicates"
        )

    def remove_duplicates(self, data: pd.DataFrame):
        data = self.__set_date_index(data=data)
        config = self.config
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

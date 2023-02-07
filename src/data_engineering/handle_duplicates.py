import pandas as pd
from src.secondary_modules.save_report import SaveReport


class DataWithoutDuplicates:

    def __init__(self,
                 data: pd.DataFrame,
                 config
                 ):

        data[config.dfstructure.date] = data.index

        self.__count_duplicates(
            data=data,
            config=config,
        )
        self.cooked_data = self.__remove_duplicates(
            data=data,
            config=config
        )

    @staticmethod
    def __count_duplicates(data: pd.DataFrame,
                           config
                           ):
        path2save = config.dirs2make.reports
        dupli_amount = data[config.dfstructure.date].duplicated(False).sum()

        SaveReport(
            path2save=path2save,
            data=list(str(dupli_amount)),
            title="Duplicates"
        )

    @staticmethod
    def __remove_duplicates(data: pd.DataFrame,
                            config
                            ):
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

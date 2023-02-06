import pandas as pd
from src.secondary_modules.save_report import SaveReport
from src.data_engineering.handle_data_types import HandleDataTypes


class HandleDuplicates:

    def __init__(self,
                 row_data: pd.DataFrame,
                 config,
                 report_title: str = "Duplicates"
                 ):
        cooked_data = HandleDataTypes(
            row_data=row_data,
            config=config
        ).cooked_data
        cooked_data[config.dfstructure.date] = cooked_data.index

        self.__count_duplicates(
            cooked_data=cooked_data,
            config=config,
            title=report_title
        )
        self.cooked_data = self.__remove_duplicates(
            cooked_data=cooked_data,
            config=config
        )

    @staticmethod
    def __count_duplicates(cooked_data: pd.DataFrame,
                           config,
                           title
                           ):
        path2save = config.dirs2make.reports
        dupli_amount = cooked_data[config.dfstructure.date].duplicated(False).sum()

        SaveReport(
            path2save=path2save,
            data=list(str(dupli_amount)),
            title=title
        )

    @staticmethod
    def __remove_duplicates(cooked_data: pd.DataFrame,
                            config
                            ):
        cooked_data.drop_duplicates(
            subset="Date",
            keep="first",
            inplace=True
        )
        cooked_data.drop(
            columns=[config.dfstructure.date],
            inplace=True
        )
        return cooked_data

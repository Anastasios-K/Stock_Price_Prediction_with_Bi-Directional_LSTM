import pandas as pd
from src.secondary_modules.save_report import SaveReport
from src.data_engineering.handle_data_types import HandleDataTypes


class HandleNanValues:
    """
    Count Nan values and record them in the project report.
    Fill in Nan values with a predetermined method (change method in config).
    """

    def __init__(self,
                 row_data: pd.DataFrame,
                 config,
                 report_title: str = "Nan Values"
                 ):
        cooked_data = HandleDataTypes(
            row_data=row_data,
            config=config
        ).cooked_data

        self.__count_nan_values(
            cooked_data=cooked_data,
            config=config,
            title=report_title
        )
        self.cooked_data = self.__replace_nan(
            cooked_data=cooked_data,
            config=config,
        )

    @staticmethod
    def __count_nan_values(cooked_data: pd.DataFrame,
                           config,
                           title):
        path2save = config.dirs2make.reports
        nan_amount = [
            f"{col}: {cooked_data[col].isna().sum()}"
            for col
            in cooked_data.columns
        ]
        SaveReport(
            path2save=path2save,
            data=nan_amount,
            title=title
        )

    @staticmethod
    def __replace_nan(cooked_data: pd.DataFrame,
                      config
                      ):

        if config.dataengin.fill_method == "polynomial":
            [
                cooked_data[col].interpolate(
                    method=config.dataengin.fill_method,
                    order=config.dataengin.poly_order,
                    direction="both",
                    inplace=True
                )
                for col
                in cooked_data.columns
            ]

        elif config.dataengin.fill_method == "linear":
            [
                cooked_data[col].interpolate(
                    method=config.dataengin.fill_method,
                    direction="both",
                    inplace=True
                )
                for col
                in cooked_data.columns
            ]

        else:
            raise ValueError("An invalid fill method is given.")

        return cooked_data

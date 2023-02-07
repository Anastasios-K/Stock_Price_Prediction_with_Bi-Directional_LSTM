import pandas as pd
from src.secondary_modules.save_report import SaveReport


class DataWithoutNans:
    """
    Count Nan values and record them in the project report.
    Fill in Nan values with a predetermined method (change method in config).
    """

    def __init__(self,
                 data: pd.DataFrame,
                 config,
                 ):

        self.__count_nan_values(
            data=data,
            config=config
        )
        self.cooked_data = self.__replace_nan(
            data=data,
            config=config,
        )

    @staticmethod
    def __count_nan_values(data: pd.DataFrame,
                           config
                           ):
        path2save = config.dirs2make.reports
        nan_amount = [
            f"{col}: {data[col].isna().sum()}"
            for col
            in data.columns
        ]
        SaveReport(
            path2save=path2save,
            data=nan_amount,
            title="Nan Values"
        )

    @staticmethod
    def __replace_nan(data: pd.DataFrame,
                      config
                      ):

        if config.dataengin.fill_method == "polynomial":
            [
                data[col].interpolate(
                    method=config.dataengin.fill_method,
                    order=config.dataengin.poly_order,
                    direction="both",
                    inplace=True
                )
                for col
                in data.columns
            ]

        elif config.dataengin.fill_method == "linear":
            [
                data[col].interpolate(
                    method=config.dataengin.fill_method,
                    direction="both",
                    inplace=True
                )
                for col
                in data.columns
            ]

        else:
            raise ValueError("An invalid fill method is given.")

        return data

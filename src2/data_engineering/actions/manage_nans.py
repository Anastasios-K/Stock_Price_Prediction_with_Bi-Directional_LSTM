import pandas as pd
from src.config.load_conifg import Config
from src.secondary_modules.report_saving import ReportSaving


class NanReplacement:
    """ Counts NaN values and fills them in by a predetermined method (change method in config). """

    def __init__(self,
                 data: pd.DataFrame,
                 config: Config):
        self.config = config
        self.no_nan_data = self.__replace_nan(data=data)
        self.__count_nan_values(data=data)

    def __count_nan_values(self, data: pd.DataFrame) -> None:
        config = self.config
        path2save = config.dirs2make.reports
        nan_amount = [
            f"{col}: {data[col].isna().sum()}"
            for col
            in data.columns
        ]
        ReportSaving(
            path2save=path2save,
            data=nan_amount,
            title="Nan Values"
        )

    def __replace_nan(self, data: pd.DataFrame) -> pd.DataFrame:
        config = self.config
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

import pandas as pd
from src.secondary_modules.report_saving import ReportSaving


class DataWithoutNans:
    """ Intermediate Class. Counts NaN values and fills them in a predetermined method (change method in config). """

    def __init__(self, data_getter_fixer):
        data = data_getter_fixer.fixed_format_data
        self.config = data_getter_fixer.config
        super().__init__(data_getter_fixer=data_getter_fixer)

        self.__count_nan_values(data=data)
        self.data_without_nans = self.replace_nan(data=data)

    def __count_nan_values(self, data: pd.DataFrame):
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

    def replace_nan(self, data: pd.DataFrame):
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

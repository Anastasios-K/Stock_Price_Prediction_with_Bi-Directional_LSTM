import pandas as pd
from src.secondary_modules.report_saving import ReportSaving
from src.data_management.data_management import FixedDTypeData


class DataProvider:

    def __init__(self, config):
        self.__raw_data = pd.read_csv(config.paths.datapath)
        self.__config = config

        self.fixed_dtype_data_obj: FixedDTypeData = FixedDTypeData()
        self.fixed_dtype_data_obj.config = self.__config
        self.fixed_dtype_data_obj.fixed_dtype_data = self.__fix_data_format()

    def __fix_data_format(self) -> pd.DataFrame:
        raw_data = self.__raw_data
        config = self.__config

        for col in raw_data.columns:
            if col == config.dfstructure.date:
                raw_data[col] = pd.to_datetime(raw_data[col])

                raw_data.set_index(
                    config.dfstructure.date,
                    inplace=True
                )

            else:
                raw_data[col] = pd.to_numeric(raw_data[col])

        fixed_data = raw_data.copy()

        # prepare list for reporting
        types = fixed_data.dtypes
        attributes = list(types.index)
        types = list(types)

        reporting_list = [
            attr + " - " + str(localtype)
            for attr, localtype
            in zip(attributes, types)
        ]
        ReportSaving(
            data=reporting_list,
            title="Dtypes",
            path2save=config.dirs2make.reports
        )
        return fixed_data

import pandas as pd
from src.secondary_modules.save_report import SaveReport


class DataGetter(object):

    def __init__(self, config):
        self.fixed_format_data = self.__fix_data_format(
            raw_data=pd.read_csv(config.paths.datapath),
            config=config
        )

    @staticmethod
    def __fix_data_format(raw_data: pd.DataFrame, config) -> pd.DataFrame:

        for col in raw_data.columns:
            if col == config.dfstructure.date:
                raw_data[col] = pd.to_datetime(raw_data[col])

                raw_data.set_index(
                    config.dfstructure.date,
                    inplace=True
                )

            else:
                raw_data[col] = pd.to_numeric(raw_data[col])

        # prepare list for reporting
        types = raw_data.dtypes
        attributes = list(types.index)
        types = list(types)

        reporting_list = [
            attr + " - " + str(localtype)
            for attr, localtype
            in zip(attributes, types)
        ]
        SaveReport(
            data=reporting_list,
            title="Dtypes",
            path2save=config.dirs2make.reports
        )
        cooked_data = raw_data
        return cooked_data

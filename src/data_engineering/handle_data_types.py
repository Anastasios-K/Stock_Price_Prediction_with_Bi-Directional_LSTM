import pandas as pd
from src.secondary_modules.save_report import SaveReport


class HandleDataTypes:

    def __init__(self,
                 row_data: pd.DataFrame,
                 config,
                 title: str = "Dtypes"
                 ):
        self.cooked_data = self.__fix_data_types(
            row_data=row_data,
            config=config,
            title=title
        )

    @staticmethod
    def __fix_data_types(row_data,
                         config,
                         title
                         ):

        for col in row_data.columns:
            if col == config.dfstructure.date:
                row_data[col] = pd.to_datetime(row_data[col])

                row_data.set_index(
                    config.dfstructure.date,
                    inplace=True
                )

            else:
                row_data[col] = pd.to_numeric(row_data[col])

        # prepare list for reporting
        types = row_data.dtypes
        attributes = list(types.index)
        types = list(types)

        reporting_list = [
            attr + " - " + str(localtype)
            for attr, localtype
            in zip(attributes, types)
        ]
        SaveReport(
            data=reporting_list,
            title=title,
            path2save=config.dirs2make.reports
        )
        cooked_data = row_data
        return cooked_data

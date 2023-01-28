import pandas as pd
from src.secondary_modules.save_report import SaveReport


class HandleDataTypes:

    def __init__(self,
                 dataframe,
                 config,
                 title: str = "Dtypes"
                 ):
        self.df = self.__fix_data_types(
            df=dataframe,
            config=config,
            title=title
        )

    @staticmethod
    def __fix_data_types(df,
                         config,
                         title
                         ):

        for col in df.columns:
            if col == config.dfstructure.date:
                df[col] = pd.to_datetime(df[col])
            else:
                df[col] = pd.to_numeric(df[col])

        # prepare list for reporting
        types = df.dtypes
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
        return df

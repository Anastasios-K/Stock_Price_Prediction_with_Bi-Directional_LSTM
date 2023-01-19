import pandas as pd
from src.secondary_modules.save_report import SaveReport
from src.data_engineering.s5_validate_data_continuity import FixContinuity


class FixDataType:

    def __init__(self,
                 dataframe,
                 title: str = "Dtypes"):
        self.df = self.__fix_data_types(
            df=dataframe,
            title=title)

    @staticmethod
    def __fix_data_types(df, title):
        for col in df.columns:
            if col == "Date":
                df[col] = pd.to_datetime(df[col])
            else:
                df[col] = pd.to_numeric(df[col])

        # prepare list for reporting
        types = df.dtypes
        idxs = list(types.index)
        vals = list(types)
        reporting_list = [name + " - " + str(type) for name, type in zip(idxs, vals)]
        SaveReport(data=reporting_list, title=title)
        return df

    def validate_continiuty(self):
        return FixContinuity(dataframe=self.df)

import pandas as pd
from src.secondary_modules.save_report import SaveReport
from src.data_engineering.s5_plot_data import PlotData


class FixDataType:

    def __init__(self,
                 dataframe,
                 config,
                 title: str = "Dtypes"):
        self.config = config
        self.df = self.__fix_data_types(
            df=dataframe,
            title=title)

    def __fix_data_types(self, df, title):
        for col in df.columns:
            if col == self.config.dfstructure.date:
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
            path2save=self.config.dirs2make.reports
        )
        return df

    def plot_data(self):
        return PlotData(df=self.df,
                        config=self.config)

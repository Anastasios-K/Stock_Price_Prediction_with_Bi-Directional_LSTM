import pandas as pd
from src.secondary_modules.save_report import SaveReport
from src.data_engineering.s6_plot_data import PlotData


class FixContinuity:

    def __init__(self,
                 dataframe,
                 title: str = "Discontinuity"):
        self.df = self.__fix_continutity_index(df=dataframe,
                                               title=title)

    @staticmethod
    def __validate_datatimes_gaps(df):
        """
        Calculate the datetime gap between the rows.
        Validate if gaps are equal to one day.
        Based on the following method the first row is always missing.
        """
        times_gaps = df["Date"] - df["Date"].shift(1)
        day_gaps = [pd.Timedelta(1, "d") == gap for gap in times_gaps]
        return day_gaps

    @staticmethod
    def __create_row(df, idx):
        """
        Create row (as dataframe type) based on the original dataframe and the index of the missing row.
        """
        missing_datetime = df.loc[idx, "Date"] - pd.Timedelta(1, "d")
        row = pd.DataFrame(columns=df.columns)
        row.loc[0, "Date"] = missing_datetime
        return row

    def __fix_continutity_index(self, df, title):
        # calculate datetime gaps
        gaps = self.__validate_datatimes_gaps(df=df)
        # detect missing row indexes
        idxs = [i for i in range(len(gaps)) if gaps[i] is False]
        # create new rows for missing rows - skip first row because of "__validate_datatimes_gaps" method
        missing_rows = [
            self.__create_row(df=df, idx=i)
            for i in idxs
            if i > 0
        ]

        if len(idxs) > 1:
            # concat orginal df and new rows, sort by date, reset index
            missing_rows = pd.concat(missing_rows)
            df = pd.concat([df, missing_rows])
            df.sort_values(by="Date", inplace=True)
            df.reset_index(inplace=True)

            SaveReport(data=idxs, title=title)
        else:
            SaveReport(data=["Discontiniuty does NOT exist"], title=title)

        return df

    def plot_data(self):
        attributes = ["Open", "Close", "High", "Low"]
        currencies = ["BTC", "ETH", "LTC", "ADA"]
        PlotData(self.df, currencies=currencies, attributes=attributes)


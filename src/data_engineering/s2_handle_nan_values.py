from src.secondary_modules.save_report import SaveReport
from src.data_engineering.s3_handle_duplicates import HandleDuplicates


class HandleNanValues:

    def __init__(self,
                 dataframe,
                 report_title: str = "Nan Values"):
        self.df = self.__replace_nan_with_avg(
            df=dataframe,
            title=report_title)

    @staticmethod
    def __count_nan_values(df, title):
        nan_amount = [
            f"{col}: {df[col].isna().sum()}"
            for col in df.columns
        ]
        SaveReport(
            data=nan_amount,
            title=title
        )
        return nan_amount

    def __replace_nan_with_avg(self, df, title):
        df.set_index("Date", inplace=True)
        nan_amount = self.__count_nan_values(df=df, title=title)

        fwd = df.copy()
        fwd.fillna(
            method="ffill",
            axis=0,
            inplace=True
        )

        bwd = df.copy()
        bwd.fillna(
            method="bfill",
            axis=0,
            inplace=True
        )
        final_df = (fwd + bwd) / 2
        final_df.reset_index(inplace=True)
        return final_df

    def hundle_duplicates(self):
        return HandleDuplicates(dataframe=self.df)


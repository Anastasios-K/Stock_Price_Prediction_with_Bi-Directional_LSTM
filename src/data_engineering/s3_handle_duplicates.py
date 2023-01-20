from src.secondary_modules.save_report import SaveReport
from src.data_engineering.s4_validate_data_types import FixDataType


class HandleDuplicates:

    def __init__(self,
                 dataframe,
                 config,
                 report_title: str = "Duplicates"):
        self.config = config
        self.df = self.__remove_duplicates(df=dataframe,
                                           title=report_title)

    def __count_duplicates(self,
                           df,
                           title):
        dupli_amount = df["Date"].duplicated(False).sum()
        SaveReport(
            path2save=self.config.dirs2make.reports,
            data=list(str(dupli_amount)),
            title=title
        )
        return dupli_amount

    def __remove_duplicates(self,
                            df,
                            title):
        dupli_amount = self.__count_duplicates(
            df=df,
            title=title
        )

        df.drop_duplicates(
            subset="Date",
            keep="first",
            inplace=True
        )
        return df

    def fix_data_types(self):
        return FixDataType(dataframe=self.df,
                           config=self.config)

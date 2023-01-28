from src.secondary_modules.save_report import SaveReport
# from src.data_engineering.s4_validate_data_types import FixDataType


class HandleDuplicates:

    def __init__(self,
                 dataframe,
                 config,
                 report_title: str = "Duplicates"
                 ):
        duplicates_quant = self.__count_duplicates(
            df=dataframe,
            config=config,
            title=report_title
        )
        self.df = self.__remove_duplicates(
            df=dataframe,
            duplicates_quant=duplicates_quant
        )

    @staticmethod
    def __count_duplicates(df,
                           config,
                           title
                           ):
        path2save = config.dirs2make.reports
        dupli_amount = df["Date"].duplicated(False).sum()

        SaveReport(
            path2save=path2save,
            data=list(str(dupli_amount)),
            title=title
        )
        return dupli_amount

    @staticmethod
    def __remove_duplicates(df,
                            duplicates_quant
                            ):
        duplicates_quant = duplicates_quant

        # douplicate condition is missing - coming soon

        df.drop_duplicates(
            subset="Date",
            keep="first",
            inplace=True
        )
        return df

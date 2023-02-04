from src.secondary_modules.save_report import SaveReport


class HandleDuplicates:

    def __init__(self,
                 dataframe,
                 config,
                 report_title: str = "Duplicates"
                 ):
        dataframe[config.dfstructure.date] = dataframe.index

        self.__count_duplicates(
            df=dataframe,
            config=config,
            title=report_title
        )
        self.df = self.__remove_duplicates(
            df=dataframe,
            config=config
        )

    @staticmethod
    def __count_duplicates(df,
                           config,
                           title
                           ):
        path2save = config.dirs2make.reports
        dupli_amount = df[config.dfstructure.date].duplicated(False).sum()

        SaveReport(
            path2save=path2save,
            data=list(str(dupli_amount)),
            title=title
        )

    @staticmethod
    def __remove_duplicates(df,
                            config
                            ):
        df.drop_duplicates(
            subset="Date",
            keep="first",
            inplace=True
        )
        df.drop(
            columns=[config.dfstructure.date],
            inplace=True
        )
        return df

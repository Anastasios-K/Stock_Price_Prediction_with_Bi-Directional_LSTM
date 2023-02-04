from src.secondary_modules.save_report import SaveReport


class HandleNanValues:
    """
    Count Nan values and record them in the project report.
    Fill in Nan values with a predetermined method (change method in config).
    """

    def __init__(self,
                 dataframe,
                 config,
                 report_title: str = "Nan Values"
                 ):
        self.__count_nan_values(
            df=dataframe,
            config=config,
            title=report_title
        )
        self.df = self.__replace_nan(
            df=dataframe,
            config=config,
        )

    @staticmethod
    def __count_nan_values(df,
                           config,
                           title):
        path2save = config.dirs2make.reports
        nan_amount = [
            f"{col}: {df[col].isna().sum()}"
            for col
            in df.columns
        ]
        SaveReport(
            path2save=path2save,
            data=nan_amount,
            title=title
        )

    @staticmethod
    def __replace_nan(df,
                      config
                      ):

        if config.dataengin.fill_method == "polynomial":
            [
                df[col].interpolate(
                    method=config.dataengin.fill_method,
                    order=config.dataengin.poly_order,
                    direction="both",
                    inplace=True
                )
                for col
                in df.columns
            ]

        elif config.dataengin.fill_method == "linear":
            [
                df[col].interpolate(
                    method=config.dataengin.fill_method,
                    direction="both",
                    inplace=True
                )
                for col
                in df.columns
            ]

        else:
            raise ValueError("An invalid fill method is given.")

        df.reset_index(inplace=True)
        return df

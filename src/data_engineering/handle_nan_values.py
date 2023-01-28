from src.secondary_modules.save_report import SaveReport


class HandleNanValues:

    def __init__(self,
                 dataframe,
                 config,
                 report_title: str = "Nan Values"
                 ):
        nan_val_quant = self.__count_nan_values(
            df=dataframe,
            config=config,
            title=report_title
        )
        self.df = self.__replace_nan_with_avg(
            df=dataframe,
            config=config,
            nan_quant=nan_val_quant
        )

    @staticmethod
    def __count_nan_values(df,
                           config,
                           title):
        path2save = config.dirs2make.reports
        nan_amount = [
            f"{col}: {df[col].isna().sum()}"
            for col in df.columns
        ]
        SaveReport(
            path2save=path2save,
            data=nan_amount,
            title=title
        )
        return nan_amount

    @staticmethod
    def __replace_nan_with_avg(df,
                               config,
                               nan_quant,
                               ):
        df.set_index(config.dfstructure.date, inplace=True)
        nan_quant = nan_quant

        # nan values condition is missing - coming soon

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

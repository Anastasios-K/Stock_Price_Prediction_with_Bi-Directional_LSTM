import os
import pandas as pd
from pandas_profiling import ProfileReport
from src.config.load_conifg import Config


class ProfilingEDA:
    def __init__(self,
                 dataframe: pd.DataFrame,
                 config: Config,
                 report_name: str):
        self.__create_eda_report(
            df=dataframe,
            config=config,
            report_name=report_name
        )

    @staticmethod
    def __create_eda_report(df: pd.DataFrame,
                            config: Config,
                            report_name: str) -> None:
        profile = ProfileReport(
            df,
            tsmode=True,
            sortby="Date"
        )
        profile.to_file(os.path.join(
            *config.dirs2make.figures,
            report_name + ".html"
        ))

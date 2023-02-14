import os
from pandas_profiling import ProfileReport


class ProfilingEDA:
    def __init__(self,
                 dataframe,
                 config,
                 report_name):
        self.__create_eda_report(df=dataframe,
                                 config=config,
                                 report_name=report_name)

    @staticmethod
    def __create_eda_report(df,
                            config,
                            report_name):
        profile = ProfileReport(
            df,
            tsmode=True,
            sortby="Date"
        )
        profile.to_file(os.path.join(
            *config.dirs2make.figures,
            report_name + ".html"
        ))

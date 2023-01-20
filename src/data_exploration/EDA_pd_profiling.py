from pandas_profiling import ProfileReport


class ProfilingEDA:
    def __init__(self,
                 dataframe,
                 report_name):
        self.__create_eda_report(df=dataframe,
                                 report_name=report_name)

    @staticmethod
    def __create_eda_report(df, report_name):
        profile = ProfileReport(df, tsmode=True, sortby="Date")
        profile.to_file(report_name)


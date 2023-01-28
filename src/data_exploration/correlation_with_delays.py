from src.data_exploration.calc_correlation import CalcCorrel


class CorrShiftedFeature:

    def __init__(self,
                 dataframe,
                 config,
                 corr_method
                 ):
        self.__calc_corr_multi_shifts(
            config=config,
            dataframe=dataframe,
            corr_method=corr_method
        )

    @staticmethod
    def __create_shifted_feaure_df(config,
                                   dataframe,
                                   shift_val
                                   ):
        # set up feature for shifting
        feature2shift = config.feature2shift.feature2shift
        # identify the location next to the original feature
        where = list(dataframe.columns).index(feature2shift)
        # shift the selected feature
        shifted_df = dataframe.copy()
        shifted_df.insert(
            loc=where+1,
            column=f"Shifted_{feature2shift}",
            value=dataframe[feature2shift].shift(shift_val)
        )
        return shifted_df

    def __calc_corr_multi_shifts(self,
                                 config,
                                 dataframe,
                                 corr_method
                                 ):
        shifts = range(1, 30)
        for shift in shifts:
            shifted_df = self.__create_shifted_feaure_df(config=config,
                                                         dataframe=dataframe,
                                                         shift_val=shift)
            CalcCorrel(
                dataframe=shifted_df,
                config=config,
                fig_title=f"Shifted_Correlation_with_Delay_{shift}",
                corr_method=corr_method
            )

from src.data_finance_technical_analysis.money_flow import MF
from src.data_finance_technical_analysis.typical_price import TP
import pandas as pd


class MFI:
    """ Money Flow Index """

    def __init__(self,
                 dataframe,
                 config,
                 ):
        self.__typical_price = TP(
            dataframe=dataframe,
            config=config
        ).typical_price

        self.__money_flow = MF(
            dataframe=dataframe,
            config=config
        ).money_flow

        tps = self.__calc_diff_tp_and_shifted_tp()
        tps = self.__calc_pos_n_neg_mf_periods(
            tps=tps,
            config=config,
        )
        tps = self.__calc_money_flow_ratio(tps=tps)

        self.mfi = self.__calc_money_flow_index(tps=tps)

    def __calc_diff_tp_and_shifted_tp(self):
        """ Calculate difference between typical price and typical price shifted by 1 """
        tps = pd.DataFrame(data=dict(
            tp_original=self.__typical_price,
            tp_shifted=self.__typical_price.shift(1)
        ))

        tps["tp_diff"] = tps["tp_original"] - tps["tp_shifted"]
        tps.loc[tps["tp_diff"] < 0, "tp_index"] = 0
        tps.loc[tps["tp_diff"] > 0, "tp_index"] = 1
        return tps

    def __calc_pos_n_neg_mf_periods(self,
                                    tps,
                                    config
                                    ):
        """ Calculate positive and negative periodic money flow """
        rolling_window = config.techanal.mfperiodwindow

        money_flow = self.__money_flow
        # initiate positive and negative money flow features
        tps["money_flow_negative"] = money_flow
        tps["money_flow_positive"] = money_flow
        # remove money flow value depending on the typical price index
        tps.loc[tps["tp_index"] == 1, "money_flow_negative"] = 0
        tps.loc[tps["tp_index"] == 0, "money_flow_positive"] = 0
        #
        tps["Periodic_Positive_MF"] = tps["money_flow_positive"].rolling(rolling_window).sum()
        tps["Periodic_Negative_MF"] = tps["money_flow_negative"].rolling(rolling_window).sum()
        return tps

    @staticmethod
    def __calc_money_flow_ratio(tps):
        tps["MFR"] = tps["Periodic_Positive_MF"] / tps["Periodic_Negative_MF"]
        return tps

    @staticmethod
    def __calc_money_flow_index(tps):
        money_flow_index = 100 - (100/(1 + tps["MFR"]))
        return money_flow_index








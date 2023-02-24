from src.data_TA_features.money_flow import money_flow
from src.data_TA_features.typical_price import typical_price
from src.config.load_conifg import Configurator
import pandas as pd


class MFI:
    """ Money Flow Index """

    def __init__(self,
                 data: pd.DataFrame,
                 config: Configurator):
        self.__config = config
        self.__typical_price = typical_price(
            data=data,
            config=config
        )

        self.__money_flow = money_flow(
            data=data,
            config=config
        )
        self.__tps = None

        self.__calc_diff_tp_and_shifted_tp()
        self.__calc_pos_n_neg_mf_periods()
        self.__calc_money_flow_ratio()

    def __calc_diff_tp_and_shifted_tp(self) -> None:
        """ Calculate difference between typical price and typical price shifted by 1 """
        tps = pd.DataFrame(data=dict(
            tp_original=self.__typical_price,
            tp_shifted=self.__typical_price.shift(1)
        ))

        tps["tp_diff"] = tps["tp_original"] - tps["tp_shifted"]
        tps.loc[tps["tp_diff"] < 0, "tp_index"] = 0
        tps.loc[tps["tp_diff"] > 0, "tp_index"] = 1
        self.__tps = tps

    def __calc_pos_n_neg_mf_periods(self) -> None:
        """ Calculate positive and negative periodic money flow """
        mf = self.__money_flow
        tps = self.__tps
        rolling_window = self.__config.techanal.mfperiodwindow

        # initiate positive and negative money flow features
        tps["money_flow_negative"] = mf
        tps["money_flow_positive"] = mf
        # remove money flow value depending on the typical price index
        tps.loc[tps["tp_index"] == 1, "money_flow_negative"] = 0
        tps.loc[tps["tp_index"] == 0, "money_flow_positive"] = 0
        #
        tps["Periodic_Positive_MF"] = tps["money_flow_positive"].rolling(rolling_window).sum()
        tps["Periodic_Negative_MF"] = tps["money_flow_negative"].rolling(rolling_window).sum()
        self.__tps = tps

    def __calc_money_flow_ratio(self) -> None:
        self.__tps["MFR"] = self.__tps["Periodic_Positive_MF"] / self.__tps["Periodic_Negative_MF"]

    def calc_money_flow_index(self) -> pd.DataFrame:
        money_flow_index = 100 - (100/(1 + self.__tps["MFR"]))
        return money_flow_index


df = pd.read_csv("data/TSCO.csv")
conf = Configurator("src/config/config.yaml")

df["asdf"] = MFI(data=df, config=conf).calc_money_flow_index()








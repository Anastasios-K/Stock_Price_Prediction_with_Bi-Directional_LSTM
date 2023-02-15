import pandas as pd
from src.data_TA_features.typical_price import TP
from src.config.load_conifg import Config


class MF:
    """ Money Flow """
    def __init__(self,
                 data: pd.DataFrame,
                 config: Config):
        self.money_flow = self.__money_flow(
            data=data,
            config=config,
        )

    @staticmethod
    def __money_flow(data: pd.DataFrame,
                     config: Config):
        typical_price = TP(
            data=data,
            config=config
        ).typical_price

        money_flow = typical_price * data[config.dfstructure.volume]
        return money_flow

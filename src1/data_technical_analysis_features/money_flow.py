import pandas as pd
from src.data_technical_analysis_features.typical_price import TP


class MF:
    """ Money Flow """
    def __init__(self,
                 data: pd.DataFrame,
                 config
                 ):
        self.money_flow = self.__money_flow(
            data=data,
            config=config,
        )

    @staticmethod
    def __money_flow(data,
                     config,
                     ):
        typical_price = TP(
            data=data,
            config=config
        ).typical_price

        money_flow = typical_price * data[config.dfstructure.volume]
        return money_flow

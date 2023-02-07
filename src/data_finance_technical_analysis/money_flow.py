import pandas as pd
from src.data_finance_technical_analysis.typical_price import TP


class MF:
    """ Money Flow """
    def __init__(self,
                 dataframe: pd.DataFrame,
                 config
                 ):
        self.money_flow = self.__money_flow(
            df=dataframe,
            config=config,
        )

    @staticmethod
    def __money_flow(df,
                     config,
                     ):
        typical_price = TP(
            dataframe=df,
            config=config
        ).typical_price

        money_flow = typical_price * df[config.dfstructure.volume]
        return money_flow

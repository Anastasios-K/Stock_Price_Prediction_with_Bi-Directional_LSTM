from src.technical_analysis.typical_price import TP


class MF:
    """ Money Flow """
    def __init__(self,
                 close_price,
                 high_price,
                 low_price,
                 volume
                 ):
        self.money_flow = self.__money_flow(
            close_price=close_price,
            high_price=high_price,
            low_price=low_price,
            volume=volume
        )

    @staticmethod
    def __money_flow(close_price,
                     high_price,
                     low_price,
                     volume
                     ):
        typical_price = TP(
            close_price=close_price,
            high_price=high_price,
            low_price=low_price
        ).typical_price

        money_flow = typical_price * volume
        return money_flow

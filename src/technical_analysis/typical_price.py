class TP:
    """ Typical Price """

    def __init__(self,
                 close_price,
                 high_price,
                 low_price
                 ):
        self.typical_price = self.__typical_price(
            close_price=close_price,
            high_price=high_price,
            low_price=low_price
        )

    @staticmethod
    def __typical_price(close_price,
                        high_price,
                        low_price
                        ):
        typical_price = (
                                close_price +
                                high_price +
                                low_price
                        ) / 3
        return typical_price

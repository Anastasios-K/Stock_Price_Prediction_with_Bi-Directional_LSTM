from src.model_data_preparation.drop_nan_rows import DropRows


class CreateLabels:

    def __init__(self,
                 data,
                 config
                 ):
        diff_col = "Diff"
        data_with_diff = self.__calc_price_difference(
            data=data,
            config=config,
            diff_col=diff_col
        )
        self.data = self.__create_labels(
            data_with_diff=data_with_diff,
            config=config,
            diff_col=diff_col
        )
        self.config = config

    @staticmethod
    def __calc_price_difference(data,
                                config,
                                diff_col
                                ):
        shifted_col = "Shifted_Close"

        data[shifted_col] = data[config.dfstructure.close].shift(1)
        data[diff_col] = (data[config.dfstructure.close] / data[shifted_col]) - 1
        return data

    @staticmethod
    def __create_labels(data_with_diff,
                        config,
                        diff_col
                        ):
        tollerance = config.labeltollerance.tollerance
        data_with_diff.loc[
            data_with_diff[diff_col] > tollerance,
            config.dfstructure.labels
        ] = 1
        data_with_diff.loc[
            data_with_diff[diff_col] < -tollerance,
            config.dfstructure.labels
        ] = -1
        data_with_diff.loc[
            (data_with_diff[diff_col] < tollerance) &
            (data_with_diff[diff_col] > -tollerance),
            config.dfstructure.labels
        ] = 0
        return data_with_diff

    def drop_nan_rows(self):
        return DropRows(data=self.data,
                        config=self.config)

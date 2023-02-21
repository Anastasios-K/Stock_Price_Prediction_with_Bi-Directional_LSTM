import numpy as np
import pandas as pd
from src.interface.interfaces import Creator
from src.config.load_conifg import Configurator
from tensorflow import keras


class LabelCreator(Creator):

    __data: pd.DataFrame
    __config: Configurator
    __diff_col = "Diff"
    __shifted_col = "Shifted_Close"

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, value):
        self.__config = value

    def _calc_price_difference(self) -> pd.DataFrame:
        """
        Shift Close feature by 1.
        Use the shifted and original Close features to calculate the percent difference.
        Add the 2 new features (shifted close and difference) in the given dataset.
        """
        temp_df = self.__data.copy()
        temp_df[self.__shifted_col] = temp_df[self.config.dfstructure.close].shift(1)
        temp_df[self.__diff_col] = (temp_df[self.config.dfstructure.close] / temp_df[self.__shifted_col]) - 1
        return temp_df

    def create_labels(self) -> (pd.DataFrame, pd.Series):
        """
        Call the _calc_price_difference to get the 2 new features (shifted close and difference).
        Create 3 classes based on the 3 conditions below and put them into the label attribute.
        Also consider a tollerance factor during the creation process.
        Drop the unused features (shifted close and difference).
        Drop the row with Nan values generated because of the shifting action.
        Synchonise the data and labels based on the timestamp.
        """
        # data with difference feature
        data_with_diff = self._calc_price_difference()
        # tollerance factor
        tollerance = self.config.labeltolerance.tolerance
        # condition 1
        data_with_diff.loc[
            data_with_diff[self.__diff_col] > tollerance,
            self.config.dfstructure.labels
        ] = 1
        # condition 2
        data_with_diff.loc[
            data_with_diff[self.__diff_col] < -tollerance,
            self.config.dfstructure.labels
        ] = 2
        # condition 3
        data_with_diff.loc[
            (data_with_diff[self.__diff_col] < tollerance) &
            (data_with_diff[self.__diff_col] > -tollerance),
            self.config.dfstructure.labels
        ] = 0
        # drop Nan values
        data_with_diff.dropna(inplace=True)
        # extract labels
        labsls = data_with_diff[self.config.dfstructure.labels]
        # drop unused features and the labels
        [
            data_with_diff.drop(columns=[col], inplace=True)
            for col in data_with_diff.columns
            if col not in self.config.featuresinuse.features
        ]
        return data_with_diff, labsls

    def create_label_weights(self, labels: pd.Series) -> dict:
        """
        Calculate class weights based on each class population.
        Crucial step when the training data is imbalanced.
        """
        lbs_weights = {}
        unique_lbs = labels.unique()
        lbs_amount = len(unique_lbs)
        lbs_matrix = keras.utils.to_categorical(
            y=labels,
            num_classes=lbs_amount
        )

        for idx in range(lbs_amount):
            weight_dict = {
                f"weight_{idx}": (1 / np.count_nonzero(lbs_matrix[:, idx] == 1)) * (len(lbs_matrix)) / lbs_amount
            }
            lbs_weights.update(weight_dict)
        return lbs_weights

import pandas as pd
import joblib
import os
from src.config.load_conifg import Config
from src.secondary_modules.time_id_creator import TimeID
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler


class ScaleData:
    """
    Scaled data.
    Three scaling methods considered:
        1. RobustScaler
        2. MinMaxScaler
        3. StandardScaler
    Set scaling method in G_params.yaml file.
    """
    def __init__(self,
                 train_set: pd.DataFrame,
                 test_set: pd.DataFrame,
                 train_labels: pd.Series,
                 test_labels: pd.Series,
                 config: Config):
        self.config = config
        self.train_labels = train_labels
        self.test_labels = test_labels
        self.scaled_train_df, scaled_test_df = self.__scale_data(
            train_df=train_set,
            test_df=test_set
        )

    def __scale_data(self,
                     train_df: pd.DataFrame,
                     test_df: pd.DataFrame):
        scaling_method = self.config.scaler.method
        if scaling_method == "robust":
            scaler = RobustScaler()
        elif scaling_method == "minmax":
            scaler = MinMaxScaler(feature_range=self.config.scaler.minmax_range)
        else:
            scaler = StandardScaler()

        scaler.fit(train_df)
        scaled_tr = scaler.transform(train_df)
        scaled_ts = scaler.transform(test_df)

        joblib.dump(scaler,
                    os.path.join(
                        self.__model_path,
                        self.__model_name,
                        f"{self.__model_name}.pkl"
                    )
                    )
        return scaled_tr, scaled_ts

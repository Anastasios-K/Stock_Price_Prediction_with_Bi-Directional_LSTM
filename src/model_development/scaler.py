import os
import pandas as pd
import joblib
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler
from src.config.load_conifg import Configurator


def scaler(
        config: Configurator,
        train_data: pd.DataFrame,
        test_data: pd.DataFrame,
        unique_id: str,
        pre_fitted_scaler_path: str = None) -> (pd.DataFrame, pd.DataFrame):
    """
    Scale train and test data in the execution.
    It can take pre-fitted scaler and apply it to both, train and test data.
    If no pre-fitted scaler is provided, it uses on of the scaler robust, MinMax and Standard Sacler.
    If no scaler is provided, the new scaler fits the train data ONLY.
    The new fitted scaler transforms both train and test data.
    The new scaler is also saved into a path set in the configurations.
    """
    if pre_fitted_scaler_path:
        # Use pre-fitted scaler
        scaler = joblib.load(pre_fitted_scaler_path)
        scaled_train_data = scaler.transform(train_data)
        scaled_test_data = scaler.transform(test_data)
    else:
        # Initiate, fit and use a new scaler
        scaling_method = config.scaler.method
        if scaling_method == "robust":
            scaler = RobustScaler()
        elif scaling_method == "minmax":
            scaler = MinMaxScaler(feature_range=config.scaler.minmax_range)
        elif scaling_method == "standardscaler":
            scaler = StandardScaler()
        else:
            ValueError("Scaling method is not given.")

        scaler.fit(train_data)
        scaled_train_data = scaler.transform(train_data)
        scaled_test_data = scaler.transform(test_data)

        # Save scaler
        joblib.dump(
            scaler,
            os.path.join(
                *config.dirs2make.figures,
                config.modelname.modelname + unique_id,
                f"{config.modelname.modelname}.pkl"
            )
        )

    scaled_train_data = pd.DataFrame(
        scaled_train_data,
        columns=train_data.columns,
        index=train_data.index
    )
    scaled_test_data = pd.DataFrame(
        scaled_test_data,
        columns=test_data.columns,
        index=test_data.index
    )
    return scaled_train_data, scaled_test_data

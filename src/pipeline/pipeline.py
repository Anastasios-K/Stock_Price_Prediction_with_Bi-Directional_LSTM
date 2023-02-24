import pandas as pd
from typing import Optional
from sklearn.model_selection import train_test_split

from src.helper.helper import Helper
from src.config.load_conifg import Configurator
from src.data_exploration.data_explorator import DataExplorator
from src.labels_creation.labels_creator import LabelCreator
from src.model_development.LSTM_builder import LstmBuilder
from src.model_development.scaler import scaler
from src.model_development.trainer import Trainer

from src.data_engineering.fix_data_format import fix_data_format
from src.data_engineering.handle_nan_values import count_nan_values, replace_nan_values
from src.data_engineering.handle_duplicates import count_duplicates, remove_duplicates

from src.data_TA_features.simple_moving_avg import simple_movinge_average
from src.data_TA_features.exponential_moving_avg import exponential_moving_average
from src.data_TA_features.moving_avg_convergence_divergence import moving_avg_convergence_divergence
from src.data_TA_features.money_flow_index import MFI


class Pipeline:
    """ The end-2-end pipeline of the Stock Price Prediction project. """

    def __init__(
            self,
            pipeline_config: Configurator,
            model_builder
    ):
        self.train_data = None
        self.test_data = None
        self.train_labels = None
        self.test_labels = None
        self.class_weights = None
        self.reshaped_tr_data = None
        self.reshaped_ts_data = None
        self.model = None
        self.__info_tracker = dict()

        self.unique_id = Helper.create_str_time_id()
        self.config = pipeline_config
        self.model_builder = model_builder
        Helper.create_required_dirs(config=self.config, unique_id=self.unique_id)

        Helper.create_required_dirs(config=self.config, unique_id=self.unique_id)
        self.__raw_data = pd.read_csv(self.config.paths.datapath)
        self.__prepare_data()
        self.__create_labels()

    def __prepare_data(self) -> None:
        """
        Called in the constractor and automatically does the following:
        1. Fix data format
        2. Sort data by index
        3. Split data into train and test sets
        4. Count, Save amount and Remove duplicates - for train and test separately
        5. Count, Save amount and Fill nan - for train and test separately
        """
        # Fix data format (data type, features, feature names etc.).
        fixed_format_data = fix_data_format(
            raw_data=self.__raw_data,
            config=self.config
        )
        # Sort data by index/timestamp.
        fixed_format_data.sort_index(
            inplace=True
        )
        # Split into train and test data.
        train_data, test_data = train_test_split(
            fixed_format_data,
            test_size=0.3,
            shuffle=False
        )
        # Count duplicates in train and test data separately. Save them in the info_tracker
        self.__info_tracker["train_set_duplicates"] = count_duplicates(
            data=train_data,
            config=self.config
        )
        self.__info_tracker["test_set_duplicates"] = count_duplicates(
            data=test_data,
            config=self.config
        )
        # Remove duplicates from train and test data separately.
        train_data_no_duplicates = remove_duplicates(
            data=train_data,
            config=self.config
        )
        test_data_no_duplicates = remove_duplicates(
            data=test_data,
            config=self.config
        )
        # Count NaN values in train and test data separately. Save them in the info_tracker
        self.__info_tracker["train_set_NaNs"] = count_nan_values(
            data=train_data,
        )
        self.__info_tracker["test_set_NaNs"] = count_nan_values(
            data=test_data,
        )
        # Fill NaN values in train and test set separately.
        self.train_data = replace_nan_values(
            data=train_data_no_duplicates,
            config=self.config
        )
        self.test_data = replace_nan_values(
            data=test_data_no_duplicates,
            config=self.config
        )

    def explore_data(self, data: Optional[pd.DataFrame] = None) -> DataExplorator:
        """
        Optional method that gives access to data exploration actions.
        If None, default data is train data.
        """
        if data is None:
            data = self.train_data

        exploration = DataExplorator(
            data=data,
            config=self.config,
            unique_id=self.unique_id
        )
        return exploration

    def enrich_data(self,
                    sma: bool = False,
                    ema: bool = False,
                    macd: bool = False,
                    mfi: bool = False) -> None:
        """
        Optional method that gives access into enriching data with technical analysis features.
        If it is integrated, it is applied into both, train and test set.
        """
        if sma:
            # Add simple moving average into train and test data
            self.train_data["SMA"] = simple_movinge_average(
                data=self.train_data,
                config=self.config
            )
            self.test_data["SMA"] = simple_movinge_average(
                data=self.test_data,
                config=self.config
            )
        if ema:
            # Add exponential moving average into train and test data
            self.train_data["EMA"] = exponential_moving_average(
                data=self.train_data,
                config=self.config,
                rolling_window=self.config.techanal.emawindow
            )
            self.test_data["EMA"] = exponential_moving_average(
                data=self.test_data,
                config=self.config,
                rolling_window=self.config.techanal.emawindow
            )
        if macd:
            # Add moving average convergence divergence into train and test data
            self.train_data["MACD"] = moving_avg_convergence_divergence(
                data=self.train_data,
                config=self.config
            )
            self.test_data["MACD"] = moving_avg_convergence_divergence(
                data=self.test_data,
                config=self.config
            )
        if mfi:
            # Add money flow index into train and test data
            self.train_data["MFI"] = MFI(
                data=self.train_data,
                config=self.config
            ).calc_money_flow_index()
            self.test_data["MFI"] = MFI(
                data=self.test_data,
                config=self.config
            ).calc_money_flow_index()

    def __create_labels(self) -> None:
        """
        Create labels.
        Update both data and labels to secure synchronisation.
        """
        self.train_data, self.train_labels = LabelCreator.create_labels(
            data=self.train_data,
            config=self.config
        )
        self.test_data, self.test_labels = LabelCreator.create_labels(
            data=self.test_data,
            config=self.config
        )

    def create_class_weights(self):
        """
        Optional method to create class wwights.
        Useful in case of imbalanced data.
        """
        self.class_weights = LabelCreator.create_label_weights(train_labels=self.train_labels)

    def scale_data(self, pre_fitted_scaler_path: str = None):
        """
        Use the scaler function to scale train and test data.
        You can set up the scaling method in the configuration yaml file.
        """
        self.train_data, self.test_data = scaler(
            config=self.config,
            train_data=self.train_data,
            test_data=self.test_data,
            unique_id=self.unique_id,
            pre_fitted_scaler_path=pre_fitted_scaler_path
        )

    def build_model(self):
        building_obj = self.model_builder(
            config=self.config,
            unique_id=self.unique_id,
            train_data=self.train_data,
            test_data=self.test_data
        )

        self.reshaped_tr_data = building_obj.reshaped_tr_data
        self.reshaped_ts_data = building_obj.reshaped_ts_data
        self.train_labels = self.train_labels[self.config.forecasthorizon.forcasthorizon:]
        self.test_labels = self.test_labels[self.config.forecasthorizon.forcasthorizon:]
        self.model = building_obj.keras_tuner_model

    def execute_training_testing_tracking(self):
        training_obj = Trainer(
            config=self.config,
            unique_id=self.unique_id,
            class_weights=self.class_weights,
            reshaped_train_data=self.reshaped_tr_data,
            train_labels=self.train_labels,
            tuner_object=self.model
        )
        self.xxx = training_obj.execute_training()


if __name__ == "__main__":

    CONFIG_PATH = "src\\config\\config.yaml"

    config = Configurator(config_path=CONFIG_PATH)
    model_builder = LstmBuilder

    run = Pipeline(pipeline_config=config, model_builder=model_builder)
    # run.explore_data().plot_multi_resolution(title="asdf")
    # run.explore_data().plot_distribution(fig_title="asda")
    # run.explore_data().plot_correlation("asd1")
    # run.explore_data().plot_autocorrelation()
    # run.explore_data().cerate_eda_report(report_name="rep123")
    #
    # run.enrich_data(sma=True, mfi=True)
    #
    run.create_class_weights()
    run.build_model()
    run.execute_training_testing_tracking()

    # xxx = run.reshaped_tr_data
    # import numpy as np
    #
    # yyy = np.array(xxx)
    # zzz = run.train_labels.values


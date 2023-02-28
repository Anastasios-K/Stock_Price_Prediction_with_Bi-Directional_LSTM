import pandas as pd
from typing import Optional
from sklearn.model_selection import train_test_split

from src.helper.helper import Helper
from src.config.load_conifg import Configurator
from src.data_exploration.data_explorator import DataExplorator
from src.labels_creation.labels_creator import LabelCreator
from src.model_development.scaler import scaler
from src.model_development.trainer import Trainer
from src.model_development.tester import Tester
from src.model_development.tracker import Tracker
from src.info_tracker.info_tracker import InfoTracker

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
        self.data_status = list()
        self.__model = None
        self.__class_weights = None
        self.info_tracker = InfoTracker()
        self.config = pipeline_config
        self.model_builder = model_builder

        self.__unique_id = Helper.create_str_time_id()
        Helper.create_required_dirs(config=self.config, unique_id=self.__unique_id)
        self.__raw_data = pd.read_csv(self.config.paths.datapath)
        self.__prepare_data()

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
        self.info_tracker.train_set_duplicates = count_duplicates(
            data=train_data,
            config=self.config
        )
        self.info_tracker.test_set_duplicates = count_duplicates(
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
        self.info_tracker.train_set_NaNs = count_nan_values(
            data=train_data,
        )
        self.info_tracker.test_set_NaNs= count_nan_values(
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
        if "preprocessed" not in self.data_status:
            self.data_status.append("preprocessed")

    def explore_data(self, data: Optional[pd.DataFrame] = None) -> DataExplorator:
        """
        Optional method that gives access to data exploration actions.
        If None, default data is train data.
        Otherwise, you can pass test data.
        """
        if data is None:
            data = self.train_data

        exploration = DataExplorator(
            data=data,
            config=self.config,
            unique_id=self.__unique_id
        )
        if "explored" not in self.data_status:
            self.data_status.append("explored")
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
        # Drop NaN values from train and test sets
        # which were created through the process of calculating the technical analysis features
        self.train_data.dropna(inplace=True)
        self.test_data.dropna(inplace=True)
        if "enriched" not in self.data_status:
            self.data_status.append("enriched")

    def scale_data(self, pre_fitted_scaler_path: str = None):
        """
        Use the scaler function to scale train and test data.
        You can set up the scaling method in the configuration yaml file.
        """
        self.train_data, self.test_data = scaler(
            config=self.config,
            train_data=self.train_data,
            test_data=self.test_data,
            unique_id=self.__unique_id,
            pre_fitted_scaler_path=pre_fitted_scaler_path
        )
        if "scaled" not in self.data_status:
            self.data_status.append("scaled")

    def build_model(self):
        """
        1. Create labels for train and test sets.
            This is the first pipeline step where the labels are required.
        2. Create and set a keras hypermodel.
        3. Refresh train and test data, train and test label.
        """
        # Create train data and labels
        train_data, train_labels = LabelCreator.create_labels(
            data=self.train_data,
            config=self.config
        )
        # Create test data and labels
        test_data, test_labels = LabelCreator.create_labels(
            data=self.test_data,
            config=self.config
        )
        # Build hypermodel
        building_obj = self.model_builder(
            config=self.config,
            number_of_classes=len(train_labels.unique()),
            unique_id=self.__unique_id,
            train_data=train_data,
            test_data=test_data,
            train_labels=train_labels,
            test_labels=test_labels
        )

        self.train_data = building_obj.reshaped_train_data
        self.test_data = building_obj.reshaped_test_data
        self.train_labels = building_obj.train_labels
        self.test_labels = building_obj.test_labels
        self.__model = building_obj.keras_hypermodel
        if "reshaped" not in self.data_status:
            self.data_status.append("reshaped")

    def execute_training_testing_tracking(self, class_weights: bool = True):
        if class_weights:
            self.__class_weights = LabelCreator.create_label_weights(train_labels=self.train_labels)
            self.info_tracker.class_weights = self.__class_weights

        training_obj = Trainer(
            config=self.config,
            unique_id=self.__unique_id,
            class_weights=self.__class_weights,
            reshaped_train_data=self.train_data,
            train_labels=self.train_labels,
            tuner_object=self.__model
        )
        trained_model = training_obj.execute_training()

        testing_obj = Tester(
            config=self.config,
            unique_id=self.__unique_id,
            test_data=self.test_data,
            test_labels=self.test_labels,
            trained_model=trained_model
        )
        testing_metrics = testing_obj.execute_testing()

        tracking = Tracker(
            best_models=testing_obj.best_models,
            config=self.config,
            tracking_info=self.info_tracker,
            unique_id=self.__unique_id,
            prediction_metrics=testing_metrics
        )
        tracking.execute_tracking()

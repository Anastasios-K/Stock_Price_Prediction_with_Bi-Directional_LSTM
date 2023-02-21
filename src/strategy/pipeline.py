import pandas as pd
from typing import Optional
from sklearn.model_selection import train_test_split
from src.config.load_conifg import Configurator
from src.strategy.data_explorator import DataExplorator
from src.strategy.data_technical_analyser import DataTechnicalAnalyser
from src.strategy.labels_creator import LabelCreator
from src.data_engineering.fix_data_format import fix_data_format
from src.data_engineering.handle_nan_values import count_nan_values, replace_nan_values
from src.data_engineering.handle_duplicates import count_duplicates, remove_duplicates
from src.data_engineering.data_visualisation import DataOverview


class Pipeline:
    """ The end-2-end pipeline of the Stock Price Prediction project. """

    def __init__(
            self,
            pipeline_config: Configurator = None,
            data_explorator: Optional[DataExplorator] = None,
            technical_analyser: Optional[DataTechnicalAnalyser] = None,
            labels_creator: LabelCreator = None
    ):
        self.config = pipeline_config
        self.__explorator = data_explorator
        self.__enricher = technical_analyser
        self.__labels_creator = labels_creator

        self.__data = pd.read_csv(self.config.paths.datapath)
        # self.train_data: pd.DataFrame
        # self.test_data: pd.DataFrame
        self.__parse_data()
        self.train_data, self.train_labels = self.create_labels_n_weights(data=self.train_data).create_labels()
        self.test_data, self.test_labels = self.create_labels_n_weights(data=self.test_data).create_labels()

    def __parse_data(self):
        """
        Called in the constractor and automatically does the following:
        1. Fix data format
        2. Sort data by index
        3. Split data into train and test sets
        4. Remove duplicates - for train and test separately
        5. Fill nan - for train and test separately
        """
        # Fix data format (data type, features, feature names etc.).
        fixed_format_data = fix_data_format(
            raw_data=self.__data,
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
        # Remove duplicates from train and test data separately.
        train_data_no_duplicates = remove_duplicates(
            data=train_data,
            config=self.config
        )
        test_data_no_duplicates = remove_duplicates(
            data=test_data,
            config=self.config
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

    def plot_various_frequencies(self, data: pd.DataFrame) -> None:
        """
        Plot various frequencies of the givven data.
        Use it freely in any step of the pipeline.
        """
        DataOverview(
            data=data,
            config=self.config
        )

    def explore_data(self, data: pd.DataFrame) -> DataExplorator:
        """ Optional method that gives access to data exploration actions. """
        assert self.__explorator is not None, \
            "Trying to explore data, but Explorator object has not been passed."
        exploration = self.__explorator
        exploration.data = data
        exploration.config = self.config
        return exploration

    def enrich_data(self, data: pd.DataFrame) -> DataTechnicalAnalyser:
        """
        Optional method that gives access into enriching data with technical analysis features.
        If it is integrated, it MUST be applied into both, train and test sets.
        """
        assert self.__enricher is not None, \
            "Trying to enrich date with TA features, but TechAnalyser object has not been passed."
        enrichment = self.__enricher
        enrichment.data = data
        enrichment.config = self.config
        return enrichment

    def create_labels_n_weights(self, data: pd.DataFrame = None) -> LabelCreator:
        """
        Automatically create labels for train and test data.
        Optionaly, it can create class weights to be used in the case of imbalanced data.

        The weight method works independently.
        So, if you want to calculate only the class weights, you can pass data=None
        """
        label_creation = self.__labels_creator
        label_creation.data = data
        label_creation.config = self.config
        return label_creation


if __name__ == "__main__":

    CONFIG_PATH = "src\\config\\config.yaml"

    config = Configurator(config_path=CONFIG_PATH)
    explorator = DataExplorator()
    enricher = DataTechnicalAnalyser()
    lb_creator = LabelCreator()

    run = Pipeline(
        pipeline_config=config,
        data_explorator=explorator,
        technical_analyser=enricher,
        labels_creator=lb_creator

    )

    run.explore_data(data=run.train_data).plot_distribution("train")
    run.explore_data(data=run.test_data).plot_distribution("test")
    run.label_weights = run.create_labels_n_weights(data=None).create_label_weights(labels=run.train_labels)



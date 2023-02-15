import pandas as pd

from src.config.load_conifg import Config
from src.secondary_modules.dir_creator import DirsCreator
from src.data_access.access_data import DataProvider
from src.data_engineering.manage_engineering import data_engineering_manager
from src.data_engineering.engineering_management import FixedDTypeData, NoDuplicateData, NoNanData, DataReady4Analysis
from src.data_engineering.actions.actions import *
from src.data_exploration.data_exploration import DataExploration
from src.data_TA_features.data_with_ta_features import TaFeaturesAddition
from src.model_data_preparation.create_labels import LabelsCreator


class RunStockPredictionProject:

    def __init__(self, config_path: str):
        # load config
        config = Config(config_path=config_path)
        # create directories
        DirsCreator(config=config)
        # import data with fixed data types
        fixed_data = DataProvider(config=config).fixed_dtype_data_obj
        # data engineering
        no_nan_data = data_engineering_manager(
            obj=fixed_data,
            action=ManageNansAction()
        )
        data_ready4analysis = data_engineering_manager(
            obj=no_nan_data,
            action=NoAction()
        )
        data_ready4analysis.plot_data_various_resolutions(
            data=data_ready4analysis.data_ready4analysis,
            config=data_ready4analysis.config,
            title="Data_Overview"
        )
        # data exploration
        data_exploration = DataExploration(obj=data_ready4analysis)
        data_exploration.plot_data_distribution()
        # data_exploration.pd_profiling_eda(report_name="EDA_PDprofiling")
        data_exploration.plot_correlation(fig_title="correlation_analysis")
        data_exploration.plot_autocorrelations()
        # technical analysis features added
        data_ta_features = TaFeaturesAddition(obj=data_ready4analysis)
        # data preparation for modelling
        self.data_ready4modelling = LabelsCreator(obj=data_ta_features)\
            .drop_nan_rows()\
            .drop_unused_features()\
            .split_data()



if __name__ == "__main__":

    CONFIG_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\src\\config\\config.yaml"
    run = RunStockPredictionProject(config_path=CONFIG_PATH)



from src.config.load_conifg import Config
from src.data_access.get_fix_data import DataGetterFixer
from src.data_engineering.data_ready4analysis import DataReady4Analysis
from src.data_exploration.data_exploration import DataExploration
from src.secondary_modules.dir_creator import DirsCreator
from src.data_technical_analysis_features.data_with_ta_features import TaFeaturesAddition
# from src.model_data_preparation.create_labels import LabelsCreator


class RunStockPredictionProject:

    def __init__(self, config_path):
        config = Config(config_path=config_path)
        DirsCreator(config=config)
        data_fixer = DataGetterFixer(config=config)

        self.data_engineering = DataReady4Analysis(data_getter_fixer_obj=data_fixer)

        data_exploration = DataExploration(data_ready4analysis=self.data_engineering)
        data_exploration.plot_data_distribution()
        # data_exploration.pd_profiling_eda(report_name="EDA_PDprofiling")
        data_exploration.plot_correlation(fig_title="correlation_analysis")
        data_exploration.plot_autocorrelations()

        self.tech_anal = TaFeaturesAddition(data_ready4analysis=self.data_engineering)

        #
        # self.data_exploration = DataExploration(data_ready4analysis=self.technical_analysis)
        # self.data_exploration.plot_data_distribution()
        # # self.data_exploration.pd_profiling_eda(report_name="EDA_PDprofiling")
        # self.data_exploration.plot_correlation(fig_title="correlation_analysis")
        # self.data_exploration.plot_autocorrelations()
        #
        # self.prep_data_modelling = LabelsCreator(data_ready4analysis=self.technical_analysis)\
        #     .drop_nan_rows()\
        #     .drop_unused_features()\
        #     .split_data()


if __name__ == "__main__":

    CONFIG_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\src\\config\\config.yaml"
    run = RunStockPredictionProject(config_path=CONFIG_PATH)



from src.config.load_conifg import Config
from src.data_access.get_data import DataGetter
from src.data_ready_for_analysis.data_ready4analysis import DataReady4Analysis
from src.data_exploration.data_exploration import DataExploration
from src.secondary_modules.create_dirs import CreateDirs
from src.model_data_preparation.create_labels import LabelsCreator


class RunStockPredictionProject:

    def __init__(self, config_path):
        config = Config(config_path=config_path)
        CreateDirs(config=config)
        row_data = DataGetter(config=config).fixed_format_data

        self.data_engineering = DataReady4Analysis(data=row_data, config=config)
        self.data_engineering.handle_nan_values()
        self.data_engineering.handle_duplicates()
        self.data_engineering.plot_diff_df_resolutions(fig_title="Tesco_Stock_Prices")

        self.technical_analysis = self.data_engineering
        self.technical_analysis.add_macd()
        self.technical_analysis.add_mfi()

        self.data_exploration = DataExploration(data_ready4analysis=self.technical_analysis)
        self.data_exploration.plot_data_distribution()
        # self.data_exploration.pd_profiling_eda(report_name="EDA_PDprofiling")
        self.data_exploration.plot_correlation(fig_title="correlation_analysis")
        self.data_exploration.plot_autocorrelations()

        self.prep_data_modelling = LabelsCreator(data_ready4analysis=self.technical_analysis)\
            .drop_nan_rows()\
            .drop_unused_features()\
            .split_data()


if __name__ == "__main__":

    CONFIG_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\src\\config\\config.yaml"
    run = RunStockPredictionProject(config_path=CONFIG_PATH)



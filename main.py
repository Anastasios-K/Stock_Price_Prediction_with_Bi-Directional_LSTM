from src.config.load_conifg import Config
from src.data_input.collect_data import GetData
from src.data_engineering.data_engineering import DataEngineering
from src.data_exploration.data_exploration import DataExploration
from src.secondary_modules.create_dirs import CreateDirs


class RunCryptoProject:

    def __init__(self, config_path):
        config = Config(config_path=config_path)
        CreateDirs(config=config)
        data = GetData(config=config).data

        self.data_engineering = DataEngineering(dataframe=data, config=config)
        self.data_engineering.handle_nan_values()
        self.data_engineering.handle_duplicates()
        self.data_engineering.handle_data_types()
        self.data_engineering.plot_data()
        self.data_engineering.set_time_as_index()
        post_eng_df = self.data_engineering.dataframe

        # self.data_exploration = DataExploration(dataframe=post_eng_df, config=config)
        # self.data_exploration.plot_data_distribution()
        # self.data_exploration.pd_profiling_eda(report_name="EDA_PDprofiling")
        # self.data_exploration.plot_correlation(fig_title="correlation_analysis")
        # self.data_exploration.plot_shifted_correlations()
        # self.data_exploration.plot_moving_avgs(fig_title="MovingAvgs")
        # self.data_exploration.plot_autocorrelations()


if __name__ == "__main__":

    CONFIG_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\src\\config\\config.yaml"
    a = RunCryptoProject(config_path=CONFIG_PATH)



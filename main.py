from src.config.load_conifg import Config
from src.data_input.collect_stock_data import GetData
from src.data_engineering.data_engineering import DataEngineering
from src.secondary_modules.create_dirs import CreateDirs


class RunCryptoProject:

    def __init__(self, config_path):
        config = Config(config_path=config_path)
        CreateDirs(config=config)
        row_data = GetData(config=config).row_data

        self.data_engineering = DataEngineering(row_data=row_data, config=config)
        self.data_engineering.handle_nan_values()
        self.data_engineering.handle_duplicates()
        self.data_engineering.plot_diff_df_resolutions(fig_title="Tesco_Stock_Prices")

        self.data_exploration = self.data_engineering.data_exploration()
        self.data_exploration.plot_data_distribution()
        self.data_exploration.pd_profiling_eda(report_name="EDA_PDprofiling")
        self.data_exploration.plot_correlation(fig_title="correlation_analysis")
        self.data_exploration.plot_autocorrelations()

        self.technical_analysis = self.data_engineering.technical_analysis()
        self.technical_analysis.add_sma()
        self.technical_analysis.add_ema()
        self.technical_analysis.add_macd()
        self.technical_analysis.add_mfi()


if __name__ == "__main__":

    CONFIG_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\src\\config\\config.yaml"
    a = RunCryptoProject(config_path=CONFIG_PATH)





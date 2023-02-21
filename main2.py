from src.config.load_conifg import Config
from src.preprocessing_factory.the_factory import FixedDTypeData, NoNanData#, NoDuplData, Ready4AnalysisData
from src.secondary_modules.info_tracker import InfoTracker


class RunStockPredictionProject:

    def __init__(self, config_path: str):
        # load config
        config = Config(config_path=config_path)

        self.fixed_data = FixedDTypeData(obj=config)
        self.nonan = NoNanData(self.fixed_data)
        # self.nodupl = NoDuplData(self.fixed_data)
        # self.nonan = NoNanData(self.nodupl)
        # self.ready = Ready4AnalysisData(self.fixed_data)


        # self.xxx = NoNanData(obj=fixed_data, config=config)
        # self.yyy = Ready4AnalysisData(obj=self.xxx, config=config)

        # self.data_ready4analysis = Ready4AnalysisData(obj=fixed_data, config=config)
        # data_ready4analysis = self.data_ready4analysis
        # data_ready4analysis.plot_data_various_resolutions(
        #     data=data_ready4analysis.data,
        #     config=data_ready4analysis.config,
        #     title="Data_Overview"
        # )
        # data_ready4analysis.plot_distribution()
        # data_ready4analysis.plot_correlation()
        # # data_ready4analysis.plot_autocorrelation()
        # # # data_ready4analysis.create_eda_report()
        # data_ready4analysis.add_ta_features()

        # self.final_data = data_ready4analysis.data


if __name__ == "__main__":

    CONFIG_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\src\\config\\config.yaml"
    run = RunStockPredictionProject(config_path=CONFIG_PATH)

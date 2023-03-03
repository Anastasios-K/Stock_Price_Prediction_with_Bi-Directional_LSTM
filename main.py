from src.pipeline.pipeline import Pipeline
from src.config.load_conifg import Configurator
from src.model_development.LSTM_builder import LstmBuilder


class RunStockPrediction:

    def __init__(self, config_path):
        # Create config object
        config = Configurator(config_path=config_path)
        # Create model_builder object
        model_builder = LstmBuilder
        # # Create pipeline object
        self.pipeline = Pipeline(pipeline_config=config, model_builder=model_builder)
        # pipe = self.pipeline
        # # Execute exploration
        # pipe.explore_data().plot_multi_resolution(title="data_overview_multiple_resolution")
        # pipe.explore_data().plot_distribution(fig_title="data_distributions")
        # pipe.explore_data().plot_correlation("correltion_heatmap")
        # pipe.explore_data().plot_autocorrelation()
        # pipe.explore_data().cerate_eda_report(report_name="explanatory_data_analysis_report")
        # # Execute enrichment
        # pipe.enrich_data(sma=False, mfi=True, ema=False, macd=True)
        # # Scale data
        # pipe.scale_data()
        # # Build model
        # pipe.build_model()
        # # Execute training testing and tracking
        # pipe.execute_training_testing_tracking()


if __name__ == "__main__":

    CONFIG_PATH = "src\\config\\config.yaml"
    run = RunStockPrediction(config_path=CONFIG_PATH)



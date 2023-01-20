from src.data_engineering.data_engineering import DataEngineering
from src.config.load_conifg import Config


class RunCryptoProject:

    def __init__(self, config_path):
        config = Config(config_path=config_path)
        self.run = DataEngineering(config=config)\
            .data_engineering


if __name__ == "__main__":

    CONFIG_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\src\\config\\config.yaml"
    a = RunCryptoProject(config_path=CONFIG_PATH)



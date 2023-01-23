from src.config.load_conifg import Config
from src.data_input.collect_data import GetData
from src.data_engineering.data_engineering import DataEngineering

# import pandas as pd
# import os
# import numpy as np
# xxx = pd.read_csv(os.path.join("data", "coin_Bitcoin.csv"))
# xxx.loc[xxx["Date"] == "2018-10-15 23:59:59", "High"] = np.nan
# xxx.to_csv(os.path.join("data", "coin_Bitcoin.csv"), index_label=False)


class RunCryptoProject:

    def __init__(self, config_path):
        config = Config(config_path=config_path)
        data = GetData(config=config).data
        self.data_engineering = DataEngineering(dataframe=data, config=config)
        self.data_engineering.handle_nan_values()
        self.data_engineering.handle_duplicates()
        self.data_engineering.handle_data_types()
        self.data_engineering.plot_data()


if __name__ == "__main__":

    CONFIG_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\src\\config\\config.yaml"
    a = RunCryptoProject(config_path=CONFIG_PATH)



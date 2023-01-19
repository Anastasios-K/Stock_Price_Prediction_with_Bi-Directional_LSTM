from src.data_engineering.s1_collect_data import GetData


class DataEngineering:

    def __init__(self, data_path):
        self.data_engineering = GetData(data_path=data_path)\
            .clean_data()\
            .hundle_duplicates()\
            .fix_data_types()\
            .validate_continiuty()\
            .plot_data()


if __name__ == "__main__":
    DATA_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\data"
    run = DataEngineering(data_path=DATA_PATH)



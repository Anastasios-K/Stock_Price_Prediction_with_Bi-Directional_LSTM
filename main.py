from src.preprocessing.collect_data import GetData


class RunCryptoProject:

    def __init__(self, data_path):
        self.run = GetData(data_path=data_path)\
            # .clean_data()


if __name__ == "__main__":

    DATA_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\data"
    run = RunCryptoProject(data_path=DATA_PATH)


x = run.run.data
x.iloc[3, :] = x.iloc[2, :]

a = x.duplicated(subset="Date", keep=False).sum()

zzz = x.drop_duplicates(subset="Date", keep="first")
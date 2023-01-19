import os
import pandas as pd
import numpy as np
from src.data_engineering.s2_handle_nan_values import HandleNanValues


class GetData:

    def __init__(self, data_path):
        self.data = self.__create_final_dataframe(data_path=data_path)

    @staticmethod
    def __read_csvs(data_path):
        data_list = [
            pd.read_csv(os.path.join(data_path, file))
            for file in os.listdir(data_path)
            if file.endswith("csv")
        ]
        return data_list

    @staticmethod
    def __add_coin_name_in_column_names(df):
        coin_name = df.loc[0, "Symbol"]
        new_cols = [coin_name + "_" + col if col != "Date" else col for col in df.columns]
        df.columns = new_cols
        return df

    @staticmethod
    def __remove_unused_cols(df):
        unused_col_names = ["SNo", "Name", "Symbol"]
        unused_cols = [[col for col in df.columns if name in col] for name in unused_col_names]
        unused_cols = list(np.concatenate(unused_cols))
        df.drop(columns=unused_cols, axis=1, inplace=True)
        return df

    @staticmethod
    def __merge_multiple_dfs(df_list):
        new_df = df_list[0]
        df_list = df_list[1:]
        for df in df_list:
            new_df = pd.merge(new_df, df, on="Date")
        return new_df

    def __create_final_dataframe(self, data_path):
        data_list = self.__read_csvs(data_path=data_path)
        # add names
        data_list = [
            self.__add_coin_name_in_column_names(df=df)
            for df in data_list
        ]
        # remove unused columns
        data_list = [
            self.__remove_unused_cols(df=df)
            for df in data_list
        ]
        final_df = self.__merge_multiple_dfs(df_list=data_list)
        return final_df

    def handle_nan_values(self):
        return HandleNanValues(dataframe=self.data)

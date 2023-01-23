import os
import pandas as pd
import numpy as np


class GetData:

    def __init__(self,
                 config):
        self.__config = config
        self.data = self.__create_final_dataframe(data_path=config.paths.datapath)

    def __read_csvs(self, data_path):
        data_list = [
            pd.read_csv(os.path.join(data_path, file))
            for file in os.listdir(data_path)
            if file.endswith(self.__config.datafiletype.datafiletype)
        ]
        return data_list

    def __add_currency_name_in_column_names(self, df):
        coin_name = df.loc[0, self.__config.dfstructure.symbol]
        new_cols = [
            coin_name + "_" + col
            if col != self.__config.dfstructure.date
            else col
            for col in df.columns
        ]
        df.columns = new_cols
        return df

    def __remove_unused_cols(self, df):
        unused_col_names = [
            self.__config.dfstructure.serialID,
            self.__config.dfstructure.name,
            self.__config.dfstructure.symbol
        ]
        unused_cols = [
            [col for col in df.columns if name in col]
            for name in unused_col_names
        ]
        unused_cols = list(np.concatenate(unused_cols))
        df.drop(columns=unused_cols, axis=1, inplace=True)
        return df

    def __merge_multiple_dfs(self, df_list):
        new_df = df_list[0]  # store the 1st df
        df_list = df_list[1:]  # start merge iteration from the 2nd df
        for df in df_list:
            new_df = pd.merge(
                new_df,
                df,
                on=self.__config.dfstructure.date
            )
        return new_df

    def __create_final_dataframe(self, data_path):
        data_list = self.__read_csvs(data_path=data_path)
        # add names
        data_list = [
            self.__add_currency_name_in_column_names(df=df)
            for df in data_list
        ]
        # remove unused columns
        data_list = [
            self.__remove_unused_cols(df=df)
            for df in data_list
        ]
        final_df = self.__merge_multiple_dfs(df_list=data_list)
        return final_df
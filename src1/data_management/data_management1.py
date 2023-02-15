# from src.data_access.get_fix_data import DataGetterFixer
# import pandas as pd
# from functools import singledispatch
# from src.secondary_modules.save_report import ReportSaving
# from src.config.load_conifg import Config
# from typing import overload
#
#
# class DTypeFixer:
#     fixed_dtype_data: pd.DataFrame
#     config: Config
#
#
# class NanHandler(DTypeFixer):
#     no_nan_data: pd.DataFrame
#     config: Config
#
#
# class DuplicateHandler(DTypeFixer):
#     no_dupl_data: pd.DataFrame
#     config: Config
#
#
# class DataReady4Analysis(NanHandler, DuplicateHandler):
#     data_ready4analysis: pd.DataFrame
#     config: Config
#
# print(type(DataGetterFixer))
#
#
# @overload
# def data_manager(obj) -> object: ...
# @overload
# def data_manager(obj: DataGetterFixer) -> DTypeFixer: ...
# @overload
# def data_manager(obj: DataGetterFixer) -> DTypeFixer: ...
#
#
# def data_manager(obj):
#     if isinstance(obj, DataGetterFixer):
#         print("fix data types")
#     else:
#         raise ValueError("DataGetterFixer object is required")
#
#     raw_data = obj.fixed_format_data
#     configuration = obj.config
#
#     def __fix_data_format() -> pd.DataFrame:
#
#         for col in raw_data.columns:
#             if col == configuration.dfstructure.date:
#                 raw_data[col] = pd.to_datetime(raw_data[col])
#
#                 raw_data.set_index(
#                     configuration.dfstructure.date,
#                     inplace=True
#                 )
#
#             else:
#                 raw_data[col] = pd.to_numeric(raw_data[col])
#
#         fixed_data = raw_data.copy()
#
#         # prepare list for reporting
#         types = fixed_data.dtypes
#         attributes = list(types.index)
#         types = list(types)
#
#         reporting_list = [
#             attr + " - " + str(localtype)
#             for attr, localtype
#             in zip(attributes, types)
#         ]
#         ReportSaving(
#             data=reporting_list,
#             title="Dtypes",
#             path2save=configuration.dirs2make.reports
#         )
#         return fixed_data
#
#     fixed_dtype_data_obj = DTypeFixer()
#     fixed_dtype_data_obj.config = configuration
#     fixed_dtype_data_obj.fixed_dtype_data = __fix_data_format()
#
#     return fixed_dtype_data_obj
#
#
# @data_manager.register
# def _(obj: DTypeFixer, action: str = "handle_nan"):
#     print("kanw handle ta nans")
#
#     data = obj.fixed_dtype_data
#     configuration = obj.config
#
#     def __count_nan_values():
#         path2save = configuration.dirs2make.reports
#         nan_amount = [
#             f"{col}: {data[col].isna().sum()}"
#             for col
#             in data.columns
#         ]
#         ReportSaving(
#             path2save=path2save,
#             data=nan_amount,
#             title="Nan Values"
#         )
#
#     def __replace_nan():
#         if configuration.dataengin.fill_method == "polynomial":
#             [
#                 data[col].interpolate(
#                     method=configuration.dataengin.fill_method,
#                     order=configuration.dataengin.poly_order,
#                     direction="both",
#                     inplace=True
#                 )
#                 for col
#                 in data.columns
#             ]
#
#         elif configuration.dataengin.fill_method == "linear":
#             [
#                 data[col].interpolate(
#                     method=configuration.dataengin.fill_method,
#                     direction="both",
#                     inplace=True
#                 )
#                 for col
#                 in data.columns
#             ]
#
#         else:
#             raise ValueError("An invalid fill method is given.")
#
#         return data
#
#     __count_nan_values()
#     no_nan_data_obj = NanHandler()
#     no_nan_data_obj.config = configuration
#     no_nan_data_obj.no_nan_data = __replace_nan()
#
#     return no_nan_data_obj
# #
# #
# # @data_manager.register
# # def _(obj: DTypeFixer, action: str = "handle_duplicates"):
# #     print("kanw handle ta duplicates")
# #
# #     data = obj.fixed_dtype_data
# #     configuration = obj.config
# #
# #     def __set_date_index():
# #         data[configuration.dfstructure.date] = data.index
# #         return data
# #
# #     def __count_duplicates():
# #         new_data = __set_date_index()
# #         path2save = configuration.dirs2make.reports
# #         dupli_amount = new_data[configuration.dfstructure.date].duplicated(False).sum()
# #
# #         ReportSaving(
# #             path2save=path2save,
# #             data=list(str(dupli_amount)),
# #             title="Duplicates"
# #         )
# #
# #     def __remove_duplicates():
# #         new_data = __set_date_index()
# #         new_data.drop_duplicates(
# #             subset="Date",
# #             keep="first",
# #             inplace=True
# #         )
# #         new_data.drop(
# #             columns=[configuration.dfstructure.date],
# #             inplace=True
# #         )
# #         return new_data
# #
# #     __count_duplicates()
# #     no_dupl_data_obj = DuplicateHandler()
# #     no_dupl_data_obj.config = configuration
# #     no_dupl_data_obj.no_dupl_data = __remove_duplicates()
# #
# #     return no_dupl_data_obj
#
#
#
# df = pd.read_csv("data/TSCO.csv")
# CONFIG_PATH = "C:\\Users\\Anast\\pythonProject\\Crypto_Prise_Prediction\\src\\config\\config.yaml"
# config = Config(config_path=CONFIG_PATH)
#
# a = DataGetterFixer(config=config)
# a.fixed_format_data = df
#
# fixedDataType = data_manager(obj=a)
#
#

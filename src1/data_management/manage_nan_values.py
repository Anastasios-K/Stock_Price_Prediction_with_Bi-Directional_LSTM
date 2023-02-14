# import pandas as pd
# from src.secondary_modules.save_report import ReportSaving
# from src.data_management.data_management import DTypeFixer
# from src.data_management.data_management import NanHandler
#
#
# def manage_nan_values(obj: DTypeFixer):
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
#     def __replace_nan() -> pd.DataFrame:
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

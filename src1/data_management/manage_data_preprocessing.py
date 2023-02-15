# from typing import overload
# from src.data_management.data_management import *
# from src.data_management.management_actions import *
# # from src.data_management.manage_duplicates import manage_duplicates
# # from src.data_management.manage_nan_values import manage_nan_values
#
#
# @overload
# def data_manager(obj: FixedDTypeData, action: ManageNansAction) -> NoNanData: ...
# @overload
# def data_manager(obj: FixedDTypeData, action: ManageDuplicatesAction) -> NoDuplicateData: ...
# @overload
# def data_manager(obj: NoNanData, action: NoAction) -> DataReady4Analysis: ...
# @overload
# def data_manager(obj: NoDuplicateData, action: NoAction) -> DataReady4Analysis: ...
#
#
# def data_manager(obj, action):
#     if isinstance(obj, FixedDTypeData) and isinstance(action, ManageNansAction):
#         manage_nan_values(obj=obj)
#     elif isinstance(obj, FixedDTypeData) and isinstance(action, ManageDuplicatesAction):
#         manage_duplicates(obj=obj)
#     elif isinstance(obj, NoNanData) and isinstance(action, NoAction):
#         manage_duplicates(obj=obj)
#     elif isinstance(obj, NoDuplicateData) and isinstance(action, NoAction):
#         manage_nan_values(obj=obj)

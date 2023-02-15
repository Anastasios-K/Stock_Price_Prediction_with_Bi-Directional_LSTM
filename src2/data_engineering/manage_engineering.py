from typing import overload
from src.data_engineering.engineering_management import *
from src.data_engineering.actions.actions import *
from src.data_engineering.actions.manage_duplicates import DuplicateRemoval
from src.data_engineering.actions.manage_nans import NanReplacement


@overload
def data_engineering_manager(obj: FixedDTypeData, action: ManageNansAction) -> NoNanData: ...
@overload
def data_engineering_manager(obj: FixedDTypeData, action: ManageDuplicatesAction) -> NoDuplicateData: ...
@overload
def data_engineering_manager(obj: NoNanData, action: NoAction) -> DataReady4Analysis: ...
@overload
def data_engineering_manager(obj: NoDuplicateData, action: NoAction) -> DataReady4Analysis: ...


def data_engineering_manager(obj, action):
    if isinstance(obj, FixedDTypeData) and isinstance(action, ManageNansAction):
        print("remove nans from fixed data type data")
        __no_nans_data_obj = NanReplacement(
            data=obj.fixed_dtype_data,
            config=obj.config
        )
        new_obj = NoNanData()
        new_obj.config = __no_nans_data_obj.config
        new_obj.no_nan_data = __no_nans_data_obj.no_nan_data.copy()

    elif isinstance(obj, FixedDTypeData) and isinstance(action, ManageDuplicatesAction):
        print("remove duplicates from fixed data type data")
        __no_dupls_data_obj = DuplicateRemoval(
            data=obj.fixed_dtype_data,
            config=obj.config
        )
        new_obj = NoDuplicateData()
        new_obj.config = __no_dupls_data_obj.config
        new_obj.no_dupl_data = __no_dupls_data_obj.no_dupl_data.copy()

    elif isinstance(obj, NoNanData) and isinstance(action, NoAction):
        print("remove duplicates from No NaNs data")
        __no_dupls_data_obj = DuplicateRemoval(
            data=obj.no_nan_data,
            config=obj.config
        )
        new_obj = DataReady4Analysis()
        new_obj.config = __no_dupls_data_obj.config
        new_obj.data_ready4analysis = __no_dupls_data_obj.no_dupl_data.copy()

    elif isinstance(obj, NoDuplicateData) and isinstance(action, NoAction):
        print("remove NaNs from No Duplicates data")
        __no_nans_data_obj = NanReplacement(
            data=obj.no_dupl_data,
            config=obj.config
        )
        new_obj = DataReady4Analysis()
        new_obj.config = __no_nans_data_obj.config
        new_obj.data_ready4analysis = __no_nans_data_obj.no_nan_data.copy()

    else:
        raise ValueError("The given objects are not a valid combination")

    return new_obj

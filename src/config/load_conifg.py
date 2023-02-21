from dataclasses import dataclass
from typing import List
import typing as t
from src.helper.helper import Helper


@dataclass
class StockName:
    stockname: str

    @classmethod
    def read_config(cls: t.Type["StockName"], obj: dict):
        return cls(
            stockname=obj["stock_name"]["stock_name"]
        )


@dataclass
class ModelName:
    modelname: str

    @classmethod
    def read_config(cls: t.Type["ModelName"], obj: dict):
        return cls(
            modelname=obj["model_name"]["model_name"]
        )


@dataclass
class Paths:
    datapath: str

    @classmethod
    def read_config(cls: t.Type["Paths"], obj: dict):
        return cls(
            datapath=obj["paths"]["data_path"]
        )


@dataclass
class InputDataStructureucture:
    date: str
    close: str
    open: str
    high: str
    low: str
    adjclose: str
    volume: str
    labels: str

    @classmethod
    def read_config(cls: t.Type["InputDataStructureucture"], obj: dict):
        return cls(
            date=obj["input_data_structure"]["date"],
            close=obj["input_data_structure"]["close"],
            open=obj["input_data_structure"]["open"],
            high=obj["input_data_structure"]["high"],
            low=obj["input_data_structure"]["low"],
            adjclose=obj["input_data_structure"]["adjclose"],
            volume=obj["input_data_structure"]["volume"],
            labels=obj["input_data_structure"]["labels"]
        )


@dataclass
class FeaturesInUse:
    features: List

    @classmethod
    def read_config(cls: t.Type["FeaturesInUse"], obj: dict):
        return cls(
            features=obj["features_in_use"]["features_in_use"]
        )


@dataclass
class Dirs2Make:
    reports: str
    figures: str
    models: str
    best_models: str

    @classmethod
    def read_config(cls: t.Type["Dirs2Make"], obj: dict):
        return cls(
            reports=obj["required_dirs"]["reports"],
            figures=obj["required_dirs"]["figures"],
            models=obj["required_dirs"]["models"],
            best_models=obj["required_dirs"]["best_models"]
        )


@dataclass
class DataEngin:
    fill_method: str
    poly_order: int

    @classmethod
    def read_config(cls: t.Type["DataEngin"], obj: dict):
        return cls(
            fill_method=obj["data_engineering"]["fill_method"],
            poly_order=obj["data_engineering"]["poly_order"]
        )


@dataclass
class DataExpl:
    corrmethod: str
    autocorrlag: int

    @classmethod
    def read_config(cls: t.Type["DataExpl"], obj: dict):
        return cls(
            corrmethod=obj["data_exploration"]["correlation_method"],
            autocorrlag=obj["data_exploration"]["auto_correlation_lags"]
        )


@dataclass
class TechAnal:
    smawindow: int
    emawindow: int
    mfperiodwindow: int
    macdshortwindow: int
    macdlongwindow: int
    signalwindow: int

    @classmethod
    def read_config(cls: t.Type["TechAnal"], obj: dict):
        return cls(
            smawindow=obj["technical_analysis"]["moving_avg_window"],
            emawindow=obj["technical_analysis"]["exp_moving_avg_window"],
            mfperiodwindow=obj["technical_analysis"]["money_flow_periods_window"],
            macdshortwindow=obj["technical_analysis"]["macd_short_window"],
            macdlongwindow=obj["technical_analysis"]["macd_long_window"],
            signalwindow=obj["technical_analysis"]["signal_window"]
        )


@dataclass
class LabelTolerance:
    tolerance: int

    @classmethod
    def read_config(cls: t.Type["LabelTolerance"], obj: dict):
        return cls(
            tolerance=obj["label_tolerance"]["tolerance"]
        )


@dataclass
class Scaler:
    method: str
    minmax_range: list

    @classmethod
    def read_config(cls: t.Type["Scaler"], obj: dict):
        return cls(
            method=obj["scaling"]["method"],
            minmax_range=obj["scaling"]["minmax_range"]
        )


@dataclass
class PlotDefault:
    title_color: str
    title_font_style: str
    title_font_size: int
    axes_line_width: int
    axes_line_color: str

    @classmethod
    def read_config(cls: t.Type["PlotDefault"], obj: dict):
        return cls(
            title_color=obj["plotting_default"]["title_color"],
            title_font_style=obj["plotting_default"]["title_font_style"],
            title_font_size=obj["plotting_default"]["title_font_size"],
            axes_line_width=obj["plotting_default"]["axes_line_width"],
            axes_line_color=obj["plotting_default"]["axes_line_color"],
        )


class Configurator:

    def __init__(self, config_path):
        config_file = Helper().read_yaml_file(path=config_path)

        self.stockname = StockName.read_config(obj=config_file)
        self.modelname = ModelName.read_config(obj=config_file)
        self.paths = Paths.read_config(obj=config_file)
        self.dfstructure = InputDataStructureucture.read_config(obj=config_file)
        self.featuresinuse = FeaturesInUse.read_config(obj=config_file)
        self.dirs2make = Dirs2Make.read_config(obj=config_file)
        self.dataengin = DataEngin.read_config(obj=config_file)
        self.dataexpl = DataExpl.read_config(obj=config_file)
        self.techanal = TechAnal.read_config(obj=config_file)
        self.labeltolerance = LabelTolerance.read_config(obj=config_file)
        self.scaler = Scaler.read_config(obj=config_file)
        self.plotdefault = PlotDefault.read_config(obj=config_file)

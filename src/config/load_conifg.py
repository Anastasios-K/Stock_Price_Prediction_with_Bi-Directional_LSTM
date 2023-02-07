from dataclasses import dataclass
import typing as t
from src.secondary_modules.read_yaml import YamlReader


@dataclass
class Paths:
    datapath: str

    @classmethod
    def read_config(cls: t.Type["Paths"], obj: dict):
        return cls(
            datapath=obj["paths"]["data_path"]
        )


@dataclass
class DfStructure:
    date: str
    close: str
    open: str
    high: str
    low: str
    adjclose: str
    volume: str
    labels: str

    @classmethod
    def read_config(cls: t.Type["DfStructure"], obj: dict):
        return cls(
            date=obj["df_structure"]["date"],
            close=obj["df_structure"]["close"],
            open=obj["df_structure"]["open"],
            high=obj["df_structure"]["high"],
            low=obj["df_structure"]["low"],
            adjclose=obj["df_structure"]["adjclose"],
            volume=obj["df_structure"]["volume"],
            labels=obj["df_structure"]["labels"]
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
    no_nans: str
    no_dupl: str
    no_zero: str

    @classmethod
    def read_config(cls: t.Type["DataEngin"], obj: dict):
        return cls(
            fill_method=obj["data_engineering"]["fill_method"],
            poly_order=obj["data_engineering"]["poly_order"],
            no_nans=obj["data_engineering"]["forced_functions"]["no_nans"],
            no_dupl=obj["data_engineering"]["forced_functions"]["no_dupl"],
            no_zero=obj["data_engineering"]["forced_functions"]["no_zero"]
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
class LabelTollerance:
    tollerance: int

    @classmethod
    def read_config(cls: t.Type["LabelTollerance"], obj: dict):
        return cls(
            tollerance=obj["label_tollerance"]
        )




@dataclass
class FileType:
    datafiletype: str

    @classmethod
    def read_config(cls: t.Type["FileType"], obj: dict):
        return cls(
            datafiletype=obj["data_files_type"]
        )


@dataclass
class Feature2Shift:
    feature2shift: str

    @classmethod
    def read_config(cls: t.Type["Feature2Shift"], obj: dict):
        return cls(
            feature2shift=obj["feature2shift"]
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


class Config:

    def __init__(self, config_path):
        config_file = YamlReader(path=config_path).content

        self.paths = Paths.read_config(obj=config_file)
        self.dfstructure = DfStructure.read_config(obj=config_file)
        self.dirs2make = Dirs2Make.read_config(obj=config_file)
        self.dataengin = DataEngin.read_config(obj=config_file)
        self.techanal = TechAnal.read_config(obj=config_file)
        self.labeltollerance = LabelTollerance.read_config(obj=config_file)

        self.feature2shift = Feature2Shift.read_config(obj=config_file)
        self.plotdefault = PlotDefault.read_config(obj=config_file)
        self.datafiletype = FileType.read_config(obj=config_file)

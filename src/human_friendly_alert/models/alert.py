# coding: utf-8

from enum import Enum, auto
from typing import NamedTuple


class AlertLevel(Enum):
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()


class AlertStatus(Enum):
    OK = 'ok'
    ALERT = 'alert'
    WIP = 'wip'


class Alert(NamedTuple):
    namespace: str
    type: str
    level: AlertLevel
    status: AlertStatus
    detail: str
    duration: int

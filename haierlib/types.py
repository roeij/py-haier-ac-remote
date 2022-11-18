from dataclasses import dataclass
from enum import Enum


class Limits(Enum):
    OFF = 0
    ONLY_VERTICAL = 1

class FanSpeed(Enum):
    MAX = 0
    MID = 1
    MIN = 2
    AUTO = 3

class Mode(Enum):
    SMART = 0
    COOL = 1
    HEAT = 2
    FAN = 3
    DRY = 4


@dataclass
class State:
    current_temp: int = 21
    target_temp: int = 21
    fan_speed: FanSpeed = FanSpeed.MIN
    mode: Mode = Mode.FAN
    health: bool = False
    limits: Limits = Limits.OFF
    power: bool = False

    def __str__(self) -> str:
        return """Haier AC State:
        Power: {},
        Current Temp: {}
        Target Temp: {}
        Fan Speed: {}
        Mode: {}
        Health: {}
        Limits: {}""".format(
            self.power,
            self.current_temp,
            self.target_temp,
            self.fan_speed,
            self.mode,
            self.health,
            self.limits,
        )

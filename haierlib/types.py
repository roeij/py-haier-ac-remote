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

class State:
    def __init__(self) -> None:
        self._current_temp = 21
        self._target_temp = 21
        self._fan_speed = FanSpeed.MIN
        self._mode = Mode.FAN
        self._health = False
        self._limits = Limits.OFF
        self._power = False

    def __str__(self) -> str:
        return """Haier AC State:
        Power: {},
        Current Temp: {}
        Target Temp: {}
        Fan Speed: {}
        Mode: {}
        Health: {}
        Limits: {}""".format(
          self._power, self._current_temp, self._target_temp,
          self._fan_speed, self._mode, self._health, self._limits
        )

    def update(self, current_temp, target_temp, fan_speed, mode, health, limits, power):
        self._current_temp = current_temp
        self._target_temp = target_temp
        self._fan_speed = fan_speed
        self._mode = mode
        self._health = health
        self._limits = limits
        self._power = power
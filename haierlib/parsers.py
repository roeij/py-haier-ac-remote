from typing import Any

import construct

from haierlib.structs import get_cmd_struct, resp_struct, state_struct
from haierlib.types import FanSpeed, Limits, Mode, State


class Parser(object):
    @classmethod
    def parse_raw(cls, data: bytes) -> State:
        resp = resp_struct.parse(data)
        return cls.parse_state(resp)

    def parse_state(resp: construct.Container[Any]) -> State:
        state = State()

        if resp.cmd.type != 34:
            return

        # Get the constructed data
        state_st = state_struct.parse(
            get_cmd_struct(resp.cmd_length).build(
                {
                    "data_magic": resp.cmd.data_magic,
                    "type": resp.cmd.type,
                    "data": resp.cmd.data,
                }
            )
        )

        # Adjust and convert to State object
        state.current_temp = state_st.current_temp
        state.target_temp = state_st.target_temp + 16
        state.fan_speed = FanSpeed(state_st.fan_speed)
        state.mode = Mode(state_st.mode)
        state.health = state_st.health % 2 != 0
        state.limits = Limits(state_st.limits)
        state.power = state_st.power % 2 != 0

        return state

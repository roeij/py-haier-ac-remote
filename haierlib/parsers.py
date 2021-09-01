import construct
from .types import *

state_struct = construct.Struct(
    'start' / construct.Int16ub,         # TODO assert == 65535
    'start_magic' / construct.Int16ub,  # TODO assert == 8704
    construct.Padding(8),
    'current_temp' / construct.Int16ub,         
    construct.Padding(8),
    'mode' / construct.Int16ub,
    'fan_speed' / construct.Int16ub,
    'limits' / construct.Int16ub,
    'power' / construct.Int16ub,
    'health' / construct.Int16ub,
    construct.Padding(2),
    'target_temp' / construct.Int16ub       # From 16!
)

def get_cmd_struct(data_len):
    return construct.Struct(
        'data_magic' / construct.Int16ub,
        'type' / construct.Int8ub,
        'data' / construct.Array(data_len - 4, construct.Int8ub),
    ) 

resp_struct = construct.Struct(
    construct.Padding(2),
    'start' / construct.Int16ub,     # TODO assert
    construct.Padding(4),
    construct.Padding(16),
    construct.Padding(16),

    # MAC address
    'mac_address' / construct.Array(12, construct.Int8ub),
    construct.Padding(4),
    construct.Padding(16),
    
    # Command sequence number and length
    construct.Padding(3),
    'seq' / construct.Int8ub,
    construct.Padding(3),
    'cmd_length' / construct.Int8ub,

    # Dynamic command array
    'cmd' / get_cmd_struct(construct.this._.cmd_length),
    'chksum' / construct.Int8ub
)

# TODO asserts, verify start magic, verify checksum
# TODO check execute() on parsers.ts for verifications

def parse_state(resp, state=None):
    if resp.cmd.type != 34:
        return
    
    # Create a new state
    if not state:
        state = State()

    # Get the constructed data
    state_st = state_struct.parse(get_cmd_struct(resp.cmd_length).build({
        'data_magic': resp.cmd.data_magic, 
        'type': resp.cmd.type, 
        'data': resp.cmd.data
    }))

    # Adjust and convert to State object
    state.update(
        current_temp=state_st.current_temp,
        target_temp=state_st.target_temp + 16,
        fan_speed=FanSpeed(state_st.fan_speed),
        mode=Mode(state_st.mode),
        health=(state_st.health % 2 != 0),
        limits=Limits(state_st.limits),
        power=(state_st.power % 2 != 0)
    )

    return state


def parse_resp(data):
    resp = resp_struct.parse(data)
    return parse_state(resp)

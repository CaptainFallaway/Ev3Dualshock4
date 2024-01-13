from .event_type import EventType

# Button press events

CROSS = EventType(304)
"""Cross button press event"""

CIRCLE = EventType(305)
"""Circle button press event"""

SQUARE = EventType(308)
"""Square button press event"""

TRIANGLE = EventType(307)
"""Triangle button press event"""

L1 = EventType(310)
"""L1 button press event"""

R1 = EventType(311)
"""R1 button press event"""

L2 = EventType(312)
"""L2 button press event"""

R2 = EventType(313)
"""R2 button press event"""

L3 = EventType(317)
"""L3 button press event (when you press left pedal)"""

R3 = EventType(318)
"""R3 button press event (when you press right pedal)"""

SHARE = EventType(314)
"""Share button press event"""

OPTIONS = EventType(315)
"""Options button press event"""

PS = EventType(316)
"""PS button press event"""

# Axis change events

LEFTJOY_X = EventType(0)
"""Left joystick X axis change event"""

LEFTJOY_Y = EventType(1)
"""Left joystick Y axis change event"""

L2_AXIS = EventType(2)
"""L2 Axis change event"""

RIGHTJOY_X = EventType(3)
"""Right joystick X axis change event"""

RIGHTJOY_Y = EventType(4)
"""Right joystick Y axis change event"""

R2_AXIS = EventType(5)
"""R2 Axis change event"""

DPAD_X = EventType(16)
"""D-Pad X axis change event"""

DPAD_Y = EventType(17)
"""D-Pad Y axis change event"""

# Event types

_EV_KEY = EventType(1)
"""Key press event type (should not be needed to be used)"""

_EV_ABS = EventType(3)
"""Axis change event type (should not be needed to be used)"""

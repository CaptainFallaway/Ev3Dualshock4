import struct
from typing import Iterator, Callable, Union, Awaitable, Coroutine

from . import constants
from .event_type import EventType

class RawEvent:
    """
    A class that represents a raw event from the controller.
    Directly from /dev/input/event4. (The stream)
    
    #### Attributes:
        time: The time of the event.
        ev_type: The event type of the event (Like axis change event or button press event types).
        ev_code: The event code of the event (What button or axis that changed).
        value: The value of the event. (The value of the axis or if the button is pressed or not)
    """

    def __init__(self, time: int, time_decimal: int, ev_type: int, ev_code: int, value: int) -> None:
        self.time = float(str(time) + "." + str(time_decimal))
        self.ev_type = ev_type
        self.ev_code = ev_code
        self.value = value


class Event:
    """
    A class that represents an event from the controller (abstracted from the raw event).
    
    #### Attributes:
        time: The time of the event.
        value: The value of the event.
        type: What type of event.
        
    #### Private attributes:
        _raw_event: The raw event.
    """

    def __init__(self, raw_event: RawEvent) -> None:
        self._raw_event = raw_event
        self.type = raw_event.ev_code
        self.time = raw_event.time
        self.value = raw_event.value

    def __str__(self) -> str:
        return vars(self).__str__()


class DeviceEventStream:
    """
    A class that represents a stream of events from the controller.

    #### Use:
        Use this class as an iterator to get events from the controller (read the stream).
    
    #### Example:
        >>> device = DeviceEventStream("/dev/input/event4")
        >>>
        >>> for event in device:
        ...     # The value has the type 'Event'
        ...     print(event)
    """

    SIZE = struct.calcsize("llHHI")

    def __init__(self, device_path: str) -> None:
        self._device_path = device_path

    def __iter__(self) -> Iterator[Event]:
        with open(self._device_path, "rb") as f:
            while True:
                event = RawEvent(*struct.unpack("llHHI", f.read(self.SIZE)))
                # print(event.ev_type == _types._EV_KEY or event.ev_type == _types._EV_ABS)
                if event.ev_type == constants._EV_KEY or event.ev_type == constants._EV_ABS:
                    yield Event(event)


class DeviceEventDispatcher:
    """
    A class that for registering events and listening for events from the controller.
    
    #### Use:
        Use this class to register events and listen for events from the controller.
        
    #### Example (Decorator):
        >>> device = DeviceEventDispatcher("/dev/input/event4")
        >>>
        >>> @device.register_event(constants.CROSS)
        >>> def handle_cross(event: Event):
        ...     if event.value == 1:
        ...         print("Cross pressed!")
        ...     else:
        ...         print("Cross released!")
        >>>
        >>> device.start_listening()

    #### Example (Normal):
        >>> device = DeviceEventDispatcher("/dev/input/event4")
        >>>
        >>> def handle_cross(event: Event):
        ...     if event.value == 1:
        ...         print("Cross pressed!")
        ...     else:
        ...         print("Cross released!")
        >>>
        >>> device.register_event(constants.CROSS, handle_cross)
        >>>
        >>> device.start_listening()
    """

    def __init__(self, device_path: str) -> None:
        self._device_path = device_path

        self.events = {}

    def register_event(self, event: EventType, callback: Union[None, Callable[[Event], None]] = None) -> Union[None, Callable[[Event], None]]:
        if isinstance(callback, Callable):
            self.events[event] = callback
            return None 
        
        def decorator(func: Callable[[Event], None]) -> None:
            self.events[event] = func

        return decorator

    def start_listening(self) -> None:
        for event in DeviceEventStream(self._device_path):
            if event.type in self.events:
                self.events[event.type](event)


    
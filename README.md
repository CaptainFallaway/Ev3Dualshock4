# Ev3Dualshock4

This is a small package for reading events from the dualshock 4 playstation controller for an ev3. The events yielded or dispatched are only axis or button press change events.

## TODO
- [ ] Add asyncio support

## Examples

Either as a generator for getting the events:

```PY
from Dualshock import DeviceEventStream, constants

device = DeviceEventStream("/dev/input/event4")

for event in device:  
    if event.type == constants.CROSS:
        if event.value == 1:
            print("Cross was pressed")
        elif event.value == 0:
            print("Cross was released")
```

Or as a event dispatcher:

```PY
from Dualshock import DeviceEventDispatcher, Event, constants

device = DeviceEventDispatcher("/dev/input/event4")

@device.register_event(constants.R2_AXIS)
def handle_r2_axis_change(event):
    print("Value changed too: " + event.value)
    print("Value changed at controller timestamp: " + event.time)

def handle_circle_state_change(event):
    if event.value == 1:
        print("Circle pressed!")
    else:
        print("Circle released!")

device.register_event(constants.CIRCLE, handle_circle)

print("starting to listen for events...")
print(device.events)

device.start_listening()
```

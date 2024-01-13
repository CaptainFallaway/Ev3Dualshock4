"""Testing the project"""

from Dualshock import DeviceEventDispatcher, DeviceEventStream, constants, Event

# device = DeviceEventStream("/dev/input/event4")

# print("Starting to listen for events...")

# for event in device:
#     if event.type == constants.CROSS:
#         print("Cross pressed!")




device = DeviceEventDispatcher("/dev/input/event4")

@device.register_event(constants.CROSS)
def handle_cross(event):
    if event.value == 1:
        print("Cross pressed!")
    else:
        print("Cross released!")

def handle_circle(event):
    if event.value == 1:
        print("Circle pressed!")
    else:
        print("Circle released!")

device.register_event(constants.CIRCLE, handle_circle)

print("starting to listen for events...")
print(device.events)

device.start_listening()
from sphero_sprk import Sphero
from communitysdk import list_connected_devices, MotionSensorKit

devices = list_connected_devices()
msk_filter = filter(lambda device: isinstance(device, MotionSensorKit), devices)
msk = next(msk_filter, None) # Get first Motion Sensor Kit


orb = Sphero()
orb.connect()

orb.set_rgb_led(0, 0, 0)


if msk != None:
        previous_value = 0

        def on_gesture(gestureValue):
            print('Gesture detected:', gestureValue)
            if gestureValue == "right":
                orb.set_rgb_led(255, 102, 26)
                orb.roll(20, 90)
            elif gestureValue == "left":
                orb.set_rgb_led(0, 255, 0)
                orb.roll(20, 270)
            elif gestureValue == "down":
                orb.set_rgb_led(102, 140, 255)
                orb.roll(20, 180)
            elif gestureValue == "up":
                orb.roll(20, 0)
                orb.set_rgb_led(255, 255, 0)
                

        def on_proximity(proximity):
                global previous_value
                delta = proximity - previous_value
                print((proximity, delta))
                orb.roll(proximity, 100)
                orb.set_rgb_led(proximity,0,0)

                previous_value = proximity
        print('Move your hand above the Motion Sensor:')
        msk.set_mode('gesture')
        msk.on_proximity = on_proximity
        msk.on_gesture = on_gesture
else:
        print('No Motion Sensor was found :(')

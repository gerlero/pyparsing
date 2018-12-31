#
# trafficLightDemo.py
#
# Example of a simple state machine modeling the state of a traffic light
#

import statemachine
import trafficlightstate


class TrafficLight:
    def __init__(self):
        # start light in Red state
        self._state = trafficlightstate.Red()

    def change(self):
        self._state = self._state.next_state()

    # get light behavior/properties from current state
    def __getattr__(self, attrname):
        return getattr(self._state, attrname)

    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self._state)


light = TrafficLight()
for i in range(10):
    print(light, end=' ')
    print(("STOP", "GO")[light.carsCanGo])
    light.crossingSignal()
    light.delay()
    print()

    light.change()
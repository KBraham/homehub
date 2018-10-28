import paho.mqtt.client as mqtt

import framework.Router
import lighting.ESPLedStripWarmWhite

if __name__ == '__main__':
    client = mqtt.Client()
    router = framework.Router(client)
    light = lighting.ESPLedStripWarmWhite(router)
    router.registerService(light)

    router.loopForever()

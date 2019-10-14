import framework.Service
import json
import math


class ESPLedStripWarmWhite(framework.Service):

    def __init__(self, router):
        super().__init__(router)
        self.serviceName = __class__.__name__
        self.debug(lambda: 'Starting class ' + self.serviceName)

        # List of all decives to follow and subscribe
        self.topicFilter = [
            'living/light1/switch',
            'living/light1/brightness/set',
            'living/light2/switch',
            'living/light2/brightness/set',
            '/devices/dimmer/dc:4f:22:4b:da:0f/w1/status',
            '/devices/dimmer/dc:4f:22:4b:da:0f/w2/status',
            '/devices/dimmer/dc:4f:22:4b:da:0f/w1/brightness',
            '/devices/dimmer/dc:4f:22:4b:da:0f/w2/brightness'
        ]

    def onMessage(self, topic, payload):
        """Callback from router for message updates"""

        # Convert led messages to old format
        # /kbdim/18:fe:34:f2:f5:de/1/ {"payload": {"l": 0, "ft": 1000}}
        # /kbdim/18:fe:34:f2:f5:de/2/ {"payload": {"l": 0, "ft": 1000}}
        self.debug('Got message' + topic + ' -> ' + payload)

        if "living/light1/switch" == topic:
            self._router.sendMessage("/devices/dimmer/dc:4f:22:4b:da:0f/w1/status_set", payload)
        
        if "living/light1/brightness/set" == topic:
            level = str(self.convertBrightness(int(payload)))
            self._router.sendMessage("/devices/dimmer/dc:4f:22:4b:da:0f/w1/brightness_set", level)

        if "living/light2/switch" == topic:
            self._router.sendMessage("/devices/dimmer/dc:4f:22:4b:da:0f/w2/status_set", payload)

        if "living/light2/brightness/set" == topic:
            level = str(self.convertBrightness(int(payload)))
            self._router.sendMessage("/devices/dimmer/dc:4f:22:4b:da:0f/w2/brightness_set", level)

        if "/devices/dimmer/dc:4f:22:4b:da:0f/w1/status" == topic:
            self._router.sendMessage("living/light1/status", payload)
        
        if "/devices/dimmer/dc:4f:22:4b:da:0f/w2/status" == topic:
            self._router.sendMessage("living/light2/status", payload)
        
        if "/devices/dimmer/dc:4f:22:4b:da:0f/w1/brightness" == topic:
            level = str(self.convertBrightnessInverse(int(payload)))
            self._router.sendMessage("living/light1/brightness/status", str(level))
        
        if "/devices/dimmer/dc:4f:22:4b:da:0f/w2/brightness" == topic:
            level = str(self.convertBrightnessInverse(int(payload)))
            self._router.sendMessage("living/light2/brightness/status", str(level))

    def convertBrightness(self, in_level):
        """Exponential conversion from level to brightness value"""
        maxp = 31
        maxv = 6.9305
        scale = maxv / maxp

        level = math.exp(scale * in_level)
        return int(level + .5)

    def convertBrightnessInverse(self, in_level):
        """Exponential conversion from brightness value to level"""
        maxp = 31
        maxv = 6.9305
        scale = maxp / maxv

        level = scale * math.log(in_level)
        return int(level + .5)

HomeHub
=======

HomeHub is a python routing framework using MQTT as transport layer. Plugins subscribe themselves to topics of which they state their interest. Plugins will receive all messages related to the topic in the onMessage callback. they can act on those messages and relay to other topics if needed.

For example, the ESPWarmWhite plugin listens to lights in the living room. This plugin converts HomeAssistant logical names (room/lightsource) to KBDIM identifiable lights (kbdimmer / light 1). In the process of routing the plugin converts brightness levels from a range into another range used by the devices. This works both ways, so confirmation of set brightness is again read by the sending party.

They main goal of this project is to provide easy hooks on MQTT messages, allow simple transportation and if needed transformation of data. It is developed in Python 3.5+ to use asyncio for asynchronous callbacks and interaction between plugins.


TODO: Make plugins configurable. The main idea of configuration is to use a set of YAML files which plugins may request to load initial config. This means that the warm white plugin no longer knows the rooms it serves, but receives a list of all topics and required conversion per topic.

class Router:
    """
    Core router for messages
    """

    _connector = None

    _services = []

    def __init__(self, connector):
        self._connector = connector
        self._connector.on_connect = self._onConnect
        self._connector.on_message = self._onMessage
        self._connector.connect("localhost", 1883, 60)

    def registerService(self, service):
        """Register new service to communicate to"""
        self._services.append(service)

    def sendMessage(self, topic, payload):
        """Send message to subscribers for specific topic channel"""

        print('Router sending message', topic, payload)
        self._connector.publish(topic, payload)

    def _onConnect(self, client, userdata, flags, rc):
        """Callback when router is connected to broker"""
        print("Connected with result code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("#")

    def _onMessage(self, client, userdata, message):
        """Receiving message for specific topic subscribed on"""
        services = [s for s in self._services if s.supportsTopic(message.topic)]

        for s in services:
            s.onMessage(message.topic, message.payload.decode('utf-8'))

    def loopForever(self):
        self._connector.loop_forever()

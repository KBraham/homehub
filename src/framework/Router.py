
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
        self._services.append(service)

    def sendMessage(self, topic, payload):
        print('Router sending message', topic, payload)
        self._connector.publish(topic, payload)

    def _onConnect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("#")

    def _onMessage(self, client, userdata, message):
        services = [s for s in self._services if s.supportsTopic(message.topic)]

        for s in services:
            s.onMessage(message.topic, message.payload.decode('utf-8'))

    def loopForever(self):
        self._connector.loop_forever()

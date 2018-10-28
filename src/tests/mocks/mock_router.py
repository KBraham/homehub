
class MockRouter:
    """
    Core router for messages
    """

    _services = []

    def __init__(self, connector):
        pass

    def registerService(self, service):
        self._services.append(service)

    def sendMessage(self, topic, payload):
        print('Router sending message', topic, payload)

    def loopForever(self):
        pass

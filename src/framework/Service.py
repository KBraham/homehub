
class Service:
    """
    Base class for all services running
    """

    serviceName = ''
    topicFilter = []

    _router = None

    def __init__(self, router):
        self._router = router

    def onMessage(self, topic, message):
        raise NotImplementedError

    def supportsTopic(self, topic):
        return topic in self.topicFilter

    ## Logging funcs

    def debug(self, message):
        if callable(message):
            message = message()

        print('DEBUG', self.serviceName, message)

    def info(self, message):
        if callable(message):
            message = message()

        print('INFO', self.serviceName, message)

    def warning(self, message):
        if callable(message):
            message = message()

        print('WARNING', self.serviceName, message)
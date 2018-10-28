import unittest
from framework import Service
from tests.mocks.mock_router import MockRouter


class TestProblem(unittest.TestCase):

    def testRouting(self):
        router = MockRouter
        service1 = Service(router)
        service2 = Service(router)

        service1.topicFilter = ['A', 'B', 'C']
        service2.topicFilter = ['B', 'C']

        self.assertTrue(service1.supportsTopic('A'))
        self.assertFalse(service1.supportsTopic('Z'))


if __name__ == '__main__':
    unittest.main()

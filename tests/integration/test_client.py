import unittest

from callfire.client import CallfireClient


class TestIntCallfireClient(unittest.TestCase):
    def test_getAccount(self):
        client = CallfireClient('api-login', 'api-password')
        account = client.me.getAccount().result()
        print(account)
        self.assertGreater(account.id, 0)

    def test_sendTexts(self):
        return

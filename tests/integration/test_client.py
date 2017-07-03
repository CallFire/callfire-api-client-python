import unittest

from callfire.client import CallfireClient


class TestIntCallfireClient(unittest.TestCase):
    def test_getAccount(self):
        client = CallfireClient('api-login', 'api-password')
        account = client.me.getAccount().result()
        print(account)
        self.assertGreater(account.id, 0)

    def test_getAccountThroughProxy(self):
        proxies = {
            "http": "https://127.0.0.1:8088",
            "https": "https://127.0.0.1:8089"
        }
        client = CallfireClient('api-login', 'api-password', {'proxies': proxies})
        account = client.me.getAccount().result()
        print(account)
        self.assertGreater(account.id, 0)

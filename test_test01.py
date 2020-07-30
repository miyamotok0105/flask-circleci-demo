import hello_world
import unittest

class TestHello(unittest.TestCase):
    
    def setUp(self):
        self.app = hello_world.app.test_client()
        self.app.testing = True
        
    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_flask_simple(self):
        result = self.app.get('/')
        assert b'HelloWorld' == result.data

if __name__ == '__main__':
    unittest.main()

import os
import re
import unittest
import tenlineapp

class TenLineTestCase(unittest.TestCase):

    def setUp(self):
        tenlineapp.app.config['TESTING'] = True
        self.app = tenlineapp.app.test_client()
        with tenlineapp.app.app_context():
            pass

    def tearDown(self):
        pass
        
    def test_get_index(self):
        rv = self.app.get('/')
        assert rv.status_code == 200
        assert re.search('<h1>\s+Hello', rv.get_data())

        
if __name__ == '__main__':
    unittest.main()
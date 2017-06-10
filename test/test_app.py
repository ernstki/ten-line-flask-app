import os
import re
import unittest
import tenline

class TenLineTestCase(unittest.TestCase):

    def setUp(self):
        tenline.app.config['TESTING'] = True
        self.app = tenline.app.test_client()
        with tenline.app.app_context():
            pass

    def tearDown(self):
        pass
        
    def test_get_index(self):
        rv = self.app.get('/')
        assert rv.status_code == 200
        assert re.search('<h1>\s+Hello', rv.get_data())

        
if __name__ == '__main__':
    unittest.main()
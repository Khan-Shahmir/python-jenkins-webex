mkdir python-jenkins-webex
cd python-jenkins-webex
git init

def add(a, b):
    return a + b

import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()



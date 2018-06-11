import unittest
import API

class testAPI(unittest.TestCase):

    def testAPI(self):
        API.ShadowSuite().generate_new_module()

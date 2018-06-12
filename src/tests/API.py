from core import exceptions
import unittest
import random
import API
import os

class TestAPI(unittest.TestCase):
    curpath = os.getcwd()
    curpath += '/'
    testModule = "sample"
    testService = "sample"
    searchString = "recon"
    seed = random.randint(111111, 999999)

    def test_NewModuleGeneration(self):
        API.ShadowSuite().generate_new_module(str(self.seed))
        if os.path.exists(self.curpath + str(self.seed) + '.py'):
            os.remove(self.curpath + str(self.seed) + '.py')

        else:
            raise exceptions.ModuleGenerationError("Generated Module Not Found!")

    def test_NewServiceGeneration(self):
        API.ShadowSuite().generate_new_service(str(self.seed))
        if os.path.exists(self.curpath + str(self.seed) + '.py'):
            os.remove(self.curpath + str(self.seed) + '.py')

        else:
            raise exceptions.ServiceGenerationError("Generated Service Not Found!")

    def test_ModuleListing(self):
        API.ShadowSuite().list_module()

    def test_ServiceListing(self):
        API.ShadowSuite().list_service()

    def test_ModuleFinding(self):
        API.ShadowSuite().find_module(self.testModule)

    def test_ServiceFinding(self):
        API.ShadowSuite().find_service(self.testService)

    def test_UseModule(self):
        API.ShadowSuite().use_module(self.testModule)

    def test_UseService(self):
        API.ShadowSuite().use_service(self.testService)

    def test_Suggest(self):
        API.ShadowSuite().suggest(self.searchString)

    def test_ClearScreen(self):
        API.ShadowSuite().clrscrn()

if __name__ == '__main__':
    unittest.main()

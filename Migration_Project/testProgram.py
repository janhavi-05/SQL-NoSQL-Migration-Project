from connection import *
from main import *
import unittest
from unittest.runner import TextTestResult, TextTestRunner

# defined all test cases
class Test(unittest.TestCase):
    def testConnectDBFalse(self):
        self.assertRaises(Exception,connectDB("University","mongodb://localhost:27017","Incorrect"))
    
    def testConnectDBTrue(self):
        assert(connectDB("University","mongodb://localhost:27017","1234"))
    
    def testConnectMongoDBFalse(self):
        self.assertRaises(Exception,connectDB("University","mongodb://localhost:27019","1234"))

    def testConnectMongoDBTrue(self):
        assert(connectDB("University","mongodb://localhost:27019","1234"))

# customizing test results output
def main():
    class CustomResult(TextTestResult):
        def __init__(self, *args, **kwargs):
            super(CustomResult, self).__init__(*args, **kwargs)
            self.success = []

        def addSuccess(self, test):
            super(CustomResult, self).addSuccess(test)
            self.success.append(test)

    unit = unittest.main(verbosity=2, exit=False, testRunner=TextTestRunner(resultclass=CustomResult))
    result = unit.result  # type: CustomResult
    # just do here all what you need...
    print('success:')
    for test in result.success:
        print(test)
    print('*' * 20 + '\n')

    print('skipped:')
    for test, reason in result.skipped:
        print('{}. reason: {}'.format(test, reason))
    print('*' * 20 + '\n')

    print('failures:')
    for test, trace in result.failures:
        print(test)
        # print(trace) ...if you need
    print('*' * 20 + '\n')

    for error in result.errors:
        # blablabla
        continue

if __name__ == "__main__":
    main()
#unittest.main(exit=False)
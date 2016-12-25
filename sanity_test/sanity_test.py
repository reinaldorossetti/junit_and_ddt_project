import unittest

from settings import variables_test as test
import test_login
import test_project_management
import test_testplan
import create_build
import thread
import multiprocessing as mp

class Test_Suite(unittest.TestCase):

    def test_main(self):

        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_login.LoginTestClass),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_project_management.project_test_class),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_testplan.test_plan_class),
            #unittest.defaultTestLoader.loadTestsFromTestCase(create_build.build_test_class),

            ])
        runner = unittest.TextTestRunner()
        runner.run (self.suite)
"""
if __name__ == "__main__":
    unittest.main()
    print "Lista de testes executados:"
    print test.list_result
"""

def suite(test):
    result = unittest.TestSuite()
    result.addTest( unittest.makeSuite(test) )
    #result.addTest( unittest.makeSuite(test_project_management.project_test_class) )
    return result

"""
try:
   thread.start_new_thread( suite, (login_test.LoginTestClass ) )
   thread.start_new_thread( suite, (test_project_management.project_test_class) )
except:
   print "Error: unable to start thread"
"""
if __name__ == '__main__':
    # Setup a list of processes that we want to run
    processes = [mp.Process(target=suite, args=(test_login.LoginTestClass)) for x in range(4)]

    # Run processes
    for p in processes:
        p.start()

    # Exit the completed processes
    for p in processes:
        p.join()

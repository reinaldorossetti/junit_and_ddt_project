"""
Testlink API Sample Python Client implementation
Autor: Reinaldo M.R.J
Date: 25-11-2014 - Version: 0.2
"""
import sys

print sys.executable
print "\n".join(sys.path)
from class_TestLink_connect import *
from datetime import datetime



class ReportTestLink(object):
    def __init__(self):
        self.TestlinkAPIClient = class_Testlink()

    #     # PASSED=p , FAILED=f , BLOCKED=b
    #     resultTest="p"
    #     # Build que esta associado aos testes.
    #     buildname="0.3.15"
    #     notes="Resultado obtido com sucesso."
    #     TestCaseName="ALL ONLINE - stress"
    #     TestPlanName="VM1110 (ZAPPER)"

    def ReportTest(self, TestCase, TestPlanName, resultTest, buildname, notes):
        # Pegar o ID do caso de Teste passando o Nome como parametro.
        tcid = self.TestlinkAPIClient.testCaseExternalID(TestCase)

        # Pegar o ID do Teste Plan passando o Nome como parametro.
        tpid = self.TestlinkAPIClient.getTestPlanId(TestPlanName)

        # Inseri os resultados no testlink.
        result = self.TestlinkAPIClient.reportTCResult(tcid, tpid, buildname, resultTest, notes)
        print "reportTCResult result was: %s" % (result)
        return result

    def new_test_plan(self, tplan_Name, project_name, Note):
        # Inseri os resultados no testlink.
        result = self.TestlinkAPIClient.createTestPlan(tplan_Name, project_name, Note)
        print "reportTCResult result was: %s" % (result)
        return result

    def getLastBuild(self, testplanid):
        """ getBuildsForTestPlan :
        Gets the last build on testplanid
        """
        try:
            builds = self.TestlinkAPIClient.getBuildsForTestPlan(testplanid)
            loop = len(builds)
            #print loop
            last = builds[loop-1]
            print last
        except (RuntimeError, TypeError, NameError):
            print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
            pass
        return last




    def TestPlanName_ID(self, plan_name):

        self.plan_name = plan_name
        if self.plan_name == "Sanity Test":
            self.testplanid = 162


        print self.testplanid
        return self.testplanid

    def TestResults(self):

        try:
            format = "%H:%M %d %Y"
            time = str(datetime.today())
            TestPlanName_ID = self.TestPlanName_ID("Sanity Test")
            buildname = "TestLink 1.9.13 (Stormbringer) DateTime: " + str(time)
            create_build = self.TestlinkAPIClient.create_build(3,buildname,"Test build")
            #buildname = self.testlink.getLastBuild(TestPlanName_ID[1])
            #  test Number: PFF-1199, TestPlanName: "Full Regression VM1110"
            #self.testNum = self.testNum.upper()
            #print "TestNumber, TestPlanID, BuildName ", self.testNum, TestPlanName_ID, buildname
            #self.testlink.ReportTest(self.testNum, TestPlanName_ID[0], result, buildname, notes)
            #print "Realizando Report in TestLink..."

        except (RuntimeError, TypeError, NameError):
               print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
               pass

if __name__ == "__main__":

    test = ReportTestLink()
    result = test.TestResults()
    print result
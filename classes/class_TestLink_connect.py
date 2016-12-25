"""
Class Testlink to connection with server TestLink
Author: Reinaldo M.R.J
Date: 25-11-2014 - Version: 0.1
"""
import testlink

# TODO: arrumar os retornos para usar TM.PASS e TM.FAIL

class class_Testlink(object):

    def __init__(self):
        
        #TESTLINK_SERVER_URL = 'https://testlink.paytvlabs.ml/lib/api/xmlrpc/v1/xmlrpc.php'
        TESTLINK_SERVER_URL = 'http://localhost/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
        # User: stormtest Pass: gvtpaytv@2015
        #TESTLINK_DEVKEY = '9e6a3a503f21a2d2a7625ffa56c7e3a9'
        TESTLINK_DEVKEY = 'fd193e851dfb567f93a22238f97f3453'
        tlh = testlink.TestLinkHelper(TESTLINK_SERVER_URL, TESTLINK_DEVKEY)
        self.myTestLink = tlh.connect(testlink.TestlinkAPIClient)
        global Project
        Project = "TestLink Automation"


    def reportTCResult(self, tcid, tpid, buildname, Result, notes):

        return self.myTestLink.reportTCResult(tcid, tpid, buildname, Result, notes)

    def testCaseIDByName(self, testcase):
             
        response = self.myTestLink.getTestCaseIDByName(testcase, testprojectname=Project)
        #response = self.myTestLink.getTestCase(testcaseexternalid='PFF-244')
        print response
        response = response[0].get("id")
        print "ID: " + str(response)
        return response

    def testCaseExternalID(self, testcase):

        response = self.myTestLink.getTestCase(testcaseexternalid=testcase, testprojectname=Project)
        print response
        #responsex = response[0].get("testcase_id")
        response = response[0].get("testcase_id")
        print "ID: " + str(response)
        return response

    def getTestPlanId(self, NEWTESTPLAN):

        response = self.myTestLink.getTestPlanByName(Project, NEWTESTPLAN)
        print "getTestPlanByName", response
        response = response[0].get("id")
        return response


    def create_build(self, test_planID, buildName, buildNotes):
        #Build kaon WM1110

        newBuild = self.myTestLink.createBuild(test_planID, buildName, buildNotes)
        isOk = newBuild[0]['message']
        if isOk == "Success!":
            newBuildID = newBuild[0]['id']
            print "New Test Build '%s' - id: %s" % (buildName, newBuildID)
        else:
            print "Error creating the Test Build '%s': %s " % (buildName, isOk)
            return False
        return True

    def createTestPlan(self, tplan_Name, project_name, note=''):
        """ create a test plan

            args variations: testprojectname - prefix

            supports also pre 1.9.14 arg definition, where 'testprojectname'
            was mandatory ('prefix' comes as alternative with 1.9.14)

            examples:
            - createTestPlan('aTPlanName', 'aTProjectName')
            - createTestPlan('aTPlanName', testprojectname='aTProjectName')
            - createTestPlan('aTPlanName', prefix='aTProjectPrefix')
        """
        print self.myTestLink.whatArgs('createTestPlan')

        new_tplan_name = self.myTestLink.createTestPlan(tplan_Name, project_name, [note])
        isOk = new_tplan_name[0]['message']
        if isOk == "Success!":
            new_tplan_name = new_tplan_name[0]['id']
            print "New Test Plan '%s' - id: %s" % (tplan_Name, project_name)
        else:
            print "Error creating the Test Plan '%s': %s " % (tplan_Name, project_name)
            return False
        return True


    def getBuildsForTestPlan(self, testplanid):
        """ getBuildsForTestPlan :
        Gets a list of builds within a test plan
        """
        test = []
        response = self.myTestLink.getBuildsForTestPlan(testplanid)
        #print "getTestPlanByName", response
        loop = len(response)
        for x in range(0,loop):
            test.append(response[x].get("name"))
            print test
        return test


    def getProjects(self):
        """ getProjects :
        Gets a list of Projects
        """
        test = []
        response = self.myTestLink.listProjects()
        print("Number of Projects in TestLink: %s " % (self.myTestLink.countProjects()))
        loop = int(self.myTestLink.countProjects())
        #loop = len(response)
        for x in range(0,loop-1):
            test.append(response[x][x])
            print test
        return test

if __name__ == "__main__":

    test = class_Testlink()
    result = test.getProjects()
    print result

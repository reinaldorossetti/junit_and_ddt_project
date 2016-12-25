import platform,sys, csv
# GET FULL PATH DIRETORY
f = sys.path[0]
# GET DIRECTORY OF PROJECT
project =  f.split("report", 1)
PROJECT_PATH = "D:\\Dropbox\\Dropbox\\positivo_selenium\\"
print "Project Path: " + PROJECT_PATH
LOGIN_PAGE = "/login.php?note=expired"
BASE_URL = "http://localhost//testlink"
MAIN_MENU = "/lib/general/navBar.php?tproject_id=0&tplan_id=0&updateMainPage=1"
INDEX_MENU = "//index.php?caller=login"
LOGOUT_PAGE = "/logout.php"
MAIN_PAGE = "/lib/general/mainPage.php"
# Delete page
DELETE_PROJECT = "/lib/project/projectEdit.php?doAction=doDelete&tprojectID="
DELETE_TESTPLAN = "/lib/plan/planEdit.php?do_action=do_delete&tplan_id="
DELETE_BUILD = "/lib/plan/buildEdit.php?do_action=do_delete&build_id="
# Main tests
LANGUAGE_MENU = "/lib/usermanagement/userInfo.php"
TEST_PLAN_PAGE = "/lib/plan/planView.php"
TEST_PROJECT = "/lib/project/projectView.php"
TEST_BUILD_PAGE = "/lib/plan/buildView.php"
REPORT_EXCEL_PATH = PROJECT_PATH + "report\\files\\"

PROJECT_PATH_LIN = "/home/reiload/Dropbox/positivo_selenium/"
LOGIN_PASS_WIN = PROJECT_PATH + "data//login_password_ok.csv"
LOGIN_PASS_LIN = PROJECT_PATH_LIN + "data/login_password_ok.csv"
LOGIN_FAIL_WIN = PROJECT_PATH + "data//loginOrPass_failed.csv"
LOGIN_FAIL_LIN = PROJECT_PATH_LIN + "data/loginOrPass_failed.csv"

PROJECT_PASS_WIN = PROJECT_PATH + "data\\projects.csv"
PROJECT_PASS_LIN = PROJECT_PATH_LIN + "data/projects.csv"

TEST_PLAN_WIN = PROJECT_PATH + "data\\test_plan.csv"
TEST_PLAN_LIN = PROJECT_PATH_LIN + "data/test_plan.csv"

TEST_BUILD_WIN = PROJECT_PATH + "data\\build.csv"
TEST_BUILD_LIN = PROJECT_PATH_LIN + "data/build.csv"

TOP_TEXT_MAIN_PAGE = "TestLink 1.9.13 (Stormbringer)"
XPATH_TOP_TEXT_MAIN_PAGE = "/html/body/div[2]/span[3]"
DELAY_FAST = 3
DELAY_HIGH = 7
SCREEN_SAVE= PROJECT_PATH + "sanity_test\\screenshots\\"
list_result = []

# GET PATH OF ACCORDING WITH OPERATING SYSTEM
platform = platform.uname()[0]
if platform == "Windows":
    PATH_TEST_OK = LOGIN_PASS_WIN
    PATH_TEST_FAIL = LOGIN_FAIL_WIN
elif platform == "Linux":
    PATH_TEST_OK = LOGIN_PASS_LIN
    PATH_TEST_FAIL = LOGIN_FAIL_LIN

if platform == "Windows":
    PROJECT_PATH_CSV = PROJECT_PASS_WIN
elif platform == "Linux":
    PROJECT_PATH_CSV = PROJECT_PASS_LIN

if platform == "Windows":
    TESTPLAN_PATH_CSV = TEST_PLAN_WIN
elif platform == "Linux":
    TESTPLAN_PATH_CSV = TEST_PLAN_LIN

if platform == "Windows":
    BUILD_PATH_CSV = TEST_BUILD_WIN
elif platform == "Linux":
    BUILD_PATH_CSV = TEST_BUILD_LIN


def get_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    print file_name
    data_file = open(file_name, "rb")
    # create a CSV Reader from CSV file
    reader = csv.reader(data_file)
    # skip the headers
    next(reader, None)
    # add rows from reader to list
    for row in reader:
         rows.append(row)
    return rows
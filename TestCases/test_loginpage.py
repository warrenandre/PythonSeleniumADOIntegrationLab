from ConfigData.config import TestData
from PageObjects.LoginPage import LoginPage

class Test_Login():
    """ Test cases for login """
    def test_login(self,setup,screen_recorder):
        try:
            self.driver = setup  # initialize  driver from conftest file
            screen_recorder.start_recording("login_test")
            lpobj = LoginPage(self.driver)  # LoginPage Object
            screen_recorder.capture_screenshot("Login")
            lpobj.verify_title(TestData.loginPageTitle)
            lpobj.login(TestData.username, TestData.password,screen_recorder)
            screen_recorder.capture_screenshot("page_login")
            is_link_visible = lpobj.is_edit_site_available()
            screen_recorder.capture_screenshot("page_edit_available")
            assert is_link_visible == TestData.adminEditSiteLink
        finally:
            # Stop recording
                recording_path = screen_recorder.stop_recording()
                print(f"Test recording saved: {recording_path}")
        
from ConfigData.config import TestData
from PageObjects.HomePage import HomePage


class Test_HomePage():

    def test_home_page_header(self, setup):
        self.driver = setup  # initialize driver from conftest file
        lpobj = HomePage(self.driver)
        actual_header_value = lpobj.get_header_value()
        assert actual_header_value== TestData.homePageHeder # verify home page header
    
    def test_home_page_sample_page(self, setup):
       
        self.driver = setup  # initialize  driver from conftest file
        lpobj = HomePage(self.driver)  # LoginPage Object
        sample_page_is_visible = lpobj.is_sample_page_visible()
        if(sample_page_is_visible):
            assert sample_page_is_visible == True  # verify sample page link is visible
        else:
            raise AssertionError("Sample page link is not visible on the home page.")
        
    # def test_profile_img_visible(self,setup):
    #     self.driver = setup  # initialize  driver from conftest file
    #     lpobj = LoginPage(self.driver)  # LoginPage Object
    #     homeobj = lpobj.login(TestData.username, TestData.password) # HomePage Object
    #     profile_img= homeobj.is_profile_img_visible()   # verify profile image
    #     assert profile_img == True







from conftest import *
from hrmpages.LoginPage import LoginPage


@pytest.mark.usefixtures("browser_setup")
class Test_Login:

    def setup_class(self):
        self.driver.get(baseURL)
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        self.login_page.login(username, password)

    def teardown_class(self):
        self.driver.quit()

from libraries.ui.base_page import BasePage

class LoginPage(BasePage):

    base_url = "https://www.saucedemo.com/"
    locators_file = "login_page.json"

    def login(self, username: str, password: str):
        """Perform Login."""
        self.navigate(self.base_url)
        self.fill("username_input", username)
        self.fill("password_input", password)
        self.click("login_button")

    def get_error_message(self) -> str:
        """Get login error message."""
        return self.get_text("error_message")
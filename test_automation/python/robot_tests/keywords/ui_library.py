"""UI Library for Robot Framework."""
from playwright.sync_api import sync_playwright
from robot.api.deco import keyword, library
from libraries.ui.login_page import LoginPage

@library
class UILibrary:
    """UI Library for Robot Framework."""

    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
        self.login_page = None

    @keyword
    def open_browser_to_login(self):
        """Open browser to login"""
        self.playwright = sync_playwright().start()
        self.browser =  self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.login_page = LoginPage(self.page)

    @keyword
    def login_with_credentials(self, username: str,password: str):
        """Login with credentials"""
        self.login_page.login(username, password)

    @keyword
    def verify_login_successful(self):
        """Verify login was successful by checking the URL."""
        assert "inventory" in self.page.url, f"Login failed. URL was: {self.page.url}"

    @keyword
    def get_login_error_message(self) -> str:
        """Get the error message shown on the login page."""
        return self.login_page.get_error_message()

    @keyword
    def close_browser(self):
        """Close browser and stop Playwright."""
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
        

from playwright.sync_api import Page
from libraries.ui.login_page import LoginPage

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in page.url

def test_invalid_login_shows_error(page: Page):
    login_page = LoginPage(page)
    login_page.login("locked_out_user", "secret_sauce")

    error = login_page.get_error_message()
    assert "locked out" in error.lower()

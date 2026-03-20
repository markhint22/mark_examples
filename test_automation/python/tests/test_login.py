"""Tests for the login functionality of the application."""
from playwright.sync_api import Page
from libraries.ui.login_page import LoginPage

def test_successful_login(page: Page):
    """Test successful login."""
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in page.url

def test_invalid_login_shows_error(page: Page):
    """Test invalid login shows error message."""
    login_page = LoginPage(page)
    login_page.login("locked_out_user", "secret_sauce")

    error = login_page.get_error_message()
    assert "locked out" in error.lower()

from pathlib import Path
from playwright.sync_api import Page, Locator
from libraries.utils.locator_loader import LocatorLoader


class BasePage:
    """Base class for all page objects."""

    base_url: str = ""
    locators_file: str = ""

    def __init__(self, page: Page):
        self.page = page
        self._locators = None

        if self.locators_file:
            locators_path = Path(__file__).parent.parent / "ui" / "locators" / self.locators_file
            self._locators = LocatorLoader(page, str(locators_path))

    def locator(self, name: str) -> Locator:
        """Get locator by name from JSON file."""
        if not self._locators:
            raise ValueError("No locators file configured for this page.")
        return self._locators.get(name)

    def navigate(self, url: str):
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()
    
    def get_url(self) -> str:
        return self.page.url

    def expect_title(self, expected_title: str):
        expect(self.page).to_have_title(expected_title)

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, value: str):
        self.page.fill(selector, value)

    def get_text(self, selector: str) -> str:
        return self.page.text_content(selector) or ""
    
    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)
    
    def wait_for_element_visible(self, selector: str, timeout: int = 30000):
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)

    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"output/screenshots/{name}.png")
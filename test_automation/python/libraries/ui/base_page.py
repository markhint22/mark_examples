from pathlib import Path
from playwright.sync_api import Page, Locator, expect
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
        self.locator(selector).click()

    def fill(self, selector: str, value: str):
        """Fill input by locator name."""
        self.locator(selector).fill(value)

    def get_text(self, selector: str) -> str:
        """Get text by locator name."""
        return self.locator(selector).text_content() or ""
    
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible by locator name."""
        return self.locator(selector).is_visible()
    
    def wait_for_element_visible(self, selector: str, timeout: int = 30000):
        """Wait for element to be visible by locator name."""
        self.locator(selector).wait_for(state="visible", timeout=timeout)

    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"output/screenshots/{name}.png")
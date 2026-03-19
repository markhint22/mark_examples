import json
from pathlib import Path
from playwright.sync_api import Page, Loader

class LocatorLoader:
    """Loads and resolves locators from JSON files"""

    def __init__(self, page: Page, locators_path: str):
        self.page = page
        self.locators = self._load_locators(locators_path)

    def _load_locators(self, path: str) -> dict:
        """Load locators from a JSON file"""
        with open(path, "r") as f:
            return json.load(f)
        
    def get(self, name: str) -> Locator:
        """Get a locator by name."""
        if name not in self.locators:
            raise KeyError(f"Locator '{name}' not found in locators file.")
        
        locator_def = self.locators[name]
        valuetype = locator_def["valuetype"]
        value = locator_def["def"]

        # Map valuetype to Playwright selector syntax
        if valuetype == "getByTestId":
            return self.page.get_by_test_id(value)
        elif valuetype == "getByRole":
            role = locator_def.get("role","button")
            return self.page.get_by_role(role, name=value)
        elif valuetype == 'getByText':
            return self.page.get_by_text(value)
        elif valuetype == 'getByLabel':
            return self.page.get_by_label(value)
        elif valuetype == 'getByPlaceholder':
            return self.page.get_by_placeholder(value)
        elif valuetype == "css":
            return self.page.locator(value)
        elif valuetype == "xpath":
            return self.page.locator(f"xpath={value}")
        else:
            raise ValueError(f"Unknown valuetype: {valuetype}")
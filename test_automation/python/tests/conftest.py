import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa", help="Target environment")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="function")
def page(page: Page):
    """override default page fixture with custom timeout"""
    page.set_default_timeout(30000)  # Set default timeout to 30 seconds
    return page
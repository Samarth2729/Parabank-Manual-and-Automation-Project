import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture
def login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login steps
        login_page = LoginPage(page)
        login_page.open_login_page()
        login_page.login("john", "demo")

        yield page

        browser.close()


BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"
@pytest.fixture
def open_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(BASE_URL)

        yield page

        context.close()
        browser.close()


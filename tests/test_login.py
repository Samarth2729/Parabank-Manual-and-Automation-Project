from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)

    # Step 1: Open login page
    login_page.open_login_page()

    # Step 2: Login with VALID credentials
    login_page.login("john", "demo")

    # Step 3: Wait for successful navigation
    page.wait_for_url("**/overview.htm")

    # Step 4: Assert logout link is visible
    assert login_page.is_logout_displayed(), "Logout link not visible – login failed"

def test_invalid_login_shows_error(page):
    login_page = LoginPage(page)

    login_page.open_login_page()
    login_page.login("invalid_user", "wrong_password")

    page.wait_for_selector("p.error")

    assert login_page.get_error_message().is_visible()
    assert login_page.get_error_message().text_content() == \
        "The username and password could not be verified."

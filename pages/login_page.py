class LoginPage:
    def __init__(self, page):
        self.page = page

    def open_login_page(self):
       self.page.goto(
            "https://parabank.parasoft.com/parabank/index.htm",
            timeout=60000
        )

    def login(self, username, password):
        self.page.fill("input[name='username']", username)
        self.page.fill("input[name='password']", password)
        self.page.click("input[value='Log In']")

    def is_logout_displayed(self):
        return self.page.locator("a[href*='logout']").is_visible()

    def get_error_message(self):
        return self.page.locator("p.error")

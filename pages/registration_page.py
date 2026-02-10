from conftest import BASE_URL

class RegistrationPage:
    def __init__(self, page):
        self.page = page

    def open_site(self):
        self.page.goto(BASE_URL)

    def click_register_link(self):
        self.page.click("a[href*='register.htm']")

    def fill_registration_form(self, user):
        self.page.wait_for_selector('input[name="customer.firstName"]', timeout=10000)

        self.page.fill('input[name="customer.firstName"]', user["first_name"])
        self.page.fill('input[name="customer.lastName"]', user["last_name"])
        self.page.fill('input[name="customer.address.street"]', user["address"])
        self.page.fill('input[name="customer.address.city"]', user["city"])
        self.page.fill('input[name="customer.address.state"]', user["state"])
        self.page.fill('input[name="customer.address.zipCode"]', user["zip"])
        self.page.fill('input[name="customer.phoneNumber"]', user["phone"])
        self.page.fill('input[name="customer.ssn"]', user["ssn"])
        self.page.fill('input[name="customer.username"]', user["username"])
        self.page.fill('input[name="customer.password"]', user["password"])
        self.page.fill('input[name="repeatedPassword"]', user["password"])

    def submit_registration(self):
        self.page.click("input[value='Register']")

    def get_success_message(self):
        return self.page.text_content("h1.title")




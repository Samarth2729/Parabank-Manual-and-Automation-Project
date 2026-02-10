from playwright.sync_api import expect

class FundTransferPage:
    def __init__(self, page):
        self.page = page
        self.transfer_funds_link = page.locator("a[href*='transfer']")
        self.amount_input = page.locator("#amount")
        self.from_account_dropdown = page.locator("#fromAccountId")
        self.to_account_dropdown = page.locator("#toAccountId")
        self.transfer_button = page.locator("input[value='Transfer']")
        self.success_message = page.locator("text=Transfer Complete")

    def open_fund_transfer(self):
        self.transfer_funds_link.click()
        expect(self.amount_input).to_be_visible()

    def enter_amount(self, amount):
        self.amount_input.fill(str(amount))

    def select_from_account(self, account):
        self.from_account_dropdown.select_option(account)

    def select_to_account(self, account):
        self.to_account_dropdown.select_option(account)

    def submit_transfer(self):
        self.transfer_button.click()
        self.page.wait_for_load_state("networkidle")

    def is_transfer_failed_due_to_insufficient_balance(self):
        expect(self.error_message).to_be_visible(timeout=5000)
        return True

from playwright.sync_api import Page




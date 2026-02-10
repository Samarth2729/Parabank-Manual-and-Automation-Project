from playwright.sync_api import Page
import re

class AccountsOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.accounts_overview_link = "a[href*='overview.htm']"
        self.account_links = "table tr td a"

    def open_accounts_overview(self):
        self.page.click(self.accounts_overview_link)
        self.page.wait_for_selector(self.account_links)

    def get_all_account_numbers(self):
        return self.page.locator(self.account_links).all_inner_texts()

    def get_account_balance(self, account_number):
        locator = (
            f"//a[text()='{account_number}']"
            "/parent::td/following-sibling::td[1]"
        )
        balance_text = self.page.locator(locator).inner_text()
        balance_value = re.sub(r"[^\d.-]", "", balance_text)
        return float(balance_value)


class FundTransferPages:
    def __init__(self, page: Page):
        self.page = page

        self.transfer_funds_link = "a[href*='transfer.htm']"
        self.amount_input = "input#amount"
        self.from_account_dropdown = "select#fromAccountId"
        self.to_account_dropdown = "select#toAccountId"
        self.transfer_button = "input[value='Transfer']"
        self.success_message = "h1:has-text('Transfer Complete')"

    def open_transfer_funds(self):
        self.page.click(self.transfer_funds_link)

    def transfer_funds(self, amount, from_account, to_account):
        self.page.fill(self.amount_input, str(amount))
        self.page.select_option(self.from_account_dropdown, from_account)
        self.page.select_option(self.to_account_dropdown, to_account)
        self.page.click(self.transfer_button)

    def is_transfer_successful(self):
        return self.page.locator(self.success_message).is_visible()
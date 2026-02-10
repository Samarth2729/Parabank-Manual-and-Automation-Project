from pages.accounts_overview_page import AccountsOverviewPage
from pages.fund_transfer_page import FundTransferPage
def test_tc_ft_01_fund_transfer_between_own_accounts(login):
    page = login
    fund_transfer = FundTransferPage(page)

    fund_transfer.open_fund_transfer()
    fund_transfer.enter_amount(100)
    fund_transfer.select_from_account("13344")
    fund_transfer.select_to_account("13344")
    fund_transfer.submit_transfer()

    assert fund_transfer.is_transfer_successful()

def test_tc_ft_04_transfer_fails_when_amount_exceeds_balance(login):
    page = login
    fund_transfer = FundTransferPage(page)

    fund_transfer.open_fund_transfer()
    fund_transfer.enter_amount(999999)   # very high amount
    fund_transfer.select_from_account("13344")
    fund_transfer.select_to_account("13344")
    fund_transfer.submit_transfer()

    assert fund_transfer.is_transfer_failed_due_to_insufficient_balance()



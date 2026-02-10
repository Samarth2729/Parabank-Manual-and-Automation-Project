from pages.overview_fundtransfer_page import AccountsOverviewPage
from pages.overview_fundtransfer_page import FundTransferPages


def test_tc_ft_06_verify_balance_updates_after_transfer(login):
    page = login

    accounts_page = AccountsOverviewPage(page)
    fund_transfer_page = FundTransferPages(page)

    # Step 1: Open overview and read accounts
    accounts_page.open_accounts_overview()
    accounts = accounts_page.get_all_account_numbers()

    from_account = accounts[0]
    to_account = accounts[1]
    transfer_amount = 50

    # Step 2: Balances before transfer
    from_before = accounts_page.get_account_balance(from_account)
    to_before = accounts_page.get_account_balance(to_account)

    print(f"\nBEFORE TRANSFER:")
    print(f"From Account {from_account} Balance: {from_before}")
    print(f"To Account {to_account} Balance: {to_before}")

    # Step 3: Transfer funds
    fund_transfer_page.open_transfer_funds()
    fund_transfer_page.transfer_funds(
        transfer_amount,
        from_account,
        to_account
    )

    # Step 4: Validate via balances (SOURCE OF TRUTH)
    accounts_page.open_accounts_overview()
    from_after = accounts_page.get_account_balance(from_account)
    to_after = accounts_page.get_account_balance(to_account)
    print(f"\nAFTER TRANSFER:")
    print(f"From Account {from_account} Balance: {from_after}")
    print(f"To Account {to_account} Balance: {to_after}")
    # Step 5: Assertions
    assert from_after == from_before - transfer_amount
    assert to_after == to_before + transfer_amount

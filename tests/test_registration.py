import time

from pages.registration_page import RegistrationPage


def test_tc_reg_01_and_06(page):
    registration = RegistrationPage(page)

    user = {
        "first_name": "Test",
        "last_name": "User",
        "address": "Street",
        "city": "City",
        "state": "State",
        "zip": "12345",
        "phone": "9999999999",
        "ssn": "123456",
        "username": f"user_{int(time.time())}",
        "password": "Test@123"
    }

    registration.open_site()                 # ✅ site opens here
    registration.click_register_link()       # ✅ click register
    registration.fill_registration_form(user)
    registration.submit_registration()

    assert "Welcome" in registration.get_success_message()

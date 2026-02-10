# Parabank-Manual-and-Automation-Project

## 📌 Project Overview

This project was created by a **Samarth Rathore** to demonstrate practical understanding of **Manual Testing fundamentals** along with **basic Automation Testing using Playwright and Python**.

The ParaBank Demo Application was chosen to practice real-world banking scenarios such as **Registration, Login, Fund Transfer, and Logout**. The focus of this project is not just automation, but learning how a QA engineer:

* Writes **clear test cases**
* Identifies and reports **functional defects**
* Handles **real application issues** professionally
* Builds a **simple, maintainable automation framework**

This project reflects a **learning-oriented approach**, showing how a fresher applies QA concepts in a structured way.

---

## 🛠 Tech Stack

* **Automation Tool:** Playwright (Beginner–Intermediate usage)
* **Programming Language:** Python
* **Test Runner:** Pytest
* **Framework Design:** Page Object Model (basic implementation)
* **Reporting:** Playwright HTML Report
* **Browser:** Chromium / Chrome

---

## 📂 Project Structure

```
Parabank-Testing-Project/
│
├── manual-testing/
│   ├── Test Plan and Automation Plan (ParaBank)
│   ├── Test Cases (Excel)
│   ├── Test Execution Report
│   └── Defect Report
│
├── automation-testing/
│   ├── pages/
│   │   ├── login_page.py
│   │   ├── registration_page.py
│   │   └── fund_transfer_page.py
│   │   └── overview_fundtransfer_page.py
│   ├── tests/
│   │   ├── test_login.py
│   │   ├── test_registration.py
│   │   └── test_fund_transfer.py
│   │   └── test_overview_fundtransfer.py
│   ├── conftest.py
│   
│
└── README.md
```

---

## ✅ Manual Testing Scope

### Modules Covered

* User Registration
* User Login & Logout
* Account Overview
* Fund Transfer
* Error Message Validation

### Testing Types Applied

* Smoke Testing
* Regression Testing
* Integration Testing
* User Acceptance Testing (UAT)
* Exploratory Testing
* Boundary Value Analysis (BVA)
* Equivalence Partitioning

### Key Deliverables

* Detailed **Test Plan**
* Well-structured **Test Cases (Excel)**
* **Test Execution Report** with Pass/Fail status
* **Bug Report** with severity & priority

---

## 🤖 Automation Testing Scope

### Automated Test Cases

#### Login Module

* Verify login with valid credentials
* Verify dashboard redirection after login
* Verify logout functionality

#### Fund Transfer Module

* Transfer between own accounts
* Verify balance update after transfer
* Validate behavior when transfer amount exceeds balance *(Defect Found)*

#### Registration Module (Partial)

* Register user with valid details
* Verify success message after registration

---

## 🧱 Automation Framework Design

* **Page Object Model (POM)** used to separate test logic and UI locators
* No assertions or waits inside page classes
* Test files control validations and synchronization
* Fixtures used for login and browser setup

---

## 🐞 Defects Identified 

During testing, multiple functional issues were identified and documented instead of forcing automation tests to pass.

### Critical Defect Example

**Bug Title:** Fund transfer allowed even when transfer amount exceeds available balance

* **Type:** Functional / Business Logic Defect
* **Severity:** Critical
* **Priority:** High

**Expected Result:**
Application should block the transfer and display an *"Insufficient balance"* message.

**Actual Result:**
Application allows the transfer to complete successfully.

📌 *This defect was reported to demonstrate proper QA responsibility, even though the application is a demo.*

---

## ⚠ Challenges Faced & Solutions

| Issue                                  | Solution                                  |
| -------------------------------------- | ----------------------------------------- |
| Flaky failures due to page load        | Used explicit waits instead of time.sleep |
| Login wait caused invalid test failure | Moved waits to test layer                 |
| Dynamic account numbers                | Fetched account numbers dynamically       |
| Missing element IDs                    | Used name-based selectors                 |
| Demo app allows invalid behavior       | Logged defects instead of forcing pass    |

---
---

## 🚀 How to Run Automation Tests

```bash
pip install playwright pytest
playwright install
pytest --headed
```

---

## 📌 Conclusion

This project was developed as part of my learning journey as a **QA Fresher**. It demonstrates my ability to:

* Perform structured **manual testing**
* Identify and report **real functional bugs**
* Automate basic workflows using **Playwright with Python**
* Follow industry-standard practices like **POM and defect reporting**

This project helped me gain hands-on confidence in both **manual and automation testing**, preparing me for entry-level QA roles.

---

👤 **Author:** Samarth Rathore
🎓 **Role:** QA Fresher / Automation Testing Trainee
🧪 **Skills:** Manual Testing, Test Case Design, Bug Reporting, Playwright (Python), Basic Automation Frameworks

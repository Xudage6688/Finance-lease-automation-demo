# Demo Automation Testing Framework

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green)](https://www.selenium.dev/)
[![pytest](https://img.shields.io/badge/pytest-7.x-orange)](https://pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

> Enterprise-grade full-stack automation testing framework for financial services - Web UI + API testing

## Core Philosophy

```python
# Design Patterns Applied
┌─────────────────────────────────────────────────────────────┐
│  Test Cases Layer     →  Business Validation Logic         │
│  Page Objects Layer   →  UI Abstraction &封装           │
│  Core Framework      →  Selenium WebDriver Abstraction   │
│  Utilities Layer     →  Cross-cutting Concerns           │
└─────────────────────────────────────────────────────────────┘
```

This framework demonstrates **real-world application of architectural patterns** in an enterprise environment:

- **POM Pattern**: Page Object Model for maintainable UI test automation
- **Layered Architecture**: Clear separation between test logic, page operations, and framework concerns
- **Data-Driven Testing**: Externalized test data with multi-environment support (UAT/PRE/PROD)
- **Dual Testing Modes**: Web UI automation + REST API testing in one framework

---

## Architecture Highlights

### Layered Design

| Layer | Purpose | Key Classes |
|-------|---------|-------------|
| `cases/` | Test execution & assertions | `test_subscription.py`, `test_pre_audit.py` |
| `page_object/` | Page element abstraction | `pre_audit.py`, `sign_order.py`, `request_pay.py` |
| `core/` | WebDriver wrapper & utilities | `basepage.py` |
| `public/utils/` | Cross-cutting concerns | logging, reporting, config |

### Design Patterns in Practice

| Pattern | Implementation |
|---------|----------------|
| **Factory** | `BasePage` serves as abstract factory for page objects |
| **Singleton** | WebDriver instance management, config file readers |
| **Strategy** | Multi-environment config switching (UAT/PRE/PROD) |
| **Decorator** | Logging decorators, retry mechanisms |

```python
# Example: BasePage Factory Pattern
class BasePage:
    """Abstract factory for page objects"""
    def __init__(self, driver):
        self.driver = driver

    def create_page_object(self, page_class):
        """Factory method - returns configured page object"""
        return page_class(self.driver)
```

### Business Domain Coverage

| Domain | Business Flow |
|--------|--------------|
| Authentication | Login, permission validation |
| Pre-Audit | Customer qualification, risk assessment |
| Order Submission | Information entry, data validation |
| Contract Signing | E-signature, contract generation |
| Fund Request | Loan disbursement process |
| Review & Approval | Credit review workflow |
| Subscription | Individual/Enterprise subscription |

---

## Technical Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.8+ |
| UI Framework | Selenium 4.x |
| Test Runner | pytest 7.x |
| Reports | Allure, HTMLTestRunner |
| API | requests, PyYAML |
| Utilities | openpyxl, xmind |

---

## Project Structure

```
demo-automation/
├── cases/                  # Test cases (business validation)
├── page_object/            # Page objects (UI abstraction)
├── core/                   # Core framework (BasePage, etc.)
├── public/utils/           # Utilities (logging, reporting)
├── data/                   # Test data & configuration
├── API_test/               # API testing module
├── conf/                   # Configuration files
├── testData/               # Test data files
├── conftest.py             # pytest fixtures
├── pytest.ini              # pytest configuration
└── main.py                 # Entry point
```

---

## Quick Start

```bash
# Clone & setup
git clone https://github.com/example/demo-automation.git

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit data/data.ini with your credentials

# Run tests
pytest

# Generate Allure report
pytest --alluredir ./temp/allure/reports
allure serve ./temp/allure/reports
```

---

## Key Takeaways (Framework Thinking)

### What Makes This Framework Enterprise-Ready

1. **Explicit Waits Over Implicit Waits**
   - `WebDriverWait` with specific conditions vs `time.sleep()`
   - More stable, faster execution

2. **Configuration Externalization**
   - Environment variables for sensitive data
   - INI/YAML for environment-specific configs

3. **Consistent Logging**
   - `logging` module with structured output
   - Automatic screenshot capture on failures

4. **Test Isolation**
   - Each test fixture properly cleaned up
   - Independent test execution supported

5. **CI/CD Ready**
   - Jenkins compatible
   - GitHub Actions ready

---

## Documentation

- [Architecture Design](docs/ARCHITECTURE.md)
- [Tech Stack](docs/TECH_STACK.md)

## License

[MIT License](LICENSE)

## Author

**Xudage6688** - [GitHub](https://github.com/Xudage6688)
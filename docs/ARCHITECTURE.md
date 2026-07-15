# Architecture Design

## Design Principles

### 1. Page Object Model (POM)

The framework implements POM pattern to separate page element locators from business logic, improving maintainability and reusability.

```
┌─────────────────────────────────────────────────────────────┐
│                      Test Cases (cases/)                    │
│                 Business Validation Layer                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Page Objects (page_object/)               │
│                  UI Abstraction Layer                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      Core (core/)                           │
│               WebDriver Abstraction Layer                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Selenium WebDriver                       │
│                       Driver Layer                          │
└─────────────────────────────────────────────────────────────┘
```

### 2. Layered Architecture

| Layer | Directory | Responsibilities |
|-------|-----------|------------------|
| Test Layer | `cases/` | Test definitions, data-driven execution, assertions |
| Page Object Layer | `page_object/` | Element locators, operations, business flows |
| Core Layer | `core/` | WebDriver wrappers, common methods, logging |
| Utility Layer | `public/utils/` | Config reading, cookie management, reporting |
| Data Layer | `data/` | Config files, test data, element definitions |
| API Layer | `API_test/` | REST API testing, YAML cases, config management |

### 3. Module Responsibilities

#### Core Module (`core/`)

- `basepage.py`: Selenium WebDriver abstraction
  - Unified element locator methods
  - Explicit/implicit wait handling
  - iframe switching
  - Screenshot capture
  - Logging integration

#### Page Object Module (`page_object/`)

| File | Business Module | Key Functions |
|------|-----------------|---------------|
| `draft_demologin.py` | Login | User authentication, permission validation |
| `pre_audit.py` | Pre-Audit | Customer qualification, credit assessment |
| `submit_order.py` | Order Submission | Information entry, validation |
| `sign_order.py` | Contract Signing | E-signature, contract generation |
| `request_pay.py` | Fund Request | Loan disbursement, fund verification |
| `approve_order.py` | Approval | Credit review workflow, approval operations |
| `subscription_app.py` | Subscription | Individual/Enterprise subscription |

#### Utility Module (`public/utils/`)

- `get_cookie.py`: Cookie management
- `readini.py`: INI config file reading
- `reports_out.py`: HTML test report generation
- `get_phone_code.py`: Verification code retrieval
- `Vin_Genarate.py`: VIN generation utility

### 4. Data-Driven Testing

Test data is externalized from code with multi-environment support:

```
data/
├── data.ini          # UAT environment config
├── pre_cookie.ini    # PRE environment config
├── elements.py       # Element locator configs
└── path_config.py    # Path configuration
```

### 5. Test Framework Integration

```
pytest
├── fixtures (conftest.py)    # Test fixtures
├── markers (pytest.ini)        # Test categorization
├── allure reports             # Allure reporting
└── HTML reports               # HTMLTestRunner reporting
```

## Design Patterns Applied

### Factory Pattern
- `BasePage` as abstract factory
- Page objects inherit and implement specific operations

### Singleton Pattern
- WebDriver instance management
- Config file readers

### Strategy Pattern
- Multi-environment config switching
- Browser-driver strategy selection

### Decorator Pattern
- Logging decorators
- Retry mechanism decorators

## Extensibility Design

### 1. Multi-Environment Support
UAT/PRE/PROD environment switching via configuration files

### 2. Parallel Execution
pytest-xdist support for parallel test execution

### 3. Report Integration
- Allure reports
- HTMLTestRunner reports
- Log files

### 4. CI/CD Integration
Jenkins, GitLab CI compatible

## Project Structure

```
demo-automation/
├── cases/              # Test cases
├── core/               # Core framework
├── page_object/        # Page objects
├── public/             # Public utilities
│   └── utils/          # Utility functions
├── data/               # Test data
├── API_test/           # API testing module
│   ├── api_keys/       # API key configs
│   ├── conf/           # API configs
│   ├── test_cases/     # API test cases
│   └── utils/          # API utilities
├── temp/               # Temporary files (reports)
├── testData/           # Test data files
├── conftest.py         # pytest fixtures
├── pytest.ini          # pytest settings
└── main.py             # Entry point
```

## Best Practices

1. **Explicit Waits Over Implicit Waits**: Use `WebDriverWait` instead of `time.sleep()`
2. **Configuration Externalization**: Use environment variables for sensitive data
3. **Consistent Logging**: Use logging module instead of print statements
4. **Type Hints**: Add type annotations for better code readability
5. **Exception Handling**: Catch specific exceptions, avoid bare except
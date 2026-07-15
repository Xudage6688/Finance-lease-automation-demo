# Tech Stack

## Core Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.8+ | Programming language |
| Selenium | 4.x | Web automation framework |
| pytest | 7.x | Testing framework |
| Allure | 2.x | Test reporting |

## Dependencies

### Web Automation
- `selenium` - Web driver
- `webdriver-manager` - Driver management

### Test Framework
- `pytest` - Test runner
- `pytest-html` - HTML reporting
- `allure-pytest` - Allure integration
- `pytest-xdist` - Parallel execution

### API Testing
- `requests` - HTTP client
- `PyYAML` - YAML parsing

### Utilities
- `openpyxl` - Excel operations
- `xmind` - Mind map parsing

### Reporting
- `HTMLTestRunner` - HTML test reports

## Development Tools

- **IDE**: PyCharm / VS Code
- **Version Control**: Git
- **Browser**: Chrome (recommended)

## Browser Driver

Project uses Chrome for testing with support for:
- Normal mode
- Debug mode (remote-debugging-port)

## Environment Management

Virtual environment recommended:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

## Configuration Management

- INI format configuration files
- YAML format test cases
- Environment variable support

## Reporting System

### HTML Report
```bash
python main.py
```

### Allure Report
```bash
pytest --alluredir ./temp/allure/reports
allure serve ./temp/allure/reports
```

## CI/CD Integration

### Jenkins
```groovy
pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'pytest --alluredir allure-results'
            }
        }
    }
}
```

### GitHub Actions
```yaml
name: Test
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: pytest
```
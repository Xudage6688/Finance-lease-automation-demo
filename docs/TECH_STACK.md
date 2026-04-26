# 技术栈

## 核心技术

| 技术 | 版本 | 用途 |
|------|------|------|
| Python | 3.8+ | 编程语言 |
| Selenium | 4.x | Web 自动化框架 |
| pytest | 7.x | 测试框架 |
| Allure | 2.x | 测试报告 |

## 依赖库

### Web 自动化
- `selenium` - Web 驱动
- `webdriver-manager` - 驱动管理

### 测试框架
- `pytest` - 测试运行器
- `pytest-html` - HTML 报告
- `allure-pytest` - Allure 集成
- `pytest-xdist` - 并行执行

### API 测试
- `requests` - HTTP 客户端
- `PyYAML` - YAML 解析

### 工具库
- `openpyxl` - Excel 操作
- `xmind` - 思维导图解析

### 报告生成
- `HTMLTestRunner` - HTML 测试报告

## 开发工具

- **IDE**: PyCharm / VS Code
- **版本控制**: Git
- **浏览器**: Chrome (推荐)

## 浏览器驱动

项目使用 Chrome 浏览器进行测试，支持：
- 普通模式
- 调试模式 (remote-debugging-port)

## 环境管理

推荐使用虚拟环境：
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

## 配置管理

- INI 格式配置文件
- YAML 格式测试用例
- 环境变量支持

## 报告系统

### HTML 报告
```bash
python main.py
```

### Allure 报告
```bash
pytest --alluredir ./temp/allure/reports
allure serve ./temp/allure/reports
```

## CI/CD 集成

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
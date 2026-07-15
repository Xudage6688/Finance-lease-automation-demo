# Demo 自动化测试框架

> 企业级全栈自动化测试框架 - 金融业务 Web UI + API 测试

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green)](https://www.selenium.dev/)
[![pytest](https://img.shields.io/badge/pytest-7.x-orange)](https://pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 核心设计理念

```
┌─────────────────────────────────────────────────────────────┐
│  测试用例层    →  业务验证逻辑                                │
│  页面对象层    →  UI 抽象与封装                              │
│  核心框架层    →  WebDriver 基础封装                         │
│  公共工具层    →  横切关注点（日志、报告、配置）              │
└─────────────────────────────────────────────────────────────┘
```

### 设计模式应用

| 模式 | 实现 |
|------|------|
| **工厂模式** | `BasePage` 作为页面对象抽象工厂 |
| **单例模式** | WebDriver 实例管理、配置读取器 |
| **策略模式** | UAT/PRE/PROD 多环境配置切换 |
| **装饰器模式** | 日志记录、重试机制 |

---

## 架构亮点

### 分层架构

| 层级 | 目录 | 职责 |
|------|------|------|
| 测试层 | `cases/` | 测试用例、数据驱动、断言 |
| 页面层 | `page_object/` | 页面元素、操作封装 |
| 核心层 | `core/` | WebDriver 封装、通用方法 |
| 工具层 | `public/utils/` | 配置、Cookie、报告 |

### 业务覆盖

| 业务模块 | 功能 |
|----------|------|
| 登录 | 用户认证、权限验证 |
| 预审 | 客户资质审核、风险评估 |
| 提报 | 订单提报、信息录入 |
| 签约 | 电子签章、合同生成 |
| 请款 | 放款流程、资金核对 |
| 审批 | 信审流程、审批流转 |
| 订阅 | 个人/企业订阅 |

---

## 技术栈

| 分类 | 技术 |
|------|------|
| 语言 | Python 3.8+ |
| 框架 | Selenium 4.x, pytest 7.x |
| 报告 | Allure, HTMLTestRunner |
| 接口 | requests, PyYAML |
| 工具 | openpyxl, xmind |

---

## 目录结构

```
demo-automation/
├── cases/              # 测试用例
├── page_object/        # 页面对象
├── core/               # 核心框架
├── public/utils/       # 工具函数
├── data/               # 测试数据
├── API_test/           # API 测试
├── conftest.py         # pytest fixtures
├── pytest.ini          # pytest 配置
└── main.py             # 入口
```

---

## 最佳实践

1. **显式等待优于隐式等待** - 使用 `WebDriverWait`
2. **配置外部化** - 环境变量、INI/YAML 配置
3. **日志规范** - 使用 logging 模块
4. **测试隔离** - fixture 独立、并行支持
5. **CI/CD 就绪** - Jenkins/GitHub Actions 兼容

---

## 文档

- [架构设计](docs/ARCHITECTURE_zh.md)
- [技术栈](docs/TECH_STACK_zh.md)

## License

[MIT License](LICENSE)

## Author

**Xudage6688** - [GitHub](https://github.com/Xudage6688)
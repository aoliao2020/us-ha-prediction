 US→H→A 市场传导预测系统的完整说明文档。

```markdown
# US→H→A 市场传导预测系统 v2.1

## 📋 项目概述

**US→H→A 市场传导预测系统**是一款基于多因子传导模型的金融市场分析工具，专注于预测美股（US）→港股（H）→A股（A）的跨市场传导效应。系统通过四步预测框架，结合机构评级、宏观情景分析和行为金融学修正，生成专业的市场预测报告。

### 核心能力
- **跨市场传导建模**：量化美股波动向港股、A股的传导衰减规律
- **板块级预测**：覆盖生物医药、新能源、半导体等6大核心板块
- **自动化报告生成**：输出专业级HTML报告与邮件通知
- **多维度数据融合**：整合技术指标、资金流向、政策催化剂

---

## 🏗️ 系统架构

### 技术栈
- **开发语言**：Python 3.8+
- **核心库**：smtplib, email.mime, datetime, os
- **数据源**：Yahoo Finance, AKShare（需外部接入）
- **部署方式**：本地脚本/定时任务（Cron）

### 模块结构
```
prediction_system.py
├── 主控模块 (main)
│   ├── 数据初始化
│   ├── 报告生成流程
│   └── 邮件分发流程
├── 报告生成模块 (generate_html_report)
│   ├── 市场数据渲染
│   ├── 板块预测表格生成
│   └── 可视化样式封装
└── 邮件服务模块 (send_detailed_email)
    ├── 邮件正文生成
    ├── HTML附件编码
    └── SMTP发送服务
```

---

## ⚙️ 安装与配置

### 环境要求
- Python 3.8 或更高版本
- SMTP邮箱服务（支持Gmail、企业邮箱等）
- 磁盘空间：> 100MB（用于存储历史报告）

### 安装步骤

1. **克隆/下载项目**
```bash
git clone [repository-url]
cd prediction-system
```

2. **创建报告目录**
系统会自动创建 `reports/` 目录，也可手动创建：
```bash
mkdir reports
```

3. **配置环境变量**

| 变量名 | 必填 | 说明 | 示例 |
|--------|------|------|------|
| `EMAIL_ENABLED` | 否 | 是否启用邮件功能 | `true` 或 `false` |
| `SENDER_EMAIL` | 条件 | 发件人邮箱地址 | `user@gmail.com` |
| `EMAIL_PASSWORD` | 条件 | 邮箱授权码/密码 | `xxxxxxxxxxxx` |
| `RECIPIENT_LIST` | 条件 | 收件人列表（逗号分隔） | `a@mail.com,b@mail.com` |
| `SMTP_SERVER` | 否 | SMTP服务器地址 | `smtp.gmail.com` |
| `SMTP_PORT` | 否 | SMTP端口 | `587`（TLS）或 `465`（SSL） |

**配置示例（Linux/Mac）：**
```bash
export EMAIL_ENABLED=true
export SENDER_EMAIL="your-email@gmail.com"
export EMAIL_PASSWORD="your-app-password"
export RECIPIENT_LIST="trader1@company.com,analyst2@company.com"
export SMTP_SERVER="smtp.gmail.com"
export SMTP_PORT="587"
```

**配置示例（Windows PowerShell）：**
```powershell
$env:EMAIL_ENABLED="true"
$env:SENDER_EMAIL="your-email@gmail.com"
# ... 其他变量
```

> **安全提示**：建议使用应用专用密码（App Password），避免使用邮箱主密码。

---

## 🚀 使用指南

### 基本运行

```bash
python prediction_system.py
```

### 运行流程

1. **系统初始化**：创建报告目录，加载市场数据
2. **数据准备**：内置模拟数据（生产环境需接入真实API）
3. **报告生成**：生成HTML格式专业报告，保存至 `reports/report_YYYYMMDD.html`
4. **邮件分发**：（如启用）发送详细文字报告+HTML附件

### 输出文件

- **HTML报告**：`reports/report_YYYYMMDD.html`
  - 响应式设计，支持移动端查看
  - 包含市场概览卡片、板块预测表格、风险提示
- **邮件内容**：纯文本详细版+HTML附件

---

## 📊 预测模型说明

### 四步预测框架

系统采用 **Multi-Factor Transmission Model v2.1**，权重分配如下：

| 步骤 | 模型组件 | 权重范围 | 说明 |
|------|----------|----------|------|
| 1 | 历史传导基线 | 30% | US→H→A历史相关性衰减模型 |
| 2 | 机构评级调整 | 40-85% | 高盛/大摩目标价偏离度修正 |
| 3 | 宏观情景乘数 | 动态 | 美联储政策/关税/DeepSeek等非线性调整 |
| 4 | LLM经验修正 | 行为金融 | 板块轮动周期/季节性/情绪面修正 |

### 覆盖板块

| 板块 | 预测方向 | 核心催化剂 | 机构评级 |
|------|----------|------------|----------|
| 生物医药 | +2.07% | 创新药出海+降息受益 | Overweight |
| 大宗商品/周期 | +1.64% | 两会政策+板块轮动 | Underweight→反弹 |
| 金融 | +1.39% | 政策托底+息差压力 | Neutral |
| 新能源 | +1.07% | 分化加剧+关税影响 | Neutral |
| 互联网 | +1.06% | AI货币化+DeepSeek | Overweight |
| 半导体 | +0.71% | 国产替代+外部冲击 | Overweight |

### 预测参数
- **预测周期**：15个交易日（约3周）
- **置信区间**：95%
- **指数预测**：
  - 恒生指数：区间 -3.5% ~ +4.5%
  - 上证指数：区间 -1.2% ~ +4.8%

---

## 📧 邮件格式

系统发送的邮件包含两部分：

### 1. 邮件正文（纯文本）
- 市场基准数据摘要
- 板块预测表格（文字版）
- TOP 3 推荐逻辑
- 风险提示
- 模型方法论简述

### 2. HTML附件
- 可视化报告（渐变色彩设计）
- 交互式表格（Hover效果）
- 响应式布局（适配手机/平板）

---

## 🔧 自定义开发

### 接入实时数据
当前版本使用内置模拟数据，生产部署时需修改 `main()` 函数中的 `market_data` 字典：

```python
# 示例：接入Yahoo Finance API
import yfinance as yf

def fetch_market_data():
    nasdaq = yf.Ticker("^IXIC")
    hsi = yf.Ticker("^HSI")
    # ... 其他数据获取逻辑
    return market_data
```

### 修改板块配置
在 `main()` 函数中修改 `predictions` 列表，调整板块名称、预测值、催化剂等。

### 自定义邮件模板
修改 `generate_email_body()` 函数可调整邮件正文格式；修改 `generate_html_report()` 中的CSS样式可调整报告视觉效果。

---

## ⚠️ 重要提示

1. **风险提示**：本系统生成的预测仅供参考，不构成投资建议。市场有风险，投资需谨慎。

2. **数据时效**：系统默认使用内置静态数据，生产环境必须接入实时数据源。

3. **邮件限制**：
   - Gmail用户需开启"不够安全的应用访问"或使用应用专用密码
   - 企业邮箱可能需要IT部门开放SMTP权限
   - 附件大小限制（通常25MB以内）

4. **时区问题**：系统使用服务器本地时间，跨区域部署时请注意时区统一（建议统一使用北京时间）。

5. **模型局限性**：
   - 黑天鹅事件无法预测
   - 政策突变可能导致模型短期失效
   - 历史传导规律可能随市场结构变化而失效

---

## 📅 版本历史

- **v2.1** (当前版本)
  - 新增四步预测框架
  - 优化HTML报告视觉效果
  - 支持环境变量配置
  - 增加详细的文字版邮件正文

---

## 📞 技术支持

- **项目维护**：[Your Name/Organization]
- **问题反馈**：[Issue Tracker URL]
- **文档更新**：随模型迭代同步更新

---

*本系统由 US→H→A Multi-Factor Transmission Model v2.1 驱动*
*生成时间：2026-02-27*
```

这份说明文档涵盖了项目的完整技术细节，包括架构设计、部署配置、使用方法和风险提示。您可以根据实际的项目仓库地址、联系方式等信息补充相应部分。需要我针对某个特定章节进行更详细的扩展吗？
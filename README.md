# 🔥 Baidu HotSearch Tracker - 百度热搜追踪系统

一个基于 Python 的热搜追踪工具，支持：

- 自动爬取百度热搜 Top10  
- 存储进 MySQL 数据库  
- 导出 CSV 文件  
---

## 📁 项目结构说明
```text
├── crawler.py          # 爬虫主程序（抓取百度热搜）
├─mysql_helper.py     # MySQL 数据库操作封装类
├─export_csv.py       # 导出数据为 CSV
├─run_scheduler.py    # 每小时自动运行爬虫
└── README.md          项目说明文档 
```

## 🚀 快速开始
### 1. 安装依赖：
```bash
pip install requests beautifulsoup4 pymysql pandas matplotlib schedule
```

### 2. 创建数据库 baidu_hot：
```sql
CREATE DATABASE baidu_hot;
```

### 3. 设置数据库连接（见 mysql_helper.py）：
```python
MySqlHelper(
    host="localhost",
    user="root",
    password="你的密码",
    database="baidu_hot"
)
```

### 4. 运行主程序：
```bash
python crawler.py
```

## ⏰ 定时自动运行（每小时）
使用 schedule 模块每小时执行一次任务：
```bash
python run_scheduler.py
```



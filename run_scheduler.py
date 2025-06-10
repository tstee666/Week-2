import schedule
import time
from crawler import run_crawler

from export_csv import export_to_csv

def job():
    print("🕐 开始抓取 + 写入数据库 + 导出 CSV...")
    run_crawler()
    export_to_csv()
    print("✅ 全部任务完成。\n")

# 每小时执行一次任务
schedule.every().hour.do(job)

print("🟢 调度器已启动，每小时自动抓取百度热搜并导出为 CSV。按 Ctrl+C 退出。")

# 启动时立即运行一次
job()

while True:
    schedule.run_pending()
    time.sleep(1)


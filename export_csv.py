import pandas as pd
from mysql_helper import MySqlHelper
from datetime import datetime

def export_to_csv():
    db = MySqlHelper(
        host="localhost",
        user="root",
        password="Tst050303.",  # ← 请换成你真实的密码
        database="baidu_hot"
    )
    
    sql = "SELECT title, hot, timestamp FROM hot_search ORDER BY timestamp DESC"
    results = db.fetchall(sql)
    db.close()

    df = pd.DataFrame(results, columns=["title", "hot", "timestamp"])

    # 生成带时间戳的文件名
    filename = f"baidu_hot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    
    print(f"✅ 导出成功：{filename}")

if __name__ == "__main__":
    export_to_csv()


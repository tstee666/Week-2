# ✅ export_csv.py - 导出MySQL数据为CSV
import pandas as pd
from mysql_helper import MySqlHelper


def export_to_csv():
    db = MySqlHelper(
        host="localhost",
        user="root",
        password="your_password",
        database="baidu_hot"
    )
    sql = "SELECT * FROM hot_search"
    results = db.fetchall(sql)
    db.close()

    df = pd.DataFrame(results, columns=["title", "hot", "timestamp"])
    df.to_csv("baidu_hot.csv", index=False, encoding="utf-8-sig")
    print("✅ 导出成功为 baidu_hot.csv")


if __name__ == '__main__':
    export_to_csv()


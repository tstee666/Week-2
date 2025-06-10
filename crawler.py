import requests
from bs4 import BeautifulSoup
from datetime import datetime
from mysql_helper import MySqlHelper

# 爬取百度热搜Top10
def fetch_baidu_hot():
    url = "https://top.baidu.com/board?tab=realtime"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.select(".category-wrap_iQLoo.horizontal_1eKyQ")[:10]
    data = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for item in items:
        title = item.select_one(".c-single-text-ellipsis").text.strip()
        hot = item.select_one(".hot-index_1Bl1a").text.strip()
        data.append((title, hot, timestamp))

    return data

# 写入数据库
def save_to_db(data):
    db = MySqlHelper(
        host="localhost",
        user="root",
        password="Tst050303.",
        database="baidu_hot"
    )
    sql = """
    INSERT INTO hot_search (title, hot, timestamp)
    VALUES (%s, %s, %s)
    """
    for record in data:
        db.execute(sql, record)
    db.close()

if __name__ == "__main__":
    try:
        hot_list = fetch_baidu_hot()
        save_to_db(hot_list)
        print(f"\u2705 已成功写入 {len(hot_list)} 条热搜数据")
    except Exception as e:
        print(f"\u274c 错误: {e}")


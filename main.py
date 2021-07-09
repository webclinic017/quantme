from jqdatasdk import *
import os
from dotenv import load_dotenv
import logging
from tqdm import tqdm
import pandas as pd

pd.set_option('display.max_rows', 4000)
pd.set_option('display.max_columns', 50)

# 加载用户名和密码环境变量
load_dotenv()
logging.basicConfig(level=logging.INFO)

username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]


# 验证
auth(username, password)

# 获取当前可调用次数
logging.info(f"验证成功, 剩余可调用次数为: { get_query_count() }")

# 获取科大讯飞的行情数据 - 2021-7-7 前的100个交易日数据
iflytek = get_price("002230.XSHE", count=10, end_date='2021-7-7')
logging.info(f"行情数据为 \n{ iflytek }")

# 获取科大讯飞的行情数据 - 2021-7-7 上午的所有分钟级别的数据
iflytek2 = get_price('002230.XSHE', start_date='2021-7-7 9:00:00',
                     end_date='2021-7-7 11:30:00', frequency='1m')
logging.info(f"行情数据为: \n{ iflytek2 }")

# 获取 2021-7-7上午 所有A股上市公司的交易数据
stocks = list(get_all_securities(['stock']).index)
for stock in tqdm(stocks):
    stock_data = get_price(stock, start_date='2021-7-7 9:00:00',
                           end_date='2021-7-7 11:30:00', frequency='1m')
    logging.info(f"行情数据为: \n{ stock_data }")

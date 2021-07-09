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
logging.info(f"验证成功, 剩余可调用次数为: {get_query_count()}")

df = get_price('000001.XSHE', start_date='2021-01-01', end_date='2021-01-31', frequency='daily', panel=False)  # 获取日K

df_month = pd.DataFrame()
df_month['open'] = df['open'].resample('M').first()
df_month['close'] = df['close'].resample('M').last()
df_month['max'] = df['high'].resample('M').max()
df_month['min'] = df['low'].resample('M').min()
df_month['volume'] = df['volume'].resample('M').sum()
df_month['money'] = df['money'].resample('M').sum()
print(df_month)

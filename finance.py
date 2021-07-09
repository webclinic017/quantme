from jqdatasdk import *
import os
from dotenv import load_dotenv
import logging
from tqdm import tqdm
import pandas as pd

pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 500)

# 加载用户名和密码环境变量
load_dotenv()
logging.basicConfig(level=logging.INFO)

username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]

# 验证
auth(username, password)

# 获取当前可调用次数
logging.info(f"验证成功, 剩余可调用次数为: {get_query_count()}")

df: pd.DataFrame = get_fundamentals(query(indicator), date="2021-01-05")
#df.to_csv('finance.csv')


#基于盈利指标选股, eps, operating_profit, inc_total_revenue_year_on_year
df = df[(df['eps'] > 0) & (df["operating_profit"] > 284197086.3) & (df['roe'] > 11) & (df['inc_total_revenue_year_on_year'] > 10)]
print(df)

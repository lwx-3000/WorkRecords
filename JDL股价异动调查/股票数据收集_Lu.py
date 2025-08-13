import tushare as ts
import pandas as pd

# 使用 Token 初始化 Tushare
pro = ts.pro_api('20f49144820af8a911ecd7cf8296d341de53750d267178d94fcd7349')  # 我的Token

def get_stock_data(stock_code, start_date, end_date):
    """
    获取指定股票代码的历史数据
    :param stock_code: 股票代码，例如 '600000.SH'
    :param start_date: 起始日期，格式：'YYYY-MM-DD'
    :param end_date: 结束日期，格式：'YYYY-MM-DD'
    :return: 包含股票历史数据的 DataFrame
    """
    # 获取历史K线数据（日K线）
    df = pro.daily(ts_code=stock_code, start_date=start_date, end_date=end_date)
    
    return df

def save_data_to_csv(data, filename):
    """
    将获取的数据保存为CSV文件
    :param data: 股票历史数据
    :param filename: 保存的文件名
    """
    data.to_csv(filename, index=False, encoding='utf-8')
    print(f"数据已保存为 {filename}")

if __name__ == "__main__":
    while True:
        # 获取用户输入的股票代码
        stock_code = input("请输入您想查询的股票代码（例如：600000.SH），输入'退出'以结束查询：").strip()
        
        # 如果用户输入"退出"，退出查询循环
        if stock_code.lower() == '退出':
            print("退出查询！")
            break
        
        # 获取查询的日期范围
        start_date = input("请输入开始日期（格式：YYYYMMDD）：").strip()
        end_date = input("请输入结束日期（格式：YYYYMMDD）：").strip()
        
        # 获取股票数据
        stock_data = get_stock_data(stock_code, start_date, end_date)
        
        # 输出获取到的数据
        if not stock_data.empty:
            print(f"\n{stock_code}的历史数据：")
            print(stock_data)  # 打印显示数据
            
            # 保存数据为CSV文件
            filename = f"{stock_code}_{start_date}_to_{end_date}.csv"
            save_data_to_csv(stock_data, filename)
        else:
            print(f"\n未能获取到 {stock_code} 的数据，请检查股票代码或日期范围是否正确。\n")

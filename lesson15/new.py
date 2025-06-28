import pandas as pd
import glob
import os
from typing import List, Dict

# 定義股票代碼到中文名稱的映射
STOCK_MAP: Dict[str, str] = {
    '2330': '台積電',
    '2303': '聯電',
    '2454': '聯發科',
    '2317': '鴻海'
}

# 資料來源目錄
DATA_DIR: str = 'data'

def merge_stock_close_prices(
    tickers: List[str], 
    stock_map: Dict[str, str], 
    data_dir: str
) -> pd.DataFrame:
    """
    讀取多支股票最新的 CSV 檔，萃取收盤價，並合併成一個 DataFrame。

    Args:
        tickers (List[str]): 要處理的股票代碼列表 (例如: ['2330', '2303'])。
        stock_map (Dict[str, str]): 股票代碼到中文名稱的映射字典。
        data_dir (str): 存放 CSV 檔案的資料夾路徑。

    Returns:
        pd.DataFrame: 一個以日期為索引，股票中文名稱為欄位的收盤價 DataFrame。
    """
    all_close_series = []

    for ticker in tickers:
        # 使用 glob 尋找符合條件的檔案
        search_path = os.path.join(data_dir, f'{ticker}_*.csv')
        list_of_files = glob.glob(search_path)

        if not list_of_files:
            print(f"警告：在 '{data_dir}' 中找不到股票代碼 {ticker} 的 CSV 檔案，將略過。")
            continue

        # 透過排序檔名找到最新的檔案 (基於 YYYY-MM-DD 日期格式)
        latest_file = sorted(list_of_files)[-1]
        print(f"正在處理檔案: {latest_file}")

        # 讀取 CSV，只取 'Date' 和 'Close' 欄位，並將 'Date' 設為索引
        df = pd.read_csv(
            latest_file,
            usecols=['Date', 'Close'],
            parse_dates=['Date'],
            index_col='Date'
        )

        # 為了合併，先將 'Close' 欄位重新命名為股票代碼
        df.rename(columns={'Close': ticker}, inplace=True)
        all_close_series.append(df[ticker])

    if not all_close_series:
        print("錯誤：沒有處理任何資料，返回空的 DataFrame。")
        return pd.DataFrame()

    # 將所有 Series 沿著欄位方向 (axis=1) 合併成一個 DataFrame
    merged_df = pd.concat(all_close_series, axis=1)

    # 將欄位名稱從股票代碼換成中文名稱
    merged_df.rename(columns=stock_map, inplace=True)

    return merged_df

if __name__ == "__main__":
    # 檢查資料目錄是否存在
    if not os.path.isdir(DATA_DIR):
        print(f"錯誤：找不到資料目錄 '{DATA_DIR}'。請先建立該目錄並放入股票 CSV 檔。")
    else:
        final_df = merge_stock_close_prices(list(STOCK_MAP.keys()), STOCK_MAP, DATA_DIR)
        print("\n--- 整合後的股票收盤價資料 ---")
        print(final_df)
#安裝Gemini-> 登入google帳戶 -> 右下角星星圖示點下 ->選取上面搜尋框出現第一個選項，會自動出現



#lesson15資料夾右鍵「在整合式終端機中開啟」->打 python lesson15_1.py->就可以開始執行

import yfinance as yf

df main():
    tw2330 = yf.download('2330.TW', start='2024-01-01', end='2024-06-01',auto_adjust=True)
    tw2303 = yf.download('2303.TW', start='2024-01-01', end='2024-06-01',auto_adjust=True)
    tw2454 = yf.download('2454.TW', start='2024-01-01', end='2024-06-01',auto_adjust=True)  
    tw2317 = yf.download('2317.TW', start='2024-01-01', end='2024-06-01',auto_adjust=True)
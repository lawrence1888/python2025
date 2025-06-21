#在lesson13資料夾右鍵點選[在整合式終端機開啟]
#終端機打 pip install streamlit
#終端機打 streamlit run main.py後，輸入email，就會跳出網頁視窗


import streamlit as st
import pandas as pd

def main():
    st.title("我的第一個Streamlit App")
    st.write("歡迎來到我的應用程式！")
    
    # Load the CSV file
    df = pd.read_csv("taiwan.csv")
    
    # Display the DataFrame
    st.write("以下是 'taiwan.csv' 的內容：")
    st.dataframe(df)

if __name__ == "__main__":
    main()
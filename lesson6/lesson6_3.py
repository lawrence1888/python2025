#注意虛擬環境，選chilee1(先前創立的虛擬環境)
# 將lesson6_3.py存檔傳至雲端
# lesson6資料夾右鍵「在整合式終端機中開啟」->打 python lesson6_3.py->就可以開始執行
#縮排按tab


import random

def play_game():
    min = 1
    max = 100
    count = 0
    target = random.randint(1, 100)
    print(target)
    print("===============猜數字遊戲=================:\n")
    while(True):
        count += 1
        keyin = int(input("猜數字範圍{0}~{1}:".format(min, max)))
        if(keyin >=min and keyin <= max):
            if(keyin == target):
                print("賓果!猜對了, 答案是:", target)
                print("您猜了",count,"次")
                break
            elif (keyin > target):
                max = keyin
                print("再小一點")
            elif (keyin < target):
                min = keyin
                print("再大一點")
            print("您猜了",count,"次\n")
        else:
            print("請輸入提示範圍內的數字")
  

while(true)：
    play_game()
    play_again=input("再玩一次(y,n)：")
    if(play_again=="n")
        break

print("遊戲結束")



#設定自動儲存：設定->經常使用設定為after delay
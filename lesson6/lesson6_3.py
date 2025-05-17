#注意虛擬環境，選chilee1(先前創立的虛擬環境)
# 將lesson6_3.py存檔傳至雲端
# lesson6資料夾右鍵「在整合式終端機中開啟」->打 python lesson6_3.py->就可以開始執行


import random
min = 1
max = 99
count = 0
random_number = random.randint(min,max)
#print(random_number)
print("=====猜數字遊戲開始=========\n\n")
while True:
  input_number = int(input(f"請輸入數字({min}~{max}):"))
  count += 1
  if(input_number == random_number):
    print(f"賓果!猜對了, 答案是:{input_number}")
    print(f"您猜了:{count}次")
    break
  elif(input_number>random_number):
    print(f"再小一點")
    max = input_number - 1
  elif(input_number<random_number):
    print(f"再大一點")
    min = input_number + 1

  print(f"您已經猜了:{count}次\n")


print("Game Over")



#設定自動儲存：設定->經常使用設定為after delay
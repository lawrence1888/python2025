import tool



def main():
    height:int = int(input("請輸入身高(cm):"))
    weight:int = int(input("請輸入體重(kg):"))

    bmi = tool.caculate_bmi(height, weight)

    print(bmi)
    print(tool.get_state(bmi))


if __name__=='__main__':
    main()

#在終端機中輸入python lesson7_2.py後，按ENTER執行
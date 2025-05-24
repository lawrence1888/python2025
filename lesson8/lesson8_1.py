#自訂的function，目的是結構化程式碼
#自訂的modue,package，目的是結構化程式


#方法一：import edu
#方法二：from edu.tools import caculate_bmi,get_state
#方法三：
from edu.tools import caculate_bmi as a1
from edu.tools import get_state as a2

def main():
    height:int = int(input("請輸入身高(cm):"))
    weight:int = int(input("請輸入體重(kg):"))

    bmi = a1(height, weight)

    print(bmi)
    print(a2(bmi))


if __name__ == '__main__':
    main()